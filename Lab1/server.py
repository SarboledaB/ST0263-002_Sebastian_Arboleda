import socket
import threading
import sys
import pickle

host="********"
port=4000

clientes = []

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((str(host), int(port)))
sock.listen(10)
sock.setblocking(False)

def msg_to_all(msg, cliente):
	for c in clientes:
		try:
			if c != cliente:
				c.send(msg)
		except:
			clientes.remove(c)

def acceptCon():
	while True:
		try:
			conn, addr = sock.accept()
			conn.setblocking(False)
			clientes.append(conn)
		except:
			pass

def processCon():
	while True:
		if len(clientes) > 0:
			for c in clientes:
				try:
					data = c.recv(1024)
					if data:
						msg_to_all(data,c)
				except:
					pass


accept = threading.Thread(target=acceptCon)
process = threading.Thread(target=processCon)

accept.daemon = True
accept.start()

process.daemon = True
process.start()

while True:
    msg = input('->')
    if msg == 'salir':
        sock.close()
        sys.exit()