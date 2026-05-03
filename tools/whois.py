import requests
from core.config import WHOIS_API_KEY, WHOIS_API_URL

def domain_cleanup(unclean_domain):
    cleaned_domain = unclean_domain.replace("www.", "").replace("https://", "")
    return cleaned_domain

def whois_check(unclean_domain):
    cleaned_domain = domain_cleanup(unclean_domain)
    headers = {"accept": "application/json", "Authorization": "Token=" + WHOIS_API_KEY}
    response = requests.get(WHOIS_API_URL + cleaned_domain, headers=headers)
    data = response.json()
    reg_date = data["created"]
    return reg_date