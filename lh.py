import requests
import json

# URL of your Flask app (change if deployed)
url = 'http://127.0.0.1:8081/analyze'

# Sample email text to analyze
sample_email_text = "This is a sample email text for TF-IDF analysis."

# Prepare the data payload
payload = {'email_text': sample_email_text}

# Send POST request
response = requests.post(url, json=payload)

# Check if the request was successful
if response.status_code == 200:
    print("TF-IDF Analysis Results:")
    print(json.dumps(response.json(), indent=4))
else:
    print(f"Error: Unable to get a response. Status code: {response.status_code}")