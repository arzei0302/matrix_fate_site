import React, { useState } from "react";
import "./TarotReading.scss";
import cardBackImage from "../../assets/oblozhka-7978539.webp"; // Путь к рубашке карт

const TarotReading = () => {
  const totalCards = 78; // Количество карт в колоде
  const [selectedCards, setSelectedCards] = useState([]);
  const [isDeckSpread, setIsDeckSpread] = useState(false); // Раскрыта ли колода

  // Функция выбора карты
  const handleCardSelect = (index) => {
    if (selectedCards.length < 3 && !selectedCards.includes(index)) {
      setSelectedCards([...selectedCards, index]);
    }
  };

  // Функция раскладывания карт с анимацией
  const handleDeckClick = () => {
    setIsDeckSpread(true);
  };

  return (
    <div className="tarotRlc">
    <div className="tarot-container">
      <h2>
        Выберите <span className="highlight">три карты</span>
      </h2>
      <p>
        Карты раскладываются следующим образом: <br />
        <strong>Прошлое:</strong> эта карта укажет на важные события прошлого. <br />
        <strong>Настоящее:</strong> покажет текущее состояние. <br />
        <strong>Будущее:</strong> предскажет возможный исход.
      </p>

      {!isDeckSpread ? (
        <div className="tarot-stack" onClick={handleDeckClick}>
          {[...Array(10)].map((_, index) => (
            <img
              key={index}
              src={cardBackImage}
              className="tarot-card stacked"
              alt="Tarot card"
              style={{
                top: `${index * -2}px`, // Немного смещаем вверх
                left: `${index * -2}px`, // Смещаем влево для эффекта стопки
                transform: `rotate(${index * 3 - 6}deg)`, // Добавляем поворот
                zIndex: 10 - index, // Контролируем порядок наложения
              }}
            />
          ))}
          <p className="click-to-spread">Нажмите, чтобы разложить</p>
        </div>
      ) : (
        <div className="tarot-deck">
          {[...Array(totalCards)].map((_, index) => (
            <img
              key={index}
              src={cardBackImage}
              className={`tarot-card ${selectedCards.includes(index) ? "chosen" : ""} spread`}
              alt="Tarot card"
              onClick={() => handleCardSelect(index)}
              style={{ animationDelay: `${index * 0.05}s` }} // Эффект постепенного разложения
            />
          ))}
        </div>
      )}
    </div>
    </div>
  );
};

export default TarotReading;
