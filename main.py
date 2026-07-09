import time
import logging
from datetime import datetime, timezone

from config import COINS, TIMEFRAMES
from binance_api import get_candles
from rsi_calculator import calculate_rsi
from alert_engine import AlertEngine
from message_builder import build_message
from telegram_sender import send_telegram


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)


engine = AlertEngine()


print("=" * 50)
print("🚀 Crypto RSI Scanner Started")
print(f"Monitoring {len(COINS)} coins...")
print("=" * 50)


while True:

    alerts_sent = 0

    print("\nStarting new scan...\n")

    for symbol in COINS:

        print("=" * 40)
        print(f"Coin: {symbol}")
        print("=" * 40)

        for timeframe in TIMEFRAMES:

            try:

                candles = get_candles(symbol, timeframe)

                rsi = calculate_rsi(candles)

                price = float(candles[-1][4])

                print(f"{timeframe} RSI: {rsi}")

                alert = engine.process(
                    symbol,
                    timeframe,
                    rsi
                )

                logger.info(
                    f"{symbol} {timeframe} alert status: {alert}"
                )

                if alert:

                    message = build_message(
                        alert_type=alert,
                        symbol=symbol,
                        timeframe=timeframe,
                        rsi=rsi,
                        price=price
                    )

                    print(message)

                    send_telegram(message)

                    alerts_sent += 1

            except Exception as e:

                logger.error(
                    f"Error scanning {symbol} {timeframe}: {e}"
                )

        print()

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    print("=" * 50)
    print(f"✅ Scan complete: {alerts_sent} alerts sent")
    print(f"🕒 {now}")
    print("⏳ Waiting 30 seconds...")
    print("=" * 50)

    time.sleep(30)