import socket 


host = socket.gethostname()
port = 3003
# getfqdn => ip 
# gethostbyname => url 
socket = socket.socket()

socket.connect((host,port))

data_server = socket.recv(1024)
print("data from server is : {} ".format(data_server))

socket.send(data_server)


socket.close()


# db access 
# sys os 
# pdb 
# package 