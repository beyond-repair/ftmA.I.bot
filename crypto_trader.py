import pandas as pd
import numpy as np

# Load data
btc_data = pd.read_csv('BTC-USD.csv')

# Calculate moving averages
btc_data['MA50'] = btc_data['Close'].rolling(50).mean()
btc_data['MA200'] = btc_data['Close'].rolling(200).mean()

# Determine trading signals
btc_data['Signal'] = np.where(btc_data['MA50'] > btc_data['MA200'], 1, 0)

# Backtest strategy
btc_data['Returns'] = np.log(btc_data['Close']/btc_data['Close'].shift(1))
btc_data['Strategy'] = btc_data['Signal'].shift(1) * btc_data['Returns']

# Calculate cumulative returns
btc_data['Cumulative Returns'] = btc_data['Strategy'].cumsum()

# Print results
print(btc_data.tail())