
import time
import pygame
import random
import pygame_textinput
import pygame.locals
import math

#selenium, psutil, sys, wmi

pygame.init()
text_garums = pygame_textinput.TextInputManager(validator = lambda text: len(text) <= 22)
textinput1 = pygame_textinput.TextInputVisualizer(manager = text_garums)
ekrans = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Brainrot')
run = True
x=50
y=50
clock = pygame.time.Clock()
kobolds_img = pygame.image.load('mini.PNG').convert_alpha()
koboldsshirt_img = pygame.image.load('shirt.PNG').convert_alpha()
koboldsskirt_img = pygame.image.load('skirt.PNG').convert_alpha()
koboldsshirtNskirt_img = pygame.image.load('shirt+skirt.PNG').convert_alpha()
koboldsdrip_img = pygame.image.load('drip.PNG').convert_alpha()
shopIcon_img = pygame.image.load('shop.png').convert_alpha()
dk_img = pygame.image.load('dragonkoin.PNG').convert_alpha()
gold_img = pygame.image.load('gold.png').convert_alpha()
water_img = pygame.image.load('lase.PNG').convert_alpha()
food_img = pygame.image.load('meat.png').convert_alpha()

kobolds_img = pygame.transform.scale(kobolds_img,
                                    (kobolds_img.get_width()*2,
                                    kobolds_img.get_height()*2))
koboldsshirt_img = pygame.transform.scale(koboldsshirt_img,
                                    (koboldsshirt_img.get_width()*2,
                                    koboldsshirt_img.get_height()*2))
koboldsskirt_img = pygame.transform.scale(koboldsskirt_img,
                                    (koboldsskirt_img.get_width()*2,
                                    koboldsskirt_img.get_height()*2))
koboldsshirtNskirt_img = pygame.transform.scale(koboldsshirtNskirt_img,
                                    (koboldsshirtNskirt_img.get_width()*2,
                                    koboldsshirtNskirt_img.get_height()*2))
koboldsdrip_img = pygame.transform.scale(koboldsdrip_img,
                                    (koboldsdrip_img.get_width()*2,
                                    koboldsdrip_img.get_height()*2))
dk_img = pygame.transform.scale(dk_img,
                                    (dk_img.get_width()/1.5,
                                    dk_img.get_height()/1.5))
gold_img = pygame.transform.scale(gold_img,
                                    (gold_img.get_width()/2,
                                    gold_img.get_height()/2))
water_img = pygame.transform.scale(water_img,
                                    (water_img.get_width()/2.5,
                                    water_img.get_height()/2.5))
food_img = pygame.transform.scale(food_img,
                                    (food_img.get_width()/2,
                                    food_img.get_height()/2))
warning_text_font = pygame.font.SysFont("Century Gothic",10,italic=True)
text_font = pygame.font.SysFont("Century Gothic",20 )
text_fontGL = pygame.font.SysFont("Century Gothic",40)

def draw_text(text,font,text_col, textX, textY):
    img = font.render(text, True, text_col)
    ekrans.blit(img, (textX,textY))

def draw_bar(x, y, value, max_value, color):
    width = 350
    height = 20

    fill = (value / max_value) * width

    pygame.draw.rect(ekrans, (0,0,0), (x, y, width, height), 2)
    pygame.draw.rect(ekrans, color, (x, y, fill, height))

def veido_shop():
    shop = []
    visas_preces = [
        (koboldsshirt_img, 100),
        (koboldsskirt_img, 150),
        (koboldsdrip_img, 99999)
    ]
    chosen = random.sample(visas_preces, 3)
    for outfit, cena in chosen:
        shop.append({"img": outfit, "price": cena})
    return shop

TaimerisTxt = "Taimeris"
dkSkaits = 100
fCena = 0
wCena = 0
gCena = 0
refreshCena = 1
food = 100
water = 100
gold_bar = 0
gold_multiplier = 1
gold_pixel = []
player_kobold = [kobolds_img,koboldsshirt_img,koboldsskirt_img,koboldsshirtNskirt_img,koboldsdrip_img]
equip = 0

shop_outfits = veido_shop()

