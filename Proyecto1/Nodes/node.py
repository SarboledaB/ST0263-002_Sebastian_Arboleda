# Lo primero que hacemos es importar las librerias necesarias
from http.server import HTTPServer, BaseHTTPRequestHandler
import http.client
from urllib.parse import urlparse
import json
import pickle
import argparse

CLIENTS = {}
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8000

parser = argparse.ArgumentParser(description=('Launch client'))

# Required field.
parser.add_argument(
    '-s', '--server', required=True, help=("The Server IP"))
# Optional field.
parser.add_argument(
    '-p', '--port', default=DEFAULT_PORT, required=False, type=int,
    help=("The Server port, It's set by default as 8000"))
parser.add_argument(
    '--host', default=DEFAULT_HOST, required=False,
    help=("The Node host IP, It's set by default as 127.0.0.1"))

args = parser.parse_args()

try:
    fileOpen = open("data_hash_table.pkl", "rb")
    hash_table = pickle.load(fileOpen)
    fileOpen.close()
except Exception as err:
    hash_table = {}


class HttpHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/all':
            self.get_all()
        else:
            query = urlparse(self.path).query
            query_components = dict(qc.split("=") for qc in query.split("&"))
            print(query_components)
            key = query_components["key"]
            print(key)
            self.get_by_key(key)

    def do_POST(self):
        if self.path == '/':
            self.post_data()

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

    def post_data(self):
        global hash_table
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        message = {
            "success": True,
            "msg": "Se ha sincronizado la data"
        }
        try:
            hash_table = pickle.loads(data)
            print(hash_table)
            file = open("data_hash_table.pkl", "wb")
            pickle.dump(hash_table, file)
            file.close()
            self.wfile.write(json.dumps(message, default=str).encode())
        except Exception as err:
            message["success"] = False
            message["msg"] = err
            self.wfile.write(json.dumps(message, default=str).encode())


def get_connection():
    global hash_table
    headers = {
        "Content-type": "application/octet-stream",
        "Accept": "*/*"
    }
    try:
        conn = http.client.HTTPConnection("%s:%d" % (args.server, args.port))
        conn.request("GET", "/node-connection")
        response = conn.getresponse().read()
        print(response)
        hash_table = pickle.loads(response)
        print(hash_table)
        file = open("data_hash_table.pkl", "wb")
        pickle.dump(hash_table, file)
        file.close()
    except Exception as err:
        print(err)


if __name__ == "__main__":
    get_connection()
    server_address = (args.host, args.port)
    httpd = HTTPServer(server_address, HttpHandler)
    httpd.serve_forever()
