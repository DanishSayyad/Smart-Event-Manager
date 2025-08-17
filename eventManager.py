from user import *
from events import *

class EventManager:
    def __init__(self):
        self.userData = userLoad()
        self.timeline = dict()
    
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
            
            self.updateTimeline()

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

    # Print indivisual event
    def displayEvent(self, event):
        attendees = ", ".join(event.attendees) if event.attendees else "None"
        print(
            f"\nID: {event.event_id}"
            f"\n{event.date}: {event.time}\n"
            f"Event: {event.name} ({event.event_type})\n"
            f"By: {attendees}"
        )

    # Displays the record
    def display_events(self):
        if not hasattr(self, 'events') or not self.events:
            print("No events scheduled!")
            return

        for event in self.events:
            self.displayEvent(event)
    
    # Function to update the csv file for events
    def updateEvents(self):
        data = []
        for event in self.events:
            data.append({
                "ID": event.event_id,
                "name": event.name,
                "date": event.date,
                "time": event.time,
                "duration": event.duration,
                "type": event.event_type,
                "location": event.location,
                "attendees": "|".join(event.attendees)
            })
        df = pd.DataFrame(data, columns=["ID", "name", "date", "time", "duration", "type", "location", "attendees"])
        df.to_csv("data/events.csv", index=False)
    
    # Tells if day is free
    def dayAvailable(self, date_str, duration):
        # Ensure timeline is updated
        if date_str not in self.timeline:
            # No events scheduled yet → whole day is free
            return duration <= 24

        day_slots = self.timeline[date_str]  # e.g. "000001110000..."
        
        # Sliding window check for continuous "0"s
        for start in range(0, 24 - duration + 1):
            if all(slot == '0' for slot in day_slots[start:start+duration]):
                return True
        
        return False

    # Tells if time slots are free
    def isConflict(self, date_str, start_time, duration):
        start_hour = int(datetime.strptime(start_time, "%H:%M").hour)
        if date_str not in self.timeline:
            return True  # No events, so no conflict

        timeline_str = self.timeline[date_str]
        for h in range(start_hour, min(start_hour + duration, 24)):
            if timeline_str[h] == '1':
                # Find the conflicting event time
                conflict_start = h
                conflict_end = h
                # Expand to full block of conflict
                while conflict_start > 0 and timeline_str[conflict_start-1] == '1':
                    conflict_start -= 1
                while conflict_end < 23 and timeline_str[conflict_end+1] == '1':
                    conflict_end += 1
                print(f"Conflict with event from {conflict_start:02d}:00 to {conflict_end+1:02d}:00 on {date_str}.")
                return False
        return True

    # Deletes event by ID
    def deleteEvent(self, event_id):
        for i, event in enumerate(self.events):
            if event.event_id == event_id:
                del self.events[i]
                self.updateEvents()
                print(f"Event with ID {event_id} deleted successfully.")
                return
        print(f"Event with ID {event_id} not found")

    # Searches event by name
    def searchElement(self, keyword):
        found = False
        for event in self.events:
            if keyword.lower() in event.name.lower():
                self.displayEvent(event)
                found = True
                break
        if not found:
            print(f"No event found with keyword '{keyword}'.")

    def session(self):
        if self.user.admin:
            while True:
                clearScreen()
                adminMenu()
                userChoice = takeChoice()

                match userChoice:
                    case 1:
                        clearScreen()
                        print("--- Add Event ---")

                        while True:
                            name = get_non_blank("Enter event name: ")
                            if any(event.name.lower() == name.lower() for event in self.events):
                                print("Event name already exists! Please enter a different name.")
                            else:
                                break
                        event_type = get_non_blank("Enter event type: ")
                        location = get_non_blank("Enter event location: ")

                        # Duration input (must be integer and non-empty)
                        while True:
                            duration_str = get_non_blank("Enter event duration (in hours): ")
                            try:
                                duration = int(duration_str)
                                if duration > 0:
                                    break
                                else:
                                    print("Duration must be a positive integer.")
                            except ValueError:
                                print("Duration must be an integer.")

                        # Date input and validation
                        while True:
                            date = get_non_blank("Enter event date (DD/MM/YYYY): ")
                            if validDate(date):
                                if not self.dayAvailable(date, duration):
                                    print("The event cannot be scheduled on this date, choose another one.")
                                    input("Press Enter to continue...")
                                    continue
                                break
                            else:
                                print("Invalid date. Please enter today or a future date in DD/MM/YYYY format.")

                        # Time input and validation
                        while True:
                            time = get_non_blank("Enter event time (HH:MM): ")
                            if date == datetime.today().strftime("%d/%m/%Y"):
                                if futureTime(time):
                                    if self.isConflict(date, time, duration):
                                        break
                                else:
                                    print("Time must be in the future for today's date.")
                            else:
                                # Accept any valid time format for future dates
                                try:
                                    datetime.strptime(time, "%H:%M")
                                    if self.isConflict(date, time, duration):
                                        break
                                except ValueError:
                                    print("Invalid time format. Please use HH:MM.")

                        # Generate new event ID (simply using count+1)
                        event_id = f"E{len(self.events)+1}"

                        # Create and add event
                        new_event = Event(event_id, name, date, time, duration, event_type, location)
                        attendees_list = []
                        while True:
                            print("\nAttendees:")
                            print(", ".join(attendees_list) if attendees_list else "None")
                            attendeeMenu()
                            choice = takeChoice()
                            if choice == 1:
                                username = no_spaces("Enter attendee username to add: ")
                                user_row = self.userData[self.userData["username"] == username]
                                if not user_row.empty:
                                    attendee_name = user_row.iloc[0]["name"]
                                    if attendee_name not in attendees_list:
                                        attendees_list.append(attendee_name)
                                    else:
                                        print("Attendee already added.")
                                else:
                                    print("Username not found.")
                            elif choice == 2:
                                username = no_spaces("Enter attendee username to remove: ")
                                user_row = self.userData[self.userData["username"] == username]
                                if not user_row.empty:
                                    attendee_name = user_row.iloc[0]["name"]
                                    if attendee_name in attendees_list:
                                        attendees_list.remove(attendee_name)
                                    else:
                                        print("Attendee not in the list.")
                                else:
                                    print("Username not found.")
                            elif choice == 3:
                                if not len(attendees_list):
                                    print("Attendees must be added!")
                                    continue
                                break
                            else:
                                print("Invalid choice.")
                        new_event.attendees = attendees_list
                        self.events.append(new_event)

                        self.updateEvents()
                        self.updateTimeline()

                        print("\nEvent added successfully!")
                        input("Press Enter to continue...")

                    case 2:
                        clearScreen()
                        print("--- All Events ---")
                        
                        if not self.events:
                            print("No events scheduled!")
                        else:
                            self.display_events()

                        input("\nPress Enter to continue...")
                    
                    case 5:
                        clearScreen()
                        id = input("Enter event id to be deleted: ").capitalize()
                        self.deleteEvent(id)

                        input("\nPress Enter to continue...")
                    
                    case 6:
                        clearScreen()
                        key = input("Enter keyword: ")
                        self.searchElement(key)
                        input("\nPress Enter to continue...")

                    case 9:
                        break;

                    case _:
                        print("Invalid choice, press Enter to continue...")
                        input()

        # Normal user
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
    
    def updateTimeline(self):
        self.timeline = dict()
        for event in self.events:
            date_str = event.date
            time_str = event.time
            duration = int(event.duration)

            start_hour = int(datetime.strptime(time_str, "%H:%M").hour)

            # Initialize timeline for the date if not present
            if date_str not in self.timeline:
                self.timeline[date_str] = ['0'] * 24

            # Mark event hours as '1' for the current day
            for h in range(start_hour, min(start_hour + duration, 24)):
                self.timeline[date_str][h] = '1'

            # If event goes past midnight, mark hours for the next day
            if start_hour + duration > 24:
                next_day = (datetime.strptime(date_str, "%d/%m/%Y") + timedelta(days=1)).strftime("%d/%m/%Y")
                if next_day not in self.timeline:
                    self.timeline[next_day] = ['0'] * 24
                for h in range(0, (start_hour + duration) - 24):
                    self.timeline[next_day][h] = '1'

        # Convert lists to binary strings
        for date in self.timeline:
            self.timeline[date] = ''.join(self.timeline[date])
                            