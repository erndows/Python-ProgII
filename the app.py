import os
import tkinter
import time
import pygame

pygame.init()

ekrans = pygame.display.set_mode((960, 960))
run = True
x=0
clock = pygame.time.Clock()
kobolds_img = pygame.image. load('mini.PNG').convert_alpha()

kobolds_img = pygame.transform.scale(kobolds_img,
                                     (kobolds_img.get_width()
                                                    ))

while run:
    ekrans.fill((0,0,0))
    ekrans.blit(kobolds_img,(x, 1))
    x += 1
    for notik in pygame.event.get():
        if notik.type == pygame.QUIT:
            run = False
    pygame.display.update()
    clock.tick(60)

pygame.quit()