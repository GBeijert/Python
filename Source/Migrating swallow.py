import random
from microbit import *

# Globals 
wall_x = 4 
gap = 0

# Methods 
def check_player_movement():
    pass

def move_wall():
    global gap, wall_x

    display.clear()
    ## Don't forget!
    #redraw bird    
        
    if(wall_x == 0):
        wall_x = 4
        gap = random.randint(0,4)
    else:
        wall_x -= 1
    
    for i in range(5):
        if(i != gap):
            display.set_pixel(wall_x, i, 9)

def check_collision():
    pass

while True:
    check_player_movement()
    move_wall()
    check_collision()

    sleep(250)