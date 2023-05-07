# Script to check all files for errors

import os

# Define the directory to check
DIRECTORY = 'auto_gpt_workspace'

# Get a list of all files in the directory
files = os.listdir(DIRECTORY)

# Loop through each file and check for errors
for file in files:
    try:
        with open(os.path.join(DIRECTORY, file), 'r') as f:
            pass
    except Exception as e:
        print(f'Error in file {file}: {e}')
