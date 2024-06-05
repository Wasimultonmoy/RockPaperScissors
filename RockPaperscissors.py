import random
import os

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

print("-----------------------------Welcome To Rock Paper Scissors Game--------------------------------------------")

print("Rules of this game: ")
print("1. Rock wins against scissors.\n2. Scissors win against paper.\n3. Paper wins against rock.")

input("So, Press any key to start the game....")
os.system('cls' if os.name == 'nt' else 'clear')

print("What do you want to choose: ")
print("1. Rock\n2. Paper\n3. Scissors")
usrChoice = int(input("Enter your choice (1, 2, or 3): "))

if usrChoice < 1 or usrChoice > 3:
    print("Invalid Input")
    exit()  # Exit the program for invalid input

# User Choice
if usrChoice == 1:
    usrChoiceName = rock
elif usrChoice == 2:
    usrChoiceName = paper
elif usrChoice == 3:
    usrChoiceName = scissors

# Computer Choice
computerChoice = random.randint(1, 3)
if computerChoice == 1:
    computerChoiceName = rock
elif computerChoice == 2:
    computerChoiceName = paper
else:
    computerChoiceName = scissors

print("Computer chose:")
print(computerChoiceName)
print("You chose:")
print(usrChoiceName)

# Winning Condition
if usrChoice == computerChoice:
    print("It's a tie!")
elif (usrChoice == 1 and computerChoice == 3) or \
     (usrChoice == 2 and computerChoice == 1) or \
     (usrChoice == 3 and computerChoice == 2):
    print("You win!")
else:
    print("Computer wins!")

print("\n")

input("press any Key to exit")
os.system('cls')