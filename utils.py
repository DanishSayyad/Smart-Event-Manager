import os
import platform

# Initial menu
def welcome():
    clearScreen()
    print("--- Smart Event Manager ---")
    print("1. Login")
    print("2. Signup")
    print("3. Exit")

# Admin menu
def adminMenu():
    clearScreen()
    print("1. Add Event")
    print("2. Display All Events")
    print("3. View Events")
    print("4. Edit Event")
    print("5. Delete Event")
    print("6. Search Event")
    print("7. Remind Attendees")
    print("8. Account Setting")
    print("9. Logout")

# User menu
def userMenu():
    clearScreen()
    print("1. View Events")
    print("2. View All Events")
    print("3. Refresh Events")
    print("4. Account Setting")
    print("5. Logout")

# Clears the screen on any OS
def clearScreen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Takes from user numeric choice
def takeChoice():
    try:
        return int(input("Enter choice: ").strip())
    except ValueError:
        return -1

# Yes or No question
def ask(question):
    while True:
        answer = input(question).lower()
        if answer not in ('y', 'n'):
            continue
        else:
            return answer == 'y'

# Get a non blank entry
def get_non_blank(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Entry cannot be blank. Please try again.")

def no_spaces(prompt="Enter username: "):
    while True:
        username = input(prompt).strip()
        if " " in username or not username:
            print("Username cannot contain spaces or be blank. Please try again.")
        else:
            return username