import requests

url = "https://fapi.binance.com/fapi/v1/klines"

params = {
    "symbol": "BTCUSDT",
    "interval": "15m",
    "limit": 5
}

response = requests.get(url, params=params)
data = response.json()

for candle in data:
    open_time = candle[0]
    open_price = candle[1]
    high = candle[2]
    low = candle[3]
    close = candle[4]

    print(f"O:{open_price} H:{high} L:{low} C:{close}")