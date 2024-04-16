import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import MealType from './pages/MealType';
import ListMeal from './pages/ListMeal';
import MealInformation from './pages/MealInformation';
import Home from './pages/Home';

function App() {
  return (
    <Router>
      <div className="hero min-h-screen">
        <Routes>
          <Route exact path="/" element={<Home/>} />
          <Route exact path="/meal" element={<MealType/>} />
          <Route exact path="/meal/:mealType" element={<ListMeal/>} />
          <Route exact path="/meal/:mealType/:mealTypeId" element={<MealInformation/>} />
          
        </Routes>
      </div>
    </Router>
  );
}

export default App;
