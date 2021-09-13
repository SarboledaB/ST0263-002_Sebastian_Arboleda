#Codigo para enviar correo adaptado de: https://realpython.com/python-send-email/#option-1-setting-up-a-gmail-account-for-development
from email import message
import pika
import smtplib, ssl
import json

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "cuentatstr@gmail.com"
password = "asdf12345."

context = ssl.create_default_context()

connection = pika.BlockingConnection(pika.ConnectionParameters('44.198.235.118', 5672, '/', pika.PlainCredentials("user", "password")))
channel = connection.channel()

def callback(ch, method, properties, body):
    data = json.loads(body.decode())
    email = str(data["email"])
    message = str(data["task"])
    # Try to log in to server and send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, email, message)
 
channel.basic_consume(queue="my_app", on_message_callback=callback, auto_ack=True)
channel.start_consuming()