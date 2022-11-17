import smtpd
import ssl
from email.message import EmailMessage

subject = "Email form python"
body = "This is a text email from python"
sendr_email = "" # Enter sender email 
receiver_email = "" # Enter receiver Email
password = input("Enter a password: ")

message = EmailMessage()
message["From"] = sendr_email
message["To"] = receiver_email
message["Subject"] = subject

context = ssl.create_default_context()

print("Sending Email!")

with smtpd.SMTP_SSL("smtp.gmail.com", 465,context=context) as server:
    server.login(sendr_email, password)
    server.sendmail(sendr_email, receiver_email, message.as_string())

print("Successful!")

