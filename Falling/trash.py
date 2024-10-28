from tkinter import *
import random

XWIDTH = 500
YWIDTH = 1000
X_OBSTACLE_SIZE = 30
Y_OBSTACLE_SIZE = 30


alive = True
#startx = random.randint(0, XWIDTH) #for generating obstacles



root = Tk()
canvas = Canvas(root, width=XWIDTH, height=YWIDTH)
canvas.pack()

#Draw Main Character
block = canvas.create_rectangle(0, 0, 50, 20, fill="brown")
canvas.move(block, 0, YWIDTH-20)

#Point objects
def create_point_object():
    point = canvas.create_rectangle(0, 0, 30, 30, fill="green")
    canvas.move(point, random.randint(0, XWIDTH-30), 0)
    return point



#Draw Food
def create_food():
    food = canvas.create_rectangle(0, 0, 10, 40, fill="red")
    canvas.move(food, random.randint(0, XWIDTH-10), 0)
    

#Draw Poison
def create_poison():
    poison = canvas.create_rectangle(0, 0, 50, 30, fill="black")
    canvas.move(poison, random.randint(0, XWIDTH-50), 0)

#Def blocks movement
def rightpush(event):
    x0, y0, x1, y1 = canvas.coords(block)
    if x1 < XWIDTH:
        canvas.move(block, 10, 0)


def leftpush(event):
    x0, y0, x1, y1 = canvas.coords(block)
    if x0 > 0:
        canvas.move(block, -10, 0)



#Main Character Movement
root.bind("<Right>", rightpush)
root.bind("<Left>", leftpush)

#Making point object fall one time
def point_block_fall():
    canvas.move(point_block, 0, 7)
    canvas.after(10, point_block_fall)


point_block = create_point_object()
canvas.after(random.randint(1000, 3000), point_block_fall)

#Collision of point object and basket one time
score = 0
xpoint0, ypoint0, xpoint1, ypoint1 = canvas.coords(point_block)
xbox0, ybox0, xbox1, ybox1 = canvas.coords(block)

if (xbox0 < xpoint0 < xbox1) or (xbox0 < xpoint1 < xbox1):
    score += 1   #ONLY ADDS TO SCORE WHEN RIGHT SIDE OF GREEN BOX GOES IN!!
    print(score)


root.mainloop()
