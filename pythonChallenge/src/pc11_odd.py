from PIL import Image, ImageDraw

im = Image.open("cave.jpg")
data = im.load()
w,h = im.size

odd = Image.new(im.mode, (w/2 +1, h/2 +1))
even = Image.new(im.mode, (w/2, h/2))

for x in xrange(0,w,2):
    for y in xrange(0,h,2):
        (nx, ny) = (x/2, y/2)
        even.putpixel((nx,ny), data[x,y])
        odd.putpixel((nx,ny), data[x+1,y])
        odd.putpixel((nx,ny+1), data[x,y+1])
        odd.putpixel((nx+1,ny+1), data[x+1,y+1])

#odd.save('odd.jpg')
even.save('even.jpg')

#odd.show()
even.show()