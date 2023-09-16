import requests

base_url = "https://www.reuters.com/markets/quote/USDEUR=X/"

payload = {}
Healders = {}

response = requests.request("GET", base_url)
if response.status_code == 200:
    rates_data = response.json()
    print(rates_data)
else:
    print(f"Request failed with status code {response.status_code}")

