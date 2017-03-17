#!/usr/bin/python2

import MySQLdb
import cgi
import cgitb
import commands
cgitb.enable()

print "content-type:text/html"
print  ""
form = cgi.FieldStorage()

user = form.getvalue('n')
email = form.getvalue('e')
password = form.getvalue('p')


# Open database connection
db = MySQLdb.connect('127.0.0.1','root','redhat','adhoc')

# prepare a cursor object using cursor() method
query = db.cursor()
q="insert into student (name,email,password) values (%s,%s,%s)"
print  q,(user,email,password)
try :
	query.execute(q,(user,email,password))
	db.commit()
	print  query.fetchall()
except  :
	db.rollback()

db.close()
# Prepare SQL query to INSERT a record into the database.
#sql = "INSERT IGNORE INTO CLIENTS( FIRSTNAME, LASTNAME, EMAIL, CONTACTNUMBER, GENDER, PASSWD) VALUES (%s,%s,%s,%s,%s,%s)" 
