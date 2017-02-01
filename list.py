#!/usr/bin/env python

import  os
import  webbrowser
import time

f=open('ip.txt')
x=f.read()

y=x.split()

#print  y
iplist=[]
ipnotlist=[]

for    i  in   y:
	ipaddr=os.system('ping  -c  2  '+i+'  &>/dev/null')

	if  ipaddr ==  0 :
		iplist.append(i)	
	else :
		ipnotlist.append(i)


print  "List of Present  IP's :   "
time.sleep(2)
for  ip  in  iplist:
	print  ip

time.sleep(2)
print "__________________________"
print "__________________________"


print  "NOt Present IP List :  "
for  nip  in   ipnotlist:
	print  nip








		

	



