from tkinter import *

root = Tk()
canvas = Canvas(root, width=500, height=1000)
canvas.pack()

block_counter = 0

def create_block():
    block = canvas.create_rectangle(0, 0, 40, 40, fill="red")
    canvas.move(block, 50, 0)
    return block


def fall_block():
    global block
    global block_counter
    
    canvas.move(block, 0, 3)

    x0, y0, x1, y1 = canvas.coords(block)
    print(f"{y1=}")

    if y1 > 1000:
        canvas.delete(block)
        block_counter += 1
        block = create_block()

    if block_counter >= 2:
        exit()





    print("in fall block")
    canvas.after(10, fall_block)


block = create_block()
canvas.after(10, fall_block)


root.mainloop()