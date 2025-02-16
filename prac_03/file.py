
# Question 1.
# Ask the user for their name
# name = input("Enter your name: ")
#
# # Open the file name.txt for writing and write the name
# file = open("name.txt", "w")
# file.write(name)
# file.close()
#
# print("Your name has been saved to name.txt.")



# # Question 2.
# file = open("name.txt", "r")
# name = file.readline().strip()  # Read the name and remove any trailing newline
# file.close()
#
# print(f"Hi {name}!")

# Question 3.
# with open("numbers.txt", "r") as file:
#     num1 = int(file.readline())
#     num2 = int(file.readline()) #pythons internal cursor automatically moves to the next line in the file
#
# result = num1 + num2
# print(result)


# Question 4.
# total = 0
# with open("numbers.txt", "r") as file:
#     for line in file:
#         total += int(line.strip())
# print(f"Total: {total}")




