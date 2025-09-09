import pandas as pd
import ta

def rsi_signal(df: pd.DataFrame):
    rsi = ta.momentum.RSIIndicator(df['Close']).rsi()
    if rsi.iloc[-2] < 30 and rsi.iloc[-1] > 30:
        return "BUY"
    elif rsi.iloc[-2] > 70 and rsi.iloc[-1] < 70:
        return "SELL"
    return None
