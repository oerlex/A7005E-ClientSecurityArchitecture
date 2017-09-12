import socket
import sys

HOST = ''    #Symbolic name, meaning all available interfaces
PORT = 8888  #Arbitraty port (NON PRIVILEDGED)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket created')

#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print("Bind failed. Error Code : "+ str(msg[0])+ " Message " + msg[1])
    sys.exit()

print("Socket bind completed")

#Start listening on socket
s.listen(10)
print("Socket now listening")

#now kepp talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print("Connected with " + addr[0] + ":" +str(addr[1]))

s.close()