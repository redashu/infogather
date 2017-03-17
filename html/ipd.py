#!/usr/bin/env python

import cgi,cgitb
import os, commands
cgitb.enable()

print "content-type:text/html"
print ""

f=open("ip.txt")
x=f.read()
f.close()

fip=x.split("\n")
l=len(fip)
print '<form action="/cgi-bin/abcd"  >'
for i in fip[0:l-1]:
	print "<input type=\"checkbox\" name=\"nn\" value=\""+i+"\">"+i
	mem=commands.getoutput("ssh "+i+" cat /proc/meminfo | grep MemTo | awk '{print $2}'")
	cpu=commands.getoutput("ssh "+i+" lscpu | grep '^CPU(s)' | awk '{print $2}'")
"""	a=commands.getoutput("ssh "+i+" cat /proc/meminfo | grep Mem ")
		for i in a:
			print i,
			"""
	print "&nbsp"+"Ram is " +int(mem)/1024.0/1024+"GB and CPU is "+cpu+"core"
	print "</br>"

print "<input type=\"submit\" value=\"Submit\">"
print "</form>"
