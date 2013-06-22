import zipfile

filename = 'channel.zip'
param="90052"
info = '' 
while param != '':
    zfile = zipfile.ZipFile( filename, "r" )
    info += zfile.getinfo(param + ".txt").comment
    content = zfile.read(param + ".txt")
    print content

    search = "Next nothing is "
    if search in content:
        param = content.split(search,1)[1]
    else: param=''

    #print param

    print info;
