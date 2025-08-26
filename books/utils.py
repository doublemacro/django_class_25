from twilio.rest import Client
from backend.private_settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

def send_whatsapp_message(to_number, message):
    """Using Twilio rest API to send business whatsapp message. Just an example, not working:"""
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(message, 'whatsapp:{}'.format(to_number), from_='whatsapp:+407438356456')

