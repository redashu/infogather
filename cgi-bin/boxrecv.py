#!/usr/bin/python2

import cgi
import  cgitb
import  commands,os,time
cgitb.enable()

print  "content-type:text/html"
print  ""

data=cgi.FieldStorage()

storage=data.getvalue('n')
apache=data.getvalue('h')

db=data.getvalue('m')

print  storage
print  apache
print  db
	








