# Nested if statements and elif statements

# This if/else statement is inside the 'if' statement block.
# If a condition is True, Python will check for the if/else statement inside the 'if' block of code.
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if(height >= 120):
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if(age <= 18): # Nested if/else statement start from here in this case.
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")



# Connect with me on:
# Instagram: instagram.com/coder_partha
# Twitter: twitter.com/hello_partha
# Github: github.com/parthadeori