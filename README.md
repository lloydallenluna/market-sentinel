# Market Sentinel

An automated cryptocurrency market monitoring system that analyzes Binance Futures data and delivers real-time RSI-based trading alerts through Telegram.

Market Sentinel demonstrates the development of an event-driven automation workflow involving API integration, technical indicator processing, alert logic, and automated notifications.

---

## Overview

Market Sentinel continuously monitors selected cryptocurrency pairs across multiple timeframes and evaluates market conditions using the Relative Strength Index (RSI).

When predefined RSI thresholds are reached, the system automatically generates and delivers alerts through Telegram, allowing users to monitor potential market opportunities without manually checking charts.

---

## Key Features

- Binance Futures API integration
- Automated cryptocurrency market monitoring
- Multi-coin and multi-timeframe analysis
- RSI-based market condition detection
- Telegram notification automation
- Custom alert engine with state tracking
- Watch and confirmed signal classification
- Duplicate alert prevention
- Secure environment variable management
- Modular Python architecture

---

## System Architecture

```text
Binance Futures API
        |
        ↓
Market Data Collection
        |
        ↓
RSI Calculation Engine
        |
        ↓
Alert Decision Engine
        |
        ↓
Message Generation
        |
        ↓
Telegram Notification
```

---

## How It Works

1. Market data is retrieved from the Binance Futures API.

2. Historical candle data is processed and RSI values are calculated across multiple timeframes.

3. The alert engine evaluates RSI conditions.

### Oversold Conditions

- RSI below or equal to 30: Confirmed Oversold
- RSI between 30 and 35: Oversold Watch

### Overbought Conditions

- RSI above or equal to 70: Confirmed Overbought
- RSI between 65 and 70: Overbought Watch

4. When a condition is triggered, the system generates a formatted alert.

5. The alert is automatically delivered through Telegram.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Binance Futures API | Real-time cryptocurrency market data |
| Pandas | Data processing and manipulation |
| Technical Analysis Library | RSI indicator calculation |
| Telegram Bot API | Automated notifications |
| Git/GitHub | Source control and project management |

---

## Project Structure

```text
market-sentinel/

├── main.py
├── config.py
├── binance_api.py
├── rsi_calculator.py
├── alert_engine.py
├── message_builder.py
├── telegram_sender.py

├── tests/
│   ├── candles_test.py
│   ├── market_test.py
│   └── telegram_test.py

├── requirements.txt
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/lloydallenluna/market-sentinel.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_chat_id
```

Run the application:

```bash
python main.py
```

---

## Example Alert

```text
RSI CONFIRMED

Coin: LABUSDT
Timeframe: 1h

RSI: 28.70
Price: 1.16

Reason:
Entered Oversold Zone
```

---

## Future Improvements

Potential enhancements include:

- Web-based monitoring dashboard
- Historical signal database
- Performance analytics
- Cloud deployment
- Machine learning-based market classification
- Advanced risk management features

---

## Author

Lloyd Allen Luna

GitHub:
https://github.com/lloydallenluna