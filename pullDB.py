from pushDB import connectDB

domains = []


def getKeys():  # This method used to get the Keys present in the DB
    conn, db = connectDB()
    keywords = []
    for keyword in db.keywords.find({}, {"keyword": 1, "_id": 0}):
        keywords.append(keyword['keyword'])
    conn.close()
    return keywords


def getUserDefinedDomains():
    conn, db = connectDB()
    domains = []
    for domain in db.domains.find({"source": "userDefined"}, {"domain": 1, "_id": 0}):
        domains.append(domain['domain'])
    conn.close()
    return domains


def getCompKeys():
    conn, db = connectDB()
    compKeys = []
    for compKey in db.compkeys.find({}, {"compkey": 1, "_id": 0}):
        compKeys.append(compKey['compkey'])
    conn.close()
    return compKeys


def getWhoisologyDomains():
    conn, db = connectDB()
    domains = []
    for domain in db.whosdomains.find({}, {"domain": 1, "_id": 0}):
        domains.append(domain['domain'])
    conn.close()
    return domains


def getWhoisologyWhoisDetails():
    conn, db = connectDB()
    return db.wh_whoisdetails.find({})


"""This method only get all succss whios whoisology domains"""

def getWhoisologyWhoisDomains():
    conn, db = connectDB()
    global domains
    for domain in db.wh_whoisdetails.find({}):
        if type(domain['domain_name']) is list:
            domains.append(domain['domain_name'][0].lower())
        else:
            domains.append(domain['domain_name'].lower())
    conn.close()
    return domains


"""This method used to get the Failed whois domains from whoisology output"""


def getWhoisologyFailedDomains():
    conn, db = connectDB()
    global domains
    for domain in db.whoisfailed.find({}, {"domain": 1, "_id": 1}):
        domains.append(domain['domain'])
    return domains
