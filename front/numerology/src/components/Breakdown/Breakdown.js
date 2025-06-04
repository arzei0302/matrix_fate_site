import React, { useEffect, useState } from "react";
import axios from "axios";
import { useTranslation } from "react-i18next";
import Accordion from "@mui/material/Accordion";
import AccordionSummary from "@mui/material/AccordionSummary";
import AccordionDetails from "@mui/material/AccordionDetails";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import ChevronLeftIcon from "@mui/icons-material/ChevronLeft";
import ChevronRightIcon from "@mui/icons-material/ChevronRight";
import IconButton from "@mui/material/IconButton";
import Typography from "@mui/material/Typography";
import './Breakdown.scss'; // 👈 тот же файл стилей, что и твой Accordions

const Breakdown = () => {
    const [data, setData] = useState(null);
    const [page, setPage] = useState(1);
    const [expanded, setExpanded] = useState(false);
    const [error, setError] = useState(null);
    const { t } = useTranslation();

    const fetchBreakdown = async (currentPage) => {
        try {
            const token = localStorage.getItem("accessToken");
            const response = await axios.get(
                `https://numerology-calculator.fi/api/prognisis/api/breakdown/?page=${currentPage}&page_size=0`,
                {
                    headers: {
                        Authorization: `Bearer ${token}`
                    }
                }
            );
            setData(response.data.results?.[0] || null);
        } catch (err) {
            console.error("Ошибка при получении breakdown:", err);
            setError("Ошибка загрузки данных");
        }
    };

    useEffect(() => {
        fetchBreakdown(page);
    }, [page]);

    const handleNext = () => setPage((prev) => prev + 1);
    const handlePrev = () => setPage((prev) => (prev > 0 ? prev - 1 : 0));

    return (
        <div className="accordion-container">
            <Accordion expanded={expanded} onChange={() => setExpanded(!expanded)}>
                <AccordionSummary expandIcon={<ExpandMoreIcon />}>
                    <Typography component="span" className="accordion-title">
                        {t("financePage.breakdownTitle", "Разбор по годам")}
                    </Typography>
                </AccordionSummary>
                <AccordionDetails>
                    {!data && !error && <div>{t("financePage.loading", "Загрузка...")}</div>}
                    {data && (
                        <div className="breakdown-card">
                            <div className="navigation">
                                <IconButton onClick={handlePrev} disabled={page === 1}>
                                    <ChevronLeftIcon />
                                </IconButton>
                                <span className="page-number">{data.title}</span>
                                <IconButton onClick={handleNext} disabled={page === data.total}>
                                    <ChevronRightIcon />
                                </IconButton>
                            </div>
                            <div
                                className="breakdown-description"
                                dangerouslySetInnerHTML={{ __html: data.description }}
                            />
                        </div>
                    )}
                </AccordionDetails>
            </Accordion>
        </div>
    );
};

export default Breakdown;
