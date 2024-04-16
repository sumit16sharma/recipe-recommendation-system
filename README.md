# Recipe Recommendation System

![recipe_banner](https://github.com/sumit16sharma/recipe-recommendation-system-frontend/assets/73477380/37185b87-97c7-4263-ab36-ec23843a75b8)

The Recipe Recommendation System provides curated meal categories like desserts, appetizers, and snacks, offering personalized recommendations based on users' past selections and nutritional preferences.

## Table of Contents

- [Functionality Overview](#functionality-overview)
- [Algorithm for Recommendation](#algo)
- [Working of Application](#working)
- [Installation](#installation)
- [Dependencies](#dependency)


## Functionality Overview <a name="functionality-overview"></a>

1. Meal Categories
   1. The system categorizes meals into different types such as desserts, appetizers, and snacks.
   2. Users can select a specific meal category to explore.

2. Curated Items:
   1. Within each meal category, the system presents a curated list of 25 items.
   2. These items are carefully selected to offer a diverse range of choices within the chosen category.

3. User Selections:
   1. Users can click on individual meal items to view more details about them.
   2. This interaction helps the system understand users' preferences and interests.
  
4. Personalized Recommendations:
   1. Allows users to refine recommendations based on specific nutritional criteria.
   2. Users can filter suggestions by calories, carbohydrates, fats, or proteins.
   3. Enables users to find items with similar nutritional content to their previous selections.
  
## Algorithm for Recommendation <a name="algo"></a>

1. Overview:
   1. Utilizes Euclidean distances to measure similarity between items.
   2. Recommends items based on user interactions and dietary preferences.

2. Functionality:
   1. Accepts meal items, clicked items, and optional nutritional parameters.
   2. Identifies top 5 similar items for each clicked item.

3. Recommendation Process:
   1. Calculates similarity scores between clicked and meal items.
   2. Ensures diversity in recommendations and customizes suggestions based on user preferences.
  
## Working of Application <a name="working"></a>

- Go to Frontend Application using this URL

  ![url](https://github.com/sumit16sharma/recipe-recommendation-system/assets/73477380/c0d36b0b-0240-4d12-9276-1747be6ac347)

- Click on "Go to Next Page"

  ![click-next](https://github.com/sumit16sharma/recipe-recommendation-system/assets/73477380/c6c31a2e-5b1e-45a9-ac30-ac95706cff83)

- Choose one of the Meal types (Let's click on Snack)

  ![choose_meal](https://github.com/sumit16sharma/recipe-recommendation-system/assets/73477380/e2c1c6d2-6f9d-4d10-88bf-4c5cb8717caa)

- We get 25 items for on Snack (Let's click on "Radish & Snap Pea Quinoa Salad and it has 200 calories")

  ![snak_items](https://github.com/sumit16sharma/recipe-recommendation-system/assets/73477380/781db14a-0e63-47b7-8c48-bc4880523aca)

- We get information regarding that meal item such as ingredients and instructions to cook this meal (Now Let's click on Go Back Button to get back to Snack Section)

  ![info_page](https://github.com/sumit16sharma/recipe-recommendation-system/assets/73477380/ac0f561d-3c17-4176-b4dc-d8b0d4b5e875)

- After coming back to the snack section, now it recommends meals based on my previous meal's nutritional content such as calories, carbs, fat and protein

  ![backtosnak](https://github.com/sumit16sharma/recipe-recommendation-system/assets/73477380/0a4e5310-3662-49be-be2a-1c60fad836dd)

## Installation <a name="installation"></a>

1. Check Docker Installation:
   1. Ensure Docker is installed on your system.
   2. If not installed, download and install [Docker](https://docs.docker.com/desktop/install/windows-install/).
  
2. Clone the Repository:

   ```bash
    git clone https://github.com/sumit16sharma/recipe-recommendation-system/
    ```

3. cd into the directory:

   ```bash
    cd recipe-recommendation-system
    ```
  
4. Start Docker Compose:

    ```bash
    docker-compose up
    ```
Note: Docker Compose up may take 3-4 minutes for setting up containers and launching the frontend application.

## Dependencies <a name="dependency">

<a href="https://nodejs.org/"><img src="https://github.com/sumit16sharma/recipe-recommendation-system/assets/73477380/617282c5-3624-4647-93bf-c96767008e8b" alt="Node.js" width="50" height="50"></a>
<a href="https://nodejs.org/"><img src="https://github.com/sumit16sharma/recipe-recommendation-system/assets/73477380/e421318c-b318-4e39-ad8f-43bf6a436e63" alt="React" width="50" height="50"></a>
<a href="https://nodejs.org/"><img src="https://github.com/sumit16sharma/recipe-recommendation-system/assets/73477380/650bc697-d02a-47f2-b6d5-452ef4d32791" alt="Python" width="50" height="50"></a>


   
