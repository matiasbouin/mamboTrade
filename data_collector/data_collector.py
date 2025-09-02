import ccxt
import pandas as pd
import sqlite3
import os
from datetime import datetime

def fetch_ohlcv_data():
    """Fetches OHLCV data from Binance and saves to CSV and SQLite."""
    
    # 1. Initialize the exchange instance
    exchange = ccxt.binance()
    
    # 2. Define the symbol and timeframe
    symbol = 'BTC/USDT'
    timeframe = '1h'
    limit = 500  # Number of candles to fetch
    
    # 3. Fetch the data
    print(f"Fetching {limit} {timeframe} candles for {symbol}...")
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)

    # Create a directory for shared data
    data_dir = "shared_data"
    os.makedirs(data_dir, exist_ok=True)
    
    # 4. Create a Pandas DataFrame
    columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
    df = pd.DataFrame(ohlcv, columns=columns)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms') # Convert ms to datetime
    
    # 5. Save to CSV
    csv_filename = os.path.join(data_dir, 'btc_usdt_1h_data.csv')
    df.to_csv(csv_filename, index=False)
    print(f"Data saved to {csv_filename}")
    
    # 6. Save to SQLite database
    db_filename = os.path.join(data_dir, 'trading_data.db')
    conn = sqlite3.connect(db_filename)
    df.to_sql('price_data', conn, if_exists='replace', index=False) # 'replace' for simplicity in PoC
    conn.close()
    print(f"Data saved to database {db_filename}")
    
    print("Data collection complete!")
    return df

if __name__ == "__main__":
    fetch_ohlcv_data()