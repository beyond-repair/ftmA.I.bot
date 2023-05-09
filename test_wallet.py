# Test script for wallet functionality

import os
import json
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
INFURA_URL = os.getenv('INFURA_URL')

# Connect to Ethereum network
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Test wallet functionality

# Check balance
balance = w3.eth.get_balance(w3.toChecksumAddress('0x1234567890123456789012345678901234567890'))
print(f'Current balance: {balance} wei')

# Send test transaction
transaction = {
    'to': '0x1234567890123456789012345678901234567890',
    'value': w3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': w3.toWei('50', 'gwei'),
}
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
transaction_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
print(f'Transaction sent: {transaction_hash.hex()}')
