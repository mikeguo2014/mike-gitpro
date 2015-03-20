#!/usr/bin/env python 
#coding=utf-8 
#python version:2.7

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'textarea':
            print attrs
    def handle_endtag(self, tag):
        if tag == 'textarea':
            print
    def handle_data(self, data):
        print data
parser = MyHTMLParser()

htmlcontent = """
<html>

<head>

<!-- set textarea css -->
<style type="text/css">
#HtmlCode{
	height:300px;
    width: 800px;
}

#CssCode {
	height:100px;
    width: 800px;
}
</style>

</head>

<body>


<div id="butt">
    <input type="button" value="Click" onClick="submitTryit()">
</div>


<div id="CodeArea">
<h2>Edit your code</h2>

<h3>demo.html</h3>
<textarea id="HtmlCode" wrap="logical">
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="demo.css" />
</head>

<body>

  <demo-style>  demo </demo-style>
  write your code...

</body>
</html>
</textarea>

<!-- demo.css editor -->
<h3>demo.css</h3>
<textarea id="CssCode" wrap="logical">
demo-style{
  color: red;
}

</textarea>
</div>


<div id="result">
<h2>Display result</h2>
<iframe frameborder="1" name="i" src="result.html"></iframe>
</div>





</body>
</html>

"""

#print 'start'
#print htmlcontent
#print 'end'

parser.feed(htmlcontent)

