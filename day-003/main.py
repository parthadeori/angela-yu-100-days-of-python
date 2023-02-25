# [Interactive Coding Exercise] Leap Year

# Write a program that works out whether if a given year is a leap year. 

year = int(input("Enter a year: "))

# EXPLANATORY VERSION - Comment the simple version to try this.

if(year % 4 == 0):
    print(f"{year} is clearly divisible by 4. (Leap year). Checking second condition...")
    if(year % 100 == 0):
        print(f"{year} is not divisible by 100 clearly. (Not a leap year). Checking final condition...")
        if(year % 400 == 0):
            print(f"{year} is finally divided by 400 clearly. (Leap year).")
            print(f"So, {year} is a Leap year.")
        else:
            print(f"{year} is not divisible by 400. (Not a leap year).")
            print(f"Hence, {year} is not a leap year")
    else:
        print(f"The second condition is omitted since {year} is not divisible by 100 clearly.")
        print(f"Hence, {year} is a Leap year.")
else:
    print(f"{year} is not divisible by 4. So, {year} is Not a leap year.")


## SIMPLE VERSION WITHOUT EXPLANATION - Comment the explanatory version to try this.

# if(year % 4 == 0):
#     if(year % 100 == 0):
#         if(year % 400 == 0):
#             print("Leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not a leap year.")



# Connect with me on:
# Instagram: instagram.com/coder_partha
# Twitter: twitter.com/hello_partha
# Github: github.com/parthadeori