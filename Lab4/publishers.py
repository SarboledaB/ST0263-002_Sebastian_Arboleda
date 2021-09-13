import pika
import json
import uuid

connection = pika.BlockingConnection(pika.ConnectionParameters('44.198.235.118', 5672, '/', pika.PlainCredentials('user', 'password')))
channel = connection.channel()

def publishTask(user, email, task):
    body = json.dumps({
            "id": uuid.uuid1(),
            "user": user,
            "email": email,
            "task": task,
            }, default=str)
    channel.basic_publish(exchange='my_exchange', routing_key='test', body=body)
    print(" [x] Enviando tarea..")

def loop():
    x = True
    while x:
        print("Bienvenido al solucionador de tareas.")
        print("Diligencia la informacion y tu tarea pronto se solucionara!!!")
        print("Para salir simplemente escribre SALIR en cualquier punto del formulario.")
        user = input('Ingresa el usuario: ')
        if user == 'salir':
            x = False
        email = input('Ingresa el correo: ')
        if email == 'salir':
            x = False
        task = input('Ingresa la tarea a realizar: ')
        if task == 'salir':
            x = False
        else:
            publishTask(user, email, task)
    connection.close()

if __name__ == '__main__':
    loop()
    