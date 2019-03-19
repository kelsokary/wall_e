from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
import math

def drawLines(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex(x1, y1)
    glVertex(x2, y2)
    glEnd()


def drawDashLine(x,y,step):
    drawLines(x,y,x+step,y)
    drawLines(x+2*step,y,x+3*step,y)
    drawLines(x + 4 * step, y, x + 5 * step, y)
    drawLines(x + 6 * step, y, x + 7 * step, y)


def drawCircle(r=0.025, xc=0, yc=0,l=0,h=2,outline=True):
    glBegin(GL_POLYGON)
    for theta in np.arange(l*math.pi, h*math.pi, 0.001):
        x = xc + r * math.cos(theta)
        y = yc + r * math.sin(theta)
        glVertex(x, y)
    glEnd()
    if outline == True:
        glColor3f(0, 0, 0)
        glBegin(GL_LINE_LOOP)
        for theta in np.arange(l * math.pi, h * math.pi, 0.001):
            x = xc + r * math.cos(theta)
            y = yc + r * math.sin(theta)
            glVertex(x, y)
        glEnd()

def drawRect(x1=0.125, y1=0.25, x2=-0.125, y2=0.25, x3=-0.125, y3=-0.15, x4=0.125, y4=-0.15, outline=True):
    glBegin(GL_POLYGON)
    glVertex(x1,y1)
    glVertex(x2,y2)
    glVertex(x3,y3)
    glVertex(x4,y4)
    glEnd()
    if outline == True:
        glColor3f(0, 0, 0)
        glBegin(GL_LINE_LOOP)
        glVertex(x1, y1)
        glVertex(x2, y2)
        glVertex(x3, y3)
        glVertex(x4, y4)
        glEnd()


def drawEyes():
    glColor3f(0,0,0.75)
    drawCircle(0.07,0.215,0.3)
    glColor3f(0.7134, 0.7809, 0.82)
    drawCircle(0.085, 0.19,0.35)
    glColor3f(0.7134, 0.7809, 0.82)
    drawCircle(0.05,0.27,0.41)
    glColor3f(0.4234, 0.592, 0.73)
    drawCircle(0.07,0.23,0.38,0,2)
    glColor3f(0,0,0)
    drawCircle(0.035,0.23,0.38,0,2)
    glColor3f(0.44, 0.44, 0.44)
    drawCircle(0.0125,0.225,0.375,0,20,False)
    glColor3f(0.28,0.401,0.5)
    drawCircle(0.0085,0.18,0.295,0,20,False)
    drawCircle(0.0085, 0.129, 0.36, 0, 20, False)



def drawHand():
    glColor3f(0.5846, 0.6571, 0.74)
    drawRect(0.1, 0.02, -0.1, 0.02, -0.1, -0.02, 0.1, -0.02)
    glColor3f(0.5846, 0.6571, 0.74)
    drawRect(0.06, 0.08, -0.1, 0.08, -0.1, 0.015, 0.06, 0.015)
    glColor3f(0.5846, 0.6571, 0.74)
    drawRect(0.13, 0.05, 0.06, 0.08, 0.06, 0.015, 0.13, 0.015)
    glColor3f(0.5846, 0.6571, 0.74)
    drawRect(0.06, -0.002, -0.1, -0.002, -0.1, -0.067, 0.06, -0.067)
    glColor3f(0.5846, 0.6571, 0.74)
    glTranslate(0, -0.082, 0)
    drawRect(0.13, 0.08, 0.06, 0.08, 0.06, 0.015, 0.13, 0.045)
    glColor3f(0.5846, 0.6571, 0.74)
    glTranslate(0,0.082,0)
    drawRect(-0.08, 0.04, -0.06, 0.04, -0.06, -0.03, -0.08, -0.03)


def drawBody():
    glColor3f(0.44, 0.6155, 0.0984)
    drawRect(0.425, 0.5, -0.425, 0.5, -0.425, -0.2, 0.425, -0.2)
    glColor3f(0.82, 0.6155, 0.0984)
    drawRect(0.45,0.5,-0.45,0.5,-0.45,0.3,0.45,0.3)
   
    drawRect(0.425, 0.5, -0.425, 0.5, -0.425, 0.45, 0.425, 0.45)
    glColor3f(0.3996, 0.4698, 0.54)
    drawRect(0.22, 0.447, 0.2, 0.447, 0.2, 0.307, 0.22, 0.307, False)
    glColor3f(0.3996, 0.4698, 0.54)
    drawRect(-0.22, 0.447, -0.2, 0.447, -0.2, 0.307, -0.22, 0.307, False)
    glColor3f(0.5846, 0.6571, 0.74)
    drawRect(0.2, 0.5, -0.2, 0.5, -0.2, 0.3, 0.2, 0.3)
    drawLines(0, 0.5, 0, 0.3)

    glColor3f(0.82, 0.6155, 0.0984)
    drawRect(-0.04, 0.29, -0.3, 0.29, -0.3, -0.04, -0.04, -0.04, False)

    drawRect(0.1, 0.6, -0.1, 0.6, -0.1, 0.5, 0.1, 0.5)
    glColor3f(1, 1, 1)
    drawLines(0.07, 0.58, -0.07, 0.58)
    glColor3f(0.51, 0.3213, 0.204)
    drawRect(0.07, 0.7, -0.07, 0.7, -0.07, 0.6, 0.07, 0.6)
    glColor3f(1, 1, 1)
    drawLines(-0.05, 0.62, -0.05, 0.68)
    glColor3f(0.51, 0.3213, 0.204)



def drawWheel():
    glColor3f(0.3, 0.3, 0.3)
    drawRect()
    glColor3f(1, 1, 1)
    drawLines(-0.125, 0.2, 0.03, 0.2)
    drawLines(0.045, 0.2, 0.085, 0.2)
    drawLines(0.125, 0.15, -0.08, 0.15)
    drawLines(0.085, 0.1, -0.125, 0.1)
    drawLines(-0.125, 0.05, 0.03, 0.05)
    drawLines(0.045, 0.05, 0.085, 0.05)
    drawLines(0.125, 0, -0.08, 0)
    drawLines(0.085, -0.05, -0.125, -0.05)
    drawLines(-0.125, -0.1, 0.03, -0.1)
    drawLines(0.045, -0.1, 0.085, -0.1)


def drawGround():
    glColor3f(0, 0, 0)
    glLineWidth(4)



def drawName():
    glColor3f(0.58, 0.2212, 0.45)
    glLineWidth(5)
    glColor3f(0.77,0.2433,0.2156)
    drawCircle(0.095,0.56,0.04,0,2,False)
    glColor3f(1,1,1)
    drawLines(0.53,0,0.53,0.08)
    drawLines(0.53,-0.01,0.59,-0.01)
    drawLines(0.53,0.04,0.59,0.04)
    drawLines(0.53,0.09,0.59,0.09)

def draw():
    glClearColor(1, 0.3, 0.4, 0.7)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glTranslate(0,0.4,0)
    glColor3f(0.9025, 0.9278, 0.95)
    drawCircle(1.2, 0, 0, 0, 2, True)
    glLoadIdentity()
    glTranslate(0, -0.7, 1)
    drawGround()
    glLoadIdentity()
    glTranslate(0.55, -0.544, 1)
    drawWheel()
    glLoadIdentity()
    glTranslate(-0.55, -0.544, 1)
    drawWheel()
    glLoadIdentity()
    glTranslate(0, -0.25, 0)
    drawBody()
    glLoadIdentity()
    glTranslate(-0.37,0.05,0)
    glScale(1,1.25,1)
    drawHand()
    glLoadIdentity()
    glRotate(180,0,1,0)
    glTranslate(-0.37,0.05,0)
    glScale(1,1.25,1)
    drawHand()
    glLoadIdentity()
    glRotate(180, 0, 1, 0)
    glTranslate(-0.35,0.18,0)
    drawEyes()
    glLoadIdentity()
    glRotate(360,0,1,0)
    glTranslate(-0.35,0.18,0)
    drawEyes()
    glLoadIdentity()
    glColor3f(0.028, 0.2212, 0.35)
    glTranslate(-0.25,-0.1,0)
    glLineWidth(5)
    drawLines(0,0,0.1,0.1)
    glTranslate(0.05,0,0)
    drawLines(0,0,0.05,0.05)
    glLoadIdentity()
    glScale(0.5,0.5,1)
    glTranslate(0.09,-0.69,0)
    drawName()
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE)
glutInitWindowSize(700, 700)
glutCreateWindow(b'WALL-E')
glutDisplayFunc(draw)                            # Initialize our window.
glutMainLoop()