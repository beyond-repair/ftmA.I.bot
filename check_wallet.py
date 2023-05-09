import requests
import json
import time
from web3 import Web3

# Set up web3 connection
w3 = Web3(Web3.HTTPProvider('https://rpcapi.fantom.network'))

# Set up Metamask wallet
private_key = 'YOUR_PRIVATE_KEY'
address = 'YOUR_WALLET_ADDRESS'

# Check wallet balance
balance = w3.eth.get_balance(address)
print('Wallet balance:', w3.fromWei(balance, 'ether'), 'FTM')

# Connect to FTM lock chain
chain_id = 250
w3.eth.chain_id = chain_id

# Check connection
if w3.isConnected():
    print('Connected to FTM lock chain')
else:
    print('Not connected to FTM lock chain')
