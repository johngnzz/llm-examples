import requests
import json
import streamlit as st

# URL to send the request to
url = 'https://www.chatbase.co/api/v1/chat'

# Request headers
headers = {
    'accept': 'application/json',
    'content-type': 'application/json',
    'authorization': 'Bearer b89dea28-1595-479c-a3cc-f01629bac4a0'
}

# Request body
body = json.dumps({
    'stream': False,
    'temperature': 0,
    'model': 'gpt-3.5-turbo'
})

# Send the request
response = requests.post(url, headers=headers, data=body)

# Parse the response
response_json = response.json()

# Print the response
st.write(response_json)

