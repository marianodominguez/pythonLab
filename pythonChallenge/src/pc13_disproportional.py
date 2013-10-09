#import urllib, urllib2

#url = 'http://www.pythonchallenge.com/pc/phonebook.php'

#req = urllib2.Request(url, '<remote/>', 
#                      headers={'Content-Type': 'application/xml'})
#response = urllib2.urlopen(req)
#print response.geturl()
#print response.info()
#the_page = response.read()
#print the_page

import xmlrpclib
server = xmlrpclib.Server('http://www.pythonchallenge.com/pc/phonebook.php')

#print server.system.listMethods()

print server.phone('Bert')
