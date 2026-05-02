from dotenv import load_dotenv
import os

load_dotenv()

VT_API_KEY = os.getenv("VT_API_KEY")
WHOIS_API_KEY = os.getenv("WHOIS_API_KEY")
URLSCAN_API_KEY = os.getenv("URLSCAN_API_KEY")

VT_API_URL = "https://www.virustotal.com/api/v3/domains/"
WHOIS_API_URL = "https://whoisjson.com/api/v1/whois?domain="
URLSCAN_API_URL = "https://urlscan.io"

SUSPICIOUS_TLDS = ["xyz", "shop"]
SUSPICIOUS_STRINGS = []
CHAR_LEN_SUSPICIOUS = 14

INPUT_FILE = "C:/Users/dovyd/OneDrive/Documents/Stalinis kompiuteris/Automation/EPERIMENTS/scam_site_detection/input/sample.txt"
OUTPUT_FOLDER = "C:/Users/dovyd/OneDrive/Documents/Stalinis kompiuteris/Automation/EPERIMENTS/scam_site_detection/output"

