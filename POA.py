import requests
import subprocess
from datetime import datetime

# Your Google Sheets ID (from the URL)
sheet_id = '...'  # Replace with your sheet ID

# Your Google API key
api_key = '...'  # Replace with your API key

# URL to fetch the Google Sheet data
url = f'https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/Sheet1?alt=json&key={api_key}'

# Fetch the Google Sheet data
response = requests.get(url)

# Get today's date in the desired format
today = datetime.now().strftime("%d-%m-%Y (IST), %A")

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Extract the rows of data from the sheet
    rows = data['values']
    
    # First row is assumed to be the header
    headers = rows[0]
    
    # Find the index of the required columns
    name_index = headers.index('Name')
    plan_index = headers.index('Plan')
    start_date_index = headers.index('Plan Start Date')
    end_date_index = headers.index('Plan End Date')
    completed_sessions_index = headers.index('Completed Sessions')
    total_sessions_index = headers.index('Total Sessions')
    workout_index = headers.index('Workout')

    # Iterate over each row (starting from row 2)
    for row in rows[1:]:
        name = row[name_index]
        plan = row[plan_index]
        plan_start_date = row[start_date_index]
        plan_end_date = row[end_date_index]
        completed_sessions = row[completed_sessions_index]
        total_sessions = row[total_sessions_index]
        workout = row[workout_index]
        
        # Prepare the message with the custom format
        message = f"""
*Plan of Action*

- 📅 *Date*: {today}
- 👤 *Name*: {name}
- 📝 *Plan*: {plan}
- ⏳ *Plan Start Date*: {plan_start_date}
- 🏁 *Plan End Date*: {plan_end_date}
- 🔢 *No. of Completed Sessions*: {completed_sessions}/{total_sessions}
- 🍽️ *Meal photos received*: 0/3
- 💪 *Workout of the Day*: {workout}
        """
        
        # Format the WhatsApp address
        phone_number = row[headers.index('Phone Number')]
        whatsapp_address = f"{phone_number}@s.whatsapp.net"
        
        # Command to execute, now including the custom message
        command = f"./sender send {whatsapp_address} '{message}'"
        
        # Execute the command
        try:
            subprocess.run(command, shell=True, check=True)
            print(f"Message sent to {whatsapp_address}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to send message to {whatsapp_address}. Error: {e}")
else:
    print(f"Failed to fetch data: {response.status_code}")
