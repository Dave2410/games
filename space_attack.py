# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 22:58:04 2019

@author: DSE063
"""

import pygame
import random
import math

#Initialize pygame
pygame.init()

#Creating the screen
screen = pygame.display.set_mode((800,600))

#Background
background = pygame.image.load('background_space.jpg')

#Title
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('colorspaceship.jpg')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0  
playerY_change = 0

#Enemy
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
enemy_status=[]
num_of_enemies=6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(2)
    enemyY_change.append(30)
    enemy_status.append('Alive')

#Enemy2
enemy2Img=pygame.image.load('alien.png')
enemy2X=random.randint(-50,0)
enemy2Y=random.randint(20,50)
enemy2X_change=3
enemy2Y_change=0
enemy2_status="Alive"
enemy2_death_count=0

#BossEnemy
bossImg=pygame.image.load('science-fiction.png')
bossX=random.randint(-200,-100)
bossY=random.randint(20,30)
bossX_change=3
bossY_change=0

#Bullet
#Ready - Cannot see the bullet
#Fire - Bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = playerY
bulletX_change = 0
bulletY_change = 15
bullet_state="ready"

#BulletEnemy
bullet2Img = pygame.image.load('001-bomb.png')
bullet2X = enemy2X
bullet2Y = enemy2Y
bullet2X_change = 0
bullet2Y_change = 10
bullet2_state="ready"


#BulletBossEnemy
bulletBossImg = []
bulletBossX = []
bulletBossY = []
bulletBossX_change = []
bulletBossY_change = []
bulletBoss_state = []
num_of_bombs=5
hit=0

for i in range(num_of_bombs):
    bulletBossImg.append(pygame.image.load('001-bomb.png'))
    bulletBossX.append(bossX)
    bulletBossY.append(bossY)
    bulletBossX_change.append(0)
    bulletBossY_change.append(4)
    bulletBoss_state.append("ready")


#Explosion
explosionImg = pygame.image.load('flame.png')
explosionX=enemyX
explosionY=enemyY

#Player Explosion
p_explosionImg = pygame.image.load('planet.png')
explosionX=playerX
explosionY=playerY

#BOSS Explosion
boss_explosionImg = pygame.image.load('burst.png')
explosionX=bossX
explosionY=bossY

#Score
score_val = 0
font = pygame.font.Font('freesansbold.ttf',32)
testX=10
testY=10
last_score=0

#Level
level_val=1
font = pygame.font.Font('freesansbold.ttf',32)
levelX=350
levelY=10

#Cup
cupImg = pygame.image.load('cup.png')
cupX=130
cupY=270

#Game Over
over_font = pygame.font.Font('freesansbold.ttf',96)

def show_score(x,y):
    score = font.render("Score : "+str(score_val),True,(255,255,255))
    screen.blit(score,(x,y))
    
def show_level(x,y):
    level = font.render("Level : "+str(level_val),True,(255,255,255))
    screen.blit(level,(x,y))
    
def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))  
    
def enemy2(x,y):
    screen.blit(enemy2Img,(x,y))  
    
def boss(x,y):
    screen.blit(bossImg,(x,y)) 
    
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))
    
def fire_enemybullet(x,y):
    global bullet2_state
    bullet2_state="fire"
    screen.blit(bullet2Img,(x+16,y+10))
    
def fire_enemybulletboss(x,y,i):
    global bulletBoss_state
    bulletBoss_state="fire"
    if i==0:
        screen.blit(bulletBossImg[i],(x+112,y+220))
    elif i==1:
        screen.blit(bulletBossImg[i],(x,y+220))
    elif i==2:
        screen.blit(bulletBossImg[i],(x+220,y+220))
    elif i==3:
        screen.blit(bulletBossImg[i],(x-112,y+220))
    elif i==4:
        screen.blit(bulletBossImg[i],(x+332,y+220))
        
def is_collision(bulletX,bulletY,enemyX,enemyY):
    distance = math.sqrt((math.pow((bulletX-enemyX),2))+(math.pow((bulletY-enemyY),2)))
    if distance < 27:
        return True
    else:
        False



def boss_collision(bulletX,bulletY,bossX,bossY):
    distance = math.sqrt((math.pow((bulletX-(bossX+112)),2))+(math.pow((bulletY-(bossY+200)),2)))
    if distance < 96:
        return True
    else:
        False

def is_pl_collision(playerX,playerY,bulletBossX,bulletBossY):
    #distance = math.sqrt((math.pow((bulletX-enemyX),2))+(math.pow((bulletY-enemyY),2)))
    distance1 = math.sqrt(math.pow(playerY-(bulletBossY+220),2) + math.pow(playerX-(bulletBossX+112),2))
    distance2 = math.sqrt(math.pow(playerY-(bulletBossY+220),2) + math.pow(playerX-bulletBossX,2))
    distance3 = math.sqrt(math.pow(playerY-(bulletBossY+220),2) + math.pow(playerX-(bulletBossX+220),2))
    distance4 = math.sqrt(math.pow(playerY-(bulletBossY+220),2) + math.pow(playerX-(bulletBossX-112),2))
    distance5 = math.sqrt(math.pow(playerY-(bulletBossY+220),2) + math.pow(playerX-(bulletBossX+332),2))
    
    if distance1 < 20 or distance2 < 20 or distance3 < 20:
        return True
    else:
        False

def explosion(x,y):
    screen.blit(explosionImg,(x,y))
    
def explosion_player(x,y):
    screen.blit(p_explosionImg,(x,y))
    
def explosion_boss(x,y):
    screen.blit(boss_explosionImg,(x,y))
    
def is_gameover(playerX,playerY,enemyX,enemyY):
    distance = math.sqrt((math.pow((playerX-enemyX),2))+(math.pow((playerY-enemyY),2)))
    if distance < 35:
        return True
    else:
        False
        
def game_over():
    game_over = over_font.render("Game Over",True,(255,255,255))
    screen.blit(game_over,(150,250))
    show_score(testX,testY)

def game_won():
    game_won = over_font.render("You Win",True,(255,255,255))
    screen.blit(game_won,(200,250))
    show_score(testX,testY)

def cup():
    screen.blit(cupImg,(cupX,cupY))

#Loop
running = True
game_play=True
flag1=1
flag2=1
hit=0

while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
                pygame.display.quit()
    while game_play:
        screen.fill((0,0,0))
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
                pygame.display.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change =-7
                    #print("Left Arrow is pressed")
                if event.key == pygame.K_RIGHT:
                    playerX_change =+7
                if event.key == pygame.K_UP:
                    playerY_change =-10
                if event.key == pygame.K_DOWN:
                    playerY_change =+10
                    
                if event.key == pygame.K_SPACE:
                    if bullet_state=="ready":
                        bulletX = playerX
                        fire_bullet(playerX,bulletY)                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    #print("Key has been released")
                    playerX_change =0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playerY_change =0
        
        #Player Movement
        playerX +=playerX_change   
        if playerX <=0:
            playerX=0
        elif playerX>=736:
            playerX=736
            
        playerY +=playerY_change 
        if playerY <=350:
            playerY=350
        elif playerY>=536:
            playerY=536            
        
        if score_val>=10:
            level_val=math.ceil(score_val/10)    
        
        
    	#EnemyFirehit
        
        bullet_hit = is_collision(bullet2X,bullet2Y,playerX,playerY)

        if not(bullet_hit):

            #Enemy Movement
            for i in range(num_of_enemies):            
                #Gameover
                if enemy_status[i]!="Dead" :
                    if playerY-enemyY[i] <= 30 and playerX-enemyX[i] <=30:
                        explosion_player(playerX,playerY)
                        print("Too close")
                        for j in range(num_of_enemies):
                            enemyY[j]=2000
                            playerY=2000
                        game_over()
                        game_play=False
                        break
                
                #Enemy Movement
                
                enemyX[i] +=enemyX_change[i]
                
                if enemyX[i] <=0:
                    enemyX_change[i]= 2
                    enemyY[i] +=enemyY_change[i] 
                    
                elif enemyX[i]>=736:
                    enemyX_change[i]= -2
                    enemyY[i] +=enemyY_change[i] 
                    

        
                #Collision
                collision = is_collision(bulletX,bulletY,enemyX[i],enemyY[i])
                if enemy_status[i]!="Dead" :
                    if collision:
                        explosion(enemyX[i],enemyY[i])
                        bullet_state="ready"
                        bulletX=playerX
                        bulletY = playerY
                        score_val +=1
                        #print(score_val)
                        enemyX[i] = random.randint(0,736)
                        enemyY[i] = random.randint(50,150)
                        if score_val>20:
                            enemy_status[i]="Dead"


                #Spawn enemy
                if enemy_status[i]!="Dead" :
                    enemy(enemyX[i],enemyY[i],i)    
                          
            #Spawn enemy2
            if score_val>=10 and enemy2_status!="Dead":
                enemy2(enemy2X,enemy2Y)
                
            #Enemy2 Movement
            enemy2X +=enemy2X_change
            
            if enemy2X <=0:
                enemy2X_change = 3
                enemy2Y +=enemy2Y_change
            elif enemy2X>=736:
                enemy2X_change= -3
                enemy2Y +=enemy2Y_change  
                
            #Bullet Movement    
            if bullet_state=="fire":
                fire_bullet(bulletX,bulletY)
                bulletY -= bulletY_change
            if bulletY<=0:
                bullet_state="ready"
                bulletY = playerY
                
                
            #Collision with Enemy2
            collision = is_collision(bulletX,bulletY,enemy2X,enemy2Y)
            if collision:
                explosion(enemy2X,enemy2Y)
                bullet_state="ready"
                bulletX=playerX
                bulletY = playerY
                score_val +=5
                #print(score_val)
                enemy2X = random.randint(0,736)
                enemy2Y = random.randint(50,150)
                if score_val>20:
                    enemy2_status="Dead"
                    bullet2_state=""

            #Bullet enemy
            if score_val>=10 and enemy2_status!="Dead":
                if bullet2_state=="ready":
                    bullet2X=enemy2X
                    fire_enemybullet(enemy2X,bullet2Y)
                            
            #EnemyBullet Movement    
            if bullet2_state=="fire" and enemy2_status!="Dead":
                fire_enemybullet(bullet2X,bullet2Y)
                bullet2Y += bullet2Y_change
            if bullet2Y>=600 and enemy2_status!="Dead":
                bullet2_state="ready"
                bullet2Y = enemy2Y

     
            player(playerX,playerY) 
            
            show_score(testX,testY)    
            
            show_level(levelX,levelY)
                        
            #print(enemy2_status)
            if enemy2_status == "Alive":
                flag2=0
            else:
                flag2=1
            flag1=0
            
            for i in range(num_of_enemies):
                if score_val>20:
                    if enemy_status[i]=="Alive":
                        flag1=0
                    else:
                        flag1+=1
            total = flag1 + flag2
            if total == num_of_enemies+1:
                
    			#Spawn boss
                boss(bossX,bossY)
    			
    			#BossEnemy Movement
                bossX +=bossX_change
                if bossX <=0:
                    bossX_change= 2
                    bossY +=bossY_change
                elif bossX>=544:
                    bossX_change= -2
                    bossY +=bossY_change
    				
    			#Collision with Boss
                collision = boss_collision(bulletX,bulletY,bossX,bossY)
                if collision:
                    hit+=1
                    #print(hit)
                    explosion(bulletX,bulletY-112)
                    bullet_state="ready"
                    bulletX=playerX
                    bulletY=playerY
                    if hit>=10:
                        explosion_boss(bossX,bossY)
                        game_won()
                        cup()
                        game_play=False                
        			
    								
    			#BossEnemy Bullet Movement
                for i in range(num_of_bombs):
                    collision_p = is_pl_collision(playerX,playerY,bulletBossX[i],bulletBossY[i])
                    if collision_p:
                        explosion_player(playerX,playerY)
                        playerX=999
                        #print("Got hit Boss")
                        game_over()
                        game_play=False 
                    else:
                        if bulletBossY[i]>=0 and bulletBossY[i]<600 and bossX>=0:
                            fire_enemybulletboss(bulletBossX[i],bulletBossY[i],i)
                            #print("Bullet Fired")
                            print(i)
                            bulletBossY[i] += bulletBossY_change[i]                       
                        elif bulletBossY[i]>=600:
                            bulletBossY[i]=bossY
                            bulletBossX[i]=bossX

                
        else:
            explosion_player(playerX,playerY)
            #print("Got hit enemy2")
            game_over()
            game_play=False
        
        pygame.display.update()      