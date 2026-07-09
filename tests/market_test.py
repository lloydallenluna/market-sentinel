import requests

url = "https://fapi.binance.com/fapi/v1/ticker/price?symbol=BTCUSDT"

response = requests.get(url)
data = response.json()

print("BTCUSDT price:", data["price"])