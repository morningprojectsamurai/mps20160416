#%matplotlib inline
from PIL import Image
import math
import random

#image size
WIDTH  = 64
HEIGHT = 64

#line length
MAX_LINE_LENGTH = 128

#color value (gray scale)
VALUE_WHITE = 255
VALUE_BLACK = 0
VALUE_GRAY = 100

### function draw line
def func_draw(pos,direction):
    flag = random.randint(0,2)
    if direction == [1,0]:
        if flag == 0:
            direction = [1,0]
        if flag == 1:
            direction = [1,1]
        if flag == 2:
            direction = [1,1]
    elif direction == [0,1]:
        if flag == 0:
            direction = [0,1]
        if flag == 1:
            direction = [1,1]
        if flag == 2:
            direction = [-1,1]
    elif direction == [1,1]:
        if flag == 0:
            direction = [1,1]
        if flag == 1:
            direction = [1,0]
        if flag == 2:
            direction = [0,1]
    elif direction == [-1,1]:
        direction = [0,1]
    #print ("flag:{0}, direction:{1},pos{2}".format(flag,direction,pos))
    pos = [x+y for (x,y) in zip(pos,direction)]
    return pos,direction


# function 
# track on the line
def func_track(pxls,startpos):
    prevpos = startpos
    pos = startpos

    line_count = 1
    pxls[pos[0],pos[1]] = VALUE_BLACK

    for idx in range(0, MAX_LINE_LENGTH):
        find_flag = False

        # direction to search
        directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
        for direction in directions:
            
            # move workpos to (pos + direction)
            workpos = [x+y for (x,y) in zip(pos,direction)]
            if (workpos[0] >= 0) and (workpos[1] >= 0) and (workpos[0]<WIDTH) and (workpos[1]<HEIGHT):
                if pxls[workpos[0],workpos[1]] == VALUE_WHITE:
                    if not workpos == prevpos :
                        #print ("pos{0},direction:{1},workpos:{2},value{3}".format(pos,direction,workpos,pxls[workpos[0],workpos[1]]))
                        prevpos = pos
                        pos = workpos
                        line_count += 1
                        find_flag = True
                        pxls[pos[0],pos[1]] = VALUE_GRAY
            if find_flag == True:
                break
        if find_flag == False:
            print ("next point was not found")
            break
            
    return line_count

### draw image
img = Image.new("L",(WIDTH,HEIGHT))
pxls=img.load()
pos = [0,0] #initial position
direction = [1,1] #initial direction
for idx in range(0,MAX_LINE_LENGTH):
    pos,direction = func_draw(pos,direction)
    if pos[0] < 0 or pos[0] >= WIDTH or pos[1] <0 or pos[1] >= HEIGHT:
        print ("line went out of image area!")
        break 
    pxls[pos[0],pos[1]] = VALUE_WHITE
img.save("sample_in.png")

### use image file
#img = Image.open("sample_in.png")
#pxls = img.load()

# track the line(sequence of white pixel)
line_count = func_track(pxls,[0,0])
print ("line length = ",line_count)
    
img.show()
img.save("sample_out.png")

print ("finish!")

