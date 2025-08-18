import os
import platform
import pandas as pd
from datetime import datetime, timedelta

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
    print("8. Check Mails")
    print("9. Clear Mails")
    print("10. Logout")

# User menu
def userMenu():
    clearScreen()
    print("1. View Events")
    print("2. View All Events")
    print("3. Refresh Events")
    print("4. Check Mails")
    print("5. Clear Mails")
    print("6. Logout")

# Attendee menu
def attendeeMenu():
    print("1. Add attendee")
    print("2. Remove attendee")
    print("3. Stop")

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


# Returns True if date_str is a valid date and is today or in the future.
def validDate(date_str, date_format="%d/%m/%Y"):
    try:
        input_date = datetime.strptime(date_str, date_format).date()
        today = datetime.today().date()
        return input_date >= today
    except ValueError:
        return False

# Returns True if time_str is ahead of current system time (today).
def futureTime(time_str, time_format="%H:%M"):
    try:
        input_time = datetime.strptime(time_str, time_format).time()
        now_time = datetime.now().time()
        return input_time > now_time
    except ValueError:
        return False

def getDuration():
    while True:
        duration_str = get_non_blank("Enter event duration (in hours): ")
        try:
            duration = int(duration_str)
            if duration > 0:
                return duration
            else:
                print("Duration must be a positive integer.")
        except ValueError:
            print("Duration must be an integer.")

# Validates time
def validTime(time_str):
    try:
        datetime.strptime(time_str.strip(), "%H:%M")
        return True
    except ValueError:
        return False

def get_time(prompt="Enter time (HH:MM): "):
    while True:
        t = get_non_blank(prompt)
        if validTime(t):
            return t
        print("Invalid time. Use HH:MM (24-hour).")
