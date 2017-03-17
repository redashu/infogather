#!/usr/bin/env python

import cgi,cgitb
import os,commands
import MySQLdb as sql

cgitb.enable()

print "content-type:text/html"
print ""


x=cgi.FieldStorage()
em=x.getvalue("e")
pa=x.getvalue("p")

sq=sql.connect("127.0.0.1","root","redhat","adhoc")
cur=sq.cursor()
query="select email from student where email=%s and password=%s"
cur.execute(query,(em,pa))

if cur.rowcount == 1:
	print "Login successfull"
	print "</br>"
	print "Please wait u are redirecting "
	print "<meta http-equiv='refresh' content='2;url=http://192.168.10.108/scan.html'>"

else:
	print "Wrong login id"
	print "<meta http-equiv='refresh' content='2;url=http://192.168.10.108/index.html'>"
	

sq.close()
