####client code

import socket
s= socket.socket( )
port =  40674 #reserve for system protocol
s.connect(('127.0.0.1',port))
print(s.recv(1024)) # size of the data packet that we can receive.1024 data packets

s.close