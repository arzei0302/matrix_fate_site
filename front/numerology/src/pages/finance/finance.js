import React, { useState, useEffect } from "react";
import { useTranslation } from "react-i18next";
import axios from "axios";
import NumerologyChart from "../../components/NumerologyChart/NumerologyChart";
import InfoTable from "../../components/InfoTable/InfoTable";
import Accordions from "../../components/Accordions/Accordions";
import DateDecodingCard from "../../components/DateDecodingCard/DateDecodingCard";

import {
  newChakraData,
  newPersonalInfo,
  months,
  years,
} from "./constants";

import {
  calculateNumerology,
  getBlocksMoney,
  getDestinationSociety,
  getFincanceOpportunity,
  getKarmaTask,
  getTalents,
  getWhatGivesMoney
} from "../../services/financeService/financeService.js";

import "./finance.scss";

function Finance() {
  const { t } = useTranslation();
  const [numerologyData, setNumerologyData] = useState({});
  const [combinedData, setCombinedData] = useState({});
  const [year, setYear] = useState(2025);
  const [month, setMonth] = useState(months[0]);
  const [day, setDay] = useState(1);
  const [error, setError] = useState(null);

  const updateCombinedData = (newData) => {
    setCombinedData((prevData) => ({
      ...prevData,
      ...newData
    }));
  };

  const getDaysInMonth = (month, year) => {
    if (month.name === "Февраль") {
      return year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0) ? 29 : 28;
    }
    return month.days;
  };

  const handleMonthChange = (e) => {
    const selectedMonth = months.find(m => m.name === e.target.value);
    setMonth(selectedMonth);
    if (day > getDaysInMonth(selectedMonth, year)) setDay(1);
  };

  const handleYearChange = (e) => {
    const selectedYear = Number(e.target.value);
    setYear(selectedYear);
    if (month.name === "Февраль" && day > getDaysInMonth(month, selectedYear)) setDay(1);
  };

  const handleCalculate = async () => {
    setCombinedData({});
    setNumerologyData({});
    try {
      const numerologyResponse = await calculateNumerology({ day, month: month.value, year });
      setNumerologyData(numerologyResponse);
      console.log(numerologyResponse.matched_programs)
      const blocksMoneyResponse = await getBlocksMoney(numerologyResponse);
      updateCombinedData({ blocksMoney: blocksMoneyResponse });

      const destinationSocietyResponse = await getDestinationSociety(numerologyResponse);
      updateCombinedData({ destinationSociety: destinationSocietyResponse });

      const financeOpportunityResponse = await getFincanceOpportunity(numerologyResponse);
      updateCombinedData({ financeOpportunity: financeOpportunityResponse });

      const karmaTaskResponse = await getKarmaTask(numerologyResponse);
      updateCombinedData({ karmaTask: karmaTaskResponse });

      const talentsResponse = await getTalents(numerologyResponse);
      updateCombinedData({ talents: talentsResponse });

      const whatGivesMoneyResponse = await getWhatGivesMoney(numerologyResponse);
      updateCombinedData({ whatGivesMoney: whatGivesMoneyResponse });
    } catch (error) {
      console.error("Ошибка при выполнении расчёта:", error.message);
    }
  };

  const handleDownload = async () => {
    document.body.style.cursor = "wait";
    const payload = {
      day,
      month: month.value,
      year
    };

    try {
      const response = await axios.post(
          "https://numerology-calculator.fi/api/finance/guest-finance-pdf/",
          payload,
          {
            responseType: "blob"
          }
      );

      const blob = new Blob([response.data], { type: "application/pdf" });
      const url = window.URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", "guest_finance_report.pdf");
      document.body.appendChild(link);
      link.click();
      link.remove();
      window.URL.revokeObjectURL(url);
    } catch (error) {
      console.error("Ошибка при скачивании PDF:", error);
    } finally {
      document.body.style.cursor = "auto"; // возвращаем обычный курсор
    }
  };

  // Вызов handleCalculate при первоначальной загрузке компонента
  useEffect(() => {
    handleCalculate(); // только для аккордеонов
  }, []);  // [] - чтобы сработало только при первом рендере

  return (
      <div className="FateRlc">
        <div className="Fate">
          <div className="FateFirstColumn">
            <div className="birthdate-container">
              <span className="bd-text">{t("financePage.enterBirthDate")}</span>

              <div className="select-container">
                <label className="select-label">{t("financePage.day")}</label>
                <select className="custom-select" value={day} onChange={(e) => setDay(Number(e.target.value))}>
                  {Array.from({ length: getDaysInMonth(month, year) }, (_, i) => i + 1).map((d) => (
                      <option key={d} value={d}>{d}</option>
                  ))}
                </select>
              </div>

              <div className="select-container">
                <label className="select-label">{t("financePage.month")}</label>
                <select className="custom-select" value={month.name} onChange={handleMonthChange}>
                  {months.map((m) => (
                      <option key={m.name} value={m.name}>{t(`months.${m.value}`)}</option>
                  ))}
                </select>
              </div>

              <div className="select-container">
                <label className="select-label">{t("financePage.year")}</label>
                <select className="custom-select" value={year} onChange={handleYearChange}>
                  {years.map((y) => (
                      <option key={y} value={y}>{y}</option>
                  ))}
                </select>
              </div>
              <button onClick={handleCalculate}>{t("financePage.calculate")}</button>
            </div>

            <NumerologyChart numbers={numerologyData} onCalculate={handleCalculate} />
          </div>

          <InfoTable
              chakraData={newChakraData}
              numbers={numerologyData}
              personalInfo={newPersonalInfo}
              showChakraTable={false}
          />
        </div>
        <button className='downloadBtn' onClick={handleDownload}>{t("financePage.download")}</button>
        <div className="accordions">
          <Accordions data={combinedData} programs={numerologyData.matched_programs} />
        </div>

        <DateDecodingCard />
      </div>
  );
}

export default Finance;
