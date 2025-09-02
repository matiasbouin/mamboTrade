import requests
import time
import os
from dotenv import load_dotenv
import ccxt

# Load environment variables from a .env file (create this file yourself)
load_dotenv()

# Configuration
SIGNAL_SERVICE_URL = "http://signal-service:8000/signal"
POLL_INTERVAL = 60  # seconds

# Initialize variables
previous_signal = None

def initialize_exchange():
    """Initialize the CCXT exchange with testnet credentials."""
    exchange = ccxt.binance({
        'apiKey': os.getenv('BINANCE_TESTNET_API_KEY'),
        'secret': os.getenv('BINANCE_TESTNET_SECRET_KEY'),
        'enableRateLimit': True,
        'options': {
            'defaultType': 'future', # or 'spot' for spot testnet
        },
    })
    
    # Set the testnet URL
    exchange.set_sandbox_mode(True)
    return exchange

def place_test_order(exchange, signal):
    """Places a test order on the Binance testnet (commented out for safety)."""
    symbol = 'BTC/USDT'
    amount = 0.001  # 0.001 BTC
    
    try:
        if signal == "BUY":
            # order = exchange.create_market_buy_order(symbol, amount)
            print(f"[MOCK] PLACING MARKET BUY ORDER FOR {amount} {symbol}")
        elif signal == "SELL":
            # order = exchange.create_market_sell_order(symbol, amount)
            print(f"[MOCK] PLACING MARKET SELL ORDER FOR {amount} {symbol}")
        # print(f"[MOCK] Order result: {order}")
    except Exception as e:
        print(f"[MOCK] Error placing order: {e}")

def main():
    global previous_signal
    # exchange = initialize_exchange() # Initialize only when you're ready to test with real mock orders
    
    print("Starting Execution Service. Polling for signals...")
    print("Press Ctrl+C to stop.")
    
    try:
        while True:
            # 1. Poll the Signal Service
            try:
                response = requests.get(SIGNAL_SERVICE_URL)
                signal_data = response.json()
                current_signal = signal_data['signal']
            except requests.exceptions.ConnectionError:
                print("Error: Could not connect to Signal Service. Is it running?")
                time.sleep(POLL_INTERVAL)
                continue
            except Exception as e:
                print(f"Error fetching signal: {e}")
                time.sleep(POLL_INTERVAL)
                continue
            
            # 2. Check if the signal has changed
            if current_signal != previous_signal:
                print(f"\n--- Signal Change Detected ---")
                print(f"New Signal: {current_signal}")
                print(f"SMAs: 50-period={signal_data['sma50']}, 200-period={signal_data['sma200']}")
                print(f"Time: {signal_data['timestamp']}")
                
                # 3. Logic for what to do on the new signal
                if current_signal == "BUY":
                    print("ACTION: PLACE BUY ORDER")
                    # place_test_order(exchange, 'BUY') # UNCOMMENT AFTER TESTING
                elif current_signal == "SELL":
                    print("ACTION: PLACE SELL ORDER")
                    # place_test_order(exchange, 'SELL') # UNCOMMENT AFTER TESTING
                else:
                    print("ACTION: HOLD (No action)")
                
                print("-----------------------------")
                
                # Update the previous signal
                previous_signal = current_signal
            else:
                # No change, just print a heartbeat so we know it's working
                print(f".", end="", flush=True)
            
            time.sleep(POLL_INTERVAL)
            
    except KeyboardInterrupt:
        print("\nExecution stopped by user.")

if __name__ == "__main__":
    main()