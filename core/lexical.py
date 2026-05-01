import ipaddress
from core.config import SUSPICIOUS_STRINGS, SUSPICIOUS_TLDS, CHAR_LEN_SUSPICIOUS

'''
Lexical rules check against the domain to determine if its clean or scam
'''

def domain_cleanin(unclean_domain):
    domain = unclean_domain.split(".")[0]
    tld = unclean_domain.split(".")[-1]
    return domain, tld

def len_count(domain):
    count_char = len(domain)
    return count_char

def check_tld(tld):
    if tld in SUSPICIOUS_TLDS:
        decision = "scam"
    else:
        decision = "clean"
    return decision

def check_dstring(domain):
    if domain in SUSPICIOUS_STRINGS:
        decision = "scam"
    else:
        decision = "clean"
    return decision

def check_dip():

    return

def check_number_digits(domain):
    lennum = sum(1 for char in domain if char.isdigit())
    if lennum >= 3:
        decision = "scam"
    else: 
        decision = "clean"
    return decision

def check_number_end():
    return


def check_number_start():
    return


def decision(unclean_domain):
    domain, tld = domain_cleanin(unclean_domain)

    return