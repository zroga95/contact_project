import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

def sendAttachedEmail(reciever_email, attachment_path):
	passworded = input('password--> ')
	sender_email = "zroga.testing@gmail.com"
	#reciever_email = "zroga95@gmail.com" #15165679414@mms.cricketwireless.net
	# Create a secure SSL context
	context = ssl.create_default_context()

	msg = MIMEMultipart()

	msg["From"] = sender_email;
	msg["To"] = reciever_email;
	# open the file to be sent  
	with open(attachment_path, "rb") as attachment:
	# instance of MIMEBase and named as p 
		p = MIMEBase('application', 'octet-stream') 
		# encode payload 
		p.set_payload(attachment.read())
	encoders.encode_base64(p)
	p.add_header('Content-Disposition', "attachment; filename= %s" 
		% os.path.split(attachment_path)[1])

	msg.attach(p)

	email_server = smtplib.SMTP('smtp.gmail.com', 587)

	email_server.starttls()

	email_server.login(sender_email, passworded)

	msg_as_string = msg.as_string()

	email_server.sendmail(sender_email, reciever_email, msg_as_string)

	email_server.quit()
