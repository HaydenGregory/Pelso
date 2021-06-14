import pygame
import os
from pygame.key import get_pressed, key_code
from pygame.display import update
pygame.init()
#* Default Width and Height of Character (GOOD)
character_width, character_height = 50, 60

#* Default Width and Height of Characters (BAD)
character_width_b, character_height_b = 100, 85

class BadGuy:
    def __init__(self, name, attack=0, health=0, character_width=100, character_height=85 ):
        self.name = name
        self.attack = attack
        self.health = health
        self.width = character_width
        self.height = character_height

class EnemyMage(BadGuy):
    def __init__(self, name, attack=0, health=0):
        super().__init__('')
        bad_warrior_import = pygame.image.load(os.path.join('Assets', 'badwiz.png'))
        bad_warrior = pygame.transform.scale(bad_warrior_import, (character_width_b, character_height_b))
        self.print = bad_warrior
        self.name = name
        self.attack = attack
        self.health = health

class GoodGuy:
    def __init__(self, name, health=3000, character_width=100, character_height=85):
        self.name = name
        self.health = health
        self.inventory = []
        self.height = character_height
        self.width = character_width

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

#! Attack Functions 
    def fire_blast(target):
        target.health -= 350

    def regeneration_spell(self):
        self.health += 200

    def lightning_blast(target):
        target.health -= 500


#! __INIT__ Function
    def __init__(self, name, health=0):
        super().__init__('Pelso', 3000)
        self.name = name
        self.health = health


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