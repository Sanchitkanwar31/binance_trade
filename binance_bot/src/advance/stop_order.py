from client_setup import get_client
from logger import logger

client = get_client()

def place_stop_limit_order(symbol, side, qty, stop_price, limit_price, tif="GTC"):
    """Place a STOP-LIMIT order on Binance Futures."""
    try:
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": "STOP",  # Stop-Limit in Futures
            "quantity": qty,
            "stopPrice": str(stop_price),
            "price": str(limit_price),
            "timeInForce": tif,
        }
        resp = client.futures_create_order(**params)
        logger.info(f" Stop-Limit Order placed: {resp}")
        return resp
    except Exception as e:
        logger.error(f" Stop-Limit order failed: {e}")
        return None
