# Python script to check the balance of a Metamask wallet

import web3

# Connect to the Ethereum network
web3 = web3.Web3(web3.HTTPProvider('https://mainnet.infura.io/v3/your-project-id'))

# Get the balance of the wallet
balance = web3.eth.get_balance('0x1234567890123456789012345678901234567890')

# Print the balance
print('Wallet balance:', web3.fromWei(balance, 'ether'), 'ETH')