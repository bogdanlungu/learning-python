""" Get info about a domain
"""
# pylint: disable=C0103
import whois


def get_domain_name():
    """The domain name"""
    print("Welcome! \nEnter the domain name:")
    return input()


def process_the_request(domain):
    """Process the request"""
    result = whois.whois(domain)
    print(result)


the_domain = get_domain_name()
process_the_request(the_domain)
