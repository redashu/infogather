#!/usr/bin/env  python2

import  time
import  platform
print  "Welcome to my INformation Gathering TooLLLL "

time.sleep(2)


print  ""
print  ""
print   "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
print  "+++++++++++++++++++++++++++++++++++++++++++++"
print   "____________________________________________"


x="""
Press  1  To  check my System IP  address  :  
Press  2  To  check my System MAC  address  :  
Press  3  To  check my System OS Type  :  
Press  4  To  check my System OS version   :  
Press  5  To  check my system Configuration   : 
Press  6  To  check  About A particular IP : 
Press   7 To list  all IP in Your Present Network : 
"""

print  x

ch=int(raw_input())

#print  type(ch)

if  ch  ==  1 :
	execfile('checkplatform.py')
elif  ch  ==  2 :
	print   "My Mac address 45:77:vb:55:22:o1 "
elif  ch  ==  3 :

	print  "Os Platform type is  "  +  platform.system()

elif  ch  ==   6 :
	execfile('checkiplive.py')

elif  ch  ==   7  :
	execfile('listallip.py')
else :
	print   "execute me !!"


 
