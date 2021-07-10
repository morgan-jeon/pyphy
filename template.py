from physics import vector
from physics import object
import pygame, math

####################################
BLACK= ( 0,  0,  0)
WHITE= (255,255,255)
BLUE = ( 0,  0,255)
GREEN= ( 0,255,  0)
RED  = (255,  0,  0)
FPS = 100
ACCEL = 10
WIDTH = 800
HEIGHT = 600
CLOCK = 0
plot = []

### ONLY EDIT THIS AREA ############

obj = object()

def objUpdate():
    obj.force = vector(0,0)
    obj.update(1/FPS)

def scrUpdate(screen):
    drawPlot(screen, obj)
    pygame.draw.circle(screen, BLACK, [obj.pos.x,obj.pos.y], 20)

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
    pygame.display.set_caption("Basic Moving")
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