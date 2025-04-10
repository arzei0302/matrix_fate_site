import React, { useState, useEffect } from "react";
import NumerologyChart from "../../components/NumerologyChart/NumerologyChart.js";
import InfoTable from "../../components/InfoTable/InfoTable.js";
import Accordions from "../../components/Accordions/Accordions.js";
import TrainingCard  from "../../components/TrainingCard/TrainingCard.js"
import { 
  newChakraData, 
  accordionConfig, 
  newPersonalInfo, 
  months, 
  years,
  defaultAccordionData
} from "./constants.js";
import { 
  calculateNumerology, 
  getChildBusiness, 
  getChildDestiny,
  getChildParentKarma,
  getChildPersonal,
  getChildPoint,
  getChildSelf,
  getTasksFromPast
} from "../../services/childService/childService.js";
import "./child.scss";
import { useTranslation } from "react-i18next";
import DateDecodingCard from "../../components/DateDecodingCard/DateDecodingCard.js"
function Child() {
  const [numerologyData, setNumerologyData] = useState({});
  const [combinedData, setCombinedData] = useState({});
  const [year, setYear] = useState(2025);
  const [month, setMonth] = useState(months[0]);
  const [day, setDay] = useState(1);
   const { t } = useTranslation();
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

    if (day > getDaysInMonth(selectedMonth, year)) {
      setDay(1);
    }
  };

  const handleYearChange = (e) => {
    const selectedYear = Number(e.target.value);
    setYear(selectedYear);

    if (month.name === "Февраль" && day > getDaysInMonth(month, selectedYear)) {
      setDay(1);
    }
  };

  const handleCalculate = async () => {
    setCombinedData({});
    setNumerologyData({});
    try {
      const numerologyResponse = await calculateNumerology({ day, month: month.value, year });
      setNumerologyData(numerologyResponse);
  
      const requests = [
        getChildBusiness(numerologyResponse),
        getChildDestiny(numerologyResponse),
        getChildParentKarma(numerologyResponse),
        getChildPersonal(numerologyResponse),
        getChildPoint(numerologyResponse),
        getChildSelf(numerologyResponse),
        getTasksFromPast(numerologyResponse)
      ];
  
      const results = await Promise.allSettled(requests);
  
      results.forEach((result, index) => {
        if (result.status === "fulfilled") {
          const key = [
            "childBusiness","childDestiny","childParentKarma","childPersonal","childPoint","childSelf","tasksFromPast"
          ][index];
  
          updateCombinedData({ [key]: result.value });
        } else {
          console.error(`Ошибка в запросе ${index + 1}:`, result.reason);
        }
      });
  
    } catch (error) {
      console.error("Ошибка при выполнении расчёта:", error.message);
    }
  };
  

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

        <InfoTable chakraData={newChakraData} numbers={numerologyData} personalInfo={newPersonalInfo} />
    
      </div>
      <div className="accordions">
      <Accordions 
    data={combinedData} 
    defaultAccordionData={defaultAccordionData}
/></div>

   
      <DateDecodingCard  />
 

<div className="trainingCards">
      {Array.from({ length: 3 }, (_, index) => (
  <TrainingCard key={index} />
))}
</div>
     
    </div>
  );
}

export default Child;
