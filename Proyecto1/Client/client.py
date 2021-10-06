import http.client
import json

SERVER = "127.0.0.1"
PORT = ":8000"

# Se obtienen todos los valores Key Value


def get_all():
    conn = http.client.HTTPConnection("34.134.143.235:8000")
    conn.request("GET", "/all")
    response = conn.getresponse()
    all = json.loads(response.read(1000).decode())
    print(all["data"])

# Se obtienen todos los valores dependiendo de la Key


def get_by_key(key):
    conn = http.client.HTTPConnection("34.134.143.235:8000")
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
    conn = http.client.HTTPConnection("34.122.28.48:8000")
    conn.request("POST", "/", params, headers)
    response = conn.getresponse()


def post_delete_value(key, value):
    params = json.dumps({
        "key": key,
        "value": value,
    })
    headers = {
        "Content-type": "application/json",
        "Accept": "text/plain"
    }
    conn = http.client.HTTPConnection("34.122.28.48:8000")
    conn.request("POST", "/delete-value", params, headers)
    response = conn.getresponse()


def post_delete_category(key):
    params = json.dumps({
        "key": key
    })
    headers = {
        "Content-type": "application/json",
        "Accept": "text/plain"
    }
    conn = http.client.HTTPConnection("34.122.28.48:8000")
    conn.request("POST", "/delete-category", params, headers)
    response = conn.getresponse()


def main():
    x = True
    print("====== Bienvenido a la biblioteca ======")
    print("Estas entrando al software de almacenamiento de libros por genero literario")
    print("Este software te dara diferentes opciones dependiendo de lo que déses realizar")
    while x:
        print("Para ver todos los libros selecciona : 1")
        print("Para ver todos los libros por genero selecciona : 2")
        print("Para almacenar un libro nuevo selecciona : 3")
        print("Para eliminar un genero selecciona : 4")
        print("Para eliminar un libro selecciona : 5")
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
        elif select == '4':
            key = input('Genero literario: ')
            post_delete_category(key)
        elif select == '5':
            key = input('Genero literario: ')
            value = input('Nombre del libro: ')
            post_delete_value(key, value)

    print("Gracias por visitarnos!!!")


if __name__ == '__main__':
    main()
