from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from extract_criminal_record import extractRecord
from generatedate import generateDateList
import time,pprint,logging

# first we need to check for next button as well
# put the function on repeat
# somehow figure out how to get a list of all possible dates 



def search_for_case():
    op = Options()
    # op.add_argument('--headless')
    op.add_argument("window-size=1920,1080")
    op.add_experimental_option("excludeSwitches", ["enable-automation"])
    op.add_experimental_option('useAutomationExtension', False)
    op.add_argument("start-maximized")
    global driver
    # getting a basic robot done
    driver = webdriver.Chrome(options=op)
    driver.get("https://eapps.courts.state.va.us/gdcourts/landing.do")
    driver.implicitly_wait(1.5)
    driver.find_element(by=By.NAME, value="accept").click()
    
    
    with open("districtcourturl.txt", "r") as fp:
        courtlinks = fp.readlines()
        for courtlink in courtlinks:
            driver.get(courtlink)
            court_name = driver.find_element(by=By.XPATH, value="//input[@name='selectedCourtName']").get_attribute('value')
            
            # date will be dynamic
            # add a loop here to get the all date data
            date_list = generateDateList()
            # date_list = ["01/02/2020", "01/03/2020","01/04/2020"]
            # looping for all the date with each court date
            for search_date in date_list:
                driver.get(courtlink)
                time.sleep(1)
                searchElement = driver.find_element(by=By.XPATH, value='//input[contains(@name, "searchTerm")]')
                searchElement.clear()
                searchElement.send_keys(str(search_date).replace("-","/"))
                print(f">>>searching for date {search_date}")
                driver.find_element(by=By.XPATH, value='//input[contains(@name, "searchTerm")]').send_keys(Keys.ENTER)
                time.sleep(1)

                linklist = []
                next_btn_available=True
                case_available = True
                try:
                    driver.find_element(by=By.XPATH , value="//td[contains(@class, 'errorFont')]")
                    print("No case found on this date")
                    next_btn_available =False
                    case_available=False
                    print(f">>>Nothing found on date {search_date}")
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
                        driver.find_element(by=By.XPATH, value="//input[@name='caseInfoScrollForward']").click()
                        print("Next button clicked")
                        time.sleep(1)

                        
                    except:
                        next_btn_available=False
                
                
                if len(linklist) !=0:
                    print(f"found {len(linklist)} links in linklist on date {search_date}")  
                    # print(linklist)
                    for link in linklist:
                        driver.get("https://eapps.courts.state.va.us/gdcourts/" + link)
                        src =driver.find_element(by=By.NAME, value="criminalDetailForm").get_attribute('outerHTML')

                        '''
                        extractrecord() function takes in a raw form with data, 
                        and returns a clean dictionary with required data.   
                        ''' 
                        print(extractRecord(src,search_date))

                        time.sleep(1)

                        
                elif len(linklist)==0:
                    print("no element in linklist")
                    
                    


            
            
            
search_for_case()