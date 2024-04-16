import json

def uploadToAws(table_name, filename, dynamodb):
    # Function to create DynamoDB table
    def create_table():
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        table.wait_until_exists()
        print("Table created:", table_name)

    # Function to read data from JSON file
    def read_json_file(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return data

    # Read data from the JSON file
    table_data = read_json_file(filename)

    # Create table if it doesn't exist
    try:
        dynamodb.describe_table(TableName=table_name)
    except dynamodb.meta.client.exceptions.ResourceNotFoundException:
        create_table()

    # Insert each item from the JSON data into the table
    for item_data in table_data:
        item = {
            'id': str(item_data['id']),
            'title': str(item_data['title']),
            'image': str(item_data['image']),
            'protein': int(item_data['protein']),
            'carbs': int(item_data['carbs']),
            'calories': int(item_data['calories']),
            'fat': int(item_data['fat'])
        }

        # Insert the item into the table
        response = table_name.put_item(Item=item)

        # Check the response
        print(response)
