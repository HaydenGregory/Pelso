
#todo: Set an inventory function. Set Boundaries for walls and enemy. Set chest object. Health display. Set seprate draw screen for combat. 
#! Imports
from math import e
import sys
import pygame
import os
import time 
import random
from pygame import key
from pygame import color
from pygame import draw
from pygame.constants import HIDDEN, QUIT
from pygame.key import get_pressed, key_code
from pygame.math import disable_swizzling
from pygame.surfarray import pixels_green
from Classes import BadGuy, GoodGuy, EnemyMage, Item, Spell, Wizard
pygame.init()

#! Defining Characters
user_character = Wizard('Pelso', 3000)
enemy_mage = EnemyMage('Magnifco the Great', 1500)

#! Defining Items
# user_character.inventory.append(HealthPotion())
# user_character.inventory.append(SpellOfConfusion(enemy_mage))
health_potion= Item('Health Potion', 0, 500)
spell_of_confusion = Spell('Spell of Confusion')
user_character.inventory.append(health_potion)
user_character.inventory.append(spell_of_confusion)


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
medium_mine_font = pygame.font.Font(os.path.join('Assets', 'Minecraft.ttf'), 20)
large_font = pygame.font.Font(os.path.join('Assets', 'Fipps-Regular.ttf'), 40)
medium_large_font = pygame.font.Font(os.path.join('Assets', 'Fipps-Regular.ttf'), 34)

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
pelso_name = medium_font.render(str(user_character.name),  True, WHITE)
battle_option1 = medium_font.render(f"""1. Fire Blast, {str(enemy_mage.name)}""", True, WHITE)
battle_option2 = medium_font.render(f"2. Lightning Strike, {str(enemy_mage.name)}", True, WHITE)
battle_option3 = medium_font.render("3. Cast Regeneration Spell", True, WHITE)
battle_option4 = medium_font.render("4. Open Inventory", True, WHITE)
battle_option5 = medium_font.render("5. Attempt to Flee", True, WHITE)
thanks_message = large_font.render("Thanks For Playing!", True, WHITE)

#! Rectangles for Characters
player = pygame.Rect(125, 700, user_character.width, user_character.height)
enemy = pygame.Rect(500, 700, enemy_mage.width, enemy_mage.height) 

#! Functions
#* Attempt Flee Function
def attempt_flee():
    answer = random.choice([True, False, False, False])
    return answer

#* Draw Text Function
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	WIN.blit(img, (x, y))

#* Player Movement Function
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

#! Drawing Functions
def draw_window_walk():
    WIN.blit(Background, (0,0))
    WIN.blit(user_character.print, (player.x, player.y))
    WIN.blit(enemy_mage.print, (enemy.x, enemy.y))
    user_character.update()
    # WIN.blit(user_character.print()(200, 200))
    pygame.display.update()

def draw_fight_sequence(message, end_message, flee_message):
    WIN.blit(fight_background, (0,0))
    pygame.draw.rect(WIN, color_light,[30, 700, 750,200])
    pygame.draw.rect(WIN, color_light, [800, 700, 700, 200])
    pygame.draw.rect(WIN, color_light, [1000, 30, 350, 100])
    enemy_name = medium_font.render(str(enemy_mage.name), True, WHITE)
    player_health = medium_font.render(f"""HP: {str(user_character.health)}""",  True, RED)
    enemy_health = medium_font.render(f"""HP: {str(enemy_mage.health)}""", True, RED)
    WIN.blit(player_health, (40, 730))
    WIN.blit(pelso_name, (40, 700))
    WIN.blit(enemy_name, (1010, 40))
    WIN.blit(enemy_health, (1010, 70))
    WIN.blit(battle_option1, (810, 710))
    WIN.blit(battle_option2, (810, 740))
    WIN.blit(battle_option3, (810, 770))
    WIN.blit(battle_option4, (810, 800))
    WIN.blit(battle_option5, (810, 830))
    user_health_bar.draw(user_character.health)
    enemy_mage_health_bar.draw(enemy_mage.health)
    draw_text(message, medium_mine_font, WHITE, 40, 800)
    draw_text(end_message, large_font, RED, WIDTH/2, HEIGHT/2)
    draw_text(flee_message, medium_large_font, RED, 50, 300)
    pygame.display.update()

