#!/usr/bin/env python2

import  os
import  time
import  commands
import  webbrowser

print  "Gathering  my OWn IP  Address  "

f=open('myipaddr.txt')
ip=f.read()
f.close()

r=range(255)[1:]

x=ip.split('.')[0:3]

y='.'.join(x)

iplistfinal=[]

for  i   in  r :
	x=os.system('arping -I eno1  '+y+'.'+str(i)+'   &>/dev/null')
	if  x  ==  0 :
		iplistfinal.append(y+'.'+str(i))
	else :
		print  ""



print  "MY IP  List is Give Below  !!"
print  iplistfinal

		











