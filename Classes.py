import pygame
import os

#* Default Width and Height of Characters
character_width, character_height = 100, 85

class BadGuy:
    def __init__(self, name, attack=0, health=0, character_width=100, character_height=85 ):
        self.name = name
        self.attack = attack
        self.health = health
        self.width = character_width
        self.height = character_height

class Warrior(BadGuy):
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
    def __init__(self, name, attack=50, health=2000):
        #* Wizards image and display size
        super().__init__(name, 100, 500)
        good_wizard_image = pygame.image.load(os.path.join('Assets', 'Wizard2.png'))#Where to find wizard
        good_wizard = pygame.transform.scale(good_wizard_image, (character_width, character_height))#What size it will display
        self.print = good_wizard


    # def draw(self):
    #     return WIN.blit(good_wizard, (100, 100))