import pygame
from constants import *

def main():
    pygame.init
    print ("Starting asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
    game_loop()

def game_loop():
    Clock = pygame.time.Clock()
    dt = 0
    while True:
        pygame.display.flip()



        dt = Clock.tick(30)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__=="__main__":
    main()