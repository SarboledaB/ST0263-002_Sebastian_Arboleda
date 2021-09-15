# ST0263-002_Sebastian_Arboleda

# Autor: Sebastian Arboleda Botero

Entregas de Tópicos espaciales en telemática.

## Documentación Laboratio 2

Chat con comunicacion por protocolo HTTP

**Protocolo y Arquitectura**
En este laboratorio se realizo una comunicacion por Protocolo HTTP
tambien se realizo en una arquitectura P2P donde los clientes se comunican entre ellos y el servidor es el que indexa la comunicacion

**Requerimientos**
**Python version**

3.8.5

**pip version**

pip 20.1.1

**Configuracion inicial**
**HOST local**
-Se debe cambiar el HOST tanto en cliente como en el servidor, en el caso local por "127.0.0.1"
-En el client.py la variable global SERVER se debe cambiar por la IP privada del servidor ej. "127.0.0.1"

en el caso de una instancia en AWS se debe colocar la ip privada de la instancia que aloja al servidor

**HOST local**
en el caso de una instancia en AWS:
-Se debe cambiar el HOST tanto en cliente como en el servidor por la IP del Servidor
-En el client.py la variable global SERVER se debe cambiar por la IP privada del servidor ej.

**Correr Cliente y Servidor local**
$ python3 server.py

// En client.py se debe colocar un puerto diferente al del servidor ej. 8080 en el metodo "msg_recv()"
// En client.py se debe colocar el puerto el cliente siguiente ej. 8081 en el metodo "send_msg()" linea 61
$ python3 client.py

// Para agregar otro cliente
// En client.py se debe colocar un puerto diferente al del servidor y al cliente anterior ej. 8081 en el metodo "msg_recv()"
// En client.py se debe colocar el puerto el cliente anterio ej. 8080 en el metodo "send_msg()" linea 61
$ python3 client.py

// Esto con fin de pruebas ya que en AWS al tener una IP diferente no hay problema en que el puerto sea el mismo

**Correr Cliente y Servidor AWS**
$ python3 server.py

$ python3 client.py
