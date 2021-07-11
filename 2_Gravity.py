from physics import vector
from physics import object
import pygame, math

TITLE = 'gravity'
####################################
BLACK= ( 0,  0,  0)
WHITE= (255,255,255)
BLUE = ( 0,  0,255)
GREEN= ( 0,255,  0)
RED  = (255,  0,  0)
FPS = 100
ACCEL = 100
WIDTH = 800
HEIGHT = 600
CLOCK = 0
plot = []
G = 1

### ONLY EDIT THIS AREA ############
obj = object()
obj.pos = vector(WIDTH/2,HEIGHT/2)

obj2 = object()

obj.mass = 1000
obj2.mass = 10

init = (G*obj.mass/200)**0.5

init *= 1

obj2.v = vector(init,0)
obj2.pos = vector(WIDTH/2,HEIGHT/2+200)

center = vector(WIDTH/2,HEIGHT/2)

def gravity(ob1, ob2):
    gravity = G * ob1.mass * ob2.mass / abs(ob1.pos - ob2.pos)**2
    return (ob1.pos - ob2.pos).normalized() * gravity

def objUpdate():
    grforce = gravity(obj, obj2)
    obj.force = -grforce
    obj2.force = grforce
    # obj.update(1/FPS)
    obj2.update(1/FPS)

def scrUpdate(screen):
    drawPlot(screen, obj)
    drawPlot(screen, obj2)
    pygame.draw.circle(screen, BLACK, [obj.pos.x,obj.pos.y], 30)
    pygame.draw.circle(screen, BLACK, [obj2.pos.x,obj2.pos.y], 20)

######## Graphing Area #############

def drawPlot(screen, object):
    plot.append((object.pos.x, object.pos.y))
    for i in range(len(plot)):
        pygame.draw.circle(screen, BLACK, [plot[i][0],plot[i][1]],1)

def graphic():
    global FPS
    global CLOCK
    pygame.init()
    screen= pygame.display.set_mode([WIDTH,HEIGHT])
    pygame.display.set_caption(TITLE)
    done= False
    clock= pygame.time.Clock()
    FPS /= ACCEL
    while not done:
        clock.tick(FPS*ACCEL)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
    
        screen.fill(WHITE)
        CLOCK += 1/FPS
    
        objUpdate()
        scrUpdate(screen)
        
        screen.blit(pygame.transform.rotate(screen, 180), (0, 0))
        pygame.display.flip()

graphic()