import React, { useState } from "react";
import { useNavigate, Link, Outlet } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { logoutAction } from "../../store/store";
import { useTranslation } from "react-i18next"; // 👈 импорт

import "./cabinet.scss";

function Cabinet() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [showConfirm, setShowConfirm] = useState(false);
  const { t } = useTranslation(); // 👈 подключаем i18n

  const handleLogout = () => {
    localStorage.removeItem("accessToken");
    localStorage.removeItem("refreshToken");
    dispatch(logoutAction());
  };

  const handleConfirmLogout = () => {
    setShowConfirm(true);
  };

  const cancelLogout = () => {
    setShowConfirm(false);
  };

  const confirmLogout = () => {
    handleLogout();
    setShowConfirm(false);
    navigate("/");
  };

  return (
      <div className="cabinetRlc">
        <div className="cabinet">
          <div className="links">
            <Link to="/cabinet/mymatrices">{t("cabinetF.myMatrices")}</Link>
            <Link to="/cabinet/tariffs">{t("cabinetF.tariffs")}</Link>
            <Link to="/cabinet/viewhistory">{t("cabinetF.history")}</Link>
            <Link to="/">{t("matrix")}</Link>
            <Link to="/">{t("finance")}</Link>
            <Link to="/">{t("compatibility")}</Link>
            <Link to="/">{t("child")}</Link>

            <button onClick={handleConfirmLogout}>{t("cabinetF.logout")}</button>
          </div>

          <div className="content">
            <Outlet />
          </div>
        </div>

        {showConfirm && (
            <div className="modal-overlay">
              <div className="modal">
                <p>{t("cabinet.logoutConfirm")}</p>
                <div className="modal-buttons">
                  <button onClick={confirmLogout}>{t("yes")}</button>
                  <button onClick={cancelLogout}>{t("no")}</button>
                </div>
              </div>
            </div>
        )}
      </div>
  );
}

export default Cabinet;
