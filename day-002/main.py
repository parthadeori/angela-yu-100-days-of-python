# Number Manipulation and F Strings in Python

# Rounding off floating point number
# i.e., if the number is 2.3 we round it off to 2 and if it's 2.7 we round it off to 3.

# In Python, we can round off floating point numbers by using round() function.

print(8/3) # This will print 2.66666666

print(round(8/3)) # This will round off and print 3

# To round off decimal places, we do it like this:
print(round(8/3, 2)) # This will round off to 2 decimal places, so it will print 2.67

print('---------------------')

# Floor division (//) - Converts floating point number into integer without using int() function
# We can do floor division by using (//)

print(8 / 3) # This will print 2.6666666
print(8 // 3) # This will print 2

print("---------------------")


# Formatting floating point numbers
print("Format method format()")
price = 49
format_price = "{:.2f}".format(price) # "{:.xf}".format(); where x is the number of places to format
print(format_price) # This will print 49.00

print('-----------------------f-String-----------------------------')

# f-Strings
# This is used to mix up or concatenate different data types.

# Without f-String
name = "John"
age = 14

print("Hello, my name is " + name + " and I am " + str(age) + " years old.")

print('---------------------')

# With f-String
name = "Peter"
age = 16

print(f"Hello, my name is {name} and I am {age} years old.")

# To use f-String, use f before the start of the quotation. Now, inside the quotation,
# we add the curly braces, inside which we will type the variable names. 

# We can also execute Python codes inside the curly braces, with the help of f-String.

print(f"2 + 3 + 4 = {2+4+5}") # This will print: 2 + 4 + 5 = 11



# Connect with me on:
# Instagram: instagram.com/coder_partha
# Twitter: twitter.com/hello_partha
# Github: github.com/parthadeori