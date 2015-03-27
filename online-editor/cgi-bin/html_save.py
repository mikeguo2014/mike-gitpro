#__author__ = 'Mike'
#coding=utf-8
#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
if form.getvalue('htmlcontent'):
   html_content = form.getvalue('htmlcontent')
else:
   html_content = "Not entered"

if form.getvalue('css1content'):
   css1_content = form.getvalue('css1content')
else:
   css1_content = "Not entered"

if form.getvalue('css2content'):
   css2_content = form.getvalue('css2content')
else:
   css2_content = "Not entered"

filename = "1.html"
file_object = open(filename,'w')
file_object.write(html_content)
file_object.close()

filename = "result\\1.html"
file_object = open(filename,'w')
file_object.write(html_content)
file_object.close()

filename = '1.css'
file_object = open(filename,'w')
file_object.write(css1_content)
file_object.close()

filename = 'result\\1.css'
file_object = open(filename,'w')
file_object.write(css1_content)
file_object.close()

filename = '2.css'
file_object = open(filename,'w')
file_object.write(css1_content)
file_object.close()

filename = 'result\\2.css'
file_object = open(filename,'w')
file_object.write(css2_content)
file_object.close()


print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Text Area - Fifth CGI Program</title>"
print "</head>"
print "<body>"
print "<h2> result\\1.html</h2>"
print '<div><iframe align="center" width="950" height="170" src="../result/1.html" frameborder="no" border="0" marginwidth="0" marginheight="0" scrolling="no"></iframe></div>'
print "<h2> result\\1.css </h2>"
print '<div><iframe align="center" width="950" height="170" src="../result/1.css" frameborder="no" border="0" marginwidth="0" marginheight="0" scrolling="no"></iframe></div>'
print "<h2> result\\2.css </h2>"
print '<div><iframe align="center" width="950" height="170" src="../result/1.css" frameborder="no" border="0" marginwidth="0" marginheight="0" scrolling="no"></iframe></div>'
print "</body>"

