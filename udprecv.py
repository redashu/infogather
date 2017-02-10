#!/usr/bin/env  python2


#  this module for creating socket

import  socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s1=socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
while  True : 
	s.bind(("",9999))
	s1.bind(("",9998))



