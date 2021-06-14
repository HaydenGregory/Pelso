#Module that allows me to create a screen and add images to the screen
import pygame
pygame.init()
win = pygame.display.set_mode((800,600))

#Variable that will keep track of the index of what slot the player is
#selecting
selectedSlot = None

#Function that checks whether there is collision or not
def collision(x,y,x2,y2,w):
    if x + w > x2 > x and y+w > y2 > y:
        return True
    else:
        return False

#Slot Class
class slotClass:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self, win):
        #Draws the slots using the x and y values
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, 50, 50))

        #Uses a function to test for collision with the mouse's x and y values
        if collision(self.x, self.y, mx, my, 66):
            global selectedSlot
            pygame.draw.rect(win, (128, 0, 0), (self.x, self.y, 50, 50))

            #This will set an integer value to a varaible, dependent on what the index of the element the player selecting is
            selectedSlot = slotArray.index(self)

        #Problem with code:
        #When the following 2 lines are uncommmented, the variable selectedSlot is set to "None", regardless of whether there is collision or not
        else:
            selectedSlot = None

#Slot array
slotArray = []
#Slot information
slotCount = 9


#Populates the slotArray with the desired slotCount
while len(slotArray) != slotCount:
    slotArray.append(slotClass(100+len(slotArray)*70,50))

#main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Mouse x and y value to set to the vars mx and my
    mx,my = pygame.mouse.get_pos()
    win.fill((0,0,0))


    #For every element in the slotArray, the function draw is called from the slotClass
    selectedSlot = None
    for i in slotArray:
        i.draw(win)
        if selectedSlot is not None:
            break

    print(selectedSlot)

    pygame.display.update()
pygame.quit()
