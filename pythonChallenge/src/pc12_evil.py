from PIL import Image, ImageDraw

im = open("evil2.gfx", 'r')
data = im.read()
out = open('evilOut.jpg', 'w');
i=0
for byte in data:
    if (i%5 == 0 ):
        out.write(byte)
    i+=1

out.close()

# open the file as image 

image = Image.open('evilOut.jpg')

image.show() 


