import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import { useNavigate  } from 'react-router-dom';

const ListMeal = () => {
  const [meals, setMeals] = useState([]);
  const [loading, setLoading] = useState(true);
  const { mealType } = useParams();
  const navigate = useNavigate();

  const [selectedOptions, setSelectedOptions] = useState({
    protein: false,
    calories: false,
    carbs: false,
    fat: false,
  });

  useEffect(() => {
    const fetchData = async () => {
        setLoading(true);
        try {
            const response = await axios.post(`http://127.0.0.1:5000/meal/${mealType}`, {
                headers: {
                    'Content-Type': 'application/json;charset=utf-8'
                },
                data: selectedOptions
            });
            setMeals(response.data);
            setLoading(false);
        } catch (error) {
          console.error('Error fetching data:', error);
          setLoading(false);
        }
      };    
  
      fetchData();
  }, [selectedOptions]);

  const handleClick = (option) => {
    setSelectedOptions(prevOptions => ({
      ...prevOptions,
      [option]: !prevOptions[option]
    }));
  };

  const onClickCard = async (meal) => {
    try {
        const response = await axios.post(
            `http://127.0.0.1:5000/clicked/${meal.id}`,
            {
                "type": mealType,
                "calories": meal.calories,
                "carbs": meal.carbs,
                "fat": meal.fat,
                "protein": meal.protein
            },
            {
                headers: {
                    'Content-Type': 'application/json;charset=utf-8'
                }
            }
        );
        console.log(response.data); // Log the response for debugging purposes
        navigate(`${meal.id}`);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

  if(loading) {
    return <div>Loading</div>
  }

  return (
    <div className="container mx-auto p-4">
    {/* Filter UI */}
    <div className="flex justify-center space-x-4 mb-4">
      <button
        onClick={() => handleClick('calories')}
        className={`btn ${selectedOptions.calories ? 'btn-active' : ''}`}
      >
        Calories
      </button>
      <button
        onClick={() => handleClick('protein')}
        className={`btn ${selectedOptions.protein ? 'btn-active' : ''}`}
      >
        Protein
      </button>
      <button
        onClick={() => handleClick('carbs')}
        className={`btn ${selectedOptions.carbs ? 'btn-active' : ''}`}
      >
        Carbs
      </button>
      <button
        onClick={() => handleClick('fat')}
        className={`btn ${selectedOptions.fat ? 'btn-active' : ''}`}
      >
        Fat
      </button>
    </div>
    {/* Meals */}
    <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-[100px]">
      {meals.map((meal, index) => (
        <div
          key={index}
          className="card bg-white text-black shadow-lg rounded-xl flex flex-col justify-between cursor-pointer"
          style={{ width: '300px', height: '400px' }}
          onClick={() => onClickCard(meal)}
        >
          <figure className="aspect-w-1 aspect-h-1">
            <img
              src={meal.image}
              alt={meal.name}
              className="object-cover rounded-t-xl"
              style={{ width: '100%', height: '100%' }}
            />
          </figure>
          <div className="card-body bg-gray-100 p-4">
            <h2 className="card-title text-black leading-9">{meal.title}</h2>
          </div>
          <div className="bg-gray-100 p-4 rounded-b-xl">
            <div>
              <p style={{ width: '70px', display: 'inline-block' }}>Calories:</p>
              <p style={{ display: 'inline-block' }}>{meal.calories}</p>
            </div>
            <div>
              <p style={{ width: '70px', display: 'inline-block' }}>Carbs:</p>
              <p style={{ display: 'inline-block' }}>{meal.carbs}g</p>
            </div>
            <div>
              <p style={{ width: '70px', display: 'inline-block' }}>Protein:</p>
              <p style={{ display: 'inline-block' }}>{meal.protein}g</p>
            </div>
            <div>
              <p style={{ width: '70px', display: 'inline-block' }}>Fat:</p>
              <p style={{ display: 'inline-block' }}>{meal.fat}g</p>
            </div>
          </div>
        </div>
      ))}
    </div>
  </div>
  )
}

export default ListMeal
