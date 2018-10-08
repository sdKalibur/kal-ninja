#!/usr/bin/python3

import os
import cgi

print("Content-type: text/html")
print
print( "<title>Testing Python CGI</title>")
print( "<h1>Testing Python CGI</h1><hr>")

diskUtil = os.system('df') 


print( "<pre>")
print(diskUtil)
print( "</pre>")


print( "html")
