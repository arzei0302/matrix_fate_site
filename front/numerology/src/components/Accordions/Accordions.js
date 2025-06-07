import * as React from 'react';
import { useState, useEffect } from 'react';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import Typography from '@mui/material/Typography';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import LockIcon from '@mui/icons-material/Lock';
import KeyboardArrowUpIcon from '@mui/icons-material/KeyboardArrowUp';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import { useTranslation } from 'react-i18next';
import './Accordions.scss';

const Accordions = ({ data, programs }) => {
  const [expanded, setExpanded] = useState(null);
  const [expandedPrograms, setExpandedPrograms] = useState([]);
  const [accordionData, setAccordionData] = useState([]);
  const { t } = useTranslation();
  const accessToken = localStorage.getItem("accessToken");

  useEffect(() => {
    if (!data || typeof data !== 'object') return;

    const transformedData = Object.entries(data).map(([key, value]) => {
      const val = Array.isArray(value) && value.length > 0 ? value[0] : value;
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

  const toggleProgram = (key) => {
    setExpandedPrograms((prev) =>
        prev.includes(key) ? prev.filter((k) => k !== key) : [...prev, key]
    );
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
                expanded={expanded === `panel-${index}` && !content.is_paid}
                onChange={handleChange(`panel-${index}`)}
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
                    <a
                        href="#"
                        className={`unlock-link ${
                            expanded === `panel-${index}` ? 'active' : ''
                        }`}
                    >
                      {t('unlock')}
                    </a>
                )}
              </AccordionSummary>

              {!content.is_paid && (
                  <AccordionDetails>
                    <Typography
                        variant="body1"
                        dangerouslySetInnerHTML={{
                          __html: t(content.description || 'noDescription'),
                        }}
                    />
                    {renderNestedTalents(content)}
                  </AccordionDetails>
              )}
            </Accordion>
        ))}
        {/* Программы */}
        {programs && programs.length > 0 && (
            <Accordion expanded={expanded === 'programs'} onChange={handleChange('programs')}>
              <AccordionSummary expandIcon={<ExpandMoreIcon />}>
                <Typography component="span" className="accordion-title">
                  {t("programs")}
                </Typography>
              </AccordionSummary>
              <AccordionDetails>
                <div className="program-list">
                  {programs.map((program, idx) => {
                    const key = `program-inner-${idx}`;
                    const title = program.name || `${program.marker_1_value}-${program.marker_2_value}-${program.marker_3_value} ${t(program.name)}`;

                    const hasIsPaid = typeof program.is_paid !== 'undefined';
                    const isUnregistered = !accessToken || !hasIsPaid;
                    const isLocked = program.is_paid === true || isUnregistered;

                    const isInnerExpanded = expandedPrograms.includes(key);

                    return (
                        <div className="program-item" key={key}>
                          <div
                              className={`program-header ${isLocked ? 'locked' : ''}`}
                              onClick={() => {
                                if (!isLocked) toggleProgram(key);
                              }}
                          >
                            {isLocked ? (
                                <LockIcon fontSize="small" />
                            ) : (
                                isInnerExpanded ? <KeyboardArrowDownIcon fontSize="small" /> : <KeyboardArrowUpIcon fontSize="small" />
                            )}
                            <Typography variant="body2">{t(title)}</Typography>
                          </div>

                          {!isLocked && isInnerExpanded && (
                              <div className="program-description">
                                <Typography
                                    variant="body2"
                                    dangerouslySetInnerHTML={{
                                      __html: t(program.description || 'noDescription'),
                                    }}
                                />
                              </div>
                          )}
                        </div>
                    );
                  })}
                </div>
              </AccordionDetails>
            </Accordion>
        )}

        {/* Основные таланты */}

      </div>
  );
};

export default Accordions;
