
#todo: Allow user to pick character. Set an inventory function. Set seprate draw screen for combat. 

import pygame
import os
from pygame import key
from pygame.key import get_pressed, key_code
from Classes import BadGuy, GoodGuy, WarriorB, Wizard
pygame.init()

# user_input = input(f"""Which Character would you like? 
# 1. Wizard
# 2. Archer
# 3. Warrior
# Enter a number: """)

# if user_input == 1:
#     user_character = Wizard(str(input("What would you like to name the Wizard? ")))
# elif user_input == 2:
#     user_character = Archer(str(input("What would you like to name the Archer? ")))
# elif user_input == 3:
#     user_character = Warrior(str(input("What would you like to name the Warrior? ")))
# d

user_character = Wizard("Dale")
warrior_enemy = WarriorB()


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
        #     WIN.blit(print(str(user_character.inventory())))
    
    pygame.quit()

if __name__ == "__main__":
    main()
