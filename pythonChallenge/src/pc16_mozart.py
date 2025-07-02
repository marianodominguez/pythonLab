import Image

im = Image.open("mozart.gif")
data = im.load()
w,h = im.size

result = Image.new(im.mode, (w*2+1, h))

offset = [0]*h

x=0
y=0

while y<h:
    marker = False
    while not marker:
        pixel = data[x,y]
        if pixel >= 200 and data[x+1, y] == 195:
            marker = True
            offset[y] = x; 
        x+=1
    y+=1
    x=0

#print offset

for y in range(h):
    for x in range(w):
        nx = x + (w - offset[y])
        #print(nx)
        result.putpixel((nx,y), data[x,y])

result.save('straight.gif')
result.show()
