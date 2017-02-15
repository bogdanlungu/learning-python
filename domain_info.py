""" Get info about a domain
"""
# pylint: disable=C0103
import re
import whois


def get_domain_name():
    """The domain name"""
    print("Welcome! \nEnter the domain name:")
    return input()


def process_the_request(domain):
    """Process the request"""
    if check_domain(domain):
        result = whois.whois(domain)
        print(result)
    else:
        print('The domain name is not valid.')


def check_domain(domain):
    """Check if the domain is valid"""
    if len(domain) > 255:
        return False
    if domain[-1] == ".":
        domain = domain[:-1]
    allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(x) for x in domain.split("."))

the_domain = get_domain_name()
process_the_request(the_domain)
