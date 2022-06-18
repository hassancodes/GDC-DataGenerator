from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from extract_criminal_record import extractRecord
from generatedate import generateDateList
import time
import pprint

# first we need to check for next button as well
# put the function on repeat
# somehow figure out how to get a list of all possible dates 



def search_for_case():

    global driver
    # getting a basic robot done
    driver = webdriver.Chrome()
    driver.get("https://eapps.courts.state.va.us/gdcourts/landing.do")
    driver.implicitly_wait(1.5)
    driver.find_element(by=By.NAME, value="accept").click()
    
    
    with open("districtcourturl.txt", "r") as fp:
        courtlinks = fp.readlines()
        for courtlink in courtlinks:
            driver.get(courtlink)
            # date will be dynamic
            # add a loop here to get the all date data
            date_list = generateDateList
            driver.find_element(by=By.XPATH, value='//input[contains(@name, "searchTerm")]').send_keys("01/02/2020")
            driver.find_element(by=By.XPATH, value='//input[contains(@name, "searchTerm")]').send_keys(Keys.ENTER)

            linklist = []
            next_btn_available=True
            case_available = True
            try:
                driver.find_element(by=By.XPATH , value="//td[contains(@class, 'errorFont')]")
                print("No case found on this date")
                next_btn_available =False
                case_available=False
            except:
                case_available=True

            while(next_btn_available):              
                try:
                    # we will get multiple links from here on.  we will store them in a list and then open then concurrently
                    # raw case links 
                    raw_clinks= driver.find_element(by=By.CLASS_NAME , value="tableborder").get_attribute("outerHTML")
                    soup= BeautifulSoup(raw_clinks, "html.parser")
                    # print(soup.find_all("a"))
                    # list of all the links on a specific search date
                    linklist.extend([x.get("href") for x in soup.find_all("a")])
                    driver.find_element(by=By.XPATH, value="//tr[4]/td[1]/span[1]/input[1]").click()

                    
                except:
                    next_btn_available=False
            
            
            if len(linklist) !=0:  
                for link in linklist:
                    driver.get("https://eapps.courts.state.va.us/gdcourts/" + link)
                    src =driver.find_element(by=By.NAME, value="criminalDetailForm").get_attribute('outerHTML')
                    extractRecord(src)
                    time.sleep(5)
                    '''
                    extractrecord() function takes in a raw form with data, 
                    and returns a clean dictionary with required data.
                    
                    ''' 
                    print("\n \n \n")
            elif len(linklist)==0:
                print("no element in linklist")
            
            
            
search_for_case()



























# payloadau = {'accept':'Accept'}
# acceptUrl = "https://eapps.courts.state.va.us/gdcourts/landing.do?landing=landing"

# aureq = requests.post(acceptUrl,data =(payloadau))

# print(aureq.headers)


# searchUrl = "https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=001&curentFipsCode=001"

# payload = {
#     "accept" :"accept"
# }
# a = requests.post("https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=001&curentFipsCode=001", data=payload)

# soup = BeautifulSoup(aureq.content, "html.parser")

# print(soup)




# =========================================================================================================================
    # driver.get("https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=001&curentFipsCode=001")
    # driver.find_element(by=By.XPATH, value='//input[contains(@name, "searchTerm")]').send_keys("01/06/2020")
    # driver.find_element(by=By.XPATH, value='//input[contains(@name, "searchTerm")]').send_keys(Keys.ENTER)


        # # we will get multiple links from here on.  we will store them in a list and then open then concurrently
        # # raw case links 
        # raw_clinks= driver.find_element(by=By.CLASS_NAME , value="tableborder").get_attribute("outerHTML")
        # soup= BeautifulSoup(raw_clinks, "html.parser")
        # # print(soup.find_all("a"))

        # # list of all the links on a specific search date
        # linklist = [x.get("href") for x in soup.find_all("a")]
    # for i in linklist:
    #     driver.get("https://eapps.courts.state.va.us/gdcourts/" + i)
    #     src =driver.find_element(by=By.NAME, value="criminalDetailForm").get_attribute('outerHTML')
    #     extractRecord(src)
    #     '''
    #     extractrecord() function takes in a raw form with data, 
    #     and returns a clean dictionary
        
    #     '''
        
    #     print("\n \n \n")
        
        
        
        
        # with open("new.html","w") as fp:
        #     fp.write(src)
        # a = extractRecord(src)
        # for i in a:
        #     # print(i)
        #     soup = BeautifulSoup(str(i), "html.parser")
        #     print(soup.prettify())   
        # break
        
        
    # print(linklist)