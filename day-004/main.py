# Day 4 Project: Rock, Paper, Scissors

import random

game_data = ["✊ (rock)", "🖐️ (paper)", "✌️ (scissors)"]

print("Welcome to Rock, Paper, Scissors")
user_choice = input("What do you want to choose? Type 0 for ✊, 1 for 🖐️  and 2 for ✌️.\n")

if(int(user_choice) != 0 and int(user_choice) != 1 and int(user_choice) != 2):
    print("Invalid input.")  
else:
    print(f"You chose: {game_data[int(user_choice)]}")

    computer_choice = random.randint(0, 2)
    print(f"Computer chose: {game_data[computer_choice]}")

    if(int(user_choice) == computer_choice):
        print("It's a draw.")
    elif(int(user_choice) == 0 and computer_choice == 1):
        print("You lose.")
    elif(int(user_choice) == 0 and computer_choice == 2):
        print("You win.")
    elif(int(user_choice) == 1 and computer_choice == 0):
        print("You win.")
    elif(int(user_choice) == 1 and computer_choice == 2):
        print("You lose.")
    elif(int(user_choice) == 2 and computer_choice == 0):
        print("You lose.")
    elif(int(user_choice) == 2 and computer_choice == 1):
        print("You win.")



# Connect with me on:
# Instagram: instagram.com/coder_partha
# Twitter: twitter.com/hello_partha
# Github: github.com/parthadeori