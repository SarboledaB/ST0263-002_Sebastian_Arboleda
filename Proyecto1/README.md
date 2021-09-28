
# **Proyecto 1 Tópicos Especiales de Telemática.**

## **Autores:**
- **Sebastian Arboleda Botero**
- **Anthony Garcia Moncada**

## **Diagrama de arquitectura**
![alt text](https://storage.googleapis.com/st0263-002/Proyecto1Telematica.drawio%20(1).png)


## **Requerimientos**

**Python version**

3.7.10

**pip version**

20.2.2

## **Ejecución**


### **Correr Servidor**

Por defecto:
``` bash
$ python3 Server/server.py
```

Para definir manualmente el puerto y/o la IP Host (por defecto son '8000' y '127.0.0.1', respectivamente):
``` bash
$ python3 Server/server.py [-p PORT] [--host HOST]
```

Para obtener ayuda sobre la implementación:

``` bash
$ python3 Server/server.py -h
```

### **Correr Nodos**

Por defecto, se debe declarar la IP del server:
``` bash
$ python3 Nodes/node.py -s {SERVER_IP}
```

Para definir manualmente el puerto y/o la IP Host (por defecto son '8000' y '127.0.0.1', respectivamente):
``` bash
$ python3 Nodes/node.py -s {SERVER} [-p PORT] [--host HOST]
```

Para obtener ayuda sobre la implementación:

``` bash
$ python3 Nodes/node.py -h
```

### **Correr Cliente**

Por defecto, se debe declarar la IP del server ( en la práctica, coresponde a '34.132.17.165'):
``` bash
$ python3 Client/client.py -s {SERVER_IP}
```

Para definir manualmente el puerto y/o la IP Host (por defecto son '8000' y '127.0.0.1', respectivamente):
``` bash
$ python3 Client/client.py -s {SERVER} [-p PORT] [--host HOST]
```

Para obtener ayuda sobre la implementación:

``` bash
$ python3 Client/client.py -h
```

### **Configurar balanceador Nginx**

``` bash
$ sudo apt-get update
$ sudo apt-get install nginx
$ sudo apt-get install git
$ sudo git clone https://github.com/SarboledaB/ST0263-002_Sebastian_Arboleda.git
$ cd ST0263-002_Sebastian_Arboleda/Proyecto1/Load_balancer
$ sudo cp ./load-balancer.conf /etc/nginx/conf.d/
$ sudo rm /etc/nginx/sites-available/default
$ sudo rm /etc/nginx/sites-enabled/default
$ sudo nginx -t
$ sudo systemctl restart nginx
```
