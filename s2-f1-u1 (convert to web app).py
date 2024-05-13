from flask import Flask, render_template, request, redirect, url_for

import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
todo_file = os.path.join(basedir, 'todo_list.txt')

todo_list = []

#
# F2-U2 Step 1
# https://github.com/microsoft/EveryoneCanCode-US/blob/main/Track_1_ToDo_App/Sprint-01%20-%20Basic%20Application/Feature%202%20-%20Save%20To-Do%20List/User%20Story%202%20-%20Load%20To-Do%20List%20from%20File.md#updating-the-code-base-for-new-functionality
#

# load the to-do list from a file
try:
    with open(todo_file, "r") as file:
        for line in file:
            todo_list.append(line.strip())
except FileNotFoundError:
    print("No existing to-do list found.")

# # continue to loop and display menu until the user selects to exit the program
# while True:
#     print() # add a couple of blank lines
#     print()
#     print("To-do list: ") # print the title of the list
#     for i, todo in enumerate(todo_list, start=1): # loop through existing to-do items with item number
#         print(f"{i}. {todo}") # print item number and todo item

#     # Print the menu
#     print() # add a blank line
#     print("Actions:")
#     print("A - Add to-do item")
#     print("R - Remove to-do item")
#     print("X - Exit")
#     choice = input("Enter your choice (A, R, or X): ")
#     choice = choice.upper() # converts the choice to uppercase

#     # user selected 'a' or 'A' to add an item to the list
#     if choice == "A":
#         todo = input("Enter the to-do item: ") 
#         todo_list.append(todo)
#         continue  # tells the program to go back to the start of the loop
#         # user selected 'r' or 'R' to remove an item from the list

#     if choice == "R":
#         item_number = input("Enter the item number to remove: ")
#         try:
#             item_number = int(item_number)
#             if item_number >= 1 and item_number <= len(todo_list):
#                 todo_list.pop(item_number - 1)
#                 continue  # tells the program to go back to the start of the loop
#             else:
#                 print("Invalid item number")
#         except ValueError:
#             print("Invalid item number")

#     # user selected 'x' or 'X' to exit the program
#     if choice == "X":
#         # save the to-do list to a file
#         #**********THIS CODE ****************
#         with open("todo_list.txt", "w") as file:
#             for todo in todo_list:
#                 file.write(f"{todo}\n")
#         #************************************
#         break

#     # user selected something else
#     print("Invalid choice")

@app.route("/")
def index():
    return render_template("s2-f1-u1.html", todo_list=todo_list)

if __name__ == "__main__":
    app.run(debug=True)

