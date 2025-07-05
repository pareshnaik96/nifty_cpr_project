import yfinance as yf
import pandas as pd

def fetch_nifty_data(period="60d", interval="1d") -> pd.DataFrame:
    symbol = "^NSEI"  # Nifty 50 index on Yahoo Finance
    df = yf.download(symbol, period=period, interval=interval)
    df.dropna(inplace=True)
    return df
