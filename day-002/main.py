# [Interactive Coding Exercise] BMI Calculator

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is calculated with the given formula: BMI = weight / (height * height); 
# where weight is in kg and height is in metre.

weight = float(input("Enter your weight in kg: ")) # can be int(), doesn't really matter
height = float(input("Enter your height in metre: ")) # has to be float() as user will enter the height in decimal

BMI = weight / (height ** 2)

bmi_as_whole = int(BMI) # This will convert floating number into whole number

print("Your BMI is " + str(bmi_as_whole))



# Connect with me on:
# Instagram: instagram.com/coder_partha
# Twitter: twitter.com/hello_partha
# Github: github.com/parthadeori