#! Printed Messages During Battle (Functions)
def end_fight_message():
    if enemy_mage.is_alive == False:
        return "VICTORY"
    else:
        return "DEFEAT"

def success_flee_message():
    return "FLEE SUCCESSFUL"

def failed_flee_message():
    return f"FLEE FAILED, {enemy_mage.name} blocked the path!"

def user_inventory_message():
    count = 1
    printable_statement = ''
    for items in user_character.inventory:
        printable_statement += f"{count}: {str(items)}.  "
        count += 1
    return printable_statement

def used_item_in_inventory_message1():
    return f"{user_character.name}, used {user_character.inventory[0]}."

def used_item_in_inventory_message2():
    return f"{user_character.name}, used {user_character.inventory[1]}."

def enemy_attack_message():
    if enemy_mage.skip_turn:
        return f"{enemy_mage.name} is confused and missed the attack."
    if enemy_mage.attack_amount[0] > 525:
        return f"**CRITICAL** {enemy_mage.name} attacks {user_character.name} for {enemy_mage.attack_amount[0]}"
    else:
        return f"{enemy_mage.name} attacks {user_character.name} for {enemy_mage.attack_amount[0]}"

def fire_blast_message():
    if user_character.attack_amount[0] > 320:
        return f"**CRITICAL** {user_character.name} hit {enemy_mage.name} for {user_character.attack_amount[0]}" 
    else:
        return f"{user_character.name} hit {enemy_mage.name} for {user_character.attack_amount[0]}" 

def lightning_blast_message():
    if user_character.attack_amount[0] > 450:
        return f"""**CRITICAL** {user_character.name} struck {enemy_mage.name} with a lightning strike for {user_character.attack_amount[0]}"""
    else:
        return f"""{user_character.name} struck {enemy_mage.name} with a lightning strike for {user_character.attack_amount[0]}"""

def regeneration_spell_message():
    if user_character.regen_amount[0] > 175:
        return f"**MASSIVE HEALTH SPELL** {user_character.name} regenerated {user_character.regen_amount[0]} health!"
    else:
        return f"{user_character.name} regenerated {user_character.regen_amount[0]} health!"

