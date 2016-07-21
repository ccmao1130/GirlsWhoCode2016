# Text Adventure
# 07/01/2016

start = "You wake up one morning and find that you aren't in your bed; you aren't even in your room. \nYou're in the middle of a giant maze. \nA sign is hanging from the ivy: \"You have one hour. Don't touch the walls.\" \nThere is a hallway to your right and to your left."

print(start)
print()
answer = False

while answer == False:
	print("Type 'left' to go left or 'right' to go right.")
	left_right = input()
	print()

	if left_right == "left":
		answer = True
		answer2 = False
		while answer2 == False: # second while loop for second option
			print("You chose to go left and you run into a troll. Type 'fight' to fight the troll or 'run' to run away.")
			fight_run = input()
			print()
		
			if fight_run == "fight":
				answer2 = True
				print("You chose to fight the troll. The troll hits you on the head and you die.")
		
			elif fight_run == "run":
				answer2 = True
				print("You chose to run away. The troll laughs as you run away like a baby.")
		
			else:
				answer2 = False # loops back to line with user's options if user's input is not one of the options
				print("Please type one of the choices.")

	elif left_right == "right":
		answer = True
		answer3 = False
		while answer3 == False: # second while loop for second option
			print("You chose to go right and you walk up to a river. Type 'yes' if you want to swim across or 'no' if you want to stay.")
			swim = input()
			print()
		
			if swim == "yes":
				answer3 = True
				print("You chose to swim across the river, but the current is too strong and you die.")

			elif swim == "no":
				answer3 = True
				print("You chose to stay and not swim across. You sit down next to the river and take a nap.")
			
			else:
				answer3 = False # loops back to line with user's options if user's input is not one of the options
				print("Please type one of the choices.")
			
	else:
		answer = False # loops back to line with user's options if user's input is not one of the optionss
		print("Please type one of the choices.")
		
print("\nEnd of story.")
