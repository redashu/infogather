#!/usr/bin/python

import os,cgi,cgitb
import commands
cgitb.enable()

print "content-type:text/html"
print ""

x=cgi.FieldStorage()
dev=x.getvalue("d")
f=open("ip.txt")
f.close()
s="."
x=commands.getoutput("ifconfig "+dev+" | grep \"inet \" | awk -F\" \" '{print $2}'")
ips=s.join(x.split(".")[0:3])
z=os.system("for i in {100..105} ; do (arping "+ips+"$i -c 2 -I "+dev+" -w 5 &>/dev/null && echo "+ips+"$i || echo ''  ) done")
print z
if z==0:
	print "<meta http-equiv='refresh' content='1;url=http://127.0.0.1/cgi-bin/ipd.py"
else:
	print "there is some error"
