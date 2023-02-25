# Multiple If Statements in Succession

# Now we are going to add another if statement for which we
# ask the user, if they want to take photos while in the rollercoaster.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0 # This 'bill' variable is created so that it calculates the final amount at the end

if(height >= 120):
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if(age < 12):
        bill = 5
        print("Child tickets are $5")
    elif(age <= 18):
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you wanna photo taken? Y or N: ") # here we have created another variable
    if(wants_photo == "Y"): # This is another 'if' statement for another condition
        bill += 3 # bill = bill + 3
    
    print(f"Your final bill is ${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")



# Connect with me on:
# Instagram: instagram.com/coder_partha
# Twitter: twitter.com/hello_partha
# Github: github.com/parthadeori