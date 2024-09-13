
import re
from datetime import datetime

def parse_chat_history(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regular expression to match the date-time pattern and message content
    pattern = r'(\d{1,2}/\d{1,2}/\d{2}, \d{1,2}:\d{2}\s*[APM]{2}) - (.+?): (.+?)(?=\n\d{1,2}/\d{1,2}/\d{2}, \d{1,2}:\d{2}\s*[APM]{2} -|\Z)'
    matches = re.findall(pattern, content, re.DOTALL)

    chat_list = []
    for match in matches:
        date_time_str, sender, message = match
        
        # Skip messages containing 'Sticker', 'Call', or 'emoji'
        if any(keyword in message for keyword in ['Sticker', 'Call', 'emoji']):
            continue
        
        # Convert date-time string to datetime object
        date_time = datetime.strptime(date_time_str, '%m/%d/%y, %I:%M %p')
        
        chat_list.append({
            'timestamp': date_time,
            'sender': sender.strip(),
            'message': message.strip()
        })

    # Sort the list by timestamp
    chat_list.sort(key=lambda x: x['timestamp'])

    return chat_list

# Usage
file_path = 'chat_history/Austin.txt'
sorted_chat_history = parse_chat_history(file_path)

# Print the sorted chat history (for demonstration purposes)
for entry in sorted_chat_history:
    print(f"{entry['timestamp']} - {entry['sender']}: {entry['message']}")
