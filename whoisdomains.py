import whois
from pullDB import *
from pushDB import *

def whoisWhoisology():
    print "Current length for whois - "+str(len(list(set(list(set(getWhoisologyDomains())-set(getWhoisologyWhoisDomains())))-set(getWhoisologyFailedDomains()))))
    for domain in list(set(list(set(getWhoisologyDomains())-set(getWhoisologyWhoisDomains())))-set(getWhoisologyFailedDomains())):
        print "Running on current domain - "+str(domain)
        try:
            insertWhoisologyWhois(whois.whois(domain))
        except Exception as error:
            insertWhoisologyFailedDomains(domain)

def whoisWhoisologyFailed():
    print "Current length for failed whois - "+str(len(getWhoisologyFailedDomains()))
    for domain in getWhoisologyFailedDomains():
        print "Running on current domain - "+str(domain)
        try:
            insertWhoisologyWhois(whois.whois(domain))
        except Exception as error:
            insertWhoisologyFailedDomains(domain)
