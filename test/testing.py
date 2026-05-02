import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

domain = "google.com"

VT_API_KEY = os.getenv("VT_API_KEY")
VT_API_URL = os.getenv("VT_API_URL")

headers = {"accept": "application/json", "x-apikey": VT_API_KEY}
response = requests.get(VT_API_URL + domain, headers=headers)
data = response.json()

with open("test.json", "w")as f:
    f.write(json.dumps(data, indent=4))