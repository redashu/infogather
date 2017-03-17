#!/usr/bin/python2

import  cgi,cgitb
import  os,commands,time

cgitb.enable()

print  "content-type:text/html"
print  ""

data=cgi.FieldStorage()

osn=data.getvalue('n')
osr=data.getvalue('r')
osc=data.getvalue('c')
osh=data.getvalue('h')
osp=data.getvalue('p')
print  "______________________"

print "\n"
print  os.system('sudo virt-install --name '+osn+' --ram '+osr+' --vcpu '+osc+' --nodisk --cdrom /var/ftp/pub/images/kali-linux-2.0-amd64.iso --graphics vnc,listen=0.0.0.0,port='+osp+'  &')

print  commands.getoutput('sudo /var/ftp/pub/noVNC/utils/launch.sh --vnc 192.168.2.108:'+osp+' &')


"""
time.sleep(2)

print  "plz wait for os "

print  "<a href=''target='_blank'>click here to access your os</a>

"""

