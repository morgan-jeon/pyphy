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

class springObj:
    startPos = vector(0,0)
    endPos = vector(0,1)
    length = 1
    k = 1

class ang_object:
    pos1 = vector(0,0)
    pos2 = vector(0,1)
    I = 1
    alpha = 0
    omega = 0
    angle = 0
    center = vector(0,0)
    force = [vector(0,0),vector(0,0)]
    torque = 0

    def update(self, timeInterval: int):
        self.torque = 0
        self.alpha = 0
        for Force in self.force:
            self.torque += (Force[0] - self.center) @ Force[1]
        self.alpha = self.torque / self.I
        self.omega += self.alpha * timeInterval
        self.angle = self.omega * timeInterval
        self.pos1 = (self.pos1 - self.center).rotated(self.angle*math.pi/180) + self.center
        self.pos2 = (self.pos2 - self.center).rotated(self.angle*math.pi/180) + self.center

obj = object()
obj.pos = vector(WIDTH/2-200, HEIGHT/2-95)
obj.mass = 10

obj2 = object()
obj2.pos = vector(WIDTH/2+200, HEIGHT/2-250)
obj2.mass = 10

spring = springObj()
spring.startPos = vector(WIDTH/2-200, HEIGHT/2+150)
spring.endPos = obj.pos
spring.length = 240
spring.k = 20

spring2 = springObj()
spring2.startPos = vector(WIDTH/2+200, HEIGHT/2+150)
spring2.endPos = obj2.pos
spring2.length = 240
spring2.k = 30

pane = ang_object()
pane.pos1 = vector(spring.startPos.x,spring.startPos.y)
pane.pos2 = vector(spring2.startPos.x,spring2.startPos.y)
pane.I = 160000
pane.center = (pane.pos1 + pane.pos2)/2 # + vector(40,0)

def objUpdate():
    spring.startPos = pane.pos1
    spring2.startPos = pane.pos2

    spring.endPos = obj.pos
    kx = (abs(spring.startPos - spring.endPos) - spring.length) * spring.k

    spring2.endPos = obj2.pos
    kx2 = (abs(spring2.startPos - spring2.endPos) - spring2.length) * spring2.k

    obj.force = (spring.startPos - spring.endPos).normalized() * kx
    obj2.force = (spring2.startPos - spring2.endPos).normalized() * kx2

    SF = []
    SF.append([pane.pos1,-obj.force])
    SF.append([pane.pos2,-obj2.force])
    pane.force = SF

    obj.force += vector(0, -obj.mass * 10)
    obj2.force += vector(0,-obj2.mass * 10)

    obj.update(1/FPS)
    obj2.update(1/FPS)
    pane.update(1/FPS)
    
def scrUpdate(screen):
    drawPlot(screen, obj)
    drawPlot(screen, obj2)
    pygame.draw.circle(screen, BLACK, [obj.pos.x,obj.pos.y], 30)
    pygame.draw.circle(screen, BLACK, [obj2.pos.x,obj2.pos.y], 30)
    pygame.draw.circle(screen, BLACK, [pane.center.x,pane.center.y], 5)
    pygame.draw.line(screen, BLACK, [spring.startPos.x,spring.startPos.y],[spring.endPos.x,spring.endPos.y], 2)
    pygame.draw.line(screen, BLACK, [spring2.startPos.x,spring2.startPos.y],[spring2.endPos.x,spring2.endPos.y], 2)
    pygame.draw.line(screen, BLACK, [pane.pos1.x,pane.pos1.y],[pane.pos2.x,pane.pos2.y], 2)

######## Graphing Area #############

def drawPlot(screen, object):
    plot.append((object.pos.x, object.pos.y, CLOCK))
    for i in range(len(plot)):
        pygame.draw.circle(screen, BLACK, [plot[i][0]+(CLOCK-plot[i][2])*5,plot[i][1]],1)

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