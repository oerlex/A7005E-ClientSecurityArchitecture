# server.py
import socket
import time

# create the socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 4434

serversocket.bind((host,port))

# Create 5 requests
serversocket.listen(5)

print("Server is up and waiting for requests..")

while True:
    clientsocket,addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))
    currentTime = time.ctime((time.time()))+ "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()