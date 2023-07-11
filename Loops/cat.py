# for i in range(2):
#     print("meow")

# # 1. While Loop execution in practice.
# while True:
#     x = int(input("Enter the password: "))
#     if x <= 0:
#         print("Please enter a positive number")
#     else:
#         print(f"Your password is {x}")
#         break

# 2. A practical example for while loop used in function

# def main():
#     # Define how many times you want the cat to meow
#     number = get_number()
#     meow(number)

# # now we need to define get_number and meow function


# def get_number():
#     while True:
#         number = int(input("Enter the number: "))
#         if number > 0:

#             # we can still put break here, but we need to return the output of the function later anyway, so just return the variable's value here
#             return number
#         else:
#             print("Please enter a proper number")


# def meow(number):
#     for i in range(number):
#         print("Meow")


# main()


# Print all element of the list

# students = ['Nam', 'Minh', 'Lee']

# for student in students:
#     print(student)

# 3. use loops for dict data type

houses = ['gryffindor', 'gryffindor', 'slytherin']

student_house = {'Nam': 'gryffindor',
                 'Minh': 'gryffindor',
                 'Lee': 'slytherin'}

# 3.1 printing keys from a dict
for student in student_house:
    print(student)

# This for loop will generate only keys (indices)

# 3.2 print both keys and values

for student in student_house:
    print(student, student_house[student], sep=", ")
