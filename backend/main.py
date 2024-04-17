from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
from boto3.dynamodb.conditions import Attr
from recommendation import recommend_items
from dotenv import load_dotenv
from flask_cors import CORS
import requests
import boto3
import time
import json
import os

from uploadToAws import uploadToAws

app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# Load environment variables from .env
load_dotenv()

region_name = "ap-southeast-1"

# Create a Secrets Manager client
session = boto3.session.Session()
client = session.client(
        service_name='secretsmanager',
        region_name=region_name
)

# Getting Credentials for my AWS 
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

# Create a DynamoDB client
dynamodb = boto3.resource('dynamodb',
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        region_name='ap-southeast-1')  # Update the region to 'ap-southeast-1'

# Tables in my DynamoDB 
clicked_table = dynamodb.Table('clicked')
dessert_table = dynamodb.Table('Dessert')
snack_table = dynamodb.Table('Snack')
appetizer_table = dynamodb.Table('Appetizer')

# Adding New Items into AWS table 
# uploadToAws('appetizer', './appetizer.json', dynamodb)

# Define the request parser
clicked_parser = reqparse.RequestParser()
clicked_parser.add_argument('type', type=str, required=True, help='Type of the item is required', location='json')
clicked_parser.add_argument('calories', type=int, required=True, help='Calories is required', location='json')
clicked_parser.add_argument('carbs', type=int, required=True, help='Carbs is required', location='json')
clicked_parser.add_argument('fat', type=int, required=True, help='Fat is required', location='json')
clicked_parser.add_argument('protein', type=int, required=True, help='Protein is required', location='json')

meal_filter = reqparse.RequestParser()
meal_filter.add_argument('calories', location='json')
meal_filter.add_argument('fat', location='json')
meal_filter.add_argument('protein', location='json')
meal_filter.add_argument('carbs', location='json')

class ClickedItem(Resource):
    def post(self, item_id):
        # Parse the request arguments
        args = clicked_parser.parse_args(req=request)
        item_type = args['type']
        calories = args['calories']
        carbs = args['carbs']
        fat = args['fat']
        protein = args['protein']

        # Get the current timestamp
        timestamp = int(time.time())

        # Prepare the item data
        item = {
            'id': item_id,
            'type': item_type,
            'calories': calories,
            'carbs': carbs,
            'fat': fat,
            'protein': protein,
            'timestamp': timestamp
        }

        # Put the item into the DynamoDB table
        clicked_table.put_item(Item=item)

        return {'message': 'Item added to clicked table'}, 201

class Meal(Resource):
    def post(self, meal_type):
        table_name = meal_type.capitalize()
        meal_table = dynamodb.Table(table_name)

        calories = None
        carbs = None
        fat = None
        protein = None

        data_str = request.data.decode('utf-8')
        data_dict = json.loads(data_str)

        # Access the inner 'data' dictionary
        inner_data = data_dict.get('data', {})

        if(inner_data['calories'] == True):
            calories = True
        
        if(inner_data['carbs'] == True):
            carbs = True

        if(inner_data['fat'] == True):
            fat = True

        if(inner_data['protein'] == True):
            protein = True

        # Testing for locally   
        
        # if(data_dict['calories'] == True):
        #     calories = True
        
        # if(data_dict['carbs'] == True):
        #     carbs = True

        # if(data_dict['fat'] == True):
        #     fat = True

        # if(data_dict['protein'] == True):
        #     protein = True

        # Query the DynamoDB table for data
        response = meal_table.scan()
        items = response.get('Items', [])

        # Check if there are more pages to scan
        while 'LastEvaluatedKey' in response:
            response = meal_table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            items.extend(response.get('Items', []))

        # Convert the items to a list of dictionaries
        meal_items = [item for item in items]
        
        clicked_items_response = clicked_table.scan(
            FilterExpression=Attr('type').eq(meal_type),
            Limit=5
        )

        clicked_items = clicked_items_response.get('Items', [])

        # Convert the clicked_items to a list of dictionaries   
        clicked_items = [item for item in clicked_items]

        # Remove clicked items from meal items by id
        # Extract IDs from clicked_items and store them in a set
        clicked_item_ids = {clicked_item['id'] for clicked_item in clicked_items}

        # Remove items from meal_items if their IDs are in clicked_item_ids
        filtered_meal_items = []
        for item in meal_items:
            if item['id'] not in clicked_item_ids:
                filtered_meal_items.append(item)

        clicked_items.sort(key=lambda x: x.get('timestamp', 0), reverse=True)

        recommended_items = recommend_items(filtered_meal_items, clicked_items, calories, protein, carbs, fat)

        # Return a proper Flask response with JSON data
        return jsonify(recommended_items)
    
class RecipeInformation(Resource):
    def get(self, recipe_id):
        api_key = '5677eb075e0a401a92152e7939d01d2b'  # Replace with your actual API key

        url = f'https://api.spoonacular.com/recipes/{recipe_id}/information'
        params = {
            'apiKey': api_key
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            recipe_info = response.json()
            return recipe_info, 200
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}, 500

api.add_resource(ClickedItem, '/clicked/<string:item_id>')
api.add_resource(Meal, '/meal/<string:meal_type>')
api.add_resource(RecipeInformation, '/recipes/<int:recipe_id>/information')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')