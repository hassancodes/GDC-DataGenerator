from pip import main
from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import multiprocessing as mp
from selenium.webdriver.chrome.options import Options
from extract_criminal_record import extractRecord
from generatedate import generateDateList,getSublists
from storeData import storeData
from rotatingproxies import get_chromedriver
import time,pprint,logging


# first we need to check for next button as well
# put the function on repeat
# somehow figure out how to get a list of all possible dates 



# with open("districtcourturl.txt", "r") as fp:
#     courtlinks = fp.readlines()
#     for courtlink in courtlinks:

SUBLIST =[]
def search_for_case(courtlink, date_list,return_dict, court_dict):

    global SUBLIST
    op = Options()
    op.add_argument("window-size=1920,1080")
    op.add_experimental_option("excludeSwitches", ["enable-automation"])
    # op.add_argument("--headless") 
    op.add_experimental_option('useAutomationExtension', False)
    op.add_argument("start-maximized")
    # global driver

    # getting a basic robot done
    driver = webdriver.Chrome(options=op)
    # driver = 
    # driver = get_chromedriver(use_proxy=True)
    driver.get("https://eapps.courts.state.va.us/gdcourts/landing.do")
    driver.implicitly_wait(1.5)
    driver.find_element(by=By.NAME, value="accept").click()
    driver.get(courtlink)
    court_name = driver.find_element(by=By.XPATH, value="//input[@name='selectedCourtName']").get_attribute('value')
    print(court_name)
    # courtName=court_name

    for search_date in date_list:
        driver.get(courtlink)
        # time.sleep(3)
        searchElement = driver.find_element(by=By.XPATH, value='//input[contains(@name, "searchTerm")]')
        searchElement.clear()
        searchElement.send_keys(str(search_date).replace("-","/"))
        print(f">>>searching for date {search_date}")
        driver.find_element(by=By.XPATH, value='//input[contains(@name, "searchTerm")]').send_keys(Keys.ENTER)
        # time.sleep(10)

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
                # time.sleep(10)
                
            

                
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
                    data_dict = extractRecord(src,search_date)
                    data_dict["courtName"] =court_name
                    SUBLIST.append(data_dict)
                    # print(extractRecord(src,search_date))

                    # time.sleep(10)

                    
            elif len(linklist)==0:
                print("no element in linklist")
    print("\n \n \n")            
    print("Len of sublist", len(SUBLIST) , court_name)
    driver.close()                
    return_dict[search_date] = SUBLIST
     


            
            
if __name__ == "__main__":
    manager = mp.Manager()
    return_dict = manager.dict()
    main_date_list = generateDateList()
    date_list = getSublists(main_date_list, 12)
    with open("districtcourturl.txt", "r") as fp:
        courtlinks = fp.readlines()
        LISTOFDATADICT =[]        
        courtCounter =0
        for courtlink in courtlinks:
            manager = mp.Manager()
            courtmanager=mp.Manager()
            return_dict = manager.dict()
            court_dict = courtmanager.dict()
            
            jobs = []
            mainList=[]
            p1 = mp.Process(target=search_for_case,args=(courtlink,date_list[0],return_dict,court_dict,))
            p2 = mp.Process(target=search_for_case,args=(courtlink,date_list[1],return_dict,court_dict,))
            p3 = mp.Process(target=search_for_case,args=(courtlink,date_list[2],return_dict,court_dict,))
            p4 = mp.Process(target=search_for_case,args=(courtlink,date_list[3],return_dict,court_dict,))
            p5 = mp.Process(target=search_for_case,args=(courtlink,date_list[4],return_dict,court_dict,))
            p6 = mp.Process(target=search_for_case,args=(courtlink,date_list[5],return_dict,court_dict,))
            p7 = mp.Process(target=search_for_case,args=(courtlink,date_list[6],return_dict,court_dict,))
            p8 = mp.Process(target=search_for_case,args=(courtlink,date_list[7],return_dict,court_dict,))
            p9 = mp.Process(target=search_for_case,args=(courtlink,date_list[8],return_dict,court_dict,))
            p10 = mp.Process(target=search_for_case,args=(courtlink,date_list[9],return_dict,court_dict,))
            p11 = mp.Process(target=search_for_case,args=(courtlink,date_list[10],return_dict,court_dict,))
            p12 = mp.Process(target=search_for_case,args=(courtlink,date_list[11],return_dict,court_dict,))
            
            
            
            
            jobs.append(p1)
            jobs.append(p2)
            jobs.append(p3)
            jobs.append(p4)
            jobs.append(p5)
            jobs.append(p6)
            jobs.append(p7)
            jobs.append(p8)
            jobs.append(p9)
            jobs.append(p10)
            jobs.append(p11)
            jobs.append(p12)
            
            
            p1.start()
            p2.start()
            p1.join()
            p2.join()
            print("---------------- waiting for 2nd to start")
            
            p3.start()
            p4.start()
            p3.join()
            p4.join()
            print("---------------- waiting for 3 to start")
            # for sec1 in jobs[0:4]:
            #     sec1.join()
                
            # print("---------------- waiting for 2nd four to start")
            # time.sleep(120)
            p5.start()
            p6.start()
            p5.join()
            p6.join()
            print("---------------- waiting for four to start")
            
            p7.start()
            p8.start()
            p7.join()
            p8.join()
            print("---------------- waiting for five to start")
            # for sec2 in jobs[4:8]:
                # sec2.join()
            # print("---------------- waiting for 3rd six to start")
            # time.sleep(100)
            p9.start()
            p10.start()
            p9.join()
            p10.join()
            
            p11.start()
            p12.start()
            p11.join()
            p12.join()
            print("--------------------waiting for last six to start")
            # time.sleep(300)

            
        # for proc in jobs[8:]:
        # for proc in jobs:
        #     proc.join()
        #         # print(dir(proc))
        # for z in return_dict.values():
        #     mainList.extend(z)
        # storeData(mainList,court_dict["courtName"])
        # print("\n \n \n \n" + court_dict["courtName"] + "Is Done!!!!!!!!!!!!!!!!!")
            # for proc in jobs:
            #     proc.join()
                    # print(dir(proc))
            for z in return_dict.values():
                print(z)
                mainList.extend(z)
            storeData(mainList,mainList[0]["courtName"])
            print("\n \n \n \n" + mainList[0]["courtName"] + "Is Done!!!!!!!!!!!!!!!!!")