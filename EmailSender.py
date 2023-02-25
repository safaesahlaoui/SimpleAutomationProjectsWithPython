from email.message import EmailMessage
from passwordFile import passwoed
import ssl
import  smtplib



email_sender='safaesahlaoui2001@gmail.com'
pwd=passwoed
email_receiver="safae.sehlaoui@usmba.ac.ma"

subject="Don't forget"
body=""""
hello there 
"""
em = EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['subject']=subject
em.set_content(body)
context =ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,pwd)
    smtp.sendmail(email_sender,email_receiver,em.as_string())



