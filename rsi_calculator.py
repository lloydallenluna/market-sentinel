import pandas as pd
from ta.momentum import RSIIndicator


def calculate_rsi(candles):

    # candles is a LIST from Binance
    closes = [float(candle[4]) for candle in candles]

    df = pd.DataFrame(closes, columns=["close"])

    rsi = RSIIndicator(close=df["close"], window=14)

    return round(rsi.rsi().iloc[-1], 2)