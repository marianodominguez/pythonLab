from PIL import Image, ImageDraw

im = Image.open("cave.jpg")
data = im.load()
w,h = im.size

even = Image.new(im.mode, (w//2, h//2))

for x in range(0,w,2):
    for y in range(0,h,2):
        (nx, ny) = (x//2, y//2)
        even.putpixel((nx,ny), data[x,y])

even.save('even.jpg')

even.show()
