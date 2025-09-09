
from market_order import place_market_order
from limit_order import place_limit_order
from advance.stop_order import place_stop_limit_order
from utils import print_balance
from logger import logger
from client_setup import get_client

client = get_client()

def place_order():
    """Take user input and place an order."""
    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    side = input("Enter side [BUY/SELL]: ").upper()
    order_type = input("Enter order type [MARKET/LIMIT/STOP_LIMIT]: ").upper()
    qty = float(input("Enter quantity: "))

    logger.info(f"Placing {order_type} order: {side} {qty} {symbol}")

    try:
        if order_type == "MARKET":
            resp = place_market_order(symbol, side, qty)

        elif order_type == "LIMIT":
            price = float(input("Enter limit price: "))
            resp = place_limit_order(symbol, side, qty, price)

        elif order_type == "STOP_LIMIT":
            stop_price = float(input("Enter stop price: "))
            limit_price = float(input("Enter limit price: "))
            resp = place_stop_limit_order(symbol, side, qty, stop_price, limit_price)

        else:
            print(" Invalid order type")
            return

        if resp:
            logger.info(f" Order executed: {resp}")
            print("\n Order executed successfully!")
        else:
            logger.error(" Order failed")
            print("\n Order failed (check logs).")

    except Exception as e:
        logger.exception(f"Error while placing order: {e}")
        # print(f"\n Error: {e}")

def main():
    """Main loop for continuous CLI bot."""
    print("\n=== Binance Futures CLI Bot ===")
    logger.info("Bot started")

    while True:
        print_balance(client)
        print("\n--- Menu ---")
        print("1. Place new order")
        print("2. Exit")

        choice = input("Choose an option [1/2]: ").strip()
        if choice == "1":
            place_order()
        elif choice == "2":
            logger.info("Bot stopped by user")
            print(" Exiting bot. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
