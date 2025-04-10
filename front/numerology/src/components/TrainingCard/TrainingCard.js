import React from "react";
import "./TrainingCard.scss";
import img from "../../assets/addservices_1.png"
const TrainingCard = () => {
  return (
    <div className="training-card">
      <div className="training-card-header">
        <img src={img} alt="Education Icon" className="icon" />
      </div>
      <div className="training-card-body">
        <h2>
          <span className="bold">УЗНАТЬ ПРО</span> <span className="highlight">ОБУЧЕНИЕ ПО МАТРИЦЕ СУДЬБЫ</span>
        </h2>
        <button className="training-button">ПЕРЕЙТИ</button>
      </div>
    </div>
  );
};

export default TrainingCard;
