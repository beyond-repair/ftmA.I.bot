import pandas as pd
import ta

# Load data
data = pd.read_csv('fantom_data.csv')

# Add technical indicators
data = ta.add_all_ta_features(data, open='open', high='high', low='low', close='close', volume='volume')

# Identify potential trades
buy_signals = data[data['macd_signal'] > data['macd']]