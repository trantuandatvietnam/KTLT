# Import module dotenv to get env var in project
from dotenv import load_dotenv
import requests
# Load all env vars 
load_dotenv()

import os
# Get api key
SHODAN_API_KEY = os.environ['API_SHODAN']
ip = '1.1.1.1'

def shodanInfo(ip):
    try:
        # Get response and convert it to JSON data
        result = requests.get(f"https://api.shodan.io/shodan/host/{ip}?key={SHODAN_API_KEY}&minify=True").json()
    except Exception as exception:
        result = {"error": "Information not avaiable!"}
    return result

print(shodanInfo(ip))
