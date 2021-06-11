
#todo: Make everything a class. Allow user to pick character. Set an inventory function. Set seprate draw screen for combat. 

import pygame
import os
from pygame import key
from pygame.key import get_pressed, key_code
from Classes import GoodGuy, Warrior, Wizard

pygame.init()

user_wizard = Wizard("Dale")
warrior_enemy = Warrior()
# user_wizard = Wizard(str(input('What is the name of your wizard? ')))


#* Window Display settings
WIDTH, HEIGHT = 1500, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wizard")

#? Background Image
background_import = pygame.image.load(os.path.join('Assets', 'Dungeon.png'))
Background = pygame.transform.scale(background_import, (WIDTH, HEIGHT))


# #* Default Width and Height of Characters
# character_width, character_height = 100, 85


WHITE = ((255, 200, 255))
FPS = 60
VEL = 5

player = pygame.Rect(125, 700, user_wizard.width, user_wizard.height)
enemy = pygame.Rect(500, 700, warrior_enemy.width, warrior_enemy.height) 

def player_movement(keys_pressed, player):
        if keys_pressed[pygame.K_RIGHT]: #* Move Left
            if player.x <= 1400: 
                player.x += VEL
        if keys_pressed[pygame.K_LEFT]: #* Move Right
            if player.x >= 0: 
                player.x -= VEL
        if keys_pressed[pygame.K_UP]: #* Move Up
            if player.y >= 0: 
                player.y -= VEL
        if keys_pressed[pygame.K_DOWN]: #* Move Down
            if player.y <= 800: 
                player.y += VEL


def draw_window_walk():
    WIN.blit(Background, (0,0))
    WIN.blit(user_wizard.print, (player.x, player.y))
    WIN.blit(warrior_enemy.print, (enemy.x, enemy.y))
    # WIN.blit(user_wizard.print()(200, 200))
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
        # elif keys_pressed[pygame.K_i]:
        #     WIN.blit(print(str(user_wizard.inventory())))
    
    pygame.quit()

if __name__ == "__main__":
    main()
