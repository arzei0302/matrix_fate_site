import * as React from 'react';
import { useState, useEffect } from 'react';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import Typography from '@mui/material/Typography';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import LockIcon from '@mui/icons-material/Lock';
import { useTranslation } from 'react-i18next';
import './Accordions.scss';

const Accordions = ({ data, defaultAccordionData }) => {
  const [expanded, setExpanded] = useState(null);
  const [accordionData, setAccordionData] = useState([]);
  const { t } = useTranslation();

  useEffect(() => {
    const normalizedData = {};

    // Преобразуем входящие данные (успешные и 403)
    if (data && typeof data === 'object') {
      Object.keys(data).forEach((key) => {
        const value = data[key];

        if (Array.isArray(value) && value.length > 0 && typeof value[0] === 'object') {
          normalizedData[key] = {
            ...value[0],
            is_paid: false
          };
        } else if (typeof value === 'object') {
          normalizedData[key] = {
            ...value,
            is_paid: value.is_paid ?? false
          };
        }
      });
    }

    // Обновляем те, что уже есть в defaultAccordionData
    const merged = defaultAccordionData.map((item) => {
      const incoming = normalizedData[item.key];
      return {
        ...item,
        ...incoming,
        title: incoming?.category?.title || incoming?.title || item.title,
        description: incoming?.description || item.description || '',
        is_paid: incoming?.is_paid ?? item.is_paid ?? false,
        category: incoming?.category || item.category || {}
      };
    });

    // Добавляем новые секции, которых не было в defaultAccordionData
    const newKeys = Object.keys(normalizedData).filter(
        (key) => !defaultAccordionData.some((item) => item.key === key)
    );

    const newData = newKeys.map((key) => {
      const value = normalizedData[key];
      return {
        key,
        title: value.category?.title || value.title || key,
        description: value.description || '',
        is_paid: value.is_paid ?? false,
        category: value.category || {}
      };
    });

    // Объединяем всё
    setAccordionData([...merged, ...newData]);
  }, [data, defaultAccordionData]);

  const handleChange = (panel) => (event, isExpanded) => {
    setExpanded(isExpanded ? panel : null);
  };

  const renderTalent = (talent) => {
    if (!talent) return null;

    return (
        <div className="talent-block" key={talent.title}>
          <Typography variant="subtitle1">{t(talent.title)}</Typography>
          {talent.description?.includes('<') ? (
              <Typography
                  variant="body2"
                  dangerouslySetInnerHTML={{ __html: t(talent.description) }}
              />
          ) : (
              <Typography variant="body2">{t(talent.description)}</Typography>
          )}
        </div>
    );
  };

  const renderNestedTalents = (content) => {
    if (content.is_paid) return null;

    const talents = [];

    if (typeof content.category === 'object') {
      for (const value of Object.values(content.category)) {
        if (
            typeof value === 'object' &&
            value !== null &&
            (value.title || value.description)
        ) {
          talents.push(renderTalent(value));
        }
      }
    }

    return talents;
  };

  return (
      <div className="accordion-container">
        {accordionData?.map((content, index) => (
            <Accordion
                key={index}
                expanded={expanded === index && !content.is_paid}
                onChange={handleChange(index)}
                className={content.is_paid ? 'locked' : ''}
            >
              <AccordionSummary expandIcon={content.is_paid ? <LockIcon /> : <ExpandMoreIcon />}>
                <Typography component="span" className="accordion-title">
                  {t(content.title)}
                </Typography>
                {content.is_paid && (
                    <a href="#" className={`unlock-link ${expanded === index ? 'active' : ''}`}>
                      {t("unlock")}
                    </a>
                )}
              </AccordionSummary>

              {!content.is_paid && (
                  <AccordionDetails>
                    <Typography
                        variant="body1"
                        dangerouslySetInnerHTML={{
                          __html: t(content?.description || 'noDescription')
                        }}
                    />
                    {renderNestedTalents(content)}
                  </AccordionDetails>
              )}
            </Accordion>
        ))}
      </div>
  );
};

export default Accordions;
