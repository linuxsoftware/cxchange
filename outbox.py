import asyncio
from email.message import EmailMessage
import aiosmtplib
from secret import EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD

async def send_rate_email(to_email, from_code, to_code, rate):
    message = EmailMessage()
    message["From"]    = "noreply@linuxsoftware.nz"
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
                          use_tls=True,
                          validate_certs=False)
