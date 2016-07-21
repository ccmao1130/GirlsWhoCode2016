# Runner Game
# 07/15/2016

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Runner Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# import city scroller file
from city_scroller_rg import Scroller

all_sprites_list = []
good_sprites = []

class RunnerSprite(pygame.sprite.Sprite):
	def __init__(self, image1):
		pygame.sprite.Sprite.__init__(self)
		self.image1 = image1
		self.image1 = pygame.image.load(self.image1)	
		self.image1 = pygame.transform.scale(self.image1, (95, 60)) # re-sizes image
		self.image1 = pygame.transform.flip(self.image1, True, False) # rotates image
		all_sprites_list.append(self.image1)
		self.rect = self.image1.get_rect()
	def draw(self, mouse_pos):
		global screen
		for x in all_sprites_list:
			screen.blit(x, mouse_pos)

class GoodSprites(pygame.sprite.Group):
	def __init__(self, image2):
		pygame.sprite.Group.__init__(self)
		self.image2 = image2
		self.image2 = pygame.image.load(self.image2)
		self.image2 = pygame.transform.scale(self.image2, (35, 35)) # re-sizes image
		#all_sprites_list.append(self.image2)
		self.rect = self.image2.get_rect()
		screen.blit(self.image2, (60, 70))


FRONT_SCROLLER_COLOR = (0, 237, 203) # TURQ
BACKGROUND_COLOR = (189, 246, 255) # LIGHT BLUE

front_scroller = Scroller(SCREEN_WIDTH, 300, SCREEN_HEIGHT-10, FRONT_SCROLLER_COLOR, 6)

front_scroller.add_buildings()
a = 0	

# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	# --- Game logic should go here
	if a % 10 == 0:
		front_scroller.add_building(-100)
	a += 1
	
	# --- Screen-clearing code goes here

	# Here, we clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.

	# If you want a background image, replace this clear with blit'ing the
	# background image.
	screen.fill(BACKGROUND_COLOR)
	
	# --- Drawing code should go here
	front_scroller.draw_buildings()
	front_scroller.move_buildings()
	
	runner = RunnerSprite("pikachu.jpg")
	mouse_pos = pygame.mouse.get_pos() # get mouse position
	runner.draw((mouse_pos[0]-30, mouse_pos[1]-30))
	
	good = GoodSprites("pokeball.jpg")
	

	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(30)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
