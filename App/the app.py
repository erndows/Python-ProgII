import os
import time
import pygame
import random
import thorpy

pygame.init()

ekrans = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Brainrot')
run = True
x=50
y=50
clock = pygame.time.Clock()
kobolds_img = pygame.image.load('mini.PNG').convert_alpha()
shopIcon_img = pygame.image.load('shop.png').convert_alpha()

kobolds_img = pygame.transform.scale(kobolds_img,
                                    (kobolds_img.get_width()*2,
                                    kobolds_img.get_height()*2))




def kustiba(run,x,y):
    while run:
        istaba = pygame.Rect(0,0,680,370)
        ekrans.fill((255, 73, 55))
        krasa = (129,0,0)
        pygame.draw.rect(ekrans, krasa,istaba)
        ekrans.blit(kobolds_img,(x, y))
        ekrans.blit(shopIcon_img,(1160,600))
        pygame.display.update()
        clock.tick(120)
        if x < 560 and x > 0:
            x += random.randint(-10,11)
            time.sleep(0.05)
        else:
            x = 0
            x += random.randint(1,100)
            time.sleep(0.05)
        if y < 260 and y > 0:
            y += random.randint(-5,6)
            time.sleep(0.05)
        else:
            y=0
            y += random.randint(1,100)
            time.sleep(0.05)
        for notik in pygame.event.get():
            if notik.type == pygame.QUIT:
                run = False
kustiba(run,x,y)




pygame.quit()