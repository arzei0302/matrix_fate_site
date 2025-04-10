import React from "react";
import { useTranslation } from "react-i18next";
import "./MyMatrices.scss";

function MyMatrices() {
    const { t } = useTranslation();

    return (
        <div className="myMatrices">
            <div className="column">
                <p>
                    {t("mymatrices.available")} <span>{t("mymatrices.dates")}</span>
                </p>
            </div>
            <div className="column">
                <p>
                    {t("mymatrices.active")} <span>{t("mymatrices.subscriptions")}</span>
                </p>
            </div>
        </div>
    );
}

export default MyMatrices;
