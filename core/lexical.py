import ipaddress
from core.config import SUSPICIOUS_STRINGS, SUSPICIOUS_TLDS, CHAR_LEN_SUSPICIOUS

'''

'''

def domain_cleanin(unclean_domain):
    domain = unclean_domain.split(".")[0]
    tld = unclean_domain.split(".")[-1]
    return domain, tld

def len_count(domain):
    count_char = len(domain)
    return count_char

def check_tld():
    return

def check_dstring():
    return

def check_dip():
    return



def decision():
    return