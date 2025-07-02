import urllib.request

def download(url):
    try:
        furl = urllib.request.urlopen(url)
        return furl.read().decode('utf-8')
    except:
        print('Unable to download file')


baseurl = r'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
param="46059"

while param != '':
    content = download(baseurl+param)
    print(content)
    search = "next nothing is "
    result = content.split(search,1)
    param = ''
    if len(result) > 1: 
        param = result[1]
    print(param)
