import React, { useEffect, useState } from "react";
import axios from "axios";
import { useTranslation } from "react-i18next";
import "./Tariffs.scss";

function Tariffs() {
  const [tariffs, setTariffs] = useState([]);
  const { t } = useTranslation();

  useEffect(() => {
    const getTariffs = async () => {
      try {
        const response = await axios.get("https://sharshenaliev.pythonanywhere.com/matrix_fate/tariffs/");
        setTariffs(response.data);
        console.log(response.data);
      } catch (error) {
        console.error("Error fetching tariffs:", error);
      }
    };

    getTariffs();
  }, []);

  return (
      <div className="tariffsRlc">
        <div className="tariffs">
          {tariffs.length > 0 ? (
              tariffs.map((tariff, index) => (
                  <div className="card" key={index}>
                    <div className="card-header">{tariff.name}</div>
                    <div className="card-body">
                      <div dangerouslySetInnerHTML={{ __html: tariff.description }} />
                      <button className="buy-button">{t("tariffs.buy")}</button>
                    </div>
                  </div>
              ))
          ) : (
              <p>{t("tariffs.loading")}</p>
          )}
        </div>
      </div>
  );
}

export default Tariffs;
