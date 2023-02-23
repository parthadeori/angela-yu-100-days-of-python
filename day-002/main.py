# [Interactive Coding Exercise] Life in Weeks

# Create a program using maths and f-Strings that tells us how many days, weeks and months we have
# left if we live until 90 years old.

# The program will take our current age as the input and output a message with our time left
# in this format: "You have x days y weeks and z months left",
# where x, y and z are replaced with the actual calculated numbers.

age = int(input("Enter your age: "))

years_remaining = 90 - age

days_remaining = years_remaining * 365 # We take 365 days in a year
weeks_remaining = years_remaining * 52 # We take 52 weeks in a year
months_remaining = years_remaining * 12 # 12 months in a year

message = f"You have {days_remaining} days {weeks_remaining} weeks and {months_remaining} months left"

print(message)



# Connect with me on:
# Instagram: instagram.com/coder_partha
# Twitter: twitter.com/hello_partha
# Github: github.com/parthadeori