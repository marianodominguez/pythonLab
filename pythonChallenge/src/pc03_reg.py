import re

pattern = r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z\n]'
file = open("equality.txt").read()

strings = re.findall(pattern, file)

print "".join([x[4] for x in strings])

