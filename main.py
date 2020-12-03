from update_circle import *

def main \
(
    width = 600,
    hight = 400
):
    pygame.init()
    screen = pygame.display.set_mode((width, hight))
    pygame.display.set_caption("Pygame Test")
    updateCircle(screen, 
                 int(width/2), 
                 int(hight/2), 
                 alias = "white")
    return

if __name__ == '__main__':
    main()