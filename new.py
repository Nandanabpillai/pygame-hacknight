import pygame, random

pygame.init()

width, height = 1100, 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

w, h = 100, 200
skySurface = pygame.image.load('sky/1.jpg').convert_alpha()
skySurface = pygame.transform.scale(skySurface,((1100,500)))
nightSky = pygame.image.load('sky/night.png').convert_alpha()
nightSky = pygame.transform.scale(nightSky,((1100,500)))
grSurface = pygame.image.load('sky/gr.png').convert_alpha()
grSurface = pygame.transform.scale(grSurface,((1100,200)))
grNight = pygame.image.load('sky/ngr.png').convert_alpha()
grNight = pygame.transform.scale(grNight,((1100,200)))
jumpan = pygame.image.load('dino/d1.png').convert_alpha()
jumpan = pygame.transform.scale(jumpan,((200,217))) 

def score():
    global points
    points+=0.2
    text=font.render("Score: " + str(int(points)), True, (0,0,0))
    textRect=text.get_rect()
    textRect.center=(1000,30)
    screen.blit(text, textRect)
    
def redrawGameWindow():
    screen.blit(jumpan, (x,y))
    pygame.display.update()

def tospawn(loop):
        return loop % 100 == 0

def spawn_cactus():
    if len(obstacles) > 0:
        prev_cactus = obstacles[-1]
        r = random.randint(prev_cactus.cactPos + 200 + 84, 1100 + prev_cactus.cactPos + 200 + 84)
        
    else:
        r = random.randint(1200, 1500)

    cact = Cact(r)
    obstacles.append(cact)

class Cact:
    def __init__(self, cactPos):
        self.cactPos = cactPos

    def cactnewPos(self, dx):
        self.cactPos -= dx
        if self.cactPos <= 0:
            obstacles.pop(0)

    def displayCact(self, cactPosY, frameCact):
        screen.blit(cactus[3], (self.cactPos, cactPosY))
        self.rect=pygame.Rect(self.cactPos, cactPosY,49,130)

loop = 0
grPos = 0
cactPos = 1020
birdPos = 980
animations = []
cactus = []
obstacles = []
bird = []
lastUpdate = pygame.time.get_ticks()
animationTime = 100
frame = 0
frameBird = 0
isJump = False
jumpCount = 5
x = 50
y = 80
points=0
font=pygame.font.SysFont('Helvetica',30)
collision = 0
sc = random.randint(250, 400)

animations.append(pygame.image.load('dino/d1.png'))
animations.append(pygame.image.load('dino/d2.png'))
animations.append(pygame.image.load('dino/d3.png'))
animations.append(pygame.image.load('dino/d4.png'))

cactus.append(pygame.image.load('dino/c1.png'))
cactus.append(pygame.image.load('dino/c2.png'))
cactus.append(pygame.image.load('dino/c3.png'))
cactus.append(pygame.image.load('dino/c4.png'))
cactus.append(pygame.image.load('dino/c5.png'))
cactus.append(pygame.image.load('dino/c6.png'))

bird.append(pygame.image.load('bird/b1.png'))
bird.append(pygame.image.load('bird/b3.png'))
bird.append(pygame.image.load('bird/b6.png'))

run = True
while run:
    loop += 1
    pygame.mixer.init()
    soundobj=pygame.mixer.Sound('audio.wav')
    soundobj.play(-1)

    for event in pygame.event.get():
        if event .type == pygame.QUIT:
            run = False

    if collision == 0:
        keys = pygame.key.get_pressed()
    
        if points < sc:
            screen.blit(grSurface, (grPos,400))
            screen.blit(skySurface, (0,0))
            if not (keys[pygame.K_SPACE] or keys[pygame.K_UP]):
                screen.blit(animations[frame], (50,300))
                frameRect=pygame.Rect(50,300,187,217)
            else:
                if not isJump:
                    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                        frameRect=pygame.Rect(50,80,187,217)
                        isJump=True
                else:
                    if jumpCount>=-5:
                        neg=1
                        if jumpCount<0:
                            neg=-1
                        y-=(jumpCount**2)*0.5*neg
                        jumpCount-=1
                    else:
                        isJump=False
                        jumpCount=5
                redrawGameWindow()
        else:
            screen.blit(grNight, (grPos,400))
            screen.blit(nightSky, (0,0))
            if not (keys[pygame.K_SPACE] or keys[pygame.K_UP]):
                screen.blit(animations[frame], (50,300))
                screen.blit(bird[frameBird], (birdPos, 70))
                birdPos -= 10
                if birdPos < 0:
                    birdPos = 980
            else:
                if not isJump:
                    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                        isJump=True
                else:
                    if jumpCount>=-10:
                        neg=1
                        if jumpCount<0:
                            neg=-1
                        y-=(jumpCount**2)*0.5*neg
                        jumpCount-=1
                    else:
                        isJump=False
                        jumpCount=10
                redrawGameWindow()
            
        grPos -= 20
        if grPos < -100:
            grPos = 0
            
        currentTime = pygame.time.get_ticks()
        if currentTime - lastUpdate >= animationTime:
            frame += 1
            frameBird += 1
            lastUpdate = currentTime
            if frame >= len(animations):
                frame = 0
            if frameBird >= len(bird):
                frameBird = 0
        
        if tospawn(loop):
            spawn_cactus()
    
        for i in obstacles:
            i.displayCact(380,0)
            i.cactnewPos(10)
            if frameRect.colliderect(i.rect):
                #print(i.rect)
                collision = 1
                screen = pygame.display.set_mode((width,height))
                pygame.display.set_caption('Game Over!!!')
                screen.blit(grSurface, (0,400))
                screen.blit(skySurface, (0,0))
                screen.blit(animations[frame], (50,300))
                i.displayCact(380,0)
                text=font.render("GAME OVER",True,(0,0,0))
                text1=font.render("Score: " + str(int(points)), True, (0,0,0))
                textRect=text.get_rect()
                textRect.center=(500,250)
                textRect1=text1.get_rect()
                textRect1.center=(500,300)
                screen.blit(text, textRect)
                screen.blit(text1, textRect1)
                clock.tick(0)
                pygame.mixer.pause()
        score()
        clock.tick(60)
        pygame.display.update()
