import React, { useEffect, useState } from "react";
import axios from "axios";
import { useTranslation } from "react-i18next";
import "./ViewHistory.scss";

function ViewHistory() {
  const { t } = useTranslation();
  const BASE_URL = "https://matrixaaa.duckdns.org";
  const accessToken = localStorage.getItem("accessToken");
  const [data, setData] = useState();

  const getHistory = async (accessToken) => {
    try {
      if (accessToken) {
        const response = await axios.get(`${BASE_URL}/matrix_auth/history/`, {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        });

        setData(response.data);
      } else {
        console.log("Access token not found");
      }
    } catch (error) {
      console.error("Error while fetching history:", error);
    }
  };

  useEffect(() => {
    if (accessToken) {
      getHistory(accessToken);
    } else {
      console.log("Access token not found on page load");
    }
  }, [accessToken]);

  const handleOpen = (item) => {
    console.log(item);
    // you can add redirect or modal logic here
  };

  return (
      <div className="viewHistory">
        <table className="tariff-table">
          <thead>
          <tr>
            <th>#</th>
            <th>{t("history.category")}</th>
            <th>{t("history.date")}</th>
            <th>{t("history.action")}</th>
          </tr>
          </thead>
          <tbody>
          {data?.length > 0 ? (
              data.map((item, index) => (
                  <tr key={item.id}>
                    <td>{index + 1}</td>
                    <td>{item.category}</td>
                    <td>{new Date(item.created_at).toLocaleDateString()}</td>
                    <td>
                      <button className="open-button" onClick={() => handleOpen(item)}>
                        {t("history.open")}
                      </button>
                    </td>
                  </tr>
              ))
          ) : (
              <tr>
                <td colSpan="4">{t("history.loading")}</td>
              </tr>
          )}
          </tbody>
        </table>
      </div>
  );
}

export default ViewHistory;
