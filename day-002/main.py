# Day 2 Project: Tip Calculator

print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $")) # Eg. bill = $150

tip = int(input("What percentage tip would you like to give? 10, 12 or 15: ")) # Eg. tip = 10

people = int(input("How many people to split the bill? ")) # Eg. people = 5

tip_as_percent = tip / 100 # 10/100 = 0.1
total_tip_amount = bill * tip_as_percent # 150 * 0.1 = 15
total_bill = bill + total_tip_amount # 150 + 15 = 165

bill_per_person = total_bill/people # 165/5 = 33

final_amount = round(bill_per_person, 2) # This will round off to 2 decimal places
final_amount = "{:.2f}".format(bill_per_person) # This will format bill_per_person to 2 decimal places

print(f"Each person should pay: ${final_amount}")



# Connect with me on:
# Instagram: instagram.com/coder_partha
# Twitter: twitter.com/hello_partha
# Github: github.com/parthadeori