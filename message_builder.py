from datetime import datetime, UTC

# Starts at 1 and increases every alert.
alert_id = 1


def build_message(alert_type, symbol, timeframe, rsi, price):

    global alert_id

    reason_map = {
        "WATCH_OVERBOUGHT": "Approaching Overbought Zone",
        "CONFIRMED_OVERBOUGHT": "Entered Overbought Zone",
        "WATCH_OVERSOLD": "Approaching Oversold Zone",
        "CONFIRMED_OVERSOLD": "Entered Oversold Zone",
    }

    icon_map = {
        "WATCH_OVERBOUGHT": "🟠",
        "CONFIRMED_OVERBOUGHT": "🔴",
        "WATCH_OVERSOLD": "🟡",
        "CONFIRMED_OVERSOLD": "🟢",
    }

    title_map = {
        "WATCH_OVERBOUGHT": "RSI WATCH",
        "CONFIRMED_OVERBOUGHT": "RSI CONFIRMED",
        "WATCH_OVERSOLD": "RSI WATCH",
        "CONFIRMED_OVERSOLD": "RSI CONFIRMED",
    }

    message = f"""#{alert_id:06}

{icon_map[alert_type]} {title_map[alert_type]}

Coin: {symbol}
Timeframe: {timeframe}

RSI: {rsi:.2f}
Price: {price:,.2f}

Reason:
{reason_map[alert_type]}

{datetime.now(UTC).strftime('%Y-%m-%d %H:%M UTC')}
"""

    alert_id += 1

    return message