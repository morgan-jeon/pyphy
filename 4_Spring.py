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
ACCEL = 5
WIDTH = 800
HEIGHT = 600
CLOCK = 0
plot = []

### ONLY EDIT THIS AREA ############

class springObj:
    startPos = vector(0,0)
    endPos = vector(0,1)
    length = 1
    k = 1

obj = object()
obj.pos = vector(WIDTH/2, HEIGHT/2-190)

spring = springObj()
spring.startPos = vector(WIDTH/2, HEIGHT/2+150)
spring.endPos = obj.pos
spring.length = 240
spring.k = 1


def objUpdate():
    spring.endPos = obj.pos
    kx = (abs(spring.startPos - spring.endPos) - spring.length) * spring.k
    obj.force = (spring.startPos - spring.endPos).normalized() * kx
    print(obj.force)
    obj.update(1/FPS)

def scrUpdate(screen):
    drawPlot(screen, obj)
    pygame.draw.circle(screen, BLACK, [obj.pos.x,obj.pos.y], 30)
    pygame.draw.line(screen, BLACK, [spring.startPos.x,spring.startPos.y],[spring.endPos.x,spring.endPos.y], 2)

######## Graphing Area #############

def drawPlot(screen, object):
    plot.append((object.pos.x, object.pos.y, CLOCK))
    for i in range(len(plot)):
        pygame.draw.circle(screen, BLACK, [plot[i][0]+(CLOCK-plot[i][2])*50,plot[i][1]],1)

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
        
        screen.blit(pygame.transform.flip(screen, False, True), (0, 0))
        pygame.display.flip()

graphic()