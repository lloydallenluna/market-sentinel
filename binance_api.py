import requests

BASE_URL = "https://fapi.binance.com"


def get_candles(symbol, interval, limit=100):

    url = BASE_URL + "/fapi/v1/klines"

    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    response = requests.get(url, params=params)
    data = response.json()

    # 🚨 HARD VALIDATION
    if not isinstance(data, list):
        raise Exception(f"Binance API error for {symbol} {interval}: {data}")

    return data