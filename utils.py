import os
import platform

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
    while(True):
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