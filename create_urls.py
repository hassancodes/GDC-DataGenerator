from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pprint



def createurls():

    global driver
    # getting a basic robot done
    driver = webdriver.Chrome()
    driver.get("https://eapps.courts.state.va.us/gdcourts/landing.do")
    driver.implicitly_wait(1.5)
    driver.find_element(by=By.NAME, value="accept").click()
    
    
    ls = []
    # ===============================================================================
    # running i 135 time cuz we have total 135 district courts to target
    for i in range(135):
        driver.find_element(by=By.XPATH, value="//*[@id='btndropdown1']").click()
        driver.implicitly_wait(2)
        driver.find_element(by=By.XPATH, value=f"//body/ul[1]/li[{i+1}]/a[1]").click()
        driver.find_element(by=By.XPATH, value="//*[contains(@href, 'caseSearch.do?')]").click()
        ls.append(driver.current_url)
        
    with open("districtcourturl.txt", "w") as fp:
        for i in ls:
            fp.write(i +"\n")         
    
createurls()
    