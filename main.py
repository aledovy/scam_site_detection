from core.config import INPUT_FILE, OUTPUT_FOLDER
from logging import log
from tools.urlscan import urlscan_results
from tools.whois import whois_check
import time
from datetime import datetime

def main():
    print("this is entry point")
    with open(INPUT_FILE, "r") as f, open(OUTPUT_FOLDER + "_output.csv", "w", newline="") as csvfile:
        for unclean_domain in f:
            unclean_domain = unclean_domain.strip()
            domain_ip = urlscan_results(unclean_domain)
            registration_date = whois_check(unclean_domain)
            print(unclean_domain, " | ", domain_ip, " | ", registration_date)
            print("Checking for domains resolved under same IP")
            


if __name__ == "__main__":
    main()