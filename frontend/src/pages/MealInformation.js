import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';
const MealInformation = () => {
  const { mealTypeId } = useParams();
  const [mealInfo, setMealInfo] = useState(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchMealInfo = async () => {
      setLoading(true);
      try {
        const response = await axios.get(`http://127.0.0.1:5000/recipes/${mealTypeId}/information`);
        setMealInfo(response.data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching meal information:', error);
        setLoading(false);
      }
    };

    fetchMealInfo();
  }, [mealTypeId]);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (!mealInfo) {
    return <div>No meal information available.</div>;
  }

  const {
    title,
    readyInMinutes,
    servings,
    extendedIngredients,
    instructions,
    sourceUrl,
  } = mealInfo;

  const handleGoBack = () => {
    navigate(-1)
  }

  return (  
    <div className="container mx-auto px-4 py-8 text-white">
    <button
        onClick={handleGoBack}
        className="absolute top-4 right-4 bg-white hover:bg-gray-600 text-black font-bold py-2 px-4 rounded focus:outline-none focus:ring focus:ring-gray-300"
      >
        More Suggestions
    </button>
    <h1 className="text-3xl font-bold mb-4">{title}</h1>
    <p className="text-gray-300 mb-2">Ready in: {readyInMinutes} minutes</p>
    <p className="text-gray-300 mb-2">Servings: {servings}</p>
    <div className="mt-4">
      <h2 className="text-xl font-semibold mb-2">Ingredients:</h2>
      <ul className="list-disc ml-4">
        {extendedIngredients.map((ingredient, index) => (
          <li key={index} className="text-gray-300">{ingredient.original}</li>
        ))}
      </ul>
    </div>
    <div className="mt-4">
      <h2 className="text-xl font-semibold mb-2">Instructions:</h2>
      <div className="text-gray-300" dangerouslySetInnerHTML={{ __html: instructions }} />
    </div>
    <p className="mt-4 text-gray-300">Source: <a href={sourceUrl} target="_blank" rel="noopener noreferrer" className="text-blue-500 hover:underline">{sourceUrl}</a></p>
</div>

);
};

export default MealInformation;
