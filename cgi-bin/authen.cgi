#!/usr/bin/python2

import mysql.connector as mariadb
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
username = form.getvalue('username')
print "content-type: text/html"



password = form.getvalue('password')

# Open database connection
db = mariadb.connect(user='root', password='redhat', database='users')

# prepare a cursor object using cursor() method
cursor = db.cursor()
#cursor2 = db.cursor()

query = "select * from CLIENTS where EMAIL= '%s'" %username
cursor.execute(query)

if next(cursor, None) is None:
    print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=\">\n";
    print "USERNAME NOT FOUND"
else:    
    
	sql = "SELECT PASSWD FROM CLIENTS WHERE EMAIL = '%s'" %username
	    
	cursor.execute(sql)
	    
	row = cursor.fetchone()

	for row in row :


		if password == row:
			print "Set-Cookie:rahulcookie=" + username + ";Path=/;\r\n"
			
			
			print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=\">\n";	
		else:
		    print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=\">\n";
		    print """<script>
		    alert('Your Password Is Incorrect')
		    </script>"""
   		    print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=\">\n";

		    #print "IT DOES NOT MATCH"


	db.close()

print ""


