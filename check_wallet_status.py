from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/your-project-id'))

if w3.isConnected():
    print('Wallet is connected')
else:
    print('Wallet is not connected')