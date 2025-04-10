import React from "react";
import { Routes, Route, useNavigate } from "react-router-dom";
// import UniversePage from "./UniversePage";
// import ArcanumGetPage from "./ArcanumGetPage";
// import ArcanumChoosePage from "./ArcanumChoosePage";
import "./additional.scss";

function Additional() {
  const navigate = useNavigate();

  return (
    <div className="additinonal-pageRlc">
      <div className="additional-page">
        
  
        {/* Главная сетка Additional */}
        <div className="cards-wrapper">
          <div className="block">
            <div className="card">
              <h2>
                Рассчитать <span className="badge">финкод</span> и{" "}
                <span className="badge">антикод</span>
              </h2>
              <p className="highlight">Зачем вам ФИНАНСОВЫЙ КОД?</p>
              <p className="description">...</p>
              <button className="primary-button" onClick={() => navigate("fincode")}>
                РАССЧИТАТЬ
              </button>
            </div>

            <div className="card">
              <h2>Подсказки <span className="badge">Вселенной</span></h2>
              <p className="description">...</p>
              <button className="primary-button" onClick={() => navigate("universe")}>
                РАССЧИТАТЬ
              </button>
            </div>
          </div>

          <div className="block">
            <div className="card">
              <h2>Подсказки <span className="badge">Арканов</span></h2>
              <p className="description">...</p>
              <button className="primary-button" onClick={() => navigate("/additional/question")}>
                ПОЛУЧИТЬ
              </button>
            </div>

            <div className="card">
              <h2>Подсказки <span className="badge">Арканов</span></h2>
              <p className="description">...</p>
              <button className="primary-button" onClick={() => navigate("arcanum/choose")}>
                ВЫБРАТЬ
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Additional;
