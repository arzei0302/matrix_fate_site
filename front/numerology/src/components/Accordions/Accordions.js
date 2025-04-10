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
  const [accordionData, setAccordionData] = useState(defaultAccordionData);
  const { t } = useTranslation();

  useEffect(() => {
    if (Object.keys(data).length > 0) {
      const normalizedData = {};

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

      const newAccordionData = Object.entries(normalizedData).map(([key, value]) => {
        return {
          key,
          ...value,
          title: value.category?.title || value.title || key,
          description: value.description || '',
          is_paid: value.is_paid ?? false
        };
      });

      setAccordionData(newAccordionData);
    }
  }, [data]);

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
          expanded={expanded === index}
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
                dangerouslySetInnerHTML={{ __html: t(content?.description ?? 'noDescription') }}
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
