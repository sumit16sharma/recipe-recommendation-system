from sklearn.metrics.pairwise import euclidean_distances

def recommend_items(meal_items, clicked_items, calories=None, protein=None, carbs=None, fat=None):
    recommended_items = []
    
    # Iterate over clicked items
    for clicked_item in clicked_items:
        similar_items = []
        clicked_vector = []
        
        # Extract feature vector for the clicked item
        for nutrient in ['calories', 'protein', 'carbs', 'fat']:
            if clicked_item.get(nutrient) is not None:
                if nutrient == 'calories' and calories is not None:
                    clicked_vector.append(calories)
                elif nutrient == 'protein' and protein is not None:
                    clicked_vector.append(protein)
                elif nutrient == 'carbs' and carbs is not None:
                    clicked_vector.append(carbs)
                elif nutrient == 'fat' and fat is not None:
                    clicked_vector.append(fat)
                else:
                    clicked_vector.append(clicked_item[nutrient])
        
        # Extract feature vectors for meal items
        meal_vectors = []
        meal_indices = []
        for index, meal_item in enumerate(meal_items):
            meal_vector = []
            for nutrient in ['calories', 'protein', 'carbs', 'fat']:
                if meal_item.get(nutrient) is not None:
                    if nutrient == 'calories' and calories is not None:
                        meal_vector.append(calories)
                    elif nutrient == 'protein' and protein is not None:
                        meal_vector.append(protein)
                    elif nutrient == 'carbs' and carbs is not None:
                        meal_vector.append(carbs)
                    elif nutrient == 'fat' and fat is not None:
                        meal_vector.append(fat)
                    else:
                        meal_vector.append(meal_item[nutrient])
            meal_vectors.append(meal_vector)
            meal_indices.append(index)
        
        # Calculate Euclidean distances between clicked item and meal items
        similarity_scores = euclidean_distances([clicked_vector], meal_vectors)[0]
        
        # Find the top 5 similar items
        top_indices = sorted(range(len(similarity_scores)), key=lambda i: similarity_scores[i])[:5]
        similar_items.extend([meal_items[i] for i in top_indices])
        
        # Remove the similar items from meal items
        meal_items = [meal_items[i] for i in range(len(meal_items)) if i not in top_indices]
        
        recommended_items.extend(similar_items)

     # Ensure at least 25 items in the response
    while len(recommended_items) < 25 and meal_items:
        recommended_items.append(meal_items.pop(0))
    
    return recommended_items