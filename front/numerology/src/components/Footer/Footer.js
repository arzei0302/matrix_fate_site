import React, { useState, useEffect } from "react";
import { useTranslation } from "react-i18next";
import "./Footer.scss";
import telegramIcon from "../../assets/telegram.png";
import VKIcon from "../../assets/VKLogo.png";
import axios from "axios";

const Footer = () => {
    const { t } = useTranslation();
    const BASE_URL = "https://matrixaaa.duckdns.org";

    const [support, setSupport] = useState({});
    const [privacyText, setPrivacyText] = useState({});
    const [offerText, setOfferText] = useState({});
    const [isPrivacyModalOpen, setIsPrivacyModalOpen] = useState(false);
    const [isOfferModalOpen, setIsOfferModalOpen] = useState(false);

    const getSupport = async () => {
        try {
            const response = await axios.get(`${BASE_URL}/other/message-support/1/`);
            setSupport(response.data);
        } catch (error) {
            console.log("Error fetching support data:", error);
        }
    };

    const getPrivacy = async () => {
        try {
            const response = await axios.get(`${BASE_URL}/other/privacy-policy/1/`);
            setPrivacyText(response.data);
        } catch (error) {
            console.log("Error fetching privacy policy:", error);
        }
    };

    const getOffer = async () => {
        try {
            const response = await axios.get(`${BASE_URL}/other/public-offer-agreement/1/`);
            setOfferText(response.data);
        } catch (error) {
            console.log("Error fetching public offer:", error);
        }
    };

    useEffect(() => {
        getSupport();
        getPrivacy();
        getOffer();
    }, []);

    return (
        <div className="footerRlc">
            <div className="horizontaLine"></div>
            <div className="footerOther">
                <div className="footer">
                    <div className="icons">
                        <img src={telegramIcon} alt="Telegram" />
                        <img src={VKIcon} alt="VK" />
                    </div>

                    <div className="help">
                        <a href={support?.reference} target="_blank" rel="noopener noreferrer">
                            {support?.title}
                        </a>
                    </div>

                    <div className="docs">
            <span
                onClick={() => setIsPrivacyModalOpen(true)}
                style={{ cursor: "pointer", textDecoration: "underline" }}
            >
              {t("footer.privacyPolicy")}
            </span>
                        <span
                            onClick={() => setIsOfferModalOpen(true)}
                            style={{ cursor: "pointer", textDecoration: "underline" }}
                        >
              {t("footer.publicOffer")}
            </span>
                    </div>
                </div>
            </div>

            {isPrivacyModalOpen && (
                <div className="modal">
                    <div className="modal-content">
                        <span className="close" onClick={() => setIsPrivacyModalOpen(false)}>&times;</span>
                        <h2>{privacyText?.title}</h2>
                        <div dangerouslySetInnerHTML={{ __html: privacyText?.description }} />
                    </div>
                </div>
            )}

            {isOfferModalOpen && (
                <div className="modal">
                    <div className="modal-content">
                        <span className="close" onClick={() => setIsOfferModalOpen(false)}>&times;</span>
                        <h2>{offerText?.title}</h2>
                        <div dangerouslySetInnerHTML={{ __html: offerText?.description }} />
                    </div>
                </div>
            )}
        </div>
    );
};

export default Footer;
