#!/usr/bin/python2

import cgi
import  cgitb
import  commands,os,time
cgitb.enable()

print  "content-type:text/html"
print  ""

data=cgi.FieldStorage()

user=data.getvalue('h')
password=data.getvalue('p')

suser=data.getvalue('l')
spassword=data.getvalue('cp')
	



	print  "<meta http-equiv='refresh' content='5;url=http://192.168.10.108/cmd.html' />"



else  :
	print  "Invalid  Authentication !!"







