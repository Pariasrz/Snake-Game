# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 13:28:40 2018

@author: PS
"""

import pygame
import random
import sys


#colors
BLACK = (18 , 18 , 18)
GREEN = (0 , 180 , 0)
RED = (255 , 0 , 0)
YELLOW = (127 , 255 , 0)
WHITE = (229 , 229 , 229)
GRAY = (255, 97 , 3)

#font
pygame.font.init()
font1 = pygame.font.SysFont('Lucida Console', 26)
font2 = pygame.font.SysFont('Lucida Console', 10)


pygame.init()

longer = False
gameover = False
score = 0
count = 0
 
#size of each cell
cell_width = 15
cell_height = 15

#snake body
snake_cells = []
 
#page
screen = pygame.display.set_mode([600, 600])
pygame.display.set_caption('SNAKEE')

#img2 = pygame.image.load("song.mp3")
#pygame.mixer.music.load("song.mp3")
#pygame.mixer.music.play(-1)
# initiating x , y
x = 200
y = 200

#importing files

#leaf
img1 = pygame.image.load("leaf.png")
img1 = pygame.transform.scale(img1, (25,25))
leaf = img1.get_rect()
leaf.x = random.randint(75, 580)
leaf.y =  random.randint(75, 580)

#apple
img2 = pygame.image.load("Apple.png")
img2 = pygame.transform.scale(img2, (25,25))
apple = img2.get_rect()
apple.x = random.randint(75, 580)
apple.y =  random.randint(75, 580)

#poisen
img3 = pygame.image.load("poison.png")
img3 = pygame.transform.scale(img3, (30,30))
poison = img3.get_rect()
poison.x = random.randint(75, 580)
poison.y =  random.randint(75, 580)

#heart
heart = pygame.image.load("heart.png")
heart = pygame.transform.scale(heart, (27,27))


#icons
icon = pygame.image.load("green-snake.png")
icon = pygame.transform.scale(icon, (80,50))

#RIP
img4 = pygame.image.load("grave.png")
img4 = pygame.transform.scale(img4, (80,80))

sound = pygame.mixer.Sound('crunching.wav')

#sound
def crunch():
    pygame.mixer.Sound.play(sound)
    pygame.mixer.music.stop()

x_step = 0
y_step = -1 * cell_height
       
#snake lenght
for i in range(10):
    snake_cells.append([x, y])
    y = y + cell_height

clock = pygame.time.Clock()
running = True
#main loop
while running:
    screen.fill(BLACK) 
    
#hearts
    screen.blit(icon , (510 ,10))
    screen.blit(heart , (470 ,30))
    screen.blit(heart , (440 ,30))
    screen.blit(heart , (410 ,30))
    #line
    pygame.draw.lines(screen, (0, 255, 0), False,  [(0, 75), (600, 75)], 1)
    
#keyboard
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_step = -1 * cell_width
                y_step = 0
            if event.key == pygame.K_RIGHT:
                x_step = cell_width
                y_step = 0
            if event.key == pygame.K_UP:
                x_step = 0
                y_step = -1 * cell_height
            if event.key == pygame.K_DOWN:
                x_step = 0
                y_step = cell_height
            if event.key == pygame.K_ESCAPE:
                pygame.display.quit()
                running = False


    #Delete the last cell
    if longer == False:
        snake_cells.pop()
        
        
   #new X and Y
    x = snake_cells[0][0] + x_step
    y = snake_cells[0][1] + y_step
    
    #adding new cells
    snake_cells.insert(0, [x, y])
                        
 #snake's head
    head_x = snake_cells[0][0]
    head_y = snake_cells[0][1]

    for i in range( len(snake_cells) ):
        if i > 0:
            body_x = snake_cells[i][0]
            body_y = snake_cells[i][1]

	    #snake colliding itself or margins
            if ( body_x == head_x and body_y == head_y ):
                gameover = True
                
            if ( head_x > 600 or head_x < 0): 
                gameover = True 
            if ( head_y > 600 or head_y < 65):
                gameover = True
 #level1        
    if score < 6 :
       text = font1.render('Level 1', True, RED)
       screen.blit(text, (10, 40))
       clock.tick(5)

       #food type 1
       screen.blit(img1,leaf)
       food = leaf
       
       for i in range( len(snake_cells) ):
           if gameover == False:
               snake = pygame.draw.rect(screen, GREEN, [snake_cells[i][0], snake_cells[i][1], cell_width, cell_height], 0)
               
               if i == 0:
                   if snake.colliderect(food):
                       longer = True
                       pygame.mixer.music.pause()
                       crunch()
                       pygame.mixer.music.unpause()
                       
                       leaf.x = random.randint(75, 580)
                       leaf.y = random.randint(75, 580)
                       score = score + 1
                    
                   else:
                       longer = False
    #level2
    if score > 5 and score < 17 :
       text = font1.render('Level 2 !', True, RED)
       screen.blit(text, (10, 40)) 
       clock.tick(10)


       #food type 2
       screen.blit(img2,apple)
       food = apple
       
       for i in range( len(snake_cells) ):
        if gameover == False:

            snake = pygame.draw.rect(screen, GREEN, [snake_cells[i][0], snake_cells[i][1], cell_width, cell_height], 0)
            if i == 0:
                if snake.colliderect(food):
                    longer = True
                    pygame.mixer.music.pause()
                    crunch()
                    pygame.mixer.music.unpause()
                    
                    apple.x = random.randint(75, 580)
                    apple.y = random.randint(75, 580)
                    score = score + 2 

                else:
                    longer = False
    if score > 10 and score < 16:        
        #food type 2
        screen.blit(img2,apple)
        food = apple
        
        #poisen
        screen.blit(img3,poison)
        food = poison
        
        for i in range( len(snake_cells) ):
            if gameover == False:
                snake = pygame.draw.rect(screen, GREEN, [snake_cells[i][0], snake_cells[i][1], cell_width, cell_height], 0)
                if i == 0:
                    if snake.colliderect(apple):
                        longer = True
                        pygame.mixer.music.pause()
                        crunch()
                        pygame.mixer.music.unpause()
                        
                        apple.x = random.randint(75, 580)
                        apple.y = random.randint(75, 580)
                        score = score + 2 
                    if snake.colliderect(poison):
                        longer = False
                        poison.x = random.randint(75, 580)
                        poison.y = random.randint(75, 580)
                        score += -5  
                        count += 1
                    else:
                        longer = False
    #Level3
    if score > 15 :
       clock.tick(12)


       #food type 2
       screen.blit(img2,apple)
       food = apple
       
       for i in range( len(snake_cells) ):
        if gameover == False:

            snake = pygame.draw.rect(screen, GREEN, [snake_cells[i][0], snake_cells[i][1], cell_width, cell_height], 0)
            if i == 0:
                if snake.colliderect(food):
                    longer = True
                    pygame.mixer.music.pause()
                    crunch()
                    pygame.mixer.music.unpause()
                    
                    apple.x = random.randint(75, 580)
                    apple.y = random.randint(75, 580)
                    score = score + 2 

                else:
                    longer = False
        wall1 = pygame.draw.rect(screen, GRAY , (200 , 350 , 400 , 10))
        wall2 = pygame.draw.rect(screen , GRAY , (0 ,250 , 400 , 10 ))
        wall3 = pygame.draw.rect(screen , GRAY , ( 0 , 450 , 400 , 10))
        wall4 = pygame.draw.rect( screen , GRAY , (200 , 530 , 400 , 10 ))
        wall5 = pygame.draw.rect( screen , GRAY , (200 , 150 , 400 , 10))
        
    if score > 17 : 
        text = font1.render('Level 3 !', True, RED)
        screen.blit(text, (10, 40)) 
        screen.blit(img2,apple)
        food = apple
        
        #poisen
        screen.blit(img3,poison)
        food = poison
        
        #walls
        wall1 = pygame.draw.rect(screen, GRAY , (200 , 350 , 400 , 10))
        wall2 = pygame.draw.rect(screen , GRAY , (0 ,250 , 400 , 10 ))
        wall3 = pygame.draw.rect(screen , GRAY , ( 0 , 450 , 400 , 10))
        wall4 = pygame.draw.rect( screen , GRAY , (200 , 530 , 400 , 10 ))
        wall5 = pygame.draw.rect( screen , GRAY , (200 , 150 , 400 , 10))
       
        for i in range( len(snake_cells) ):
         if gameover == False:

            snake = pygame.draw.rect(screen, GREEN, [snake_cells[i][0], snake_cells[i][1], cell_width, cell_height], 0)
            if i == 0:
                if snake.colliderect(apple):
                    longer = True
                    pygame.mixer.music.pause()
                    crunch()
                    pygame.mixer.music.unpause()
                    apple.x = random.randint(75, 580)
                    apple.y = random.randint(75, 580)
                    score = score + 2 
                if snake.colliderect(poison):
                        longer = False
                        poison.x = random.randint(75, 580)
                        poison.y = random.randint(75, 580)
                        count += 1
                elif snake.colliderect(wall1):
                    gameover = True
                elif snake.colliderect(wall2):
                    gameover = True
                elif snake.colliderect(wall3):
                    gameover = True
                elif snake.colliderect(wall4):
                    gameover = True
                elif snake.colliderect(wall5):
                    gameover = True
                else:
                    longer = False
        
    
    if count == 1:
        pygame.draw.rect(screen, BLACK, (410,30 ,30 ,40 ))
    if count == 2:
        pygame.draw.rect(screen, BLACK, (410,30 ,60 ,40 ))
    if count == 3:
        gameover = True
        
    
    #Score
    text = font1.render('Score: ' + str(score), True, YELLOW)
    screen.blit(text, (10, 10))
    
    #Game Over
    if gameover == True:
        screen.fill(BLACK)
        screen.blit(img4,(265 , 250))
        text = font1.render('Game Over!', True, RED)
        screen.blit(text, (225, 330))
    #text
    text = font2.render('Press Esc to Exit', True, WHITE) 
    screen.blit(text, (1, 590))
     

    pygame.display.update()
