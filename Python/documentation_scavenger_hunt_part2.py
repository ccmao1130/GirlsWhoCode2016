# Documentation Scavenger Hunt Part 2 / Bubbles
# 07/14/2016

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
BLUE = (0, 115, 237)
ORANGE = (255, 165, 0)
GREY = (129, 129, 129)
TURQ = (0, 237, 203)
LIGHT_BLUE = (189, 246, 255)
SKY_BLUE = (101, 208, 255)
PURPLE = (121, 0, 232)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)
CYAN = (0, 255, 255) # it's like neon blue
colors = [GREEN, RED, BLUE, ORANGE, GREY, TURQ, LIGHT_BLUE, SKY_BLUE, PURPLE, PINK, CYAN]

def random_color():
	return random.choice(colors)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("Documentation Scavenger Hunt Part 2")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

screen.fill(WHITE)

class Circle():
	def __init__(self, mouse_pos):
		self.mouse_pos = list(mouse_pos)
		self.size = random.randint(20, 80) # assigned here so that the size of the circle will not keep changing because if it is assigned in the draw function, it will keep redrawing the circle, so it will keep resizing the circle
		speed = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
		self.color = random_color() # assigned here so that colors will not keep flashing because if it is assigned in the draw function, it will keep redrawing the circle, so it will keep choosing another color
		# self.x = random.randint(-5, 5) # assigned here so that x speed will not keep changing because if it is assigned in the move function, it will keep moving the circle, so it will keep changing the x speed
		# self.y = random.randint(-5, 5) # assigned here so that y speed will not keep changing because if it is assigned in the move function, it will keep moving the circle, so it will keep changing the y speed
		self.x = speed[random.randint(0, len(speed)-1)] # this makes sure that the circles will keep moving because it will not have a x speed of 0
		self.y = speed[random.randint(0, len(speed)-1)] # this makes sure that the circles will keep moving because it will not have a y speed of 0
	
	def draw(self):
		global screen
		pygame.draw.circle(screen, self.color, self.mouse_pos, self.size)
		# pygame.draw.circle(screen, self.color, self.mouse_pos, self.size, 5) # use this line if don't want circles to be filled in
	
	def move(self):
		self.mouse_pos[0] += self.x
		self.mouse_pos[1] += self.y
		
circle_list = []
# for x in range(5):
	# circle_list.append(Circle(mouse_pos))

# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	# --- Game logic should go here
	
	# --- Screen-clearing code goes here

	# Here, we clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.

	# If you want a background image, replace this clear with blit'ing the
	# background image.
	screen.fill(BLACK)
	
	# --- Drawing code should go here
	pressed = pygame.mouse.get_pressed()
	mouse_pos = pygame.mouse.get_pos()
	
	if pressed[0] == 1:
		circle_list.append(Circle(mouse_pos))
		# draw_circle = Circle(mouse_pos)
		# draw_circle.draw()
	
	z = 0
	for x in circle_list:
		circle_list[z].draw()
		circle_list[z].move()
		z += 1
		
	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(30)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