#! Game Loop Functions
def fight_loop():
    clock = pygame.time.Clock()
    message = ''
    end_message = ''
    flee_message = ''
    player_turn = True
    in_inventory = False
    while enemy_mage.is_alive and user_character.is_alive:
        FPS = 60
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        keys_pressed = pygame.key.get_pressed()
        if player_turn:
            if in_inventory:
                message = user_inventory_message() + "0. Return."
                if keys_pressed[pygame.K_1]:
                    health_potion.use_health_potion(user_character)
                    message = used_item_in_inventory_message1()
                    draw_fight_sequence(message, end_message, flee_message)
                    in_inventory = False
                    time.sleep(1)
                if keys_pressed[pygame.K_2]:
                    spell_of_confusion.use_spell(enemy_mage)
                    message = used_item_in_inventory_message2()
                    draw_fight_sequence(message, end_message, flee_message)
                    player_turn = False
                    in_inventory = False
                    time.sleep(1)
                if keys_pressed[pygame.K_0]:
                    in_inventory = False
                    time.sleep(1)
                draw_fight_sequence(message, end_message, flee_message)
            else:
                if keys_pressed[pygame.K_1]:
                    user_character.fire_blast(enemy_mage)
                    message = fire_blast_message()
                    del user_character.attack_amount[0]
                    player_turn = False
                if keys_pressed[pygame.K_2]:
                    user_character.lightning_blast(enemy_mage)
                    message = lightning_blast_message()
                    del user_character.attack_amount[0]
                    player_turn = False
                if keys_pressed[pygame.K_3]:
                    user_character.regeneration_spell()
                    message = regeneration_spell_message()
                    del user_character.regen_amount[0]
                    player_turn = False
                if keys_pressed[pygame.K_4]:
                    in_inventory = True
                if keys_pressed[pygame.K_5]:
                    if attempt_flee():
                        flee_message = success_flee_message()
                        enemy_mage.is_alive = False
                        player_turn = False
                        draw_fight_sequence(message, end_message, flee_message)
                        main()
                    else:
                        flee_message = failed_flee_message()
                        player_turn =False
                        draw_fight_sequence(message, end_message, flee_message)
        else:
            flee_message = ''
            time.sleep(2)
            enemy_mage.attack(user_character)
            message = enemy_attack_message()
            if enemy_mage.attack_amount:
                del enemy_mage.attack_amount[0]
            player_turn = True
            enemy_mage.skip_turn = False
        
        if user_character.health <= 0:
            user_character.is_alive = False
        if enemy_mage.health <= 0:
            enemy_mage.is_alive = False
        
        if user_character.is_alive != True or enemy_mage.is_alive != True:
            end_message = end_fight_message()
            draw_fight_sequence(message, end_message, flee_message)
            time.sleep(5)
        print(enemy_mage.attack_amount)
        draw_fight_sequence(message, end_message, flee_message)

def startscreen():
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if WIDTH/2 <= mouse[0] <= WIDTH/2+140 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+40:
                break
            if WIDTH/2 <= mouse[0] <= WIDTH/2+140 and HEIGHT/2+80 <= mouse[1] <= HEIGHT/2+120:
                pygame.quit()
        WIN.blit(start_screen_image, (0,0))

        mouse = pygame.mouse.get_pos()
        if WIDTH/2 <= mouse[0] <= WIDTH/2+140 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+40:
            pygame.draw.rect(WIN,color_light,[WIDTH/2,HEIGHT/2,140,40])
        else:
            pygame.draw.rect(WIN,color_dark,[WIDTH/2,HEIGHT/2,140,40])	
        if WIDTH/2 <= mouse[0] <= WIDTH/2+140 and HEIGHT/2+80 <= mouse[1] <= HEIGHT/2+120:
            pygame.draw.rect(WIN,color_light,[WIDTH/2,HEIGHT/2+80,140,40])
        else:pygame.draw.rect(WIN,color_dark,[WIDTH/2,HEIGHT/2+80,140,40])

        WIN.blit(start, (WIDTH/2+23,HEIGHT/2))
        WIN.blit(quit, (WIDTH/2+37, HEIGHT/2+80))

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

def end_screen():
    while True:
        WIN.blit(start_screen_image, (0,0))
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if WIDTH/2 <= mouse[0] <= WIDTH/2+140 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+40:
                break
            if WIDTH/2 <= mouse[0] <= WIDTH/2+140 and HEIGHT/2+80 <= mouse[1] <= HEIGHT/2+120:
                pygame.quit()
        mouse = pygame.mouse.get_pos()
        if WIDTH/2 <= mouse[0] <= WIDTH/2+140 and HEIGHT/2+80 <= mouse[1] <= HEIGHT/2+120:
            pygame.draw.rect(WIN,color_light,[WIDTH/2,HEIGHT/2+80,140,40])
        else:pygame.draw.rect(WIN,color_dark,[WIDTH/2,HEIGHT/2+80,140,40])
        WIN.blit(thanks_message, (450, 600))
        WIN.blit(quit, (WIDTH/2+37, HEIGHT/2+80))
        pygame.display.update()

if __name__ == "__main__":
    startscreen()
    main()
    fight_loop()
    end_screen()