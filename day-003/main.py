# Logical Operators

# Allow us to check multiple conditions on the same line of code.
# There are three Logical Operators: and, or, not

# 'and' - Returns True if both statements are true
a = 12
print(a > 15 and a > 10) # This will print False
print(a > 10 and a < 15) # This will print True

# 'or' - Returns True if one of the statements is true
print(a > 15 or a > 10) # This will print True
print(a > 15 or a > 17) # This will print False

# 'not' - Reverse the result, returns False if the result is true
print(not(a > 16)) # This will print True
print(not(a > 15 or a < 20)) # This will print False

##################################################################

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if(height >= 120):
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if(age < 12):
        print("People under 12 years should pay $5")
    elif(age <= 18):
        print("People under 12-18 years should pay $7.")
    elif(age >= 45 and age <= 55): # Logical Operator Condition added
        print("You get a free ride.")
    else:
        print("People over 18 years should pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")



# Connect with me on:
# Instagram: instagram.com/coder_partha
# Twitter: twitter.com/hello_partha
# Github: github.com/parthadeori