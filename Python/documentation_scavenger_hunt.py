# Documentation Scavenger Hunt / Bouncing Ball
# 07/07/2016

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
GREY = (127, 127, 127)
random_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# WRITE YOUR CODE HERE
pygame.init()

x = 350
y = 250
dx = random.randint(-10,10) # how fast/direction of x
dy = random.randint(-10,10) # how fast/direction of y
r = random.randint(20,80)

# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here
	screen.fill(GREEN) # Here, we clear the screen to white. Don't put other drawing commands above this, or they will be erased with this command.

    # --- Drawing code should go here
	pygame.draw.circle(screen, random_color, (x, y), r) # if want to flash random colors, insert "(random.randint(0,255), random.randint(0,255), random.randint(0,255))" in place of "random_color"
	x += dx
	y += dy
	
	if x < 0 or x > SCREEN_WIDTH:
		dx *= -1
	
	if y < 0 or y > SCREEN_HEIGHT:
		dy *= -1

    # --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

    # --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit
pygame.quit()
exit() # Needed when using IDLE
