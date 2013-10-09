from PIL import Image, ImageDraw

im = Image.open("wire.png")
data = im.load()

out = Image.new(im.mode, (100,100))
w = 100
t = 0
i=0

#spiral

while i<w*w:
    y=t
    for x in xrange(t, w-t):
        out.putpixel((x ,y) , data[i,0])
        i+=1
    t+=1
    x=w-t
    for y in xrange(t, w-t):
        out.putpixel((x,y), data[i,0])
        i+=1
    y=w-t
    for x in xrange(w-t , t-1, -1):
        out.putpixel((x,y), data[i,0])
        i+=1
    x=t-1
    t+=1
    for y in xrange(w-t, t, -1):
        out.putpixel((x,y), data[i,0])    
        i+=1

out.save('italy_14.jpg')
out.show()


