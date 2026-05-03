import requests
import json
from core.config import VIEWDNS_API_KEY

HOST = "142.251.156.119"
VIEWDNS_API_URL = "https://api.viewdns.info/reverseip/"

def reverse_ip_lookup(host):
    params = {
        "host": host,
        "apikey": VIEWDNS_API_KEY,
        "output": "json"
    }
    response = requests.get(VIEWDNS_API_URL, params=params)

    if response.status_code != 200:
        raise RuntimeError(f"viewdns API failed ({response.status_code}): {response.text}")

    data = response.json()
    domains = [d["name"] for d in data["response"]["domains"]]
    return domains

if __name__ == "__main__":
    domains = reverse_ip_lookup(HOST)
    print(f"Found {len(domains)} domains:")
    for domain in domains:
        print(domain)

    with open("test.json", "w") as f:
        json.dump(domains, f, indent=4)
