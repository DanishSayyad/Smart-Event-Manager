from user import *

# Loads the events data from csv
def eventLoad():
    return pd.read_csv("data/events.csv")

class Event:
    def __init__(self, event_id=0, name=None, date=None, time=None, duration=None, event_type=None, location=None):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.time = time
        self.duration = duration
        self.event_type = event_type
        self.location = location
        self.attendees = []

class EventManager:
    def __init__(self):
        self.userData = userLoad()
    
    # Returns true if the entered credentials are found
    def login(self):
        clearScreen()
        creds = takeCreds()
        userData = userLoad()

        if userLook(creds, userData):
            user = userData[
                (userData["username"] == creds["username"]) &
                (userData["password"] == creds["password"])
            ].iloc[0]

            self.user = User(user["name"], user["username"], user["email"], user["password"], user["admin"])

            if self.user.admin:
                self.events = self.fillEvents(1)
            else:
                self.events = self.fillEvents(0)

            clearScreen()
            print("Hello ", self.user.name, "! Press Enter to start session...", sep = "")
            input()

            return True
        
        return False
    
    def signup(self):
        clearScreen()
        print("User Sign Up")
        info = takeInfo()

        # Check for existing username or email
        exists = (
            (self.userData["username"] == info["username"]) |
            (self.userData["email"] == info["email"])
        )

        if self.userData[exists].shape[0] > 0:
            return False
        
        new_row = pd.DataFrame([info])
        self.userData = pd.concat([self.userData, new_row], ignore_index=True)
        self.userData.to_csv("data/users.csv", index=False)
        return True
    
    def fillEvents(self, admin=1):
        eventData = eventLoad()
        if not admin:
            # Only include events where the user's name is in the attendees list
            eventData = eventData[eventData['attendees'].str.contains(self.user.name, na=False)]
        events = []
        for _, row in eventData.iterrows():
            event = Event(
                event_id=row["ID"],
                name=row["name"],
                date=row["date"],
                time=row["time"],
                duration=row["duration"],
                event_type=row["type"],
                location=row["location"]
            )
            # Split attendees by '|'
            if 'attendees' in row and pd.notna(row['attendees']):
                event.attendees = [att.strip() for att in row['attendees'].split('|')]
            events.append(event)
        return events

    # Displays the record
    def display_events(self):
        if not hasattr(self, 'events') or not self.events:
            print("No events scheduled!")
            return

        for event in self.events:
            attendees = ", ".join(event.attendees) if event.attendees else "None"
            print(
                f"\n{event.date}: {event.time}\n"
                f"Event: {event.name} ({event.event_type})\n"
                f"By: {attendees}"
            )
    
    def session(self):
        if self.user.admin:
            while True:
                clearScreen()
                adminMenu()
                userChoice = takeChoice()

                match userChoice:
                    case 1:
                        pass

                    case 2:
                        clearScreen()
                        print("--- All Events ---")
                        
                        if not self.events:
                            print("No events scheduled!")
                        else:
                            self.display_events()

                        input("\nPress Enter to continue...")

                    case 9:
                        break;

                    case _:
                        print("Invalid choice, press Enter to continue...")
                        input()

        else:
            while True:
                clearScreen()
                userMenu()
                userChoice = takeChoice()

                match userChoice:
                    case 2:
                        clearScreen()
                        print("--- All Events ---")
                        
                        if not self.events:
                            print("No events scheduled!")
                        else:
                            self.display_events()

                        input("\nPress Enter to continue...")

                    case 3:
                        self.events = self.fillEvents(0)

                    case 5:
                        break

                    case _:
                        print("Invalid choice, press Enter to continue...")
                        input()

        # Updating userdata at logout
        # self.userData = userLoad()
                            