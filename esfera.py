from OpenGL.GL import *
from OpenGL.GLU import *

def draw_sphere():
    glPushMatrix() 
    glColor3f(0.0, 0.5, 1.0)  
    quadric = gluNewQuadric()  
    gluSphere(quadric, 1, 32, 32)  
    glPopMatrix()  
