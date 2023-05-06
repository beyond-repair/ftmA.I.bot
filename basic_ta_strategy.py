import pandas as pd
import numpy as np
import requests
import json
import time
import hmac
import hashlib
import base64
import urllib.parse

# Define API keys
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'

# Define API endpoints
base_url = 'https://ftx.com/api/'

# Define authentication function

def generate_signature(api_secret, endpoint, ts, request_body):
    payload = f'{ts.upper()}{endpoint}{request_body}'
    signature = hmac.new(api_secret.encode(), payload.encode(), hashlib.sha256).hexdigest()
    return signature

# Define API request function

def call_api(method, endpoint, params=None, data=None):
    # Define request parameters
    ts = str(int(time.time() * 1000))
    request_body = ''
    if params:
        request_body = urllib.parse.urlencode(params)
    if data:
        request_body = json.dumps(data)
    signature = generate_signature(api_secret, endpoint, ts, request_body)
    headers = {
        'FTX-KEY': api_key,
        'FTX-SIGN': signature,
        'FTX-TS': ts
    }
    # Send request
    response = requests.request(method, base_url + endpoint, params=params, data=data, headers=headers)
    # Return response
    return response.json()