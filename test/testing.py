unclean_domain = "goo222gle.com"

lennum = sum(1 for char in unclean_domain if char.isdigit())

print(lennum)