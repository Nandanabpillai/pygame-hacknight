import pygame, random

pygame.init()

width, height = 1100, 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

w, h = 100, 200
skySurface = pygame.image.load('sky/1.jpg').convert_alpha()
skySurface = pygame.transform.scale(skySurface,((1100,500)))
grSurface = pygame.image.load('sky/gr.png').convert_alpha()
grSurface = pygame.transform.scale(grSurface,((1100,200)))
spriteRun = pygame.image.load('dino/dsprite.png').convert_alpha()
jumpan = pygame.image.load('dino/d1.png').convert_alpha()
jumpan = pygame.transform.scale(jumpan,((300,217)))
spriteCact = pygame.image.load('dino/csprite.png').convert_alpha()

def get_image(sheet, frame, width, height):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
    image.set_colorkey((0,0,0))
    return image  

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

grPos = 0
cactPos0 = 1020
cactPos1 = 1020
cactPos2 = 1020
cactPos3 = 1020
cactPos4 = 1020
cactPos5 = 1020
animations = []
cactus = []
lastUpdate = pygame.time.get_ticks()
lastUpdateCact = pygame.time.get_ticks()
animationTime = 1000
frame = 0
frameCact = 0
jumpCount = 10
isJump = False
x = 50
y = 200
points=0
font=pygame.font.SysFont('Helvetica',30)
collision = 0

for i in range(4):
    animations.append(get_image(spriteRun, i, 300, 217))

cactus.append(get_image(spriteCact,0,81,124))
cactus.append(get_image(spriteCact,1.1,75,160))
cactus.append(get_image(spriteCact,2.2,74,155))
cactus.append(get_image(spriteCact,3.1,78,130))
cactus.append(get_image(spriteCact,3.5,92,149))
cactus.append(get_image(spriteCact,4.5,90,138))
        
cactRect=[0,0,0,0,0,0]         
run = True
while run:
    pygame.mixer.init()
    soundobj=pygame.mixer.Sound('audio.wav')
    soundobj.play()
    for event in pygame.event.get():
        if event .type == pygame.QUIT:
            run = False
    if collision == 0:

        keys = pygame.key.get_pressed()
    
        screen.blit(grSurface, (grPos,400))
        grPos -= 10
    
        if grPos < -100:
            grPos = 0
        screen.blit(skySurface, (0,0))

        currentTimeCact = pygame.time.get_ticks()
        if currentTimeCact - lastUpdateCact >= animationTime:
            frameCact = random.randint(0,5)
            lastUpdateCact = currentTimeCact
        if (frameCact == 0):
            screen.blit(cactus[0], (cactPos0,380))
            cactRect[0]=[cactPos0,380,80,124]
            cactPos0 -= 10
        
        if (frameCact == 1):
            screen.blit(cactus[1], (cactPos1,345))
            cactRect[1]=[cactPos1,345,78,160]
            cactPos1 -= 10

        if (frameCact == 2):
            screen.blit(cactus[2], (cactPos2,360))
            cactRect[2]=[cactPos2,360,87,145]
            cactPos2 -= 10
        
        if (frameCact == 3):
            screen.blit(cactus[3], (cactPos3,380))
            cactRect[3]=[cactPos3,380,66,130]
            cactPos3 -= 10
        
        if (frameCact == 4):
            screen.blit(cactus[4], (cactPos4,355))
            cactRect[4]=[cactPos4,355,95,149]
            cactPos4 -= 10
    
        if (frameCact == 5):
            screen.blit(cactus[5], (cactPos5,365))
            cactRect[5]=[cactPos5,365,86,138]
            cactPos5 -= 10
        
        if cactPos0 < -200:
            cactPos0 = 1020
        if cactPos1 < -200:
            cactPos1 = 1020
        if cactPos2 < -200:
            cactPos2 = 1020
        if cactPos3 < -200:
            cactPos3 = 1020
        if cactPos4 < -200:
            cactPos4 = 1020
        if cactPos5 < -200:
            cactPos5 = 1020
        currentTime = pygame.time.get_ticks()
        if currentTime - lastUpdate >= animationTime:
            frame += 1
            lastUpdate = currentTime
            if frame >= len(animations):
                frame = 0
        
        if not (keys[pygame.K_SPACE] or keys[pygame.K_UP]):
            screen.blit(animations[frame], (50,300))
            frameRect=pygame.Rect(50,300,300,217)
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
        score()
        clock.tick(60)
        
        if frameRect.colliderect(cactRect[frameCact]):
            collision = 1
            screen = pygame.display.set_mode((width,height))
            pygame.display.set_caption('Game Over!!!')
            screen.blit(grSurface, (0,400))
            screen.blit(skySurface, (0,0))
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


   
    pygame.display.update()