# scam_site_detection

> **Status: Work in Progress**

A tool for detecting scam/malicious websites using domain pivoting and multi-signal analysis.

## How it works

1. Takes a list of domains from an input file
2. Uses URLScan to pivot on IPs — finding other domains hosted on the same infrastructure
3. Runs each domain through a set of checks to classify it as clean or scam
4. Outputs results to a CSV file

## Checks / Modules

| Module | File | Status |
|---|---|---|
| Lexical analysis | `core/lexical.py` | In progress |
| Index check | `core/index.py` | Stub |
| Tranco rank | `core/tranco.py` | Stub |
| SEO signals | `core/seo.py` | Stub |
| IP pivoting | `tools/ip_pivoting.py` | Stub |
| URLScan integration | `tools/urlscan.py` | Stub |
| VirusTotal integration | `tools/virus_total.py` | Stub |
| WHOIS lookup | `tools/whois.py` | Stub |

### Lexical analysis (`core/lexical.py`)

Rules implemented so far:
- Domain and TLD extraction (`domain_cleanin`)
- Domain character length check (`len_count`) — threshold: 14 chars
- Suspicious TLD check (`check_tld`) — e.g. `.xyz`, `.shop`
- Suspicious string match (`check_dstring`)
- Excessive digit count (`check_number_digits`) — flags 3+ digits
- Stubs: `check_dip`, `check_number_end`, `check_fchar`, `check_lchar`, `check_number_start`
- `decision()` — aggregator function (not yet implemented)

### Config (`core/config.py`)

Centralised settings loaded via `python-dotenv`:
- API keys: VirusTotal, WHOIS, URLScan (loaded from `.env`)
- `SUSPICIOUS_TLDS`, `SUSPICIOUS_STRINGS`, `CHAR_LEN_SUSPICIOUS`
- `INPUT_FILE` / `OUTPUT_FOLDER` paths

## APIs used

- VirusTotal
- WHOIS
- URLScan
- Google Lighthouse

## Project structure

```
scam_site_detection/
├── main.py              # Entry point
├── core/
│   ├── config.py        # Settings and constants
│   ├── lexical.py       # Lexical domain checks
│   ├── index.py         # Index-based checks (stub)
│   ├── tranco.py        # Tranco rank check (stub)
│   └── seo.py           # SEO signals (stub)
├── tools/
│   ├── urlscan.py       # URLScan API client (stub)
│   ├── ip_pivoting.py   # IP pivot logic (stub)
│   ├── virus_total.py   # VirusTotal API client (stub)
│   └── whois.py         # WHOIS lookup (stub)
├── input/
│   └── sample.txt       # Sample domain list
├── .env.example         # API key template
├── dockerfile
└── docker-compose.yml
```

## Setup

1. Copy `.env.example` to `.env` and fill in your API keys
2. Run with Docker: `docker-compose up`
   or directly: `python main.py`
