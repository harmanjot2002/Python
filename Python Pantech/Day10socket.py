import socket
s=socket.socket()
port=40674
s.bind(('',port))
print("Socket binded to %s" %(port))

s.listen(5)
print("socket is listening")
while True:
    c,addr=s.accept()
    print('Got connection from',addr)
    s.send(b'Thank you for connecting')
    c.close()