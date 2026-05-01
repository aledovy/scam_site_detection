from core.config import VT_API_KEY, VT_API_URL
import requests
import json

def getvt_json(unclean_domain):
    headers = {"accept": "application/json", "x-apikey": VT_API_KEY}
    response = requests.get(VT_API_URL, headers=headers)
    data = response.json()
    return data