#!/usr/bin/env python 
import cgi


print  "content-type:text/html"
print  ""

print  commands.getoutput('sudo /var/ftp/pub/noVNC/utils/launch.sh --vnc 192.168.10.108:5911 &')

