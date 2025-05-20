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

const Accordions = ({ data }) => {
  const [expanded, setExpanded] = useState(null);
  const [accordionData, setAccordionData] = useState([]);
  const { t } = useTranslation();
  console.log('accdata',data)
  useEffect(() => {
    if (!data || typeof data !== 'object') return;

    const transformedData = Object.entries(data).map(([key, value]) => {
      const val = Array.isArray(value) && value.length > 0 ? value[0] : value;

      // 🧠 распаковка, если category внутри category
      const realCategory = val?.category?.category || val?.category || {};
      const isPaid = realCategory?.is_paid ?? val?.is_paid ?? false;

      return {
        key,
        title: realCategory?.title || val?.title || key,
        description: val?.description || '',
        is_paid: isPaid,
        category: realCategory
      };
    });

    setAccordionData(transformedData);
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
    if (content.is_paid) return null;

    const talents = [];

    if (typeof content.category === 'object') {
      for (const value of Object.values(content.category)) {
        if (typeof value === 'object' && (value.title || value.description)) {
          talents.push(renderTalent(value));
        }
      }
    }

    return talents;
  };

  return (
      <div className="accordion-container">
        {accordionData.map((content, index) => (
            <Accordion
                key={index}
                expanded={expanded === index && !content.is_paid}
                onChange={handleChange(index)}
                className={content.is_paid ? 'locked' : ''}
            >
              <AccordionSummary
                  expandIcon={content.is_paid ? <LockIcon /> : <ExpandMoreIcon />}
                  onClick={(e) => {
                    if (content.is_paid) {
                      e.stopPropagation();
                      e.preventDefault();
                    }
                  }}
              >
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
                          __html: t(content.description || 'noDescription')
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
