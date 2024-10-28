from tkinter import *
import random


XWIDTH = 500
YWIDTH = 750
X_POINT_BLOCK_SIZE = 30
Y_POINT_BLOCK_SIZE = 30

score = 0
block_counter = 0
move_speed = 2
is_play_again = False



root = Tk()
root.title("CS 190: Final Project")
canvas = Canvas(root, width=XWIDTH, height=YWIDTH)
canvas.pack()

#create basket
def create_basket():
    basket = canvas.create_rectangle(0, 0, 50, 20, fill="#632809")
    canvas.move(basket, 0, YWIDTH-20)
    return basket


def create_block():
    global block_counter

    colors_lst = ["#DE4841", "#DE8141", "#F0CE35", "#50925E", "#509291", "#5D6CE7", "#7B4796", "#E990E0"]
    fill_color = colors_lst[random.randint(0, len(colors_lst)-1)]
    
    block =canvas.create_rectangle(0, 0, X_POINT_BLOCK_SIZE, Y_POINT_BLOCK_SIZE, fill=fill_color, outline="")
    canvas.move(block, random.randint(0, XWIDTH-X_POINT_BLOCK_SIZE), 0)
    block_counter += 1
    return block
    

    
def fall_collision_block():
    global score
    global basket 
    global block
    global block_counter
    global move_speed

    #Move speed
    if block_counter < 4:
        canvas.move(block, 0, move_speed)

    if 4 <= block_counter < 7:
        canvas.move(block, 0, move_speed+1)

    if 7 <= block_counter < 10:
        canvas.move(block, 0, move_speed+2)

    if 10 <= block_counter < 13:
        canvas.move(block, 0, move_speed+3)

    if 13 <= block_counter < 16:
        canvas.move(block, 0, move_speed+4)

    if 16 <= block_counter < 19:
        canvas.move(block, 0, move_speed+6)

    if 19 <= block_counter < 21:
        canvas.move(block, 0, move_speed+8)

    if block_counter >= 21:
        canvas.move(block, 0, move_speed+12)
    
    #Collision detection 
    x0basket, y0basket, x1basket, y1basket = canvas.coords(basket)
    x0block, y0block, x1block, y1block, = canvas.coords(block)

    if (y1block > y0basket and x0basket<=x0block<=x1basket) or (y1block > y0basket and x0basket<=x1block<=x1basket):
        canvas.delete(block)
        score = score + 1
        print(score)
        block = create_block()
    
    

    
    if y0block > YWIDTH:
        canvas.delete(block)
        end_game()

        
        
       



    canvas.after(10, fall_collision_block)
        





#basket movement
def rightpush(event):
    x0, y0, x1, y1 = canvas.coords(basket)
    if x1 < XWIDTH:
        canvas.move(basket, 10, 0)

def leftpush(event):
    x0, y0, x1, y1 = canvas.coords(basket)
    if x0 > 0:
        canvas.move(basket, -10, 0)




#Writing score to a file, New window saying game over
def end_game():
    global score
    global block_counter
    global basket
    global game_over_window
    global is_play_again

    #reset
    block_counter = 0
    canvas.move(basket, 0, YWIDTH-20)


    try:
        with open("scores.txt", 'a') as scores_file:
            scores_file.write(str(score) + "\n")

    except Exception as err:
            print(err)

    game_over_window = Toplevel()
    game_over_window.geometry("200x100")
    game_over_window.title(":(")

    label = Label(game_over_window, text="GAME OVER")
    label.grid(row=0, column=0,)
    

    score_label = Label(game_over_window, text=f"Score: {score}")
    score_label.grid(row=1, column=0)


    button = Button(game_over_window, text="Play again?")
    button.grid(row=2, column=0)
    button.bind("<ButtonPress>", start_game)

    is_play_again = True

    game_over_window.mainloop()



root.bind("<Right>", rightpush)
root.bind("<Left>", leftpush)



#Starts create block, fall, create block process 
def start_game(event):
    global block
    global basket
    global game_over_window
    global score
    
    score = 0

    if is_play_again == True:
        game_over_window.destroy()
        
    basket = create_basket()
    block = create_block()
    canvas.after(10, fall_collision_block)



start_game(None)



root.mainloop()




'''
All coded by Evie Wilbur

Time log:

4 hours spent on a scratched idea over break

11/25 - 30 min
11/26 - 30 min
11/29 - 1hr
11/30 - 50 min
12/2 - 1 hr 20 min
12/3 - 2 hr
12/4 - 1hr 30 min
12/5 - 2 hr 30 min
12/8 - 40 min
12/9 - 1 hr 40 min

'''