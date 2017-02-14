#!/usr/bin/python2

import  socket

s=socket.socket()

s.bind(("192.168.1.81",1234))

s.listen(6)

for  i   in   range(100):
	x,y=s.accept()
	print  x.recv(100)
	
	x.send(raw_input("type your message  :   "))
	



s.close()
"""
print  "connection socket  here  ",connd
print  "connection address  ",clientaddr

print  "____________________"


print  "connection socket  here  ",connd1
print  "connection address  ",clientaddr1

print  connd.recv(100)
print  connd1.recv(100)
connd.send("hiiii")
connd1.send("hello")
"""



