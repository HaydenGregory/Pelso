
#todo: Set an inventory function. Set Boundaries for walls and enemy. Set chest object. Health display. Set seprate draw screen for combat. 

import sys
import pygame
import os
from pygame import key
from pygame.constants import HIDDEN, QUIT
from pygame.key import get_pressed, key_code
from Classes import BadGuy, GoodGuy, WarriorB, Wizard
pygame.init()


user_character = Wizard('Pelso')
warrior_enemy = WarriorB()

#* Window Display settings
WIDTH, HEIGHT = 1500, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pelso")

#? Start Menu Image
start_screen_image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Title Screen.png')), (WIDTH, HEIGHT))
#? Background Image Walking
background_import = pygame.image.load(os.path.join('Assets', 'Dungeon.png'))
Background = pygame.transform.scale(background_import, (WIDTH, HEIGHT))

smallfont = pygame.font.Font(os.path.join('Assets', 'Fipps-Regular.ttf'), 20)
# light shade of the buttons
color_light = (170,170,170)
# dark shade of the buttons
color_dark = (100,100,100)

WHITE = ((255, 255, 255))
FPS = 60
VEL = 5

start = smallfont.render('START' , True , WHITE)
quit = smallfont.render('QUIT', True, WHITE)

player = pygame.Rect(125, 700, user_character.width, user_character.height)
enemy = pygame.Rect(500, 700, warrior_enemy.width, warrior_enemy.height) 


def player_movement(keys_pressed, player):
        if keys_pressed[pygame.K_RIGHT]: #* Move Right
            user_character.print = user_character.wizard_right
            user_character.update()
            if player.x <= 1400: 
                player.x += VEL
        if keys_pressed[pygame.K_LEFT]: #* Move Left
            user_character.print = user_character.wizard_left
            user_character.update()
            if player.x >= 0: 
                player.x -= VEL
        if keys_pressed[pygame.K_UP]: #* Move Up
            user_character.print = user_character.wizard_up
            user_character.update()
            if player.y >= 0: 
                player.y -= VEL
        if keys_pressed[pygame.K_DOWN]: #* Move Down
            user_character.print = user_character.wizard_down
            user_character.update()
            if player.y <= 800: 
                player.y += VEL


def draw_window_walk():
    WIN.blit(Background, (0,0))
    WIN.blit(user_character.print, (player.x, player.y))
    WIN.blit(warrior_enemy.print, (enemy.x, enemy.y))
    user_character.update()
    # WIN.blit(user_character.print()(200, 200))
    pygame.display.update()





def startscreen():
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
        #checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if WIDTH/2 <= mouse[0] <= WIDTH/2+140 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+40:
                break
            if WIDTH/2 <= mouse[0] <= WIDTH/2+140 and HEIGHT/2+80 <= mouse[1] <= HEIGHT/2+120:
                    pygame.quit()
        WIN.blit(start_screen_image, (0,0))
        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()
        if WIDTH/2 <= mouse[0] <= WIDTH/2+140 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+40:
            pygame.draw.rect(WIN,color_light,[WIDTH/2,HEIGHT/2,140,40])
        else:
            pygame.draw.rect(WIN,color_dark,[WIDTH/2,HEIGHT/2,140,40])	
        # if mouse is hovered on a button it
        # changes to lighter shade
        if WIDTH/2 <= mouse[0] <= WIDTH/2+140 and HEIGHT/2+80 <= mouse[1] <= HEIGHT/2+120:
            pygame.draw.rect(WIN,color_light,[WIDTH/2,HEIGHT/2+80,140,40])
        else:pygame.draw.rect(WIN,color_dark,[WIDTH/2,HEIGHT/2+80,140,40])

        # superimposing the text onto our button
        WIN.blit(start, (WIDTH/2+23,HEIGHT/2))
        WIN.blit(quit, (WIDTH/2+37, HEIGHT/2+80))
        # updates the frames of the game
        pygame.display.update()

def main():
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        draw_window_walk()
        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed, player)
        if player.colliderect(enemy):
            break
        # elif keys_pressed[pygame.K_i]:
        #     WIN.blit(print(str(user_character.inventory())))
    
    pygame.quit()


if __name__ == "__main__":
    startscreen()
    main()
