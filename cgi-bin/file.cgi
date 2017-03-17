#!/usr/bin/python2

import cgi
import  cgitb
import  commands,os,time
cgitb.enable()
y=cgi.FieldStorage()

print  "content-type:text/html"
print  ""
os.system('nmap -n  192.168.10.0/24  -sS   |  grep -i report |  cut -d" "  -f5  >ip.txt')
f=open('ip.txt')
ip=f.read()
fip=ip.split('\n')
l=len(fip)
print   '<form action="/cgi-bin/re.cgi">'
for  i  in  fip[0:l-1]:
	print  '<input type="checkbox" name="n" value='+i+'>' +i 
	print   "&nbsp"+ "RAM is  3GB AND cpu is  4 core "
	print  "</br>"


print   '<input type="submit">'
print   '</form>'
