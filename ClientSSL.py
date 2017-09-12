import ssl
import socket

#Set variables (note that the port is 4434)
host = socket.gethostname()
port = 10021
context = ssl.create_default_context()
context.check_hostname = False
context.load_verify_locations("/etc/ssl/certs/mycert.pem")

print (host)
#Wrap the socket using the ssl library

conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=host)

#Connect and send a packet
conn.connect((host, port))
cert = conn.getpeercert()
print(cert)
conn.close()