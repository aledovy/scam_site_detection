import requests
import json
import time


target_domain = "google.com"


payload = {
  "url": target_domain,
  "visibility": "public",
  "country": "de",
  "tags": [
    "iloveurlscan",
    "testing"
  ]
}

headers = {
  "Content-Type": "application/json",
  "api-key": API_KEY
}

response = requests.post(url, json=payload, headers=headers)

data = response.json()

uuid = data["uuid"]

time.sleep(20)

url = "https://urlscan.io/api/v1/result/" + uuid + "/"

headers = {"api-key": API_KEY}

response2 = requests.get(url, headers=headers)

data2 = response2.json()

#print(json.dumps(data2, indent=4))

ip = data2["page"]["ip"]

print(ip)


with open("file.json", "w") as f:
    f.write(json.dumps(data2, indent=4))