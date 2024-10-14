import requests
import subprocess

# Your Google Sheets ID (from the URL)
sheet_id = '...'

# Your Google API key
api_key = '...'

# URL to fetch the Google Sheet data
url = f'https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/Sheet1?alt=json&key={api_key}'

# Fetch the Google Sheet data
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Extract the rows of data from the sheet
    rows = data['values']
    
    # First row is assumed to be the header
    headers = rows[0]
    
    # Find the index of the 'Name', 'Phone Number', and 'Message' columns
    name_index = headers.index('Name')
    phone_index = headers.index('Phone Number')
    message_index = headers.index('Message')

    # Iterate over each row (starting from row 2)
    for row in rows[1:]:
        name = row[name_index]
        phone_number = row[phone_index]
        message = row[message_index]
        
        # Print the name, phone number, and message (for logging purposes)
        print(f"Sending message to {name} at {phone_number} with message: {message}")
        
        # Format the WhatsApp address
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
