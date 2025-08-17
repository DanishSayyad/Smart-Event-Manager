import pandas as pd

# Loads the user data from csv
def userLoad():
    return pd.read_csv("data/users.csv")

# Returns a dictionary of user credentials
def takeCreds():
    print("User Login")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    return {"username": username, "password": password}

# Verifies username and password
def userLook(creds, userData):
    username = creds.get("username")
    password = creds.get("password")
    match = userData[
        (userData["username"] == username) & (userData["password"] == password)
    ]
    return not match.empty