# Enviando y recibiendo mails con python

Artículo orginal [aquí](https://automatetheboringstuff.com/chapter16/)

## Enviando un mail

```python
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
```

## ¿Qué función práctica puede tener esto?

Mañana veremos una implementación curiosa.

De momento, si quieres saber cómo recibir datos del mail aquí tienes [una prueba](https://github.com/deleyva/automatiza-tu-aprendizaje/blob/master/recibir-mail.py?raw=true).

## ¿Quieres enviar archivos adjuntos?

[Aquí](https://www.linkedin.com/pulse/python-script-send-email-attachment-using-your-gmail-account-singh/) tienes más información. Y [aquí](https://stackoverflow.com/questions/3362600/how-to-send-email-attachments).
