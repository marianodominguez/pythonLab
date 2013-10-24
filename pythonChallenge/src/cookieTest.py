import urllib
import httplib2

http = httplib2.Http()

url = 'http://www.pythonchallenge.com/pc/return/cookies.html'   
http.add_credentials('huge', 'file')

response, content = http.request(url, 'GET')

print response
