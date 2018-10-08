#!/usr/bin/env python3
import os
print( "Content-type: text/html")
print('')
print( "<title>Process usage </title>"
 	"<h1>System Process usage</h1>"
 	"<hr>"
	)

print(os.uname())

print('<hr>')
# Create a loop to extract these values on mount points only
# ssh root@remoteServer "bash -s" -- < /var/www/html/ops1/sysMole -time Aug 18 18
