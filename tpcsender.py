#!/usr/bin/python2

import  socket

s=socket.socket()

s.connect(("192.168.1.81",1234))


while  True :
	s.send("hello python socket")

	print  s.recv(100)


