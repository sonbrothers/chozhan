from selenium import webdriver
from pullDB import *
from pushDB import insertWhoisologyDomains,insertCompKeys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def grepDomains(listOfDomains): # Receiving all the domains of the current page

    d = []
    for i in listOfDomains:
        # print i.text
        d.append(i.text)
    l = len(d)
    domains = []
    for i in range(len(d)):
        new = d[i].split("\n")
        domains = domains + new
    # print domains
    for domain in domains:
        # insertDomains_w(i)
        print domain
        insertWhoisologyDomains(domain) # Inserting all the domains to the whoology table
    time.sleep(3) #You can define your own ends on the application Response

def getWhoisologyData():
    for key in getKeys():
        if key not in getCompKeys():
            print key
            driver=webdriver.Firefox()
            driver.get("https://whoisology.com")
            try:
                driver.find_element_by_name("domain_keyword[]").send_keys(key)
                driver.find_element_by_name("search").click()
                try:
                    insertCompKeys(key)
                    grepDomains(driver.find_elements_by_xpath("//*[@class='terzium']"))#Sending all the domains of the current page to grep function
                    while True:
                        WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="thispage"]/following-sibling::a[1]'))).click()
                        grepDomains(driver.find_elements_by_xpath("//*[@class='terzium']"))
                    insertCompKeys(key)
                    driver.quit()
                except Exception as error:
                    print error
            except Exception as error:
                print error

