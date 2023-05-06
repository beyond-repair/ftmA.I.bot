# Implement the TA strategy that we wrote earlier

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
fantom_data = pd.read_csv('fantom_data.csv')

# Define buy and sell signals
fantom_data['buy_signal'] = np.where(fantom_data['price'] < fantom_data['price'].rolling(window=20).mean(), 1, 0)
fantom_data['sell_signal'] = np.where(fantom_data['price'] > fantom_data['price'].rolling(window=20).mean(), 1, 0)

# Buy and sell
position = 0
for i in range(len(fantom_data)):
    if fantom_data['buy_signal'][i] == 1:
        position = 1
    elif fantom_data['sell_signal'][i] == 1:
        position = 0
    fantom_data['position'][i] = position

# Visualize results
sns.lineplot(x='date', y='price', data=fantom_data)
sns.scatterplot(x='date', y='price', hue='position', data=fantom_data)
plt.show()