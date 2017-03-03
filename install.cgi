#!/usr/bin/python2

import cgi
import  cgitb
import  commands,os,time
cgitb.enable()
y=cgi.FieldStorage()

print  "content-type:text/html"
print  ""

c=y.getvalue('g')

if  c  ==  'p' :
	time.sleep(2)
	commands.getoutput('sudo  useradd -s /usr/bin/python newu')
	os.system('sudo echo redhat |  passwd  newu --stdin')
	print  "plz wait for python   !!"
	print  "<meta http-equiv='refresh' content='0; url=https://192.168.2.3:4200'>"
