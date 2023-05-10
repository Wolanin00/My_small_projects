import smtplib

EMAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "testowy100daysms@gmail.com"
MY_PASSWORD = 'REMOVED'


class NotificationManager:

    def __init__(self):
        pass

    def send_email_message(self, price, url, title):
        with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Amazon low price!\n\n"
                    f"Your product :{title} is under target price.\n"
                    f"It only costs now: ${price}.\n"
                    f"Check on website: {url}".encode('utf-8')
                )
