#Python provides two levels of access to network services.
#At a low level,we can access the basic socket support in the underlying operating system, which allows you to implement clients and servers for both connection-oriented and connectionless protocols.
#It has libraries that provides to specific application-level network protocols,like FTP,HTTP and so on.
#To create a socket,we must use the socket.socket() function available in the socket module.
#socket_family:This is either AF_UNIX or AF_INET.
#socket_type:This is either SOCK_STREAM or SOCK_DGRAM.
#protocol:This is usually left out,defaulting to 0.

#Import socket module
import socket
#Create a socket object.
s=socket.socket()
#Define the port on which you want to connect
port=40674
#Connect to server on local computer
s.connect(('127.0.0.1',port))
#Receive data from the server
print(s.rcv(1024))
#close the connection
s.close()
