import requests
import time


BASE_URL = "https://fapi.binance.com"


def get_candles(symbol, interval, limit=100):

    endpoint = "/fapi/v1/klines"

    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    max_retries = 3

    for attempt in range(1, max_retries + 1):

        try:

            response = requests.get(
                BASE_URL + endpoint,
                params=params,
                timeout=10
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException as e:

            print(
                f"⚠️ Binance API request failed "
                f"(attempt {attempt}/{max_retries}): {e}"
            )

            if attempt < max_retries:
                time.sleep(3)

            else:
                raise Exception(
                    f"Binance API failed after {max_retries} attempts"
                )