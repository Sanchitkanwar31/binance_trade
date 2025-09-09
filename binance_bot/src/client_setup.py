import os
import logging
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")
FUTURES_URL = "https://testnet.binancefuture.com/fapi"

def get_client() -> Client:
    # forces all futures requests (client.futures_*) to go to USDT-M Futures Testnet when we rin client below command../fapi = Futures API path (USDT-M Futures).
    client = Client(API_KEY, API_SECRET, testnet=True)
    client.FUTURES_URL = FUTURES_URL
    logging.info("Binance Futures Testnet client initialized")
    return client
