# Smart Event Manager

A comprehensive command-line event management system built in Python that allows users to create, manage, and track events with an integrated mail notification system. The application supports both admin and regular user roles with different levels of access and functionality.

## Features

### 🔐 **User Management**
- **User Registration & Login**: Secure signup and login system
- **Role-Based Access Control**: Separate admin and regular user interfaces
- **User Profile Management**: Store user information with admin privileges

### 📅 **Event Management**
- **Create Events**: Add new events with detailed information (name, date, time, duration, type, location)
- **View Events**: Display all events or filter by specific dates
- **Edit Events**: Modify existing event details including attendees
- **Delete Events**: Remove events from the system
- **Search Events**: Find events by keyword matching
- **Conflict Detection**: Automatic scheduling conflict prevention

### 👥 **Attendee Management**
- **Add/Remove Attendees**: Manage event participants by username
- **Attendee Validation**: Verify attendees exist in the user database
- **Automatic Notifications**: Send reminder emails to all attendees

### 📧 **Mail System**
- **Mail Viewing**: Check received mails in the system
- **Professional Templates**: Well-formatted reminder emails

### ⏰ **Smart Scheduling**
- **Timeline Management**: 24-hour timeline tracking for each day
- **Conflict Resolution**: Prevent double-booking and scheduling conflicts
- **Past Event Filtering**: Automatically hide expired events
- **Duration Management**: Support for multi-hour events

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pandas library

### Clone and Run

1. **Clone the repository**:
```bash
git clone <repository-url>
cd smart-event-manager
```

2. **Install required dependencies**:
```bash
pip install pandas
```

3. **Ensure data directory exists**:
```bash
mkdir data
```

4. **Initialize CSV files** (if not present):
   - Create `data/users.csv`, `data/events.csv`, and `data/mails.csv`
   - Sample data files are provided in the repository

5. **Run the application**:
```bash
python main.py
```

## How to Use

### First Time Setup

1. **Run the application**: `python main.py`
2. **Create an admin account**: Choose option 2 (Signup) and select 'y' when asked if you're an admin
3. **Login**: Use your credentials to access the system

### Sample User Accounts (from provided data)
- **Admin**: Username: `danish100`, Password: `DanishAdmin`
- **Regular User**: Username: `jay315`, Password: `JayNormal`

## Feature Usage Guide

### 🔑 **Admin Features**

#### **1. Add Event**
```
1. Login as admin
2. Select "1. Add Event"
3. Enter event details:
   - Event name: "Team Meeting"
   - Event type: "Meeting"  
   - Location: "Conference Room A"
   - Duration: 2 (hours)
   - Date: 25/08/2025
   - Time: 14:00
4. Add attendees by username
5. Event is created and saved
```

#### **2. Edit Event**
```
1. Select "4. Edit Event"
2. Enter event ID: E1
3. Choose what to edit:
   - Name, Type, Location, Duration, Date, Time, or Attendees
4. Make changes and select "8. Done"
```

#### **3. Delete Event**
```
1. Select "5. Delete Event"
2. Enter event ID to delete: E2
3. Event is permanently removed
```

#### **4. Search Events**
```
1. Select "6. Search Event"
2. Enter keyword: "meeting"
3. All events containing "meeting" are displayed
```

#### **5. Send Reminders**
```
1. Select "7. Remind Attendees"
2. System automatically sends emails to all event attendees
3. Confirmation message shows number of mails sent
```

### 👤 **Regular User Features**

#### **1. View Your Events**
```
1. Login as regular user
2. Select "1. View Events"
3. Choose:
   - "1" for today's events
   - "2" for specific date events
```

#### **2. Check Mails**
```
1. Select "4. Check Mails"
2. All reminder emails are displayed
```

## Sample CLI Workflow

### Creating and Managing an Event (Admin)

```bash
$ python main.py

--- Smart Event Manager ---
1. Login
2. Signup  
3. Exit
Enter choice: 1

User Login
Enter username: danish100
Enter password: DanishAdmin

Hello Danish Sayyad! Press Enter to start session...

1. Add Event
2. Display All Events
3. View Events
4. Edit Event
5. Delete Event
6. Search Event
7. Remind Attendees
8. Check Mails
9. Logout
Enter choice: 1

--- Add Event ---
Enter event name: Python Workshop
Enter event type: Workshop
Enter event location: Lab 101
Enter event duration (in hours): 3
Enter event date (DD/MM/YYYY): 28/08/2025
Enter event time (HH:MM): 10:00

Attendees:
None
1. Add attendee
2. Remove attendee
3. Stop
Enter choice: 1
Enter attendee username to add: jay315

Attendees:
Jayvardhan Gaikwad
1. Add attendee
2. Remove attendee
3. Stop
Enter choice: 3

Event added successfully!
```

### Viewing Events (Regular User)

```bash
$ python main.py

Enter choice: 1
Enter username: jay315
Enter password: JayNormal

1. View Events
2. View All Events
3. Refresh Events
4. Check Mails
5. Logout
Enter choice: 2

--- All Events ---

ID: E1
20/08/2025: 16:00
Event: Learn AI (Workshop)
By: Danish Sayyad, Janvi Maharnawar
```

## File Structure

```
smart-event-manager/
├── main.py              # Entry point
├── eventManager.py      # Core event management logic
├── events.py           # Event class and data loading
├── user.py             # User management and authentication
├── mails.py            # Mail system functionality
├── utils.py            # Utility functions and menus
└── data/
    ├── users.csv       # User database
    ├── events.csv      # Events database
    └── mails.csv       # Mail records
```

## Key Features in Detail

### **Conflict Detection System**
The system maintains a 24-hour timeline for each day, preventing scheduling conflicts by:
- Tracking occupied time slots
- Validating new event times against existing bookings
- Providing clear conflict messages with specific times

### **Role-Based Access Control**
- **Admins**: Full CRUD operations on events, user management, mail system access
- **Regular Users**: View-only access to their assigned events, mail checking

### **Data Persistence**
All data is stored in CSV files for easy backup and portability:
- User information and credentials
- Complete event details with attendees
- User Mail system