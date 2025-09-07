import ccxt
import pandas as pd
import psycopg2
import os
from datetime import datetime

def fetch_ohlcv_data():
    """Fetches OHLCV data from Binance and saves to CSV and PostgreSQL."""
    
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
    
    # 6. Save to PostgreSQL database
    save_to_postgres(df)
    
    print("Data collection complete!")
    return df

def save_to_postgres(df):
    """Saves DataFrame to PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            port=os.getenv('DB_PORT', '5432')  # Default PostgreSQL port
        )
        
        # Create table if not exists
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS price_data (
                    timestamp TIMESTAMP PRIMARY KEY,
                    open FLOAT,
                    high FLOAT,
                    low FLOAT,
                    close FLOAT,
                    volume FLOAT
                )
            """)
        
        # Insert data
        for _, row in df.iterrows():
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO price_data (timestamp, open, high, low, close, volume)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (timestamp) DO NOTHING
                """, (row['timestamp'], row['open'], row['high'], 
                      row['low'], row['close'], row['volume']))
        
        conn.commit()
        print(f"Data saved to PostgreSQL database {os.getenv('DB_NAME')}")
        
    except Exception as e:
        print(f"Error saving to PostgreSQL: {e}")
        # You might want to raise the exception or handle it differently
        raise
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    fetch_ohlcv_data()