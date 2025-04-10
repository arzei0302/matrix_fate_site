import React, { useState, useEffect } from "react";
import { FaSignInAlt, FaUser, FaBars, FaTimes } from "react-icons/fa";
import { Link, useLocation } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { loginAction, logoutAction } from "../../store/store";
import "./Header.scss";
import SignIn from "../SignIn/SignIn";
import { useTranslation } from 'react-i18next'; // ✅
const Header = () => {
  const location = useLocation();
  const dispatch = useDispatch();
  const isAuthenticated = useSelector((state) => state.isAuthenticated);
  const [activeItem, setActiveItem] = useState(location.pathname);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const { t, i18n } = useTranslation() // <--- используем i18n
  const toggleLang = () => {
    const newLang = i18n.language === "fi" ? "en" : "fi";
    i18n.changeLanguage(newLang);
  };

  useEffect(() => {
    const accessToken = localStorage.getItem("accessToken");
    if (accessToken) {
      dispatch(loginAction());
    } else {
      dispatch(logoutAction());
    }
  }, [dispatch]);

  const handleSuccessfulLogin = () => {
    dispatch(loginAction());
    setIsModalOpen(false);
  };

  const handleLinkClick = (path) => {
    setActiveItem(path);
    setIsMenuOpen(false); // закрываем меню
  };

  return (
    <div className="headerRlc">
      <nav className="header">
        {/* Бургер-иконка */}
        <div className="burger-icon" onClick={() => setIsMenuOpen(!isMenuOpen)}>
          {isMenuOpen ? <FaTimes size={22} /> : <FaBars size={22} />}
        </div>

        {/* Меню */}
        <div className={`menu ${isMenuOpen ? "open" : ""}`}>
          <div className={`menu-item ${activeItem === "/" ? "active" : ""}`}>
            <Link to="/" onClick={() => handleLinkClick("/")}>{t("matrix")}</Link>
          </div>
          <div className={`menu-item ${activeItem === "/finance" ? "active" : ""}`}>
            <Link to="/finance" onClick={() => handleLinkClick("/finance")}>{t("finance")}</Link>
          </div>
          <div className={`menu-item ${activeItem === "/compatibility" ? "active" : ""}`}>
            <Link to="/compatibility" onClick={() => handleLinkClick("/compatibility")}>{t("compatibility")}</Link>
          </div>
          <div className={`menu-item ${activeItem === "/child" ? "active" : ""}`}>
            <Link to="/child" onClick={() => handleLinkClick("/child")}>{t("child")}</Link>
          </div>
          <div className={`menu-item ${activeItem === "/prognoses" ? "active" : ""}`}>
            <Link to="/prognoses" onClick={() => handleLinkClick("/prognoses")}>{t("prognosis")}</Link>
          </div>
        </div>

        {/* Аутентификация + Переключалка языка */}
        <div className="auth">
          <button className="lang-switch" onClick={toggleLang}>
            🌐 {i18n.language === "fi" ? "Suomi" : "English"}
          </button>

          {isAuthenticated ? (
            <div className="logout">
              <button className="logout-button">
                <FaUser className="icon" />
                <div><Link to="/cabinet">{t("cabinet")}</Link></div>
              </button>
            </div>
          ) : (
            <button className="login-button" onClick={() => setIsModalOpen(true)}>
              <FaSignInAlt className="icon" /> {t("login")}
            </button>
          )}
        </div>
      </nav>

      <SignIn
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        onSuccess={handleSuccessfulLogin}
      />
    </div>
  );
};

export default Header;
