from models.original_domain import OriginalDomain

URL = "https://dnstwister.report/search?ed=70617970616c2e636f6d"
DOMAIN = "paypal.com"

original_domain = OriginalDomain(DOMAIN, URL)
original_domain.gather_info()
print()
