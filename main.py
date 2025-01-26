import ccxt
import time

# Initialize exchange
exchange = ccxt.coinbase({
    'apiKey': 'Add your own api key here',
    'secret': 'Add your private key here',
})

symbol = 'ETH/USDC'
buy_price_threshold = 3000  # Adjust based on your strategy
sell_price_threshold = 3800  # Adjust based on your strategy
position = None  # Track if you hold any ETH

def get_price():
    ticker = exchange.fetch_ticker(symbol)
    return ticker['last']

while True:
    try:
        price = get_price()
        print(f"Current price: {price}")

        if position is None and price <= buy_price_threshold:
            # Buy
            exchange.create_market_buy_order(symbol, 0.01)  # Example: Buy 0.01 ETH
            position = price
            print(f"Bought at {price}")

        elif position and price >= sell_price_threshold:
            # Sell
            exchange.create_market_sell_order(symbol, 0.01)
            profit = price - position
            print(f"Sold at {price}, Profit: {profit}")
            position = None

        time.sleep(10)  # Fetch prices every 10 seconds

    except Exception as e:
        print(f"Error: {e}")
        time.sleep(60)
