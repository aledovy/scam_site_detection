import requests
import time
from core.config import URLSCAN_API_KEY, URLSCAN_API_URL

def urlscan_scanend():
    url = "https://urlscan.io/api/v1/scan"

    payload = {
    "url": URLSCAN_API_URL,
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
    scanid = data["uuid"]
    time.sleep(10)
    return scanid

def urlscan_results(scanid):
    scan_id = "YOUR_scanId_PARAMETER"
    url = "https://urlscan.io/api/v1/result/" + scanid + "/"

    headers = {"api-key": "YOUR_API_KEY_HERE"}

    response = requests.get(url, headers=headers)

    data = response.json()
    return data