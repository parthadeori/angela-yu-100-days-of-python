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

# elif Statement - If we have multiple 'if' statements, then we use the 'elif' statements.

#'elif' statements required condition to be passed on.
# We can add many 'elif' statements we want.
# In this case, we are using 'elif' statement nested inside the 'if' statement.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if(height >= 120): # If this condition is True, this 'if' block code will execute.
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if(age < 12): # If 'age' is less than 12, this code block will execute.
        print("People under 12 years should pay $5")
    elif(age <= 18): # If 'age' is lesser or equal to 18, then this code will execute. 
        print("People under 12-18 years should pay $7.")
    else: # If 'age' is 19 or more, then this code will execute
        print("People over 18 years should pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")



# Connect with me on:
# Instagram: instagram.com/coder_partha
# Twitter: twitter.com/hello_partha
# Github: github.com/parthadeori