import asyncio
from email.message import EmailMessage
import aiosmtplib
from secret import FROM_EMAIL_ADDRESS, EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD

async def send_rate_email(to_email, from_code, to_code, rate):
    # FIXME check this is a valid email address?
    message = EmailMessage()
    message["From"]    = FROM_EMAIL_ADDRESS
    message["To"]      = to_email
    message["Subject"] = "Exchange Rate"
    message.set_content(f"""
The exchange rate from {from_code} to {to_code} is {rate}.
""")
    await aiosmtplib.send(message,
                          hostname=EMAIL_HOST,
                          port=465,
                          username=EMAIL_HOST_USER,
                          password=EMAIL_HOST_PASSWORD,
                          use_tls=True)
