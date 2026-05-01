import requests
from core.config import WHOIS_API_KEY, WHOIS_API_URL

def whois_check():
    headers = {"accept": "application/json", "Authorization": "Token=" + WHOIS_API_KEY}
    response = requests.get(WHOIS_API_URL, headers=headers)
    data = response.json()
    return data