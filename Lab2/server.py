#Lo primero que hacemos es importar las librerias necesarias
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

CLIENTS = {}
HOST = "127.0.0.1"

class HttpHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/connection':
            self.get_connection()

    def do_POST(self):
        if self.path == '/':
            self.post_msg()
        elif self.path == '/clients':
            self.get_clients()

    def get_connection(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        CLIENTS[len(CLIENTS)] = self.client_address[0]
        message = {"client": len(CLIENTS)}
        self.wfile.write(json.dumps(message).encode())

    def get_clients(self):
        content_length = int(self.headers['Content-Length'])
        post_data = json.loads(self.rfile.read(content_length).decode())
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        message = {"clients": []}
        for item in range (len(CLIENTS)):
            if item != post_data["cliente"] - 1:
                message["clients"].append(CLIENTS[item])
        self.wfile.write(json.dumps(message).encode())

    def post_msg(self):
      content_length = int(self.headers['Content-Length'])
      post_data = json.loads(self.rfile.read(content_length).decode())

if __name__ == "__main__":
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, HttpHandler)
    httpd.serve_forever()