rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#import random libary
import random

#grabs player's input as int
player = int(input("What do you chose? Type 0 for Rock, 1 for Scissors, 2 for Paper:\n"))

#generates random move for the computer player
comp = random.randint(0, 2)

# List for ascii art to be reffered to
game_images = [rock, paper, scissors]

#checks if both values are the same, if so player loses
if player >= 3 or player < 0:
	print(f'''
	You fumbled and make an invalid choice \n \n
	Computer chose:
	{game_images[comp]}\n
	You lose!
	''')
#checks if both values are the same, if so a draw
elif player == comp:
	print(f'''
	{game_images[player]}\n
	Computer chose:
	{game_images[comp]}\n
	It is a draw
	''')
# Checks winning combination Rock vs Scissors for the player
elif player == 0 and comp == 2:
	print(f'''
	{game_images[player]}\n
	Computer chose:
	{game_images[comp]}\n
	You win!
	''')
# Checks winning combination Paper vs Rock for the player
elif player == 1 and comp == 0:
	print(f'''
	{game_images[player]}\n
	Computer chose:
	{game_images[comp]}\n
	You win!
	''')
# Checks winning combination Scissors vs Paper for the player
elif player == 2 and comp == 1:
	print(f'''
	{game_images[player]}\n
	Computer chose:
	{game_images[comp]}\n
	You win!
	''')
# If not a draw or victory for the player it is a win for the computer player
# _values fill ascii art automatically
else:
	print(f'''
	{game_images[player]}\n
	Computer chose:
	{game_images[comp]}\n
	You lose!
	''')
