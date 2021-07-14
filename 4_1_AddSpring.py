from physics import vector
from physics import object
import pygame, math
# import matplotlib

####################################
BLACK= ( 0,  0,  0)
WHITE= (255,255,255)
BLUE = ( 0,  0,255)
GREEN= ( 0,255,  0)
RED  = (255,  0,  0)
FPS = 1000
ACCEL = 50
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
obj.mass = 200
obj.pos = vector(WIDTH/2, HEIGHT/2+50)

spring = springObj()
spring.startPos = vector(WIDTH/2, HEIGHT/2+150)
spring.endPos = obj.pos
spring.length = 150
spring.k = 16

obj2 = object()
obj2.mass = 200
obj2.pos = vector(WIDTH/2, HEIGHT/2-200)

spring2 = springObj()
spring2.startPos = obj.pos
spring2.endPos = obj2.pos
spring2.length = 150
spring2.k = 16

def objUpdate():
    spring.endPos = obj.pos
    spring2.startPos = obj.pos
    spring2.endPos = obj2.pos
    kx = (abs(spring.startPos - spring.endPos) - spring.length) * spring.k
    kx2 = (abs(spring2.startPos - spring2.endPos) - spring2.length) * spring2.k
    obj.force = (spring.startPos - spring.endPos).normalized() * kx
    obj.force += (spring2.startPos - spring2.endPos).normalized() * -kx2
    obj2.force = (spring2.startPos - spring2.endPos).normalized() * kx2
    obj.update(1/FPS)
    obj2.update(1/FPS)

def scrUpdate(screen):
    # drawPlot(screen, obj)
    drawPlot(screen, obj2)
    pygame.draw.circle(screen, BLACK, [obj.pos.x,obj.pos.y], 20)
    pygame.draw.line(screen, BLACK, [spring.startPos.x,spring.startPos.y],[spring.endPos.x,spring.endPos.y], 2)
    pygame.draw.circle(screen, BLACK, [obj2.pos.x,obj2.pos.y], 20)
    pygame.draw.line(screen, BLACK, [spring2.startPos.x,spring2.startPos.y],[spring2.endPos.x,spring2.endPos.y], 2)

######## Graphing Area #############

def drawPlot(screen, object):
    plot.append((object.pos.x, object.pos.y, CLOCK))
    for i in range(len(plot)):
        pygame.draw.circle(screen, BLACK, [plot[i][0]+(CLOCK-plot[i][2])*3,plot[i][1]],1)

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