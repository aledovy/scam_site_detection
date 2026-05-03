import requests
import json


def reverse_dns_lookup(unclean_domain):

    host = ""
    output = 'json'
    api_url = f'https://api.viewdns.info/reverseip/?host={host}&apikey={apikey}&output={output}'

    response = requests.get(api_url)
    data = response.json()

    return data