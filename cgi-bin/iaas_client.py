#!/usr/bin/env python2


import  commands,os,time,socket


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


serverip="192.168.1.254"
serverp=9999
while True :
	os_name=raw_input("enter your os name :  ")
	os_ram=raw_input("enter your os RAM in MB  :  ")
	os_cpu=raw_input("enter your os CPU in COre  :  ")
	os_hdd=raw_input("enter your os Hard disk in GB  :  ")
	s.sendto(os_name,(serverip,serverp))
	s.sendto(os_ram,(serverip,serverp))
	s.sendto(os_cpu,(serverip,serverp))
	s.sendto(os_hdd,(serverip,serverp))
	


