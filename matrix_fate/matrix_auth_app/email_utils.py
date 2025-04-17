# import requests
# from config import settings

# BREVO_API_URL = "https://api.brevo.com/v3/smtp/email"


# def send_email_brevo(to_email: str, subject: str, content: str):
#     headers = {
#         "accept": "application/json",
#         "api-key": settings.API_KEY_BREVO,
#         "content-type": "application/json",
#     }

#     payload = {
#         "sender": settings.DEFAULT_BREVO_SENDER,
#         "to": [{"email": to_email}],
#         "subject": subject,
#         "htmlContent": f"<html><body><p>{content}</p></body></html>"
#     }

#     response = requests.post(BREVO_API_URL, headers=headers, json=payload)

#     if response.status_code >= 400:
#         raise Exception(f"Ошибка отправки письма: {response.status_code} {response.text}")
