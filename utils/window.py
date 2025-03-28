import pygame as pg
from camera import init
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from esfera import draw_sphere


def main():
   
    init()  
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  
        draw_sphere()  
        pygame.display.flip()  
        pygame.time.wait(10)  

    pygame.quit()

if __name__ == "__main__":
    main()
