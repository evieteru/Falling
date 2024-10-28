from tkinter import *
import random


XWIDTH = 500
YWIDTH = 1000
X_OBSTACLE_SIZE = 30
Y_OBSTACLE_SIZE = 30

score = 0
block_counter = 0
move_speed = 2

root = Tk()
canvas = Canvas(root, width=500, height=1000)
canvas.pack()

def create_block():
    global block_counter


    block =canvas.create_rectangle(0, 0, 40, 40, fill="red")
    canvas.move(block, random.randint(0, XWIDTH-40), 0)
    block_counter += 1
    print(block_counter)
    return block
    

    
def fall_collision_block():
    global score
    global block
    global move_speed



    if block_counter < 4:
        canvas.move(block, 0, move_speed)

    if 4 <= block_counter < 7:
        canvas.move(block, 0, move_speed+2)

    if 7 <= block_counter < 10:
        canvas.move(block, 0, move_speed+4)

    if 10 <= block_counter < 13:
        canvas.move(block, 0, move_speed+6)

    if 13 <= block_counter < 16:
        canvas.move(block, 0, move_speed+8)

    if 16 <= block_counter < 19:
        canvas.move(block, 0, move_speed+10)

    if block_counter >= 19:
        canvas.move(block, 0, move_speed+12)


    x0block, y0block, x1block, y1block, = canvas.coords(block)

    if y0block > YWIDTH:
        block = create_block()

    

    canvas.after(10, fall_collision_block)



block = create_block()
canvas.after(10, fall_collision_block)

root.mainloop()