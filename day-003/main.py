# [Interactive Coding Exercise] BMI 2.0

# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height. 
# It should tell them the interpretation of their BMI based on the BMI value. 

# 1. Under 18.5 they are 'underweight' 
# 2. Over 18.5 but below 25 they have a 'normal weight' 
# 3. Over 25 but below 30 they are 'overweight' 
# 4. Over 30 but below 35 they are 'obese' 
# 5. Above 35 they are 'clicnically obese'

# Round the result to it's nearest whole number.

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

BMI = round(weight/(height**2), 2)

if(BMI < 18.5):
    print(f"Your BMI is {BMI}. You are underweight.")
elif(BMI < 25):
    print(f"Your BMI is {BMI}. You have a normal weight.")
elif(BMI < 30):
    print(f"Your BMI is {BMI}. You are overweight.")
elif(BMI < 35):
    print(f"Your BMI is {BMI}. You are obese.")
else:
    print(f"Your BMI is {BMI}. You are clinically obese.")



# Connect with me on:
# Instagram: instagram.com/coder_partha
# Twitter: twitter.com/hello_partha
# Github: github.com/parthadeori