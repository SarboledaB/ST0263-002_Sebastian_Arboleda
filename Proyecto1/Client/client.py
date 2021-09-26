import http.client
import json

SERVER = "127.0.0.1"
PORT = ":8000"

# Se obtienen todos los valores Key Value


def get_all():
    conn = http.client.HTTPConnection(SERVER + ":8001")
    conn.request("GET", "/all")
    response = conn.getresponse()
    all = json.loads(response.read(1000).decode())
    print(all["data"])

# Se obtienen todos los valores dependiendo de la Key


def get_by_key(key):
    conn = http.client.HTTPConnection(SERVER + ":8001")
    conn.request("GET", "/?key=" + key)
    response = conn.getresponse()
    all = json.loads(response.read(1000).decode())
    print(all["data"])

# envia el mensaje a cada cliente


def post_value(key, value):
    params = json.dumps({
        "key": key,
        "value": value,
    })
    headers = {
        "Content-type": "application/json",
        "Accept": "text/plain"
    }
    conn = http.client.HTTPConnection(SERVER + PORT)
    conn.request("POST", "/", params, headers)
    response = conn.getresponse()


def main():
    x = True
    print("====== Bienvenido a la biblioteca ======")
    print("Estas entrando al software de almacenamiento de libros por genero literario")
    print("Es software te dara diferentes opciones dependiendo de lo que deses realizar")
    while x:
        print("Para ver todos los libros seleciona : 1")
        print("Para ver todos los libros por genero seleciona : 2")
        print("Para alamcenar un libro nuevo seleciona : 3")
        print("Para salir escribe : salir")
        select = input('->')
        if select == 'salir':
            x = False
        elif select == '1':
            get_all()
        elif select == '2':
            key = input('Genero literario: ')
            get_by_key(key)
        elif select == '3':
            key = input('Genero literario: ')
            value = input('Nombre del libro: ')
            post_value(key, value)

    print("Gracias por visitarnos!!!")


if __name__ == '__main__':
    main()