gCenaInt = 0
poga_nospiesta = False
shopPoga_nospiesta = False
timer_active = False
timer_locked = False
timer_end_time = 0
timer_minutes = 0
game_over = False

decay_timer = pygame.time.get_ticks()

pygame.key.set_repeat(400, 25)

while run:
    notikumi = pygame.event.get()
    textinput1.update(notikumi)
    if not game_over:
        #Spēlēs galvenā loga vizualizācija
        tWidth, tHeight = text_font.size(f"{TaimerisTxt}")
        fWidth, fHeight = text_font.size(f"{fCena}")
        wWidth, wHeight = text_font.size(f"{wCena}")
        gWidth, gHeight = text_font.size(f"{gCena}")

        istaba = pygame.Rect(0,0,680,370)
        ekrans.fill((255, 73, 55))
        krasa = (129,0,0)

        pygame.draw.rect(ekrans, krasa,istaba)
        for px, py in gold_pixel:
            ekrans.set_at((px, py), (255, 215, 0))
        pygame.draw.rect(ekrans,(0,0,0),(750,50,350,30) )
        pygame.draw.rect(ekrans,(0,0,0),(750,175,350,30) )
        pygame.draw.rect(ekrans,(0,0,0),(750,300,350,30) )
        pygame.draw.rect(ekrans,(255, 222, 89),(20,610,tWidth+20,tHeight+10) )
        pygame.draw.rect(ekrans,(255, 222, 89),(1150,50,fWidth+20,30) )
        pygame.draw.rect(ekrans,(255, 222, 89),(1150,175,wWidth+20,30) )
        pygame.draw.rect(ekrans,(255, 222, 89),(1150,300,gWidth+20,30) )
        
        draw_text(f"{TaimerisTxt}", text_font,(0,0,0), 30,610)
        draw_text("Ēdiens", text_font,(0,0,0), 790, 20)
        draw_text("Ūdens", text_font,(0,0,0), 780, 145)
        draw_text("Zelts", text_font,(0,0,0), 780, 270)
        draw_text(f"{dkSkaits}", text_fontGL,(0,0,0), 70, 380)
        draw_text(f"{fCena}", text_font,(0,0,0), 1160, 50)
        draw_text(f"{wCena}", text_font,(0,0,0), 1160, 175)
        draw_text(f"{gCena}", text_font,(0,0,0), 1160, 300)
        draw_text("(Izmanto taimerim hh:mm formātu)", warning_text_font,(0,0,0), 560, 700)

        draw_bar(750, 50, food, 100, (0,255,0))
        draw_bar(750, 175, water, 100, (0,0,255))
        draw_bar(750, 300, gold_bar, 100, (255,215,0))

        ekrans.blit(player_kobold[equip], (x, y))
        ekrans.blit(shopIcon_img,(1160,600))
        ekrans.blit(gold_img,(740,260))
        ekrans.blit(dk_img,(0,370))
        ekrans.blit(water_img,(740,130))
        ekrans.blit(food_img,(745,10))

        mouse = pygame.mouse.get_pos()
    
        
        #Healthbar sistēma
        if pygame.time.get_ticks() - decay_timer >3500:
            decay_timer = pygame.time.get_ticks()

            food -= 0.5
            water -= 1  
        #Timer apdāvināšanas sistēma
        if timer_active:
            remaining = timer_end_time - time.time()
            if remaining <= 0:
                # reward formula: x ^1.78 (x - minūšu daudzums)
                reward = int(timer_minutes ** 1.78 * gold_multiplier)
                dkSkaits += reward

                print(f"{reward} DK")
                timer_active = False
                timer_locked = False
            else:
                mins_left = int(remaining // 60)
                secs_left = int(remaining % 60)

                draw_text(f"{mins_left:02}:{secs_left:02}", text_font, (0,0,0), 30, 650)
        
        #Kustību sistēma
        if x < 560 and x > 0:
            x += random.randint(-10,11)
        else:
            x = 0
            x += random.randint(1,100)
        if y < 260 and y > 0:
            y += random.randint(-5,6)
        else:
            y=0
            y += random.randint(1,100)

        #Onscreen pogu interaktivitāte
        
        for notik in notikumi:
            if notik.type == pygame.WINDOWFOCUSLOST:
                game_over = True
            if food <= 0 or water <= 0:
                    game_over = True
            if notik.type == pygame.QUIT:
                run = False
            if notik.type == pygame.MOUSEBUTTONDOWN:
                if 1150 <= mouse[0] <= fWidth+1170 and 50 <= mouse[1] <= 80 and dkSkaits >= fCena:
                    dkSkaits -= fCena
                    fCena +=1
                    food += math.log(101 - food + 1) * 5
                    food = min(food, 100)
                if 1150 <= mouse[0] <= wWidth+1170 and 175 <= mouse[1] <= 205 and dkSkaits >= wCena:
                    dkSkaits -= wCena
                    wCena +=1
                    water += math.log(101 - water + 1) * 5
                    water = min(water, 100)
                if 1150 <= mouse[0] <= gWidth+1170 and 300 <= mouse[1] <= 330 and dkSkaits >= gCena:
                    dkSkaits -= gCena
                    gCenaInt +=1
                    gCena = gCenaInt **2
                    gold_bar += 1
                    gold_multiplier += 1

                    px = random.randint(0, 679)
                    py = random.randint(0, 369)
                    while True:
                        if (px, py) in gold_pixel:
                            break
                        else:
                            px = random.randint(0, 679)
                            py = random.randint(0, 369)
                            gold_pixel.append((px, py))
                if 1160 <= mouse[0] <= 1160+shopIcon_img.get_width() and 600 <= mouse[1] <= 600+shopIcon_img.get_height():
                     shopPoga_nospiesta = True
                if 20 <= mouse[0] <= tWidth+40 and 610 <= mouse[1] <= tHeight+620 and not timer_locked:
                    poga_nospiesta = True      
        if shopPoga_nospiesta == True:
            
            refreshCenaX, refreshCenaY = text_font.size(f"{refreshCena} DK")
            for notik in notikumi:
                if notik.type == pygame.MOUSEBUTTONDOWN:
                    if 590 <= mouse[0] <= 640+refreshCenaX and 540 <= mouse[1] <= 550+refreshCenaY:
                        shop_outfits = veido_shop()
                        refreshCena = math.ceil(refreshCena * 1.5)
                    

            pygame.draw.rect(ekrans, (255,255,255), (340,160,600,450))
            draw_text("Veikals", text_fontGL, (0,0,0), 565, 170)
            pygame.draw.rect(ekrans, (0,50,0), (590,540,50+refreshCenaX,10+refreshCenaY))
            draw_text(f"{refreshCena} DK", text_font, (255,255,255), 615, 540)
            draw_text("X", text_font, (0,0,0), 920, 160)

            for i, item in enumerate(shop_outfits):
                outfit = item["img"]
                cena = item["price"]

                ekrans.blit(outfit, (385 + i * 200, 300))

                cenu_textX, cenu_textY = text_font.size(f"{cena} DK")
                pygame.draw.rect(ekrans, (0,128,0), (385 + i * 200 - 10, 400, cenu_textX+20, cenu_textY), 2)

                draw_text(f"{cena} DK", text_font, (0,0,0), 385 + i * 200, 400)
                if notik.type == pygame.MOUSEBUTTONDOWN:
                    if 385 + i * 200 - 10 <= mouse[0] <= 385 + i * 200 - 10 + cenu_textX + 20 and 400 <= mouse[1] <= 400 + cenu_textY:
                        if dkSkaits >= cena:
                            dkSkaits -= cena
                            equip = player_kobold.index(outfit)
                            shopPoga_nospiesta = False
                        else:
                            print("Nav pietiekami DK")
                            shopPoga_nospiesta = False
            if notik.type == pygame.MOUSEBUTTONDOWN:
                if 920 <= mouse[0] <= 940 and 160 <= mouse[1] <= 188:
                    shopPoga_nospiesta = False
            
                

        #Timer loga parādīšana
        if poga_nospiesta == True:
            pygame.draw.rect(ekrans, (255,255,255), (440,260,450,300))
            pygame.draw.rect(ekrans, (129,0,0), (625,520,80,30))
            ekrans.blit(textinput1.surface, (490, 360))
            draw_text("Atcelt", text_font, (0,0,0),635,520 )
            
            #Atcelt pogas funkcionalitāte
            if notik.type == pygame.MOUSEBUTTONDOWN and 625<=mouse[0]<=705 and 520<=mouse[1]<=550:
                poga_nospiesta = False
                istaba = pygame.Rect(0,0,680,370)
                ekrans.fill((255, 73, 55))
                krasa = (129,0,0)
                print(f"{textinput1.value}")
                #Timer apstiprināšanas sistēma
                try:
                    pulkst = textinput1.value.split(":")
                    if len(pulkst) != 2:
                        raise ValueError("Nepareizs formāts")
                    hours = int(pulkst[0])
                    minutes = int(pulkst[1])
                    if hours < 0 or minutes < 0 or minutes >= 60:
                        raise ValueError("Nepareizs laiks")
                    elif hours == 0 and minutes == 0:
                        raise ValueError("Laiks nevar būt 00:00")
                    elif hours > 99:
                        raise ValueError("Nevar vairāk par 99 stundām")
                    if not timer_locked:
                        timer_minutes = hours * 60 + minutes
                        timer_end_time = time.time() + timer_minutes * 60
                        timer_active = True
                        timer_locked = True
                    poga_nospiesta = False
                except ValueError as e:
                    print(f"Kļūda: {e}")
                    textinput1.value = ""
                
                #Main spēles loga uzlikšana
                pygame.draw.rect(ekrans, krasa,istaba)
                pygame.draw.rect(ekrans,(0,0,0),(750,50,350,30) )
                pygame.draw.rect(ekrans,(0,0,0),(750,175,350,30) )
                pygame.draw.rect(ekrans,(0,0,0),(750,300,350,30) )
                pygame.draw.rect(ekrans,(255, 222, 89),(20,610,tWidth+20,tHeight+10) )
                pygame.draw.rect(ekrans,(255, 222, 89),(1150,50,fWidth+20,30) )
                pygame.draw.rect(ekrans,(255, 222, 89),(1150,175,wWidth+20,30) )
                pygame.draw.rect(ekrans,(255, 222, 89),(1150,300,gWidth+20,30) )

                draw_text(f"{TaimerisTxt}", text_font,(0,0,0), 30,610)
                draw_text("Ēdiens", text_font,(0,0,0), 790, 20)
                draw_text("Ūdens", text_font,(0,0,0), 780, 145)
                draw_text("Zelts", text_font,(0,0,0), 780, 270)
                draw_text(f"{dkSkaits}", text_fontGL,(0,0,0), 70, 380)
                draw_text(f"{fCena}", text_font,(0,0,0), 1160, 50)
                draw_text(f"{wCena}", text_font,(0,0,0), 1160, 175)
                draw_text(f"{gCena}", text_font,(0,0,0), 1160, 300)

                ekrans.blit(player_kobold[equip], (x, y))
                ekrans.blit(shopIcon_img,(1160,600))
                ekrans.blit(gold_img,(740,260))
                ekrans.blit(dk_img,(0,370))
                ekrans.blit(water_img,(740,130))
                ekrans.blit(food_img,(745,10))
    
    if game_over:
        ekrans.fill((0,0,0))

        draw_text("YOU LOST", text_fontGL,(255,0,0),500,300)

        pygame.draw.rect(ekrans,(255,255,255),(540,400,200,50))
        draw_text("Try Again", text_font,(0,0,0),580,415)

        mouse = pygame.mouse.get_pos()

        for notik in notikumi:
            if notik.type == pygame.QUIT:
                run = False
            if notik.type == pygame.MOUSEBUTTONDOWN:
                if 540 <= mouse[0] <= 740 and 400 <= mouse[1] <= 450:
                    TaimerisTxt = "Taimeris"
                    dkSkaits = 100
                    fCena = 0
                    wCena = 0
                    gCena = 0
                    food = 100
                    water = 100
                    gold_bar = 0
                    gold_pixels = []

                    gCenaInt = 0
                    poga_nospiesta = False
                    timer_active = False
                    timer_locked = False
                    timer_end_time = 0
                    timer_minutes = 0
                    game_over = False
            
    pygame.display.update()
    clock.tick(30)
    continue

pygame.quit()