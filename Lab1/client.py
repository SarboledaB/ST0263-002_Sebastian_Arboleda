import socket
import threading
import sys
import pickle

host = "localhost"
port = 4000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((str(host), int(port)))


def msg_recv():
	while True:
		try:
			data = sock.recv(1024)
			if data:
				print(pickle.loads(data))
		except:
			pass

def send_msg(msg):
	sock.send(pickle.dumps(msg))

msg_recv = threading.Thread(target=msg_recv)

msg_recv.daemon = True
msg_recv.start()

while True:
    msg = input('->')
    if msg != 'salir':
        send_msg(msg)
    else:
        sock.close()
        sys.exit()
