from utils import *
from eventManager import EventManager

def welcome():
    clearScreen()
    print("--- Smart Event Manager ---")
    print("1. Login")
    print("2. Signup")
    print("3. Exit")

def main():

    manager = EventManager()

    while(True):
        welcome()
        choice = takeChoice()
        match(choice):
            case 1:
                if(manager.login()):
                    manager.session()
                else:
                    print("Invalid credentials, press Enter to try again")
                    input()
            case 2:
                # signup()
                pass
            case 3:
                break
            case _:
                print("Invalid choice, press enter to try again")
                input()

if __name__ == "__main__":
    main()
