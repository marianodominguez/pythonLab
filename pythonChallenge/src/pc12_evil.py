from PIL import Image

out = [None]*5

im = open("evil2.gfx", 'r')
data = im.read()
for i in range(5):
 out[i] = open('evilOut'+ str(i) +'.jpg', 'w');
i=0

for byte in data:
    out[i].write(byte)
    i = (i+1) % 5

[out[i].close() for i in range(5)]

# open the file as image 

#image = Image.open('evilOut.jpg')

#image.show() 


