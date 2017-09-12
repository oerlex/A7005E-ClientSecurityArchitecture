#client.py
import socket

#Create socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Get Hostname
host = socket.gethostname()

port = 8888

#Connect to the hostname on the defined port
mysocket.connect((host,port))

#Limit receiving size to 1024 bytes
tm = mysocket.recv(1024)

mysocket.close()

print("The time got from the server is %s" % tm.decode('ascii'))