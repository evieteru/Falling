from tkinter import *
import random


XWIDTH = 500
YWIDTH = 1000
X_POINT_BLOCK_SIZE = 30
Y_POINT_BLOCK_SIZE = 30

score = 0
block_counter = 0
move_speed = 2


root = Tk()
canvas = Canvas(root, width=500, height=1000)
canvas.pack()

#create basket
basket = canvas.create_rectangle(0, 0, 50, 20, fill="brown")
canvas.move(basket, 0, YWIDTH-20)





root = Tk()



game_over_window = Toplevel()
game_over_window.geometry("200x100")
game_over_window.title(":(")

label = Label(game_over_window, text="GAME OVER")
label.grid(row=0, column=0)

button = Button(game_over_window, text="Play again?")
button.grid(row=1, column=0)
button.bind("<ButtonPress>", new_game)

game_over_window.mainloop()


root.mainloop()