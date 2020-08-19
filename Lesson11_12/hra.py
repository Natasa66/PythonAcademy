#Pygame
# domovska stranka pygame : https://www.pygame.org
#pip install pygame==2.0.0dev10   python 3.8     inak len pip install pygame v Terminal
import random

import pygame
import math
from pygame.locals import *   #vsetko z pygame.locals - pohyb klaevsou atd

pygame.init()
pygame.mixer.init()

width, height = 1024, 768   # nastavime rozlisenie na 1024x768
screen = pygame.display.set_mode((width,height))  # dve zatvorky, lebo ten prameter je tuple

#vytvorime obrazok - dame mu cestu, kde to ma hladat
background = pygame.image.load("resources/images/snow-bg.jpg")
player = pygame.image.load("resources/images/olaf.png")    # hrac na obrazovke bude Olaf
castle = pygame.image.load("resources/images/castle.png")    # hrad
snowflake = pygame.image.load("resources/images/snowflake.png")
healthbar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")
win = pygame.image.load("resources/images/win.png")
loose = pygame.image.load("resources/images/loose.png")

#nacitam jazveca - styri obrazky spolu tvoria jazveca v pohybe - royfazovany
badger_pictures = [
    pygame.image.load("resources/images/badger.png"),
    pygame.image.load("resources/images/badger2.png"),
    pygame.image.load("resources/images/badger3.png"),
    pygame.image.load("resources/images/badger4.png"),
]# modulo %  >  0 % 4 -> 0   , 1 % 4 -> 1, 2 % 4 -> 2,  3 % 4 -> 3, 4 % 4 -> 0, 5 % 4 -> 1
# jazvecov mam viac, budem si ich ukladat do zoznamu bagders, vzdy ked sa objavi dalsi jazvec,
# alebo jeden zmizmne, alebo sa pohne, aktualizujem si ich pocet a polohu
badgers = []
badger_speed = 7
badger_timer = 100 # kazdych 100 prekresleni obrazovky sa mi objavi novy jazvec
badger_picture = 0     # ktory z tych styroch obrazkov ma vykreslit

# klavesy W S A D  - mteda hore, dole, dolava, doprava
#sluzia na pohyb so strelou
#vytvorime si pole, do ktoreho zapiseme, ktoru klavesu mame stlacenu
keys = [False, False, False, False]
#         W       S      A      D
#---------------------------------------------
player_position = [300,100]  #400,123 / 500, 100
player_speed = 10

#---------------------strely = vlocky----------------------------------
snowflakes = []
snowflakes_speed = 5

#----------------------  trafili Olafa?  - pocitam zivoty  -------------------
running = 1   #ak == 1   hra bezi
health_value = 194
needed_time = 60000     # 60000 - timer -- ak tolko vydrzim, tak som vyhral

#-------------------- hudba a zvuky -------------------
hit = pygame.mixer.Sound ("resources/audio/explode.wav")
#main_music = pygame.mixer.Sound("resources/audio/moonlight.wav")
shoot = pygame.mixer.Sound("resources/audio/shoot.wav")
enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
hit.set_volume(0.05)
shoot.set_volume(0.05)
enemy.set_volume(0.05)
pygame.mixer.music.load("resources/audio/moonlight.wav")
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(0.25)

