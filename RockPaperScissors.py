import random
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

# Write your code below this line 👇

print("************************************************************************")
print("*       WELCOME TO THE 'ROCK', 'PAPER', 'SCISSORS' TOURNAMENT!!!.      *")
print("************************************************************************")

choice = input("What do you choose? Type '0' for Rock, '1' for Paper, '2' for Scissors\n")
game_image = [rock, paper, scissors]

player_choice = int(choice)
print(game_image[player_choice])
computer_choice = random.randint(0, 2)
print("computer choice:")
print(computer_choice)
print(game_image[computer_choice])

if (computer_choice == 0) and (player_choice == 1):
    print("You win!")

elif (computer_choice == 1) and (player_choice == 2):
    print("You win!")

elif (computer_choice == 2) and (player_choice == 0):
    print("You win!")

elif computer_choice == player_choice:
    print("Draw")

# elif player_choice > computer_choice:
# print("Your input is invalid")
else:
    print("You lose!")
