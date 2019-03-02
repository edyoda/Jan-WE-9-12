# "www.magicbricks.com" => get/post => response 
# Transport layer : TCP and UDP
# TCP :  http,smtp,ftp
# UDP :  DNS , 
# Sockets : 
# cleint (socket)		TCP 	(socket)server 


# server : ip , port 

# bind((ip,port))
# listen()
# accept()
# send/recv => byte 


# client :

# connect((ip,port))
# send/recv 

import socket

host = socket.gethostname()
port = 3003

server_socket = socket.socket()
server_socket.bind((host,port))

server_socket.listen(1)

client_sock ,addr = server_socket.accept()
data_server = b"This is the data from server"
client_sock.send(data_server)

data_client = client_sock.recv(1024)
print("Data recieved from client : {} ".format(data_client))

print(data_server == data_client)


server_socket.close()




