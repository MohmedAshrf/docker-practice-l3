!pip install requests
import requests
from bs4 import BeautifulSoup

URL = 'https://catfact.ninja/facts'



response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

data = soup.select("data")
print(data)
print(data[0][0])

