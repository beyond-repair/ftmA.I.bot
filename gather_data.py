import requests
import time

def get_block_data(block_number):
    url = f'https://api.fantom.foundation/api/v1/getBlockByNumber/{block_number}'
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    block_numbers = range(1, 100)
    for block_number in block_numbers:
        try:
            block_data = get_block_data(block_number)
            print(block_data)
        except:
            print(f'Error getting data for block {block_number}')
        time.sleep(1)