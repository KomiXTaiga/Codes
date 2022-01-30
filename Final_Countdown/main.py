import smtplib
import ssl
from email.message import EmailMessage
from emails import emails
from random import randint

def get_ran(emails):
	x = randint(0,emails)
	return x

subject = "Congratulations today is your not lucky day!"
body = "Filler Text"
sender_email = "Not Showing you this Rambo"
password = "Not Showing you this Rambo"
message = EmailMessage()
message["From"] = sender_email
message["To"] = "Filler text"
message["Subject"] = subject
message.set_content(body)

f = True
while f == True:
	context = ssl.create_default_context()
	print("Sending Email!")
	x = get_ran(len(emails))
	reciever_email = emails[x-1]
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, reciever_email, message.as_string())
	print("Sucess")
