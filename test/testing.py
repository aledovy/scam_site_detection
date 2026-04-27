unclean_domain = "google.com"

domain = unclean_domain.split(".")[0]
tld = unclean_domain.split(".")[-1]

print(domain, tld)

count_char = len(domain)
print(count_char)