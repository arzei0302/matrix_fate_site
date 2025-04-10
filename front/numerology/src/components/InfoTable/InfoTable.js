import React from "react";
import "./InfoTable.scss";
import bracket from "../../assets/bezimeni-6-kopiya-8982948.webp";
import { useTranslation } from "react-i18next";

const InfoTable = ({ chakraData, numbers, personalInfo, showChakraTable = true }) => {
  const { t } = useTranslation();

  return (
    <div className="infoTable">
      {/* Таблица чакр */}
      {showChakraTable && (
        <div className="chakraTable">
          <h2 className="chakra-title">{t("infoTable.title")}</h2>
          <p className="chakra-subtitle">{t("infoTable.subtitle")}</p>

          <table>
            <thead>
              <tr>
                <th>{t("infoTable.chakraName")}</th>
                <th>{t("infoTable.body")}</th>
                <th>{t("infoTable.energy")}</th>
                <th>{t("infoTable.emotion")}</th>
              </tr>
            </thead>
            <tbody>
              {chakraData?.slice().reverse().map((chakra, index) => {
                const oKey = `o${7 - index}`;
                const pKey = `p${7 - index}`;
                const qKey = `q${7 - index}`;
                return (
                  <tr key={index} style={{ backgroundColor: chakra.color }}>
                    <td>{t(`chakra_${7 - index}`)}</td>
                    <td>{numbers?.[oKey] ?? 0}</td>
                    <td>{numbers?.[pKey] ?? 0}</td>
                    <td>{numbers?.[qKey] ?? 0}</td>
                  </tr>
                );
              })}
            </tbody>
            <tfoot>
              <tr className="totalRow">
                <td>{t("infoTable.total")}</td>
                <td>{numbers.o ?? 0}</td>
                <td>{numbers?.p ?? 0}</td>
                <td>{numbers?.q ?? 0}</td>
              </tr>
            </tfoot>
          </table>
        </div>
      )}

      {/* Личный расчет */}
      <div className="personalInfo">
        {personalInfo?.map((info, index) => (
          <div key={index}>
            <div className="personalInfoContent">
              <div className="personalInfoLeftTop">
                <span>{t(info.title)}</span>
                <p>{t(info.description)}</p>
              </div>
              <div className="personalInfoLeftMiddle">
                <div className="elements">
                  <div className="sky">
                    {t(info.skyLabel)}: <span>{numbers?.[info.skyKey] ?? 0}</span>
                  </div>
                  <div className="earth">
                    {t(info.earthLabel)}: <span>{numbers?.[info.earthKey] ?? 0}</span>
                  </div>
                </div>
                <img src={bracket} alt="Bracket" />
                <div className="result">{numbers?.[info.resultKey] ?? 0}</div>
              </div>
              <div className="personalInfoLeftBottom">
                <div className="spirit">
                  {t(info.spiritLabel)}: <span>{numbers?.[info.spiritKey] ?? 0}</span>
                </div>
                <div className="question">{t(info.question)}</div>
              </div>
            </div>
            {index < personalInfo.length - 1 && <div className="horizontalLine"></div>}
          </div>
        ))}
      </div>
    </div>
  );
};

export default InfoTable;
