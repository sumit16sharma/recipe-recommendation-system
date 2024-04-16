import React from 'react'
import { Link } from 'react-router-dom';

const MealType = () => {
  return (
    <div>
  <h1 className="text-4xl font-bold mb-10 text-center">Choose one of the meals</h1>
  <div className="p-4 grid grid-cols-3 gap-4">
    <Link to="/meal/snack" className="bg-gray-800 rounded-lg shadow-lg overflow-hidden block">
      <img className="w-full h-64 object-cover" src='https://images.pexels.com/photos/70497/pexels-photo-70497.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1' alt="Snack" />
      <div className="p-4">
        <h2 className="text-lg font-bold mb-2 text-white">Snack</h2>
      </div>
    </Link>
    <Link to="/meal/dessert" className="bg-gray-800 rounded-lg shadow-lg overflow-hidden block">
      <img className="w-full h-64 object-cover" src='https://images.pexels.com/photos/1854652/pexels-photo-1854652.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1' alt="Dessert" />
      <div className="p-4">
        <h2 className="text-lg font-bold mb-2 text-white">Dessert</h2>
      </div>
    </Link>
    <Link to="/meal/appetizer" className="bg-gray-800 rounded-lg shadow-lg overflow-hidden block">
      <img className="w-full h-64 object-cover" src='https://images.pexels.com/photos/1639556/pexels-photo-1639556.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1' alt="Appetizer" />
      <div className="p-4">
        <h2 className="text-lg font-bold mb-2 text-white">Appetizer</h2>
      </div>
    </Link>
  </div>
</div>

  )
}

export default MealType
