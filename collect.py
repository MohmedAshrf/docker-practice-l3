import requests
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

facts = []
for i in range(30):
    URL = 'https://catfact.ninja/facts?page=' + str(i)
    try:
        response = requests.get(URL)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        text = json.loads(response.text)
        facts.extend([fact['fact'] for fact in text['data']])
    except requests.exceptions.RequestException as e:
        logging.error(f"Error during API request: {e}")

# Save facts to a file
with open("outfile.txt", "w") as outfile:
    outfile.write("\n".join(facts))
