# Day 14 Project: Higher Lower Game

from art import logo, vs
from game_data import data
import random

def format_data(account):
    """
    Takes the account data and returns the printable format.
    """
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """
    Take the user guess and follower counts and return if they got it right.
    """

print(logo)

account_a = random.choice(data)
account_b = random.choice(data)

if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}")
print(vs)
print(f"Against B: {format_data(account_a)}")

guess = input("Who has more followers? Type 'A' or 'B': ").lower()

a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]