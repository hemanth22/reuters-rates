import requests
import json

# URL of the Reuters page with the data
url = "https://www.reuters.com/markets/quote/USDEUR=X/"

# Send an HTTP GET request to the URL
response = requests.get(url)

data = response.content.decode('utf-8')
