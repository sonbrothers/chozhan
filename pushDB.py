from dbName import dbName
import pymongo


# dbname=dbName #Deriving DB name from dbName Global variable

def connectDB():
    try:
        conn = pymongo.MongoClient()  # Connecting to the MongoDB
        db = conn[dbName]
        return conn, db
    except Exception as error:
        print ("Database Connection Failed: %s" % error)


def insertDomains():
    conn, db = connectDB()  # Connecting DB through
    manualDomains = open('input/domains')
    for domain in manualDomains.readlines():
        if domain.strip() not in db.domains.distinct('domain'):
            db.domains.insert({"domain": domain, "source": "userDefined"})
    conn.close()
    manualDomains.close()


def insertKeywords():
    conn, db = connectDB()
    fileKeyWords = open('input/keywords')
    for keyword in fileKeyWords.readlines():
        if keyword.strip() not in db.keywords.distinct('keyword'):
            db.keywords.insert({"keyword": keyword})
    conn.close()


# This function used to insert the whoislogy completed keys to the database
def insertCompKeys(compkey):
    conn, db = connectDB()
    if compkey not in db.compkeys.distinct('compkey'):
        db.compkeys.insert({"compkey": compkey})
    conn.close()


def insertWhoisologyDomains(domain):
    conn, db = connectDB()
    if domain not in db.whosdomains.distinct('domain'):
        db.whosdomains.insert({"domain": domain})
    conn.close()

def insertWhoisologyWhois(whoisdata):
    conn, db = connectDB()
    if whoisdata['domain_name'] not in [None, ""]:
        if type(whoisdata['domain_name']) is not list:
            domain = whoisdata['domain_name']
        else:
            domain = whoisdata['domain_name'][0]
    domain = domain.lower()
    if domain not in db.wh_whoisdetails.distinct('domain_name'):
        db.wh_whoisdetails.insert(whoisdata)
    conn.close()


""" This method used to save all domains which failed whois search"""


def insertWhoisologyFailedDomains(domain):
    conn, db = connectDB()
    if domain not in db.whoisfailed.distinct('domain'):
        db.whoisfailed.insert({"domain": domain})
    conn.close()
