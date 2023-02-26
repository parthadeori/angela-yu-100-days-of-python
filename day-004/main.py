# [Interactive Coding Exercise] Treasure Map

# You are going to write a program which will mark a spot with an X. The map is made of 3 rows of blank squares,

#      1     2    3
# 1 ['⬜','⬜','⬜']
# 2 ['⬜','⬜','⬜']
# 3 ['⬜','⬜','⬜']

# Your program should allow you to enter the position of the treasure using a two-digit system. 
# The first digit is the horizontal 'column' number and the second digit is the vertical 'row' number. 

# Example Output 1: column 2, row 3 would be entered as: 23
# ['⬜','⬜','⬜']
# ['⬜','⬜','⬜']
# ['⬜','X','⬜']
# 
# Example Input 2: column 3, row 1 would be entered as: 31 
# Example Output 2:
# ['⬜','⬜','X']
# ['⬜','⬜','⬜']
# ['⬜','⬜','⬜']


# SOLUTION
row1 = ['⬜', '⬜', '⬜'] # First list    [11, 21, 31]
row2 = ['⬜', '⬜', '⬜'] # Second list   [12, 22, 32]
row3 = ['⬜', '⬜', '⬜'] # Third list    [13, 23, 33]

map = [row1, row2, row3] # Lists inside list

print(f"{row1}\n{row2}\n{row3}")
print('''
[11, 21, 31] 
[12, 22, 32]
[13, 23, 33]
''')

position = input("Where do you want to put 'X'? Enter any number from the list ") # '23'

horizontal = int(position[0]) # 2
vertical = int(position[1]) # 3

selected_row = map[vertical - 1] # map[3 - 1] = map[2] = row3
selected_row[horizontal - 1] = "X" # row3[2 - 1] = row3[1] = 23
# This will replaced that position's block with an 'X'

# map[vertical - 1][horizontal - 1] = "X"  # Short version

print(f"{row1}\n{row2}\n{row3}")


# Connect with me on:
# Instagram: instagram.com/coder_partha
# Twitter: twitter.com/hello_partha
# Github: github.com/parthadeori