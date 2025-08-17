import pandas as pd
from utils import *

class User:
    def __init__(self, name, username, email, password, admin):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.admin = admin == 1

# Loads the user data from csv
def userLoad():
    return pd.read_csv("data/users.csv")

# Returns a dictionary of user credentials
def takeCreds():
    print("User Login")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    return {"username": username, "password": password}

def takeInfo():
    name = get_non_blank("Enter name: ")
    username = no_spaces("Enter username: ")
    email = get_non_blank("Enter email: ")
    password = get_non_blank("Enter password: ")
    admin = ask("Are you an admin? (y/n): ")
    return {
        "name": name,
        "username": username,
        "email": email,
        "password": password,
        "admin": int(admin)
    }

# Verifies username and password
def userLook(creds, userData):
    username = creds.get("username")
    password = creds.get("password")
    match = userData[
        (userData["username"] == username) & (userData["password"] == password)
    ]
    return not match.empty