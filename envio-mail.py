import smtplib
import getpass

password = getpass.getpass()
user = input('Usuario: ')
destinatario = input('Destinatario: ')
subject = input('Asunto: ')
text = input('Cuerpo del mensaje: ')

message = 'Subject: {}\n\n{}'.format(subject, text)
smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtpObj.ehlo()


smtpObj.login(user, password)
smtpObj.sendmail(user, destinatario, message)
smtpObj.quit()