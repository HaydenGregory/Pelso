
#todo: Set an inventory function. Set Boundaries for walls and enemy. Set chest object. Health display. Set seprate draw screen for combat. 
#! Imports
import sys
import pygame
import os
from pygame import key
from pygame import color
from pygame.constants import HIDDEN, QUIT
from pygame.key import get_pressed, key_code
from Classes import BadGuy, GoodGuy, EnemyMage, Wizard
pygame.init()

#! Defining Characters
user_character = Wizard('Pelso', 3000)
enemy_mage = EnemyMage('Magnifco the Great', 500, 1500)

#! Window Display settings
WIDTH, HEIGHT = 1500, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pelso")

#! Health Bars
class HealthBar():
	def __init__(self, x, y, hp, max_hp):
		self.x = x
		self.y = y
		self.hp = hp
		self.max_hp = max_hp

	def draw(self, hp):
		#update with new health
		self.hp = hp
		#calculate health ratio
		ratio = self.hp / self.max_hp
		pygame.draw.rect(WIN, RED, (self.x, self.y, 150, 30))
		pygame.draw.rect(WIN, GREEN, (self.x, self.y, 150 * ratio, 30))

user_health_bar = HealthBar(190, 740, user_character.health, user_character.max_hp)
enemy_mage_health_bar = HealthBar(1150, 80, enemy_mage.health, enemy_mage.max_hp)


#! Background Images
#? Start Menu Image
start_screen_image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Title Screen.png')), (WIDTH, HEIGHT))
#? Background Image Walking
background_import = pygame.image.load(os.path.join('Assets', 'Dungeon.png'))
Background = pygame.transform.scale(background_import, (WIDTH, HEIGHT))
#? Background Image Fight
fight_background = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'fighting.jpg')), (WIDTH, HEIGHT))

#! Fonts
medium_font = pygame.font.Font(os.path.join('Assets', 'Fipps-Regular.ttf'), 20)
small_font = pygame.font.Font(os.path.join('Assets', 'Fipps-Regular.ttf'), 10)

#! Colors 
color_light = (170,170,170)
color_dark = (100,100,100)
RED = ((255, 0, 0))
GREEN = ((0, 255, 0))
WHITE = ((255, 255, 255))
FPS = 60
VEL = 5

#! Texts to be displayed
start = medium_font.render('START' , True , WHITE)
quit = medium_font.render('QUIT', True, WHITE)

#* User displays
player_health = medium_font.render(f"""HP: {str(user_character.health)}""",  True, RED)
pelso_name = medium_font.render(str(user_character.name),  True, WHITE)
battle_option1 = medium_font.render(f"""1. Fire Blast, {str(enemy_mage.name)}""", True, WHITE)
battle_option2 = medium_font.render(f"2. Lightning Strike, {str(enemy_mage.name)}", True, WHITE)
battle_option3 = medium_font.render("3. Cast Regeneration Spell", True, WHITE)
battle_option4 = medium_font.render("4. Open Inventory", True, WHITE)
battle_option5 = medium_font.render("5. Attempt to Flee", True, WHITE)
#* Enemy displays 
enemy_name = medium_font.render(str(enemy_mage.name), True, WHITE)
enemy_health = medium_font.render(f"""HP: {str(enemy_mage.health)}""", True, RED)

#! Rectangles for Characters
player = pygame.Rect(125, 700, user_character.width, user_character.height)
enemy = pygame.Rect(500, 700, enemy_mage.width, enemy_mage.height) 

#! Functions

def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	WIN.blit(img, (x, y))

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
    WIN.blit(enemy_mage.print, (enemy.x, enemy.y))
    user_character.update()
    # WIN.blit(user_character.print()(200, 200))
    pygame.display.update()

def draw_fight_sequence():
    WIN.blit(fight_background, (0,0))
    pygame.draw.rect(WIN, color_light,[30, 700, 450,200])
    pygame.draw.rect(WIN, color_light, [800, 700, 700, 200])
    pygame.draw.rect(WIN, color_light, [1000, 30, 350, 100])
    WIN.blit(player_health, (40, 730))
    WIN.blit(pelso_name, (40, 700))
    WIN.blit(enemy_name, (1010, 40))
    WIN.blit(enemy_health, (1010, 70))
    WIN.blit(battle_option1, (810, 710))
    WIN.blit(battle_option2, (810, 740))
    WIN.blit(battle_option3, (810, 770))
    WIN.blit(battle_option4, (810, 800))
    WIN.blit(battle_option5, (810, 830))
    user_health_bar.draw(3000)
    enemy_mage_health_bar.draw(1500)
    pygame.display.update()

#! Game Loop Functions
def fight_loop():
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        draw_fight_sequence()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_1] == 1:
            user_character.fire_blast(enemy_mage)
            draw_text(f"{user_character.name} hit {enemy_mage.name} for 350", small_font, WHITE, 40, 740)
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
    
    # pygame.quit()


if __name__ == "__main__":
    startscreen()
    main()
    fight_loop()