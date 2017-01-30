#!/usr/bin/env python2

import  webbrowser


x='''
Enter any Message  for check your pattern 
'''

print  x

s=raw_input()

if  'lo'  in  s :

#	commands.getoutput('firefox  http://www.google.com/search?q='+s)
	webbrowser.open_new_tab('http://www.google.com/maps?q='+s)
	execfile('input.py')

else :
	print   "no match found !!"
	execfile('input.py')



