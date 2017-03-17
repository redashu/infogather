#!/usr/bin/python2

import cgi,cgitb,os,commands

print  "content-type:text/html"
print  ""

ip=["192.168.10.108","192.168.10.107","192.168.10.104"]


x='''
<html>
<form action="http://192.168.10.108/cgi-bin/boxrecv.py">
	<input type="checkbox" name="n">  NFS  <br/>
	<input type="checkbox" name="h"> HTTP  <br/>
	<input type="checkbox" name="m"> Mariadb  <br/>
	   <input type="submit" value="select">
</form>
</html>
'''

print  x
