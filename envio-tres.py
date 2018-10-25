import smtplib
import getpass
import time

password = getpass.getpass()
user = input('Usuario: ')
destinatario = input('Destinatario: ')
mensajes = []
for i in range(3):
	text = input('Cuerpo del mensaje: ')
	subject = input('Asunto: ')
	mensajes.append('Subject: {}\n\n{}'.format(subject, text))

smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtpObj.ehlo()

smtpObj.login(user, password)
for i in range(3):
    smtpObj.sendmail(user, destinatario, mensajes[i])
    time.sleep(3)

smtpObj.quit()
