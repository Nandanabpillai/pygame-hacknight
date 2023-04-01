 import pygame, sys

pygame.init()

width, height = 1100, 500
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

w, h = 100, 200
skySurface = pygame.image.load('sky/1.jpg').convert_alpha()
skySurface = pygame.transform.scale(skySurface,((1100,400)))
grSurface = pygame.image.load('sky/gr.png').convert_alpha()
grSurface = pygame.transform.scale(grSurface,((1100,200)))
spriteRun = pygame.image.load('dino/dsprite.png').convert_alpha()

def get_image(sheet, frame, width, height):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
    image.set_colorkey((0,0,0))
    return image  

animations = []
animationSteps = 4
lastUpdate = pygame.time.get_ticks()
animationTime = 150
frame = 0

for i in range(animationSteps):
    animations.append(get_image(spriteRun, i, 300, 217))
    
run = True
while run:
    for event in pygame.event.get():
        if event .type == pygame.QUIT:
            run = False

    screen.blit(grSurface, (0,300))
    screen.blit(skySurface, (0,0))

    currentTime = pygame.time.get_ticks()
    if currentTime - lastUpdate >= animationTime:
        frame += 1
        lastUpdate = currentTime
        if frame >= len(animations):
            frame = 0
    screen.blit(animations[frame], (50,200))
    
    pygame.display.update()
    clock.tick(60) #maximum frame rate
