#!/usr/bin/python2

import cgi
import  cgitb
import  commands,os,time
cgitb.enable()

print  "content-type:text/html"
print  ""

data=cgi.FieldStorage()

puser=data.getvalue('p')

if  puser == 'python':
	commands.getoutput('sudo docker run -it  -d ashu/paas')
	print  "plz wait for python launch !!"
	print  "<a href='https://192.168.10.108:4200'>"
	print   "click here for python"
	print   "</a>"

elif  puser == 'ruby':
	print  "wait for ruby "
elif  puser == 'perl':
	print  "perl is reloading "
else :
	print  "wrong choice !!"
	



