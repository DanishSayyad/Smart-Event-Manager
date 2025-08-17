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
