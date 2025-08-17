import pandas as pd

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
