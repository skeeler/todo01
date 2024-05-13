todo_list = []

#
# F1-U1 Step 1
# https://github.com/microsoft/EveryoneCanCode-US/blob/main/Track_1_ToDo_App/Sprint-01%20-%20Basic%20Application/Feature%201%20-%20Manage%20Todo%20List/User%20Story%201%20-%20Add%20Item%20to%20List.MD#2-create-the-apppy-application-file
#
# todo_list.append("Buy milk")
# todo_list.append("Learn more about Azure")
# todo_list.append("Complete first Python project")
# for todo in todo_list:
#     print(todo)

#
# F1-U1 Step 2
# https://github.com/microsoft/EveryoneCanCode-US/blob/main/Track_1_ToDo_App/Sprint-01%20-%20Basic%20Application/Feature%201%20-%20Manage%20Todo%20List/User%20Story%201%20-%20Add%20Item%20to%20List.MD#update-the-application-to-be-interactive
#
# continue to loop and display menu until the user selects to exit the program
while True:
    print() # add a couple of blank lines
    print()
    print("To-do list: ") # print the title of the list
    for todo in todo_list: # loop through existing to-do items
        print(todo)

    # Print the menu
    print() # add a blank line
    print("Actions:")
    print("A - Add to-do item")
    print("X - Exit")
    choice = input("Enter your choice (A or X): ")
    choice = choice.upper() # converts the choice to uppercase

    # user selected 'a' or 'A' to add an item to the list
    if choice == "A":
        todo = input("Enter the to-do item: ") 
        todo_list.append(todo)
        continue  # tells the program to go back to the start of the loop

    # user selected 'x' or 'X' to exit the program
    if choice == "X":
        break # tells the program to exit the loop

    # user selected something else
    print("Invalid choice")

