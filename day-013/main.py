# Reproduce the Bug - Solution

# Instead of random number between 1 to 6, we changed the randint
# function from 0 to 5.

from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])



# Connect with me on:
# Instagram: instagram.com/coder_partha
# Twitter: twitter.com/CoderPartha
# Github: github.com/parthadeori