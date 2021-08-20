#Lo primero que hacemos es importar las librerias necesarias
from http.server import HTTPServer, BaseHTTPRequestHandler
import http.client
import threading
import json

CLIENT = 1
SERVER = "127.0.0.1"
HOST = "127.0.0.1"

class HttpHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        if self.path == '/':
            self.post_msg()

    def post_msg(self):
      content_length = int(self.headers['Content-Length'])
      post_data = json.loads(self.rfile.read(content_length).decode())
      print('\r' + str(post_data["cliente"]) + ":" + post_data["msg"] + '\n->', end='')
      resp = {
          "ok": True
      }
      self.wfile.write(json.dumps(resp).encode())


#Se envia la conexion al servidor para que sea indexada
def send_conn():
    conn = http.client.HTTPConnection(SERVER + ":8000")
    conn.request("GET", "/connection")
    response = conn.getresponse()
    global CLIENT
    CLIENT = json.loads(response.read(1000).decode())["client"]

#obtiene los las direcciones de los clientes
def get_clients(msg):
    params = json.dumps({
            "cliente": CLIENT,
            })
    headers = {
        "Content-type": "application/json",
        "Accept": "text/plain"
        }
    conn = http.client.HTTPConnection(SERVER + ":8000")
    conn.request("POST", "/clients", params, headers)
    response = conn.getresponse()
    clients = json.loads(response.read(1000).decode())
    for item in clients["clients"]:
        send_msg(msg, item)
        
#envia el mensaje a cada cliente
def send_msg(msg, client):
    params = json.dumps({
            "cliente": CLIENT,
            "msg": msg,
            })
    headers = {
        "Content-type": "application/json",
        "Accept": "text/plain"
        }
    conn = http.client.HTTPConnection(client + ":" + "8000")
    conn.request("POST", "/", params, headers)

def msg_recv():
    server_address = (HOST, 8000)
    httpd = HTTPServer(server_address, HttpHandler)
    httpd.serve_forever()

msg_recv = threading.Thread(target=msg_recv)

msg_recv.daemon = True
msg_recv.start()

x = True
send_conn()
while x:
    msg = input('->')
    if msg != 'salir':
        get_clients(msg)
    else:
        x = False
