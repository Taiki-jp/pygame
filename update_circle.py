from time import sleep
import pygame

aliasList = \
{
    "black" : (0, 0, 0),
    "white" : (255, 255, 255)
}

def updateCircle \
(
    screen, 
    x = 0, 
    y = 0,
    aliasList = aliasList,
    alias = None, 
    R = 50,
    G = 50,
    B = 10,
    width = 0
):
    if alias != None:
        print(f"alias {alias} is set !!")
    else:
        print(f"alias isn't set. Using (R, G, B) = {R}, {G}, {B}")
    for step in range(10, 250, 10):
        if alias != None:
            screen.fill((aliasList[alias][0],
                         aliasList[alias][1],
                         aliasList[alias][2]))
        else:
            screen.fill((R, G, B))
        pygame.draw.circle(screen, 
                           (R, G, B),
                           (x, y),
                           step,
                           width)
        pygame.display.update()
        sleep(1)
    return