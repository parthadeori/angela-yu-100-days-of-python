# [Interactive Coding Exercise] Average Height

# You are going to write a program that calculates the 
# average student height from a List of heights. 

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
    total_height = total_height + height
print(total_height) 

number_of_students = 0
for student in student_heights:
    number_of_students += 1    # number_of_students = number_of_students + 1
print(number_of_students)

average_height = round(total_height/number_of_students)
print(average_height)



# Connect with me on:
# Instagram: instagram.com/coder_partha
# Twitter: twitter.com/CoderPartha
# Github: github.com/parthadeori