import pygame
import os

from pygame.key import get_pressed, key_code
from pygame.display import update
pygame.init()
#* Default Width and Height of Characters
character_width, character_height = 50, 60

class BadGuy:
    def __init__(self, name, attack=0, health=0, character_width=100, character_height=85 ):
        self.name = name
        self.attack = attack
        self.health = health
        self.width = character_width
        self.height = character_height

class WarriorB(BadGuy):
    def __init__(self):
        super().__init__('Warrior', 60, 150)
        bad_warrior_import = pygame.image.load(os.path.join('Assets', 'badwarrior.png'))
        bad_warrior = pygame.transform.scale(bad_warrior_import, (character_width, character_height))
        self.print = bad_warrior

class GoodGuy:
    def __init__(self, name, attack=0, health=0, character_width=100, character_height=85):
        self.name = name
        self.attack = attack
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
    def __init__(self, name, attack=50, health=2000):
        #* Wizards image and display size
        super().__init__(name, 100, 500)
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
