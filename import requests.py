import requests

# Define the URL of the API endpoint
url = "https://api.coingecko.com/api/v3/coins/"

# Ask user to enter the name or ticker of a cryptocurrency
crypto = input("Enter the name or ticker of a cryptocurrency: ")

# Make a request to the API and retrieve the data
response = requests.get(url + crypto.lower())
data = response.json()

# Extract the required data from the API response
name = data['name']
ticker = data['symbol']
price = data['market_data']['current_price']['usd']
volume = data['market_data']['total_volume']['usd']
price_change = data['market_data']['price_change_percentage_24h']
description = data['description']['en']

# Print the data in a nice format
print(f"Name: {name}")
print(f"Ticker: {ticker}")
print(f"Price: {price}")
print(f"Volume: {volume}")
print(f"Price change (24h): {price_change}%")
print(f"Description: {description}")
