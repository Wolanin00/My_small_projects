from twilio.rest import Client

TWILIO_SID = "REMOVED"
TWILIO_AUTH_TOKEN = "REMOVED"
TWILIO_VIRTUAL_NUMBER = "REMOVED"
TWILIO_VERIFIED_NUMBER = "REMOVED"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
