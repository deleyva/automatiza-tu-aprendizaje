import smtplib
import getpass

preguntas = [
	'¿Cómo puedes poner un carácter \ barra invertida en una cadena?',
	'¿Cómo se pueden recortar caracteres de espacios en blanco desde el principio o el final de una cadena?',
	'¿Cómo es el código para un diccionario vacío?',
	'¿Cuál es la principal diferencia entre un diccionario y una lista?',
	'¿Qué módulo y función se pueden utilizar para "imprimir en bonito" los valores del diccionario?',
	''

]

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