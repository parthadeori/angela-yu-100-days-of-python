# Understanding the Offset and Appending Items to Lists

fruits = ["apple", "cherry", "pear", "banana", "orange"]
print(fruits)

print(fruits[0]) # This will return 'apple'
print(fruits[1]) # This will return 'cherry'
print(fruits[2]) # This will return 'pear'

print(fruits[-1]) # This will return the last item from the list, i.e., 'orange'
print(fruits[-2]) # This will return 'banana'

print(len(fruits)) # This will return 5

# We can replace an item in the list by specifying its position
fruits[2] = "pineapple" # Pear is replaced with Pineapple
print(fruits)

# We can add a new item to our list by using .append() function
fruits.append("dragonfruit")
print(fruits)

# We can add a new list inside our fruits list by using .extend() function
fruits.extend(["mango", "strawberry", "plum"])
print(fruits)



# Connect with me on:
# Instagram: instagram.com/coder_partha
# Twitter: twitter.com/hello_partha
# Github: github.com/parthadeori