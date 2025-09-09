
from client_setup import get_client
from logger import logger

client = get_client()

def place_limit_order(symbol, side, qty, price, tif="GTC"):
    """Place a LIMIT order on Binance Futures."""
    try:
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": "LIMIT",
            "timeInForce": tif,
            "quantity": qty,
            "price": str(price),
        }
        resp = client.futures_create_order(**params)
        logger.info(f" Limit Order placed: {resp}")
        return resp
    except Exception as e:
        logger.error(f" Limit order failed: {e}")
        return None
