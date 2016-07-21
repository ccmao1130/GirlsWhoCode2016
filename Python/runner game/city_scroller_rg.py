# City Scroller - Runner Game
# 07/15/2016

import pygame
import random

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Building():
	def __init__(self, x_point, y_point, width, height, color):
		self.x_point = x_point
		self.y_point = y_point
		self.width = width
		self.height = height
		self.color = color
		
	def draw(self):
		# global screen
		pygame.draw.rect(screen, self.color, (self.x_point, self.y_point, self.width, self.height), 0)

	def move(self, speed):
		self.x_point += speed

class Scroller(object):
	def __init__(self, width, height, base, color, speed):
		self.width = width
		self.height = height
		self.base = base
		self.color = color
		self.speed = speed
		self.building_list = []

	def add_buildings(self):
		x = 0
		while x < self.width:
			x += self.add_building(x)

	def add_building(self, x_location):
		global SCREEN_HEIGHT
		m = random.randint(self.height, self.base)
		building = Building(x_location, m, 120, SCREEN_HEIGHT-m, self.color)
		self.building_list.append(building)
		return 120

	def draw_buildings(self):
		for i in self.building_list:
			i.draw()
		
	def move_buildings(self):
		for i in self.building_list:
			i.move(self.speed)