#---------------------------------------------------------------
#hlavny cyklus - bude nekonecny dovtedy, kym nezatvorime obrazovku
while running:
    badger_timer -=1  #pocitadlo prkresleni obrazovky

    screen.blit(background, (0,0))  # na poziciu 0,0 nakresli moj obrazok - snehova vlocka
    screen.blit(castle, (0,0))  # na poziciu 0,0 nakresli 1.castle   - ten ma velkost 200x200
    screen.blit(castle, (0,205))  # na poziciu 0,205 nakresli 2.castle   - ten ma velkost 200x200
    screen.blit(castle, (0,410))  # na poziciu 0,410 nakresli 3.castle   - ten ma velkost 200x200
    # ---------------- pridame sledovanie mysi  -----------------

    position = pygame.mouse.get_pos()  # x,y
    # SMEROM K MYSI SA MA OLAF POZERAT
    # musim si vypocitat uhol voci y- ovej suradnici - atg 9(rozdiel x-ovych sur, rozdiel y-ovych sur)
    angle = math.atan2(position[1] - (player_position[1]+32), position[0] - (player_position[0]+25))  # radiany
    #                                 y                                         x
    # o tento uhol natocim Olafa -hraca,  +32   a  +25  znamenaju, ze Olafa budem rotovat podla jeho stredu
    # a nie podla jeho laveho horneho rohu
    playerrot = pygame.transform.rotate(player, 360 - angle * 57.29)  # prepocitam na stupne
    player_position_new = (
        player_position[0] - playerrot.get_rect().width/2,
        player_position[1] - playerrot.get_rect().height/2,
    )
    # -----------------------------------------------------------

    #screen.blit(player, player_position)  # na poziciu player_position nakresli olafa - kreslim ho
    screen.blit(playerrot, player_position_new)  # novy obrazok - natoceny podla mysi
        # posledneho, aby v pripade, ze bude na pozicci hradu, bude sa kreslit v popredi

    #-------------------------------------------------------------------------
    if badger_timer == 0:  # teba tam supnut dalsieho jazveca
        badgers.append(([750, random.randint(10, 1000),badger_picture]))   #supnem ho na kraj obrazovky (x) a y je nahodne
        #                 x              y              ktory obrazok
        badger_timer = 100  # a nastavim pocitadlo prekresleneni na startovaciu hodnotu
    #-------------------------------------------------------------------
    # vystrelime sip a zistime, ci netrafil jazveca
    # na strielanie stlacime medzerovnik
    if snowflakes:
        index = 0
        for projectile in snowflakes:
            if projectile[1] > 1024 or projectile[1] < 0 or projectile[2]>768 or projectile[2] < 0:
                snowflakes.pop(index)
            else:
                velx = math.cos(projectile[0]) * snowflakes_speed
                vely = math.sin(projectile[0]) * snowflakes_speed
                projectile[1] += velx
                projectile[2] += vely
                #screen.blit(snowflake, (projectile[1],projectile[2]))
                #projectile[1] =+ snowflakes_speed

                #este zrotujeme hviezdicku
                projectilerot = pygame.transform.rotate(snowflake, 360 - projectile[0]*57.29)  #preocitame na stupne
                screen.blit(projectilerot, (projectile[1], projectile[2]))
            index += 1
        #-------------------------------------------------------------------
    if badgers:      # ak tam nejakeho mame, tak ho/ich ideme vykreslit
        index = 0  # tu mam info, kolkeho jazveca vykreslujem
        for badger in badgers:
            if badger[0] <= 200:  # jazvec je na urovni hradu   - x-ova suranica je menje ako 200
                #badger narazil do hradu -teda pride do ciela- a teda hracov zivot znizime
                health_value -= random.randint(1,9)
                badgers.pop(index)   # tohto jazveca vyhodim zo zoznamu, uz je mimo "bojoveho pola"
            else:
                screen.blit(badger_pictures[badger[2] % 4], (badger[0], badger[1]))  # vsetky ostatne vykreslim
                #           badger_list[0],  (badger[0-3], badger[1]))
                #             obrazok       suradnica x   suradnica y
                badger[2] +=1
                badger[0] -= random.randint(0, badger_speed)    # 0 - 9
            badger_rect = pygame.Rect(badger_pictures[badger[2] % 4].get_rect())
            #badger_rec      obdlznik okolo obrazka
            badger_rect.top = badger[1]
            badger_rect.left = badger[0]   #badegr_rect  ma teraz poziciu jazveca
            index_projectile = 0
            # ideme prejst vsetky strely a checkovat ci sa nezrazili s jazvecovym obdlznikom
            for projectile in snowflakes:
                projectile_rect = pygame.Rect(snowflake.get_rect())  # urobim obdlznik oklo snowflake
                projectile_rect.top = projectile[2]
                projectile_rect.left = projectile[1]
                if badger_rect.colliderect((projectile_rect)):  # zrazili sa tie obdlzniky? - tato funkcia to zisti
                    # musime vymazat jazveca a snowflake
                    enemy.play()
                    hit.play()
                    badgers.pop(index)
                    snowflakes.pop(index_projectile)
                index_projectile += 1

            index =+ 1 #badger_pictures [6]

    #---------------------- healthbar  -------------------------------
    screen.blit(healthbar, (5,5))
    for health1 in range(health_value):
        screen.blit(health,(health1+8,8)) #postupne a bude naplnat healthbar cervenou farbou po jednom obdlznicku sirky 8
    #--------------------------------------------------------------------
    for event in pygame.event.get(): # zachyti hocico spravime - pohyb mysou, klavesa atd.
        if event.type == pygame.QUIT:  # vstupom je nejaky "quit pohyb" - u nas "zavri okno"
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys[0] = False
            elif event.key == K_a:
                keys[1] = False
            elif event.key == K_s:
                keys[2] = False
            elif event.key == K_d:
                keys[3] = False
            elif event.key == K_SPACE:   # hrac stlacil medzerovnik, teda striela
                shoot.play()
                snowflakes.append([0,player_position[0],player_position[1]]) # na pozicii hraca vznikne vlocka - strela
                #               uhol   x - suradniaca      y - suradnica hraca
        if event.type == pygame.MOUSEBUTTONDOWN:  # strielame mysou
            shoot.play()
            position = pygame.mouse.get_pos()
            snowflakes.append([math.atan2(position[1] - player_position_new[1], position[0] - player_position_new[0]),
                                         player_position_new[0],
                                         player_position_new[1]])


    #y - suranice
    if keys[0]:  #  W
        if player_position[1] >= 0:              #1024 x 768       nebude vybiehat z obrazovky
            player_position[1] -= player_speed
    elif keys[2]:  #  S
        if player_position[1] <= 738:     #0 , 0  -  lavy horny roh     nebude vybiehat z obrazovky
            player_position[1] += player_speed

    #tato cast su x-suradnice
    if keys[1]:   # A   - dolava
        if player_position[0] >= 200:
            player_position[0] -= player_speed      # nebude vybiehat z obrazovky
    elif keys[3]:   #  D    - doprava
        if player_position[0] <= 1000:
            player_position[0] += player_speed     # nebude vybiehat z obrazovky

