from tkinter import *
import random
import config as cfg
GAME_WIDTH=cfg.GAME_WIDTH
GAME_HEIGHT=cfg.GAME_HEIGHT
SPEED=cfg.SPEED
SPACE_SIZE=cfg.SPACE_SIZE
BODY_PARTS=cfg.BODY_PARTS
SNAKE_COLOR=cfg.SNAKE_COLOR
FOOD_COLOR=cfg.FOOD_COLOR
BACKGROUND_COLOR=cfg.BACKGROUND_COLOR

class Snake:
    pass
class Food:
    pass

def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_collision():
    pass

def game_over():
    pass

if __name__ == '__main__':
    window=Tk()
    window.title("Snake Game")
    window.resizable(False,False)

    score=0
    direction='down'

    label=Label(window,text="Score:{}".format(score),font=('consolas',40))
    label.pack()

    canvas=Canvas(window,bg=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH)
    canvas.pack()
    window.update()

    window.mainloop()