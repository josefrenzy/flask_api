import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_USER') or "guzmangordillojose@gmail.com"
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS') or "jtdrszpclrpthfdp"

with smtplib.SMTP_SSL('smtp.gmail.com', port=465) as smtp:

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = "An HTML Email"
    body = """Te voy a meter la pistola :3"""
    msg = f"Subject: {subject}  {body}"

    smtp.sendmail(EMAIL_ADDRESS, 'narelygarcialuis@gmail.com',msg)