#------------------ vypiseme zostavajuci cas --------------------
    font = pygame.font.Font(None, 24)
    timertext = font.render(
        str(
            (needed_time - pygame.time.get_ticks()) // 60000
        ) + ":" + str(
            (needed_time - pygame.time.get_ticks()) // 1000 % 60
        ).zfill(2), True, (0, 0, 0))   # zfill  - zlava doplna nulami na dve miesta - aby tam boli vzdy dve cislice
    #     co,antialiasing, R  G  B     > mozem si namiesat lubovolnu farbu   255 255 255    60 120 50
    #    text bude v tvare  mim min: sec sec
    text_rectangle = timertext.get_rect()
    text_rectangle.topright = [1000, 5]   # pravy horny roh  sa vykresli na pozicii 1000,5
    screen.blit(timertext, text_rectangle)

#-------------------------------------------------------------------

    if health_value <= 0:
        running = 0   #hra sa skoncila
        winning_condition = 0  # 0 - prehra
    elif needed_time <= pygame.time.get_ticks():   # ticks su v ms ..... neede_time je tiez v ms
        running = 0
        winning_condition = 1
    #prekreslime obrazovku a hore na zaciatku while vykreslime novu poziciu
    pygame.display.flip()  # prekresluje obrazovku  cca 1/2-3msec

if winning_condition == 0:
    screen.blit(loose, (100,100))
else:
    screen.blit(win, (100,100))

while True:
     for event in pygame.event.get(): # vykreslene je ci sme vyhrali alebo prehrali a cakame na zavretie okna
        if event.type == pygame.QUIT:  # vstupom je nejaky "quit pohyb" - u nas "zavri okno"
            pygame.quit()
            exit(0)
     pygame.display.flip()  # prekresluje obrazovku


