def round_to_step(value: float, step: float) -> float:
    return (value // step) * step if step else value

def get_symbol_filters(client, symbol: str) -> dict:
    info = client.futures_exchange_info()
    s = next((x for x in info["symbols"] if x["symbol"] == symbol.upper()), None)
    if not s:
        raise ValueError(f"Symbol {symbol} not found on Futures.")
    f = {flt["filterType"]: flt for flt in s["filters"]}
    return {
        "tickSize": float(f["PRICE_FILTER"]["tickSize"]),
        "stepSize": float(f["LOT_SIZE"]["stepSize"]),
        "minQty": float(f["LOT_SIZE"]["minQty"]),
    }

def print_balance(client):
    """Fetch and display USDT Futures account balance."""
    balances = client.futures_account_balance()
    for b in balances:
        if b["asset"] == "USDT":
            balance = b.get("balance", "N/A")
            available = b.get("availableBalance", "N/A")
            withdrawable = b.get("withdrawAvailable", "N/A")  # may not exist in testnet

            print(f"\n Balance Summary (USDT):")
            print(f"   Total Balance: {balance}")
            print(f"   Available Balance: {available}")
            print(f"   Withdrawable: {withdrawable}")
            break
