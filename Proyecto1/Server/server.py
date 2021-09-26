# Lo primero que hacemos es importar las librerias necesarias
from http.server import HTTPServer, BaseHTTPRequestHandler
import http.client
from urllib.parse import urlparse
import json
import pickle

HOST = "127.0.0.1"
try:
    fileOpen = open("data_hash_table.pkl", "rb")
    hash_table = pickle.load(fileOpen)
    fileOpen.close()
except Exception as err:
    hash_table = {}

try:
    nodesFile = open("data_nodes.pkl", "rb")
    nodes = pickle.load(nodesFile)
    nodesFile.close()
except Exception as err:
    nodes = []


class HttpHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/all':
            self.get_all()
        elif self.path == '/node-connection':
            self.get_connection()
        else:
            query = urlparse(self.path).query
            query_components = dict(qc.split("=") for qc in query.split("&"))
            key = query_components["key"]
            self.get_by_key(key)

    def do_POST(self):
        if self.path == '/':
            self.post_data()
        elif self.path == '/delete-category':
            self.post_delete_category()
        elif self.path == '/delete-value':
            self.post_delete_value()

    def get_by_key(self, key):
        global hash_table
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        message = {
            "success": True,
            "msg": "Se ha sincronizado la data",
            "data": hash_table[key]
        }
        self.wfile.write(json.dumps(message, default=str).encode())

    def get_all(self):
        global hash_table
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        message = {
            "success": True,
            "msg": "Se ha sincronizado la data",
            "data": hash_table
        }
        self.wfile.write(json.dumps(message, default=str).encode())

    def get_connection(self):
        global hash_table
        global nodes
        self.send_response(200)
        self.send_header('Content-type', 'application/octet-stream')
        self.end_headers()
        if not self.client_address[0] in nodes:
            nodes.append(self.client_address[0])
            print(nodes)
            file = open("data_nodes.pkl", "wb")
            pickle.dump(nodes, file)
            file.close()
        self.wfile.write(pickle.dumps(hash_table))

    def post_data(self):
        global hash_table
        content_length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(content_length).decode())
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        message = {
            "success": True,
            "msg": "Se ha sincronizado la data"
        }
        try:
            if data["key"] in hash_table.keys():
                hash_table[data["key"]].append(data["value"])
            else:
                hash_table[data["key"]] = [data["value"]]

            file = open("data_hash_table.pkl", "wb")
            pickle.dump(hash_table, file)
            self.send_msg(pickle.dumps(hash_table))
            file.close()
            self.wfile.write(json.dumps(message, default=str).encode())
        except Exception as err:
            message["success"] = False
            message["msg"] = err
            self.wfile.write(json.dumps(message, default=str).encode())

    def post_delete_value(self):
        global hash_table
        content_length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(content_length).decode())
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        message = {
            "success": True,
            "msg": "Se ha sincronizado la data"
        }
        try:
            if data["key"] in hash_table.keys():
                if data["value"] in hash_table[data["key"]]:
                    hash_table[data["key"]].remove(data["value"])

            file = open("data_hash_table.pkl", "wb")
            pickle.dump(hash_table, file)
            self.send_msg(pickle.dumps(hash_table))
            file.close()
            self.wfile.write(json.dumps(message, default=str).encode())
        except Exception as err:
            message["success"] = False
            message["msg"] = err
            self.wfile.write(json.dumps(message, default=str).encode())

    def post_delete_category(self):
        global hash_table
        content_length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(content_length).decode())
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        message = {
            "success": True,
            "msg": "Se ha sincronizado la data"
        }
        try:
            if data["key"] in hash_table.keys():
                del hash_table[data["key"]]

            file = open("data_hash_table.pkl", "wb")
            pickle.dump(hash_table, file)
            self.send_msg(pickle.dumps(hash_table))
            file.close()
            self.wfile.write(json.dumps(message, default=str).encode())
        except Exception as err:
            message["success"] = False
            message["msg"] = err
            self.wfile.write(json.dumps(message, default=str).encode())

    def send_msg(self, msg):
        global nodes
        headers = {
            "Content-type": "application/octet-stream",
            "Accept": "*/*"
        }
        for ip in nodes:
            try:
                conn = http.client.HTTPConnection(ip + ":8001")
                conn.request("POST", "/", msg, headers)
                response = conn.getresponse()
            except Exception as err:
                print(err)


if __name__ == "__main__":
    server_address = (HOST, 8000)
    httpd = HTTPServer(server_address, HttpHandler)
    httpd.serve_forever()
