import socket
from utilities import crc

# Creat a Socket
sock = socket.socket()
sock.connect(('127.0.0.1',9999))

# Get data from user
data = input('Please input a message: ')
generator = input('Please input a generator: ')

crc_code = crc(data,generator)
print(crc_code)

request = data + ' ' + generator + ' '+ crc_code
sock.send(request.encode())

response = sock.recv(1024)
print(response.decode())

sock.close()
