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
obj.v = vector(15,0)
obj.pos = vector(WIDTH/2,HEIGHT/2-200)

obj2 = object()
obj2.v = vector(-15,0)
obj2.pos = vector(WIDTH/2,HEIGHT/2+200)

center = vector(WIDTH/2,HEIGHT/2)

def objUpdate():
    obj.force = obj.v.norm().normalized()*(obj.mass*(abs(obj.v)**2)/200)
    obj2.force = obj2.v.norm().normalized()*(obj2.mass*(abs(obj2.v)**2)/200)
    obj.update(1/FPS)
    obj2.update(1/FPS)

def scrUpdate(screen):
    drawPlot(screen, obj)
    drawPlot(screen, obj2)
    pygame.draw.line(screen, BLUE, [obj.pos.x,obj.pos.y],[center.x,center.y], 3)
    pygame.draw.line(screen, BLUE, [obj2.pos.x,obj2.pos.y],[center.x,center.y], 3)
    pygame.draw.circle(screen, BLACK, [obj.pos.x,obj.pos.y], 20)
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