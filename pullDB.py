from pushDB import connectDB

def getKeys(): # This method used to get the Keys present in the DB
    conn,db=connectDB()
    keywords=[]
    for keyword in db.keywords.find({},{"keyword":1,"_id":0}):
        keywords.append(keyword['keyword'])
    conn.close()
    return keywords

def getUserDefinedDomains():
    conn,db=connectDB()
    domains=[]
    for domain in db.domains.find({"source":"userDefined"},{"domain":1,"_id":0}):
        domains.append(domain['domain'])
    conn.close()
    return domains

def getCompKeys():
    conn,db=connectDB()
    compKeys=[]
    for compKey in db.compkeys.find({},{"compkey":1,"_id":0}):
        compKeys.append(compKey['compkey'])
    conn.close()
    return compKeys

def getWhoisologyDomains():
    conn,db=connectDB()
    domains=[]
    for domain in db.whosdomains.find({},{"domain":1,"_id":0}):
        domains.append(domain['domain'])
    conn.close()
    return domains
