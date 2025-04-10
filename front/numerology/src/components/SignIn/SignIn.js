import React, { useState } from "react";
import axios from "axios";
import "./SignIn.scss";

const SignIn = ({ isOpen, onClose, onSuccess }) => {
  const [step, setStep] = useState(1);
  const [login, setLogin] = useState("");
  const [code, setCode] = useState("");
  const [showInfoModal, setShowInfoModal] = useState(false);
  const BASE_URL = "https://matrixaaa.duckdns.org";

  if (!isOpen) return null;

  const sendEmail = async (data) => {
    setShowInfoModal(true); 
    if (!data.login) return;
    try {
      await axios.post(`${BASE_URL}/matrix_auth/send-code/`, {
        email: data.login,
      });
      setStep(2);
    // Показать сообщение

      setTimeout(() => {
        setShowInfoModal(false); // Авто-скрытие через 3 сек
      }, 1000);
    } catch (error) {
      console.log(error);
    }
  };

  const sendToken = async (data) => {
    try {
      const response = await axios.post(`${BASE_URL}/matrix_auth/verify-code/`, {
        email: data.login,
        code: data.code,
      });

      if (response.data.access && response.data.refresh) {
        localStorage.setItem("accessToken", response.data.access);
        localStorage.setItem("refreshToken", response.data.refresh);

        if (onSuccess) onSuccess();
      }
    } catch (error) {
      console.log("Ошибка при отправке кода:", error);
    }
  };

  return (
    <div className="signInContentOverlay" onClick={onClose}>
      <div className="signInContent" onClick={(e) => e.stopPropagation()}>
        <button className="close-button" onClick={onClose}>✖</button>
        <div className="signInTitle">Войти</div>

        {step === 1 ? (
          <>
            <input
              type="text"
              placeholder="Введите почту"
              value={login}
              onChange={(e) => setLogin(e.target.value)}
            />
            <button className="signInButton" onClick={() => sendEmail({ login })}>Дальше</button>
          </>
        ) : (
          <>
            <input type="text" value={login} disabled />
            <input
              type="text"
              placeholder="Введите код"
              value={code}
              onChange={(e) => setCode(e.target.value)}
            />
            <div className="signInButtons">
              <button className="nextButton" onClick={() => sendToken({ login, code })}>Войти</button>
              <button className="backButton" onClick={() => setStep(1)}>Назад</button>
            </div>
          </>
        )}

        {showInfoModal && (
          <div className="info-modal">
            📧 Код отправлен на вашу почту
          </div>
        )}
      </div>
    </div>
  );
};

export default SignIn;
