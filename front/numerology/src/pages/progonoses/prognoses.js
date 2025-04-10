import React, { useState, useEffect } from "react";
import {
    newChakraData,
    accordionConfig,
    newPersonalInfo,
    months,
    years,
    defaultAccordionData
} from "./constants.js";
import DateDecodingCard from "../../components/DateDecodingCard/DateDecodingCard.js";
import Accordions from "../../components/Accordions/Accordions.js";
import './prognoses.scss';
import axios from "axios";
import { useTranslation } from "react-i18next";

function Prognoses() {
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

    const BASE_URL = "https://matrixaaa.duckdns.org";
    const handleCalculate = async () => {
        setCombinedData({});
        setNumerologyData({});
        setError(null);

        // Форматируем дату рождения
        const formattedDay = day < 10 ? `0${day}` : day;
        const formattedMonth = month.value < 10 ? `0${month.value}` : month.value;
        const dateBirth = `${formattedDay}.${formattedMonth}.${year}`;

        try {
            const response = await axios.get(`${BASE_URL}/prognisis/prognosis/?birth_date=${dateBirth}`);
            console.log("Ответ от сервера:", response.data);
            setCombinedData(response.data);
        } catch (error) {
            console.error("Ошибка при выполнении расчёта:", error.message);
            setError("Произошла ошибка при получении прогноза");
        }
    };

    useEffect(() => {
        console.log("combinedData:", combinedData);
    }, [combinedData]);

    return (
        <div className="prognoses">
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

            {error && <div className="error-message">{error}</div>}

            <div className="accordions">
                <Accordions
                    data={combinedData}
                    defaultAccordionData={defaultAccordionData}
                />
            </div>

            <DateDecodingCard />
        </div>
    );
}

export default Prognoses;
