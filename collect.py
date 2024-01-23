import requests
import json

facts = []
for i in range(30):
  URL = 'https://catfact.ninja/facts?page='+str(i)
  response = requests.get(URL)
  text= json.loads(response.text)
  facts.extend([fact['fact'] for fact in text['data']])


with open("outfile.txt", "w") as outfile:
  outfile.write("\n".join(facts))

