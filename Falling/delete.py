from tkinter import *
import random

XWIDTH = 500
YWIDTH = 1000
X_POINT_BLOCK_SIZE = 30
Y_POINT_BLOCK_SIZE = 30


root = Tk()
canvas = Canvas(root, width=500, height=1000)
canvas.pack()

#create basket
basket = canvas.create_rectangle(0, 0, 50, 20, fill="brown")
canvas.move(basket, 0, YWIDTH-20)

block =canvas.create_rectangle(0, 0, X_POINT_BLOCK_SIZE, Y_POINT_BLOCK_SIZE, fill="red")
canvas.move(block, random.randint(0, XWIDTH-X_POINT_BLOCK_SIZE), 0)


x0block, y0block, x1block, y1block, = canvas.coords(block)


def move_block():
    canvas.move(block, 0, YWIDTH+1)

canvas.after(1000, move_block)

x0block, y0block, x1block, y1block, = canvas.coords(block)


if y0block > YWIDTH:
        print(f'before{basket=}')
        canvas.delete(basket)
        print(f'after{basket=}')


        canvas.delete(block)

root.mainloop()