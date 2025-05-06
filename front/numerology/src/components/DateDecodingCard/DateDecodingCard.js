import React, { useEffect, useState } from "react";
import "./DateDecodingCard.scss";
import axios from "axios";

const DateDecodingCard = () => {
  const [tariffs, setTariffs] = useState([]);
  const lang=localStorage.getItem("i18nextLng")

  const mockTariffs = [
    {
      name: "ДЛЯ СЕБЯ",
      subtitle: "Доступ к расшифровке одной даты",
      type: "forever"
    },
    {
      name: "ПОСЧИТАЮ ВСЕХ",
      subtitle: "Доступ ко всем калькуляторам на один месяц",
      type: "month"
    },
    {
      name: "ПРОФЕССИОНАЛ",
      subtitle: "Доступ ко всем калькуляторам на один год",
      type: "year"
    }
  ];
  const types = ["forever", "month", "year"];
  const formatDate = (date) => {
    return date.toLocaleDateString("ru-RU", {
      day: "2-digit",
      month: "2-digit",
      year: "numeric"
    });
  };
let button="";
if (lang=="en") {
  button="Buy"
} else {
  button="Ostaa"
}
  useEffect(() => {
    const getTariffs = async () => {
      try {
        const response = await axios.get("https://numerology-calculator.fi/other/tariffs/");

        const orderTypeMap = {
          1: "month",
          2: "year",
          3: "forever"
        };

        const mappedTariffs = response.data.map((item) => ({
          ...item,
          type: orderTypeMap[item.order] || null
        }));

        console.log("Mapped tariffs:", mappedTariffs); // <-- здесь уже с типами
        setTariffs(mappedTariffs);

      } catch (error) {
        console.error("Ошибка при получении тарифов:", error);
      }
    };

    getTariffs();
  }, []);

  return (
      <div className="containerRlc">
        <div className="container">
          {tariffs.length > 0 ? (
              tariffs.map((tariff, index) => {
                const today = new Date();
                let period;
                if(lang=="en"){
                  period = "Forever";
                }
                else {
                  period = "Ikuisesti"
                }

                if (tariff.type === "month") {
                  const nextMonth = new Date(today);
                  nextMonth.setMonth(nextMonth.getMonth() + 1);
                  period = `${formatDate(today)} - ${formatDate(nextMonth)}`;
                } else if (tariff.type === "year") {
                  const nextYear = new Date(today);
                  nextYear.setFullYear(nextYear.getFullYear() + 1);
                  period = `${formatDate(today)} - ${formatDate(nextYear)}`;
                }

                return (
                    <div className={`tariff-card ${tariff.type}`} key={index}>
                      <div className="tariff-content">
                        <div className="tariff-icon">
                          {tariff.type === "month" && (
                              <svg width="30px" height="30px" viewBox="0 0 24 24" fill="none">
                                <path
                                    d="M7 10.0288C7.47142 10 8.05259 10 8.8 10H15.2C15.9474 10 16.5286 10 17 10.0288M7 10.0288C6.41168 10.0647 5.99429 10.1455 5.63803 10.327C5.07354 10.6146 4.6146 11.0735 4.32698 11.638C4 12.2798 4 13.1198 4 14.8V16.2C4 17.8802 4 18.7202 4.32698 19.362C4.6146 19.9265 5.07354 20.3854 5.63803 20.673C6.27976 21 7.11984 21 8.8 21H15.2C16.8802 21 17.7202 21 18.362 20.673C18.9265 20.3854 19.3854 19.9265 19.673 19.362C20 18.7202 20 17.8802 20 16.2V14.8C20 13.1198 20 12.2798 19.673 11.638C19.3854 11.0735 18.9265 10.6146 18.362 10.327C18.0057 10.1455 17.5883 10.0647 17 10.0288M7 10.0288V8C7 5.23858 9.23858 3 12 3C14.7614 3 17 5.23858 17 8V10.0288"
                                    stroke="#000000"
                                    strokeWidth="2"
                                    strokeLinecap="round"
                                    strokeLinejoin="round"
                                />
                              </svg>
                          )}
                          {tariff.type === "forever" && (
                              <svg fill="#000000" width="30px" height="30px" viewBox="0 0 256 256">
                                <path d="M244,128a52,52,0,0,1-88.76953,36.76953q-.0857-.0857-.166-.17676L95.02832,96.80371a44,44,0,1,0,0,62.39258l8.60449-9.71533a4,4,0,1,1,5.98926,5.30371l-8.68652,9.8081q-.08057.09083-.166.17676a52,52,0,1,1,0-73.53906q.0857.0857.166.17676l60.03613,67.78906a44,44,0,1,0,0-62.39258l-8.60449,9.71533a4,4,0,1,1-5.98926-5.30371l8.68652-9.8081q.08057-.09082.166-.17676A52,52,0,0,1,244,128Z" />
                              </svg>
                          )}
                          {tariff.type === "year" && (
                              <svg width="30px" height="30px" viewBox="0 0 24 24" fill="none">
                                <circle cx="12" cy="8" r="4" fill="#000000" />
                                <path d="M4 20c0-4 4-6 8-6s8 2 8 6" stroke="#000000" strokeWidth="2" />
                              </svg>
                          )}
                        </div>
                        <div className="tariff-name">{tariff.name}</div>
                        <div className="tariff-subtitle">{tariff.description}</div>
                        <div className="tariff-period">{period}</div>
                        <div className="tariff-price">
                          {tariff.price}
                        </div>
                      </div>
                      <button className="tariff-button">{
                        button
                      }</button>
                    </div>
                );
              })
          ) : (
              <p>Загрузка тарифов...</p>
          )}
        </div>
      </div>
  );
};

export default DateDecodingCard;
