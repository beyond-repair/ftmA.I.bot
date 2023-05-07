# Import the requests library
import requests

# Define the API endpoint and parameters
url = 'https://api.ftmscan.com/api'
params = {
    'module': 'account',
    'action': 'balance',
    'address': '0x742d35Cc6634C0532925a3b844Bc454e4438f44e',
    'tag': 'latest',
    'apikey': 'YourApiKeyToken'
}

# Make the API request
response = requests.get(url, params=params)

# Print the JSON response
print(response.json())