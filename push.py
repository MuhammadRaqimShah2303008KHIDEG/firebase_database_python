import firebase_admin
from firebase_admin import credentials, db
import time
from datetime import datetime

# Initialize Firebase with your credentials and database URL
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://test-3b45c-default-rtdb.firebaseio.com/"})

# Get a reference to the Firebase Realtime Database
ref = db.reference('/')
counter = 0  # Corrected variable name

# Continuously add data
while counter < 6:
    # Your data to be added
    if counter >=3:
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = {
            "Alert": "ATM is not Working",
            "timestamp": time_now
        }
        
        

        # Push data to the database
        ref.push(new_data)
    else: 
        print("Counter is less")
    counter += 1  # Corrected variable name
    time.sleep(1)  # Add a sleep to control the rate of data addition

print("Data added 6 times.")
