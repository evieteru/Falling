from tkinter import *
import random
import time

XWIDTH = 500
YWIDTH = 1000

point_block_list = []

root = Tk()
canvas = Canvas(root, width=XWIDTH, height=YWIDTH)
canvas.pack()



#Point objects
def create_point_object():
    global point
    point = canvas.create_rectangle(0, 0, 30, 30, fill="green")
    canvas.move(point, random.randint(0, XWIDTH-30), 0)

    point_block_list.append(point)
    print(point_block_list)


    canvas.after(3000, create_point_object)
    






#Making point object fall one time
def point_block_fall():
    for point in point_block_list:
        canvas.move(point, 0, 7)
        #canvas.after(10, point_block_fall)


    





canvas.after(3000, create_point_object)
canvas.after(10, point_block_fall)




root.mainloop()
