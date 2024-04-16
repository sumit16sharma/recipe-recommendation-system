<h1>Recipe Recommendation Backend</h1>

This is the backend of a recipe recommendation system built using Flask, AWS DynamoDB, and Scikit-learn.
<br/>
<br/>

**<h2>Table of Contents</h2>**

- <a name="introduction">[Introduction](#introduction)</a>
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Endpoints](#endpoints)
  - [Recommendation Algorithm](#recommendation-algorithm)
  - [Understanding Euclidean Distances](#euclidean)
- [Frontend Repository](#frontend)
- [Contributing](#contributing)
- [License](#license)

<h2 name="introduction">Introduction</h2>

The Recipe Recommendation Backend is a Flask application designed to provide recipe recommendations based on user interactions and dietary preferences. It utilizes AWS DynamoDB to store recipe data and user interactions, and Scikit-learn for recommendation algorithms.


<h2 name="setup">Setup</h2>
<h3 name="prerequisites">Prerequisites</h3>
Before running the application, ensure you have the following installed:

- Python 3.x
- Pip (Python package manager)
- AWS account with DynamoDB access
- AWS CLI configured with appropriate credentials


<h2 name="installation">Installation</h2>

1. Clone the repository:
   
   ```bash
    git clone https://github.com/sumit16sharma/recipe-recommendation-backend.git && cd recipe-recommendation-backend
    ```
2. Install dependencies::
   
   ```bash
    pip install -r requirements.txt
    ```

<h2 name="usage">Usage</h2>

<h3 name="endpoints">Endpoints</h3>

<p>The backend provides the following endpoints:</p>

- `/clicked/<string:item_id>` (POST): Records user clicks on recipe items.
- `/meal/<string:meal_type>` (POST): Provides recipe recommendations based on meal type and user interactions.
- `/recipes/<int:recipe_id>/information` (GET): Retrieves detailed information about a specific recipe.

<h2 name="recommendation-algorithm">Recommendation Algorithm</h2>

<p>The recommendation algorithm utilizes a content-based filtering approach, calculating similarity between recipes based on their nutritional content. One of the key components of this process is the calculation of similarity scores using the `euclidean_distances` function from Scikit-learn. The main steps include:</p>

1. **Recording User Interactions**: When a user clicks on a recipe, the backend records the interaction in a DynamoDB table.
2. **Generating Recommendations**: When requested, the backend retrieves the user's recent interactions and calculates the similarity between clicked items and available recipes. The top similar recipes are recommended to the user.

<h3 name="euclidean">Understanding Euclidean Distances</h3>

- <p>Euclidean distance is a measure of the straight-line distance between two points in Euclidean space. In the context of recipe recommendations, it is used to quantify the similarity between different recipes based on their nutritional attributes.</p>

- <p>The `euclidean_distances` function in Scikit-learn calculates the pairwise distances between points in two datasets. In our case, it computes the distance between the nutritional profiles of each clicked recipe (user's preference) and all available recipes in the dataset.</p>

- <p>The algorithm considers nutritional attributes such as calories, protein, carbs, and fat to create feature vectors for each recipe. These feature vectors represent the recipe's position in the nutritional space.</p>

- <p>By comparing these feature vectors using Euclidean distances, the algorithm identifies recipes that are similar to the ones the user has interacted with. This similarity metric helps in generating personalized recipe recommendations tailored to the user's preferences.</p>

- <p>Overall, `euclidean_distances` plays a crucial role in the recommendation process by quantifying the similarity between recipes based on their nutritional content, enabling the backend to provide relevant and personalized recommendations to the users.</p>

<h2 name="frontend">Frontend Repository</h2>

The frontend repository for this project can be found at [frontend-repo-link](frontend-repo-link).

<h2 name="contributing">Contributing</h2>

<p>Contributions are welcome! If you have any ideas, suggestions, or improvements, please feel free to open an issue or submit a pull request.</p>

<h2 name="license">License</h2>

<span>This project is licensed under the</span> 
[MIT](#point-1)
