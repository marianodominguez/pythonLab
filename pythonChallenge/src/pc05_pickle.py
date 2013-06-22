import pprint
import pickle
reader = pickle.load(open('banner.p'))
#pprint.pprint(reader)
s = ''
for list in reader:
    for chr,times in list: 
        s+= times * chr
    s+="\n"

print s
