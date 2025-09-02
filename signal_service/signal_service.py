from fastapi import FastAPI
import pandas as pd
import sqlite3
import uvicorn

app = FastAPI(title="Trading Signal Service")

def calculate_signal():
    """Calculates the SMA crossover signal from the database."""
    # 1. Read data from SQLite (you could also read from CSV)
    db_filename = 'shared_data/trading_data.db'
    conn = sqlite3.connect(db_filename)
    query = "SELECT timestamp, close FROM price_data ORDER BY timestamp"
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    # 2. Calculate SMAs
    short_window = 50
    long_window = 200
    df['sma50'] = df['close'].rolling(window=short_window).mean()
    df['sma200'] = df['close'].rolling(window=long_window).mean()
    
    # 3. Get the last valid calculated values
    latest_data = df.iloc[-1]
    sma50 = latest_data['sma50']
    sma200 = latest_data['sma200']
    
    # 4. Determine signal
    if sma50 is None or sma200 is None:
        signal = "HOLD" # Not enough data yet
    elif sma50 > sma200:
        signal = "BUY"
    else:
        signal = "SELL"
        
    return {
        "signal": signal,
        "sma50": sma50,
        "sma200": sma200,
        "timestamp": latest_data['timestamp']
    }

@app.get("/signal")
async def get_signal():
    """API endpoint to get the current trading signal."""
    return calculate_signal()

if __name__ == "__main__":
    # Run the server on localhost, port 8000
    uvicorn.run(app, host="127.0.0.1", port=8000)