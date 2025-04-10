import React, { useState } from "react";
import NumerologyChart from "../../components/NumerologyChart/NumerologyChart";
import InfoTable from "../../components/InfoTable/InfoTable";
import { 
    newChakraData, 
    newPersonalInfo,
    months, 
    years,
    defaultAccordionData
} from "./constants";
import "./compatibility.scss";
import CompabilitySchema from "../../components/CompabilitySchema/CompabilitySchema";
import Accordions from "../../components/Accordions/Accordions";
import DateDecodingCard from "../../components/DateDecodingCard/DateDecodingCard.js";
import { 
  getChildBusiness,
  getChildDestiny,
  getChildParentKarma,
  getChildPersonal,
  getChildPoint,
  getChildSelf,
  getTasksFromPast
} from "../../services/compability/compability.js";
import api from "../../services/axiosInstance.js"; 
import { useTranslation } from "react-i18next";
function Compatibility() {
  const [numerologyData, setNumerologyData] = useState({});
  const [combinedData, setCombinedData] = useState({});
  const [numerologyData1, setNumerologyData1] = useState({});
const [numerologyData2, setNumerologyData2] = useState({});
  const { t } = useTranslation();
  const [year, setYear] = useState(2025);
  const [month, setMonth] = useState(months[0]);
  const [day, setDay] = useState(1);
  
  const [year1, setYear1] = useState(2025);
  const [month1, setMonth1] = useState(months[0]);
  const [day1, setDay1] = useState(1);
  
  const getDaysInMonth = (month, year) => {
    if (month.name === "Февраль") {
      return year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0) ? 29 : 28;
    }
    return month.days;
  };
  const updateCombinedData = (newData) => {
    setCombinedData((prevData) => ({
      ...prevData,
      ...newData
    }));
  };
  // Обработчики изменения даты
  const handleMonthChange = (e) => {
    const selectedMonth = months.find(m => m.name === e.target.value);
    setMonth(selectedMonth);
    if (day > getDaysInMonth(selectedMonth, year)) {
      setDay(1);
    }
  };

  const handleMonthChange1 = (e) => {
    const selectedMonth = months.find(m => m.name === e.target.value);
    setMonth1(selectedMonth);
    if (day1 > getDaysInMonth(selectedMonth, year1)) {
      setDay1(1);
    }
  };

  const handleYearChange = (e) => {
    const selectedYear = Number(e.target.value);
    setYear(selectedYear);
    if (month.name === "Февраль" && day > getDaysInMonth(month, selectedYear)) {
      setDay(1);
    }
  };

  const handleYearChange1 = (e) => {
    const selectedYear = Number(e.target.value);
    setYear1(selectedYear);
    if (month1.name === "Февраль" && day1 > getDaysInMonth(month1, selectedYear)) {
      setDay1(1);
    }
  };
  const handleCalculate = async () => {
    setNumerologyData({})
    setNumerologyData1({});
    setNumerologyData2({});
    setCombinedData({});

    try {
        const [compatibilityResponse, matrixResponse1, matrixResponse2] = await Promise.all([
            api.post(`https://matrixaaa.duckdns.org/compatibility/calculate-compatibility/`, {
                day,
                month: month.value,
                year,
                day2: day1,
                month2: month1.value,
                year2: year1,
            }),
            api.post(`https://matrixaaa.duckdns.org/compatibility/calculate-matrix/`, {
                day,
                month: month.value,
                year,
            }),
            api.post(`https://matrixaaa.duckdns.org/compatibility/calculate-matrix/`, {
                day: day1,
                month: month1.value,
                year: year1,
                 category:"compatibility"
            })
        ]);

        setNumerologyData(compatibilityResponse.data);
        setNumerologyData1(matrixResponse1.data);
        setNumerologyData2(matrixResponse2.data);
        
        const requests = [
            getChildBusiness(matrixResponse1.data),
            getChildDestiny(matrixResponse1.data),
            getChildParentKarma(matrixResponse1.data),
            getChildPersonal(matrixResponse1.data),
            getChildPoint(matrixResponse1.data),
            getChildSelf(matrixResponse1.data),
            getTasksFromPast(matrixResponse1.data),
        ];

        const results = await Promise.allSettled(requests);

        results.forEach((result, index) => {
            if (result.status === "fulfilled") {
                const keys = [
                    "childBusiness",
                    "childDestiny",
                    "childParentKarma",
                    "childPersonal",
                    "childPoint",
                    "childSelf",
                    "tasksFromPast"
                ];
                updateCombinedData({ [keys[index]]: result.value });
            } else {
                console.error(`Ошибка в запросе ${index + 1}:`, result.reason);
            }
        });

    } catch (error) {
        console.error("Ошибка при выполнении расчёта:", error.message);
    }
};


  
  // Функция для запроса совместимости
  

  return (
    <div className="compatibilityRlc">
      <div className="compatibility">
        <div className="pairSchema">
          <div className="schema">
          <div className="birthdate-container">
              <span className="bd-text">{t("financePage.enterBirthDate")}</span>
              <div className="select-container">
                <label className="select-label">{t("financePage.day")}</label>
                <select className="custom-select" value={day} onChange={(e) => setDay(Number(e.target.value))}>
                  {Array.from({ length: getDaysInMonth(month, year) }, (_, i) => (
                    <option key={i} value={i + 1}>{i + 1}</option>
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
            </div>

            <div className="NumerologyChart">
              <NumerologyChart numbers={numerologyData1} />
            </div>
            <InfoTable chakraData={newChakraData} numbers={numerologyData1} personalInfo={newPersonalInfo} showChakraTable={false} />
          </div>

          <div className="schema">
          <div className="birthdate-container">
              <span className="bd-text">{t("financePage.enterBirthDate")}</span>
              <div className="select-container">
                <label className="select-label">{t("financePage.day")}</label>
                <select className="custom-select" value={day1} onChange={(e) => setDay1(Number(e.target.value))}>
                  {Array.from({ length: getDaysInMonth(month1, year1) }, (_, i) => (
                    <option key={i} value={i + 1}>{i + 1}</option>
                  ))}
                </select>
              </div>
              <div className="select-container">
                <label className="select-label">{t("financePage.month")}</label>
                <select className="custom-select" value={month1.name} onChange={handleMonthChange1}>
                  {months.map((m) => (
                    <option key={m.name} value={m.name}>{t(`months.${m.value}`)}</option>
                  ))}
                </select>
              </div>
              <div className="select-container">
                <label className="select-label">{t("financePage.year")}</label>
                <select className="custom-select" value={year1} onChange={handleYearChange1}>
                  {years.map((y) => (
                    <option key={y} value={y}>{y}</option>
                  ))}
                </select>
              </div>
            </div>

            <div className="NumerologyChart">
              <NumerologyChart numbers={numerologyData2} />
            </div>
            <InfoTable chakraData={newChakraData} numbers={numerologyData2} personalInfo={newPersonalInfo} showChakraTable={false} />
          </div>
        </div>

        <div className="compabilitySchema">
          <div className="compabilitySchemaAction">
            <p>{t("financePage.commatrix")}</p>

            <button onClick={handleCalculate}>{t("financePage.btn")}</button>
          </div>
          <CompabilitySchema personalInfo={newPersonalInfo} numbers={numerologyData}  />
        </div>
        
        <Accordions data={combinedData} defaultAccordionData={defaultAccordionData} />
      </div>

      <DateDecodingCard />
    </div>
  );
}

export default Compatibility;
