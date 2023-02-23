# Type Error, Type Checking and Type Conversion

# len() function doesn't work with integers.
# print(len(123)) # This will give an error of TypeError

print(len("123")) 
# This will print 3 because it has 3 characters 
# but the position of characters will start from 0.

print('--------------------')

# Data Type Checking
# We can check type of data by using the type() function

print(type(123)) # This will print <class 'int'> which means integer
print(type("Hello123")) # This will print <class 'str'> which means string
print(type(23.8)) # This will print <class 'float'> which means float
print(type(True)) # This will print <class 'bool'> which means boolean

print('---------------------')

# Data Types Conversion
# We cannot concatenate string and integers. To concatenate string with integers,
# We have to convert either one of them. 
# To convert integer to string, we can use the str() function
a = 123
print(type(a)) # This will print <class 'int'>
a = str(123)
print(type(a)) # This will print <class 'str'>

print('---------------------')


# To convert string to integer, we can use the int() function
b = "456"
print(type(b)) # This will print <class 'str'>
b = int("456")
print(type(b)) # This will print <class 'int'>

print('---------------------')

# Let's use str() and int() function to concatenate string and integers.

num_char = len(input("What is your name? ")) 
# This will print the number of characters of the user's name
# This is of class int

num_char_str = str(num_char) 
# We converted the class int to class str by using str() function
# Now, num_char_str holds the value as str

print("Your name has " + num_char_str + " characters")
# We have concatenate strings and integers by converting integers to strings.
# Enter your name in the console to check the result.

# The below code will give an error.
# num_char = len(input("What is your name? "))
# print("Your name has " + num_char + " characters.")

print('---------------------')

# We can convert string like "123" or integers to float by using float() function



# Connect with me on:
# Instagram: instagram.com/coder_partha
# Twitter: twitter.com/hello_partha
# Github: github.com/parthadeori