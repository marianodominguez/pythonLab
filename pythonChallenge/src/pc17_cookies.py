import cookielib, urllib2

# create a password manager
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

top_level_url= "http://www.pythonchallenge.com/"

password_mgr.add_password(None, top_level_url, "huge", "file")

handler = urllib2.HTTPBasicAuthHandler(password_mgr)


cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), handler)

r = opener.open("http://www.pythonchallenge.com/pc/return/romance.html")

for cookie in cj:
    print "cookie:", cookie
