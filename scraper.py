import urllib
import re
from html import HTML


import webbrowser

def link(text, url):
    return '<a href="%s">%s</a>' % (url, text)


def MakeHTML(arg1):

	'''Napravi HTML file i otvori ga u browser'''

	f = open('output.html', 'w')
	f.write('<table border="1">')
	for link in arg1:
		f.write('<tr><td>' + '<a href="http://www.vijesti.me' + link[0].strip('"') + '"> ' + link[1] +  '</a>' + '</td></tr>')
	f.close()
	
urls = ["http://your.web.site"]

#regex = '<title>(.+?)</title>'
regex = '<a href=(.+?) title=(.+?)>'
regex2 = '<a class="link" href=(.+?) title=(.+?)>'
pattern = re.compile(regex)
pattern2 = re.compile(regex2)
for x in urls:
	htmlfile = urllib.urlopen(x)
	htmltext = htmlfile.read()
	titles = re.findall(pattern, htmltext)
	titles2 = re.findall(pattern2, htmltext)
	MakeHTML(titles2)
	for x in titles:
		print "http://www.vijesti.me" + x[0].strip('"'), x[1]
	for x in titles2:
		print "http://www.vijesti.me" + x[0].strip('"'), x[1]
