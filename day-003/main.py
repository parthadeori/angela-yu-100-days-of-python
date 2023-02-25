# [Interactive Coding Exercise] Love Calculator

# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word 'TRUE' occurs. 
# Then check for the number of times the letters in the word 'LOVE' occurs. 
# Then combine these numbers to make a 2 digit number. 

# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is 'x', you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:
# "Your score is 'y', you are alright together."

# Otherwise, the message will just be their score. e.g.:
# "Your score is 'z'."

# Write your code below this line:

name1 = input("Enter your name: ") # Peter
name2 = input("Enter your lover's name: ") # Rose

combined_names = name1 + name2 # PeterRose
lower_case_str = combined_names.lower() # peterrose

t = lower_case_str.count("t") # 1
r = lower_case_str.count("r") # 2
u = lower_case_str.count("u") # 0
e = lower_case_str.count("e") # 3

true = t + r + u + e # 6

l = lower_case_str.count("l") # 0
o = lower_case_str.count("o") # 1
v = lower_case_str.count("v") # 0
e = lower_case_str.count("e") # 3

love = l + o + v + e # 4

love_score = str(true) + str(love) # "6" + "4" = "64"
love_score_int = int(love_score) # 64

# For Love Scores less than 10 or greater than 90
if(love_score_int < 10 or love_score_int > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif(love_score_int >= 40 and love_score_int <= 50): # For Love Scores between 40 and 50
    print(f"Your love score is {love_score}, you are alright together.")
else:
    print(f"Your love score is {love_score}")




# Connect with me on:
# Instagram: instagram.com/coder_partha
# Twitter: twitter.com/hello_partha
# Github: github.com/parthadeori