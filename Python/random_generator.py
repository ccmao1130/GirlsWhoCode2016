# Random Generator
# 07/06/2016

import random
import time # for program to wait

# Menu

adj = ["Spicy ", "Sweet ", "Sour ", "Fresh ", "Salty ", "Crunchy ", "Greasy "]
food = ["Chicken ", "Beef ", "Bacon ", "Soup ", "Noodles ", "Pasta ", "Shrimp "]
style = ["Marinated ", "Boiled ", "Roasted ", "Fried ", "Grilled ", "Poached ", "Braised "]

menu = [
"1. " + adj[random.randint(0,6)] + style[random.randint(0,6)] + food[random.randint(0,6)], 
"2. " + adj[random.randint(0,6)] + style[random.randint(0,6)] + food[random.randint(0,6)],
"3. " + adj[random.randint(0,6)] + style[random.randint(0,6)] + food[random.randint(0,6)],
"4. " + adj[random.randint(0,6)] + style[random.randint(0,6)] + food[random.randint(0,6)],
"5. " + adj[random.randint(0,6)] + style[random.randint(0,6)] + food[random.randint(0,6)], 
"6. " + adj[random.randint(0,6)] + style[random.randint(0,6)] + food[random.randint(0,6)],
"7. " + adj[random.randint(0,6)] + style[random.randint(0,6)] + food[random.randint(0,6)],
"8. " + adj[random.randint(0,6)] + style[random.randint(0,6)] + food[random.randint(0,6)],
"9. " + adj[random.randint(0,6)] + style[random.randint(0,6)] + food[random.randint(0,6)],
"10. " + adj[random.randint(0,6)] + style[random.randint(0,6)] + food[random.randint(0,6)]
]

print("Menu: ")
for i in range(10):
	print(menu[i])

time.sleep(3)

# Band Name

adverb = ["Miserably ", "Godly ", "Lively ", "Needy ", "Tremendously "]
adj2 = ["Fierce ", "Spooky ", "Happy ", "Ordinary ", "Enchanting "]
noun = ["Gorillas ", "Elephants ", "Rhinos ", "Cheese ", "Bananas "]

print("\nYour band name is: ")
print(adverb[random.randint(0,4)] + adj2[random.randint(0,4)] + noun[random.randint(0,4)])

time.sleep(3)

# Haiku

syllables5 = ["Cherry blossoms bloom", "Explode into night", "The warmth on my skin", "I see the sun set", "Summer here again", "And life is renewed"]
syllables7 = ["Softly falling from the tree", "Fire falls beneath the trees", "Music plays sweetly, drifting"]

print("\nHaiku: ")
for i in range(3):
	print(syllables5[random.randint(0,5)] + ", ")
	print(syllables7[random.randint(0,2)] + ", ")
	print(syllables5[random.randint(0,5)] + ". ")
	print()
	
time.sleep(4)

# Haiku - Extra Mile: multiple haikus

answer2 = False
while answer2 == False:
	print("Do you want more haikus? (yes/no) ")
	more = input()
	more = more.lower()
	if more == "yes":
		answer2 = False
		print("\nHere's another haiku...")
		for i in range(3):
			print(syllables5[random.randint(0,5)] + ", ")
			print(syllables7[random.randint(0,2)] + ", ")
			print(syllables5[random.randint(0,5)] + ". ")
			print()
		time.sleep(4)
	else:
		answer2 = True
		print("\nFine. I won't bother you with more haikus.")
		
time.sleep(3)

# Menu - Extra Mile: Hang Man

possible = ["girl", "code", "computer", "scratch", "python"]
word = possible[random.randint(0,4)]
answer = False
tries = 3

print("\nWelcome to Hang Man!")
print("Your possible guesses are: ")
for i in range(len(possible)):
	print(possible[i])
print("\nYou have 3 tries to guess the right word.")
while answer == False:
	print("What word would you like to guess?")
	guess = input()
	guess = guess.lower()
	if guess == word:
		answer = True
		print("\nYou guessed right!")
	else:
		tries = tries - 1
		if tries == 1: # just for grammatical reasons
			print("\nGuess again! You have " + str(tries) + " try left.")
		elif tries == 0:
			answer = True
			print("\nGame over! \nYou have no tries left. \nThe correct word was: " + word)
		else:
			print("\nGuess again! You have " + str(tries) + " tries left.")

time.sleep(2)
