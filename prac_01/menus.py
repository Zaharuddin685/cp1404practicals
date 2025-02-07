"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message

"""

user_name = input("Enter name: ")
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
users_choice = input(">>> ").upper()
while users_choice != "Q":
    if users_choice == "H":
        print(f"Hello {user_name}")
    elif users_choice == "G":
        print(f"Goodbye {user_name}")
    else:
        print("Invalid choice")
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    users_choice = input(">>>").upper()
print("Finished.")
