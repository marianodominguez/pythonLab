from PIL import Image
import sys

im = Image.open("oxygen.png").load()
endX=608
step=7
s=''
for x in range(0, endX, step):
    s += chr(im[x,46][1])

print(s)

found = [105,110,116,101,103,114,105,116,121]

for c in found:
    sys.stdout.write(chr(c))
