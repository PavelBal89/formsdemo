#!/usr/bin/env python3


import cgi, cgitb 

 
form = cgi.FieldStorage() 


first_name = form.getvalue('name')
last_name = form.getvalue('phone')

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2>Hello %s %s</h2>" % (first_name, last_name))
print ("</body>")
print ("</html>")