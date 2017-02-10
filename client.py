#!/usr/bin/env python2


import  socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


while True:
	msg=raw_input("[root@instructor Desktop]# ")

	s.sendto(msg,("192.168.1.81",9999))
	x=s.recvfrom(100)
	print  x[0]



s.close()




