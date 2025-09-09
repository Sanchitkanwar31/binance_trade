from client_setup import get_client
from logger import logger

client = get_client()

def place_market_order(symbol, side, qty):
    """Place a MARKET order on Binance Futures."""
    try:
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": "MARKET",
            "quantity": qty,
        }
        resp = client.futures_create_order(**params)
        logger.info(f" Market Order placed: {resp}")
        return resp
    except Exception as e:
        logger.error(f" Market order failed: {e}")
        return None
