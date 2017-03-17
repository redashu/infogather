#!/usr/bin/python2


import mysql.connector as mariadb
import cgi
import cgitb
import commands


cgitb.enable()


print "content-type:text/html"
print  ""
form = cgi.FieldStorage()

FIRSTNAME = form.getvalue('fname')
LASTNAME = form.getvalue('lname')
EMAIL = form.getvalue('email')
CONTACT_NUMBER = form.getvalue('contact')
GENDER = form.getvalue('gen')
PASSWD = form.getvalue('passwd')

# Open database connection
db = mariadb.connect(user='root', password='redhat', database='users')

# prepare a cursor object using cursor() method
cursor = db.cursor()


# Prepare SQL query to INSERT a record into the database.
sql = "INSERT IGNORE INTO CLIENTS( FIRSTNAME, LASTNAME, EMAIL, CONTACTNUMBER, GENDER, PASSWD) VALUES (%s,%s,%s,%s,%s,%s)" 

try:
   # Execute the SQL command
   cursor.execute(sql , (FIRSTNAME, LASTNAME, EMAIL, CONTACTNUMBER, GENDER, PASSWD))
   # Commit your changes in the database
   db.commit()
   
except:
   # Rollback in case there is any error
   db.rollback()




   

# disconnect from server
db.close()
