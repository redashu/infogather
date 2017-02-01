#!/usr/bin/env python2


ip_check=raw_input("Enter  IP address to Check its Present in Your lab or Not :   ")


import  os


c=os.system('ping   -c  2   '+ip_check+'   &>/dev/null')


if  c  ==   0:
	print  "___________________________________________________"
	print  "___________________________________________________"
	print  "___________________________________________________"
	print  "IP  Address   "+ip_check+"   Present in This LAb !!"


else :
	print  "IP  "+ip_check+"  Not Present in LAB   !!"


 
