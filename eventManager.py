from creds import *
from utils import clearScreen

class Event:
    def __init__(self, event_id=0, name=None, date=None, time=None, event_type=None, location=None):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.time = time
        self.event_type = event_type
        self.location = location

class EventManager:
    def __init__(self):
        self.userData = userLoad()
    
    # Returns true if the entered credentials are found
    def login(self):
        clearScreen()
        creds = takeCreds()

        if userLook(creds, self.userData):
            user = self.userData[
                (self.userData["username"] == creds["username"]) &
                (self.userData["password"] == creds["password"])
            ].iloc[0]

            self.username = user["username"]
            self.email = user["email"]
            self.admin = user["admin"] == 1
            self.name = user["name"]

            clearScreen()
            print("Hello ", self.name, "! Press Enter to start session...", sep = "")
            input()

            return True
        
        return False
    
    def session(self):
        print("Reached session")