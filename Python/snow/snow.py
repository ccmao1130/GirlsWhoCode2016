# Snow Animation
# 07/11/2016

"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
BROWN = (139, 69, 19)
SNOW_BLUE = (219, 255, 255)
LIGHT_BLUE = (101, 208, 255)
LIGHTER_BLUE = (189, 246, 255)
TURQ = (0, 237, 203)

snow_colors = [SNOW_BLUE, WHITE, LIGHT_BLUE, LIGHTER_BLUE]

pygame.init()

# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)
image1 = pygame.image.load("winter.jpg")
image1 = pygame.transform.scale(image1, size)

pygame.display.set_caption("Snow")

class SnowFlake():
	'''
	This class will be used to create the SnowFlake Objects.
	It takes: 
		- size - an integer that tells us how big we want the snowflake
		- position - a 2 item list that tells us the coordinates of the snowflake (x,y) 
		- wind - a boolean that lets us know if there is any wind or not.  
	'''

	def __init__(self, size, position, wind=False):
		self.size = size
		self.position = position
		self.wind = wind
		self.color = snow_colors[random.randint(0, len(snow_colors)-1)]

	def fall(self, speed):
		"""
		Take in a integer that represents the speed at which the snowflake is falling in the y-direction.  
		A positive integer will have the snowflake falling down the screen. 
		A negative integer will have the snowflake falling up the screen. 
		
		If wind = True
			the x direction of the snowflake changes
		"""
        # if speed > 0:
		self.position[1] += speed # position is (x,y) which is a list so to change the y coordinate, you need the second element (index) of the list
		if self.wind == True:
			self.position[0] += speed/2
		
	def draw(self):
		"""
		Uses pygame and the global screen variable to draw the snowflake on the screen
		"""
		global screen 
		global snow_colors
		snow = snow_colors[random.randint(0, len(snow_colors)-1)]
		pygame.draw.circle(screen, snow, self.position, self.size) # comment out if don't want flashing colors
		# pygame.draw.circle(screen, self.color, self.position, self.size) # uncomment if don't want flashing colors

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Speed
speed = 1

#INITIALIZE YOUR SNOWFLAKE HERE! 
snow_list = []
for x in range(5):
	snow_list.append(SnowFlake(random.randint(1,7), [random.randint(0,800), 0]))

# -------- Main Program Loop -----------
while not done:
	# --- Main event loops
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	# --- Game logic should go here

	# --- Screen-clearing code goes here

	# Here, we clear the screen to white. Don't put other drawing commands above this, or they will be erased with this command.

	# If you want a background image, replace this clear with blit'ing the background image.
	screen.blit(image1, [0,0])
	
	# --- Drawing code should go here
	
	# Draw Snowman
	pygame.draw.circle(screen, WHITE, (150, 500), 50) # body
	pygame.draw.circle(screen, WHITE, (150, 430), 40) # body
	pygame.draw.circle(screen, WHITE, (150, 375), 30) # body
	pygame.draw.circle(screen, BLACK, (140, 367), 7) # eyes # moved down for wink
	pygame.draw.circle(screen, WHITE, (140, 372), 7) # wink
	pygame.draw.circle(screen, BLACK, (160, 365), 7) # eyes
	pygame.draw.polygon(screen, ORANGE, [[145,376], [155, 376], [150, 386]], 0) # nose
	pygame.draw.circle(screen, BLACK, (150, 419), 5) # buttons
	pygame.draw.circle(screen, BLACK, (150, 440), 5) # buttons
	pygame.draw.circle(screen, BLACK, (150, 480), 5) # buttons
	pygame.draw.circle(screen, BLACK, (150, 503), 5) # buttons
	pygame.draw.circle(screen, BLACK, (150, 526), 5) # buttons
	pygame.draw.rect(screen, BLACK, (120, 337, 60, 15), 0) # hat
	pygame.draw.rect(screen, BLACK, (130, 312, 40, 40), 0) # hat
	pygame.draw.line(screen, BROWN, (90, 405), (120, 425), 3) # left arm
	pygame.draw.line(screen, BROWN, (179, 425), (209, 405), 3) # right arm
	pygame.draw.line(screen, BROWN, (100, 410), (100, 400), 3) # left finger
	pygame.draw.line(screen, BROWN, (90, 416), (101, 411), 3) # left finger
	pygame.draw.line(screen, BROWN, (200, 400), (200, 410), 3) # right finger
	pygame.draw.line(screen, BROWN, (200, 411), (211, 416), 3) # right finger
	pygame.draw.rect(screen, TURQ, (122, 390, 56, 10), 0) # scarf
	pygame.draw.rect(screen, TURQ, (127, 390, 10, 40), 0) # scarf
	
	# Begin Snow
	z = 0
	for y in snow_list:
		snow_list[z].draw()
		snow_list[z].fall(random.randint(1,15))
		z += 1

	# End Snow
	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
	
	for x in range(5): # draw more snowflakes
		snow_list.append(SnowFlake(random.randint(1,7), [random.randint(0,800), 0]))

	# --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
