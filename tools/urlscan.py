import requests
import time
from core.config import URLSCAN_API_KEY, URLSCAN_API_URL

def urlscan_scanend(unclean_domain):
    url = "https://urlscan.io/api/v1/scan"

    payload = {
    "url": unclean_domain,
    "visibility": "public",
    "country": "de",
    "tags": [
        "iloveurlscan",
        "testing"
    ]
    }

    headers = {
    "Content-Type": "application/json",
    "api-key": URLSCAN_API_KEY
        }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    if response.status_code != 200:
        raise RuntimeError(f"urlscan scan failed ({response.status_code}): {data}")

    scanid = data["uuid"]
    time.sleep(10)
    return scanid

def urlscan_results(unclean_domain):
    scanid = urlscan_scanend(unclean_domain)
    url = "https://urlscan.io/api/v1/result/" + scanid + "/"
    headers = {"api-key": URLSCAN_API_KEY}

    for _ in range(6):
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            target_ip = data["page"]["ip"]
            return target_ip
        time.sleep(10)

    raise TimeoutError(f"urlscan result not ready for scan {scanid}")