# Binance Trading Bot

A modular Python trading bot for Binance Futures & Spot markets. Supports **market, limit, and stop-limit orders**, with clean logging, extendable strategies, and a CLI interface.

> ⚠️ *This project is for educational purposes only. Trading involves risk — use at your own discretion.*

---

## Features

* Market, limit, and stop-limit orders
* Continuous CLI trading loop
* Balance tracking with USDT summary
* Centralized logging to `bot.log`
* Modular and extensible (custom strategies)

---

## Project Structure

```
binance_bot/
│── src/
│   ├── main.py               # Main CLI loop
│   ├── client_setup.py       # Binance client setup
│   ├── utils.py              # Balance and helpers
│   ├── logger.py             # Logging config
│   ├── market_order.py       # Market order logic
│   ├── limit_order.py        # Limit order logic
│   ├── stop_limit_order.py   # Stop-limit order logic
│   └── strategies.py         # Extend with custom strategies
│
├── requirements.txt
├── bot.log                   # Log file (auto-created)
└── README.md
```

---

## Setup

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd trade_b
```

### 2. Create Virtual Environment

```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing:

```bash
pip install python-binance
```

### 4. Configure API Keys

Edit `binance_bot/src/client_setup.py` and add your Binance **API\_KEY** and **API\_SECRET**.

---

## Usage

### Run the Bot

```bash
python binance_bot/src/main.py
```

### Place Direct Orders

* Market Order:

  ```bash
  python binance_bot/src/market_order.py
  ```
* Limit Order:

  ```bash
  python binance_bot/src/limit_order.py
  ```
* Stop-Limit Order:

  ```bash
  python binance_bot/src/stop_limit_order.py
  ```

### Logs

* All trades and errors are logged in **bot.log**
* Example entry:

  ```
  2025-09-09 15:30:22 - INFO - Placing LIMIT order: BUY 0.01 BTCUSDT @ 26000
  2025-09-09 15:30:24 - INFO - Order executed successfully: {...}
  ```

---

## Extending the Bot

You can add new strategies in `strategies.py`:

```python
def moving_average_strategy(client, symbol, qty):
    # Example strategy logic
    pass
```

Then import it in `main.py` and call inside the trading loop.

---

## Notes & Disclaimer

* Test first in Binance Testnet before running with real funds.
* Requires Python 3.7+
* Ensure API keys have only necessary permissions.
* Use at your own risk. The authors are not responsible for financial losses.

---

## License

This project is licensed under the **MIT License** — free to use and modify.
