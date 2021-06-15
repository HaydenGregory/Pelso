from typing import Annotated
import pygame
import os
import random
from pygame.key import get_pressed, key_code
from pygame.display import update
pygame.init()
#* Default Width and Height of Character (GOOD)
character_width, character_height = 50, 60

#* Default Width and Height of Characters (BAD)
character_width_b, character_height_b = 100, 85

class Item:
    def __str__(self):
        return self.name

    def __init__(self, name, attack_boost=0, health_boost=0):
        self.attack_boost = attack_boost
        self.health_boost = health_boost
        self.name = name
    
    def use_health_potion(self, target):
        target.health += self.health_boost

    def use_spell(self, spell, target):
        spell(target)

class Spell:
    def __str__(self):
        return self.name
    
    def __init__(self, name):
        self.name = name
    
    def use_spell(self, target):
        hit = random.choice([True, False])
        if hit == True:
            target.attack_amount = random.randint(100,150)
        else:
            target.attack_amount = 0

class BadGuy:
    def __init__(self, name, health=0, character_width=100, character_height=85 ):
        self.name = name
        self.health = health
        self.width = character_width
        self.height = character_height

class EnemyMage(BadGuy):
    def __init__(self, name, health=0):
        super().__init__('')
        bad_warrior_import = pygame.image.load(os.path.join('Assets', 'badwiz.png'))
        bad_warrior = pygame.transform.scale(bad_warrior_import, (character_width_b, character_height_b))
        self.print = bad_warrior
        self.name = name
        self.attack_amount = []
        self.health = health
        self.is_alive = True
        if self.health <= 0:
            self.is_alive = False
        self.max_hp = 1500

#! Bad Guy Attack Function

    def attack(self, target):
        attack_amount = random.randint(350, 650)
        self.attack_amount.append(attack_amount)
        target.health -= attack_amount

class GoodGuy:
    def __init__(self, name, health=3000, character_width=100, character_height=85):
        self.name = name
        self.health = health
        self.height = character_height
        self.width = character_width
        self.attack_amount = []
        self.regen_amount = []
        self.is_alive = True

    # def use_item(item):
        
class Wizard(GoodGuy):
                    #* How it calls on the images to be looped

    def update(self):
        self.current_sprite += 1
        if self.current_sprite >= len(self.walk_down):
            self.current_sprite = 0
        self.wizard_down = self.walk_down[self.current_sprite]
        self.wizard_up = self.walk_up[self.current_sprite]
        self.wizard_left = self.walk_left[self.current_sprite]
        self.wizard_right = self.walk_right[self.current_sprite]

#! Good Guy Attack Functions 
    def fire_blast(self, target):
        attack_amount = random.randint(200, 350)
        self.attack_amount.append(attack_amount)
        target.health -= attack_amount
    
    def regeneration_spell(self):
        regeneration_amount = random.randint(130, 200)
        self.regen_amount.append(regeneration_amount)
        self.health += regeneration_amount

    def lightning_blast(self, target):
        attack_amount = random.randint(350, 500)
        self.attack_amount.append(attack_amount)
        target.health -= attack_amount

#! __INIT__ Function
    def __init__(self, name, health=0):
        super().__init__('Pelso', 3000)
        self.name = name
        self.health = health
        self.max_hp = 3000
        self.inventory = []

        #* Walking function for Wizard.
        self.walk_left = []
        self.walk_right =[]
        self.walk_up = []
        self.walk_down = []
        self.walk_down.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Wizard_facing.png')), (character_width, character_height)))
        self.walk_down.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Wizard_facing2.png')), (character_width, character_height)))
        self.walk_down.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Wizard_facing3.png')), (character_width, character_height)))
        self.walk_left.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Wizard_left1.png')), (character_width, character_height)))
        self.walk_left.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Wizard_left2.png')), (character_width, character_height)))
        self.walk_left.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Wizard_left3.png')), (character_width, character_height)))
        self.walk_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Wizard_right1.png')), (character_width, character_height)))
        self.walk_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Wizard_right2.png')), (character_width, character_height)))
        self.walk_right.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Wizard_right3.png')), (character_width, character_height)))
        self.walk_up.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Wizard_up1.png')), (character_width, character_height)))
        self.walk_up.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Wizard_up2.png')), (character_width, character_height)))
        self.walk_up.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Wizard_up3.png')), (character_width, character_height)))
        good_wizard = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Wizard_facing.png')), (character_width, character_height))#Where to find wizard
        self.current_sprite = 0
        self.wizard_down = self.walk_down[self.current_sprite]
        self.wizard_up = self.walk_up[self.current_sprite]
        self.wizard_left = self.walk_left[self.current_sprite]
        self.wizard_right = self.walk_right[self.current_sprite]
        self.print = good_wizard

#! Good Guy Use Items Function
    def use_item(self, item, target):
        return item(target)