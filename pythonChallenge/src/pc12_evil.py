from PIL import Image, ImageDraw

im = Image.open("evil1.jpg")
data = im.load()
w,h = im.size

image = Image.new(im.mode, (w, h))

i,j = (0,0)
for x in xrange(0, w):
    for y in xrange(0, h, 6):
            for i in xrange(0,6):
                image.putpixel(( x +i, y ), data[x,y])
                
            
image.show() 

# new image folded in x, 6 

#images.append( Image.new(im.mode, (h / 6 , w / 6 )) )      

#images[1].show()  