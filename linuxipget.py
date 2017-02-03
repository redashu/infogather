#!/usr/bin/env python2


import  commands
import   time

print  "Listing Your Lan Card  NameS :  "
time.sleep(2)

print  "#################################"
print  "_________________________________"


print   commands.getoutput('tcpdump  -D')

print  "_________________________________"
print  "_________________________________"
lan=raw_input("type  your lan card name from above list :  ")

x=commands.getoutput('ifconfig    '+lan)

y=x.split('inet')[1]

ip_address=y.split()[0]

f=open('myipaddr.txt','w')
f.write(ip_address)
f.close()


print   "Your  IP Address of  Give  Lan card  " +lan+ " is  :  ",ip_address

print  "______________________________"
print  ""
print  ""
print   "Going  back to Main Menu !! "
time.sleep(2)


execfile('infogather.py')


