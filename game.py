import sys, pygame
from pygame.locals import*
import random

#USABLE VARIABLES

#screen size
size=width,height=(1200,800)

#road
road_w=int (width/1.6)

#roadmark
roadmark_w=int(width/80)

#lanes
right_lane=width/2 + road_w/4
left_lane=width/2 - road_w/4

#enemy speed
speed=1

#GAME INITIALIZATION
pygame.init()


#screen size
screen =pygame.display.set_mode(size)

#windows title
pygame.display.set_caption("Awesome Car Game")

#screen background
screen.fill((41, 182, 246))



#screen update
pygame.display.update()

#load player car
car = pygame.image.load("car.png")
car_loc=car.get_rect()
car_loc.center=right_lane, height*0.8

#load enemy car
enemy = pygame.image.load("enemy.png")
enemy_loc = enemy.get_rect()
enemy_loc.center=left_lane, height*0.2

counter = 0
running=True

#GAME LOOP
while running:
    counter += 1
    
    #increase speed levels
    if counter == 5000:
        speed += 0.15
        counter = 0
        print("LEVEL UP", speed)

    #enemy appear continuously and randomly
    enemy_loc[1] += speed
    if enemy_loc[1] > height:
        if random.randint(0,1,) == 0:
            enemy_loc.center = right_lane, -200
        else:
            enemy_loc.center = left_lane, -200

    #GAME END
    if car_loc[0] == enemy_loc[0] and enemy_loc[1]>car_loc[1] - 128:
        print ("GAME OVER")
        break
    
    #event listeners
    for event in pygame.event.get():
        if event.type==QUIT:
            running=False

        #GAME CONTROLS    
        if event.type ==KEYDOWN:
            
            #move left
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2),0])
            
            #move right
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w/2),0])

    #SCREEN ELEMENTS
    
    #road color
    pygame.draw.rect(
        screen,
        (50,50,50),
        (width/2 - road_w/2, 0, road_w, height)
    )
    
    #yellow mark
    pygame.draw.rect(
        screen,
        (255,240,60),
        (width/2 - roadmark_w/2 , 0, roadmark_w, height)
    )

    #white lane left
    pygame.draw.rect(
        screen,
        (255,255,255),
        (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height)
    )

    #wight lane right
    pygame.draw.rect(
        screen,
        (255,255,255),
        (width/2 + road_w/2 - roadmark_w*3 , 0, roadmark_w, height)
    )    
    
    
    screen.blit(car,car_loc)
    screen.blit(enemy,enemy_loc)
    
    #cars udpate
    pygame.display.update()

pygame.quit()