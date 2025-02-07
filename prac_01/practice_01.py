"""
get gross pay
TAX_RATE = 12%

net_pay = gross pay - (gross pay * TAX_RATE)
display net_pay

"""
from http.cookiejar import user_domain_match
from tkinter.font import names
from unicodedata import category

# TAX_RATE = 0.12
# gross_pay = float(input("Enter gross pay: "))
# net_pay = gross_pay - (gross_pay * TAX_RATE)
# print(net_pay)

"""
0-4 = baby
5-17 = child
18-65 = adult
66+ = old

"""
# age = int(input("Enter age: "))
# if age < 5:
#     category = "baby"
# elif age < 18:
#     category = "child"
# elif age < 66:
#     category = "adult"
# else:
#     category = " old"
#
# print(f"Your age is {age} and you are a {category}")


"""
get secret_number
  while number != secret_number
  display wrong number message
  get number
display correct number message

"""
# SECRET_NUMBER = 12
# random_number = int(input("Enter number: "))
# while random_number != SECRET_NUMBER:
#     print("Wrong number")
#     random_number = int(input("Enter number: "))
# print("Correct number")


# age = int(input("Enter age: "))
# while age < 0 or age > 120:
#     print("Invalid age")
#     age = int(input("Enter age: "))
# if age < 5:
#     category = "baby"
# elif age < 18:
#     category = "child"
# elif age < 66:
#     category = "adult"
# else:
#     category = " old"
# print(f"Your age is {age} and you are a {category}")

# for i in [2,4,-8,99]:
#     print(i, end=" ")

# NAME = "zaharuddin"
# for i in [NAME]:
#     print(i)

"""
get number of people
for i in number of people
  get age
  
display total age
display average

"""
# number_of_people = int(input("Number of people: "))
# total = 0
# for i in range(number_of_people):
#     age_of_person = int(input("Age: "))
#     total += age_of_person
# average_age = total/number_of_people
#
# print(f"The total ages are {total}")
# print(f"The average is is {average_age}")

"""
total = 0
count = 0

get age
while age != -1:
  total += age
  count += 1
  get age

average_age = total/count

"""

# total = 0
# count = 0
#
# age_of_person = int(input("Enter age: "))
# while age_of_person != -1:
#     total += age_of_person
#     count += 1
#     age_of_person = int(input("Enter age: "))
#
# average_age = total/count
# print(f"Your total is {total}")
# print(f"Average age is {average_age}")



# for i in range(3):
#     for j in range(4):
#         print(i ,"-" ,j)

# for round_number in range(1,4):
#     for player_name in ["Miles", "Emma","Chet"]:
#         print(f"Round {round_number}: {player_name}")
#     print("-------")

# x = 5
# y = 10
# if x <10:
#     if y > 10 and x > 5:
#         print("A")
#     else:
#         print("hey")
# else:
#     print("B")


"""
get number of gifts
get number of students

student gifts = number of gifts/ number of students
gifts left over = num of gifts - student gifts

"""

# num_of_gifts = int(input("Number of gifts:"))
# num_of_students = int(input("Number of students: "))
#
# student_gifts = num_of_gifts // num_of_students
# print(f"Gifts per student: {student_gifts}")
# gifts_left_over = num_of_gifts % num_of_students
# print(f"Gifts left over : {gifts_left_over}")
#

# item_price = int(input("Price of item:"))
# gst_included = input("Is GST included: (y/n) ")
#
# GST_RATE = 0.07
#
# if gst_included == 'y':
#     item_price= item_price + (item_price * GST_RATE)
#
# print(f"Your final price is ${item_price}")
#
#


# user_number = int(input("Number: "))
# for i in range(1,user_number + 1):
#     print(i)
#

# SECRET_NUMBER = 7
#
# random_number = int(input("Number:"))
# while random_number != SECRET_NUMBER:
#     print("Wrong number")
#     random_number = int(input("Number:"))

#input validation
# user_name = input("Name")
# user_salary = int(input("Salary: "))
#
# while user_name == " "


# total_age = 0
# number_of_people = int(input("Number of people: "))
#
# for i in range(number_of_people):
#     age_of_person = int(input("Age: "))
#     total_age += age_of_person
#
# average_age = total_age/number_of_people
# print(average_age)
#
#


for i in range(1,4):
    for j in range(2,10,3):
        print(i, "-", j +i )






