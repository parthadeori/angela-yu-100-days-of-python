# [Interactive Coding Exercise] Banker Roulette - Who will pay the bill?

# You are going to write a program which will select a random 
# name from a list of names. The person selected will have to 
# pay for everybody's food bill. Use the random module.

import random

name_string = input("Give me everybody's names, separated by a comma. ")
names = name_string.split(", ")

num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today.")


# Connect with me on:
# Instagram: instagram.com/coder_partha
# Twitter: twitter.com/hello_partha
# Github: github.com/parthadeori