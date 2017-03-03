#!/usr/bin/python2

import cgi
import  cgitb
import  commands,os,time
cgitb.enable()

print  "content-type:text/html"
print  ""

data=cgi.FieldStorage()

user=data.getlist('n')

print  user

	



