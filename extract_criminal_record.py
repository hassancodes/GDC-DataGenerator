from timeit import repeat
from bs4 import BeautifulSoup
import pprint


# this is the main function to extract the data from case source page
def extractRecord(src):
    soup = BeautifulSoup(src, "html.parser")
    tbclass = soup.find_all("td", class_="tableback")
    # we dont want the 3 and 5 index tablebackclass
    talkbackclass = tbclass[:3] + tbclass[4:5]
    # print(len(talkbackclass)) 
    # tbcount is counter so I can Handle the exception of Hearing Information, In which we only the finalized data, the rest of the data in the section will be ignored
    
    tbcount=0
    # this will have the final result for each case
    FinalDict = {}
    for i in talkbackclass:
        if tbcount==2:
            soup = BeautifulSoup(str(i),"html.parser")
            tb = soup.find_all("table")[2]
            # print("TB" , len(tb))
            # print(len(tb.find_all("tr")))
            
            trlist1 = BeautifulSoup(str(tb.find_all("tr")[0]),"html.parser")
            trlist2 = BeautifulSoup(str(tb.find_all("tr")[-1]),"html.parser")
            
            
            tdlist1 = [x for x in [str(td.text).split("\n") for td in trlist1][0] if x.strip()]
            tdlist2 = [x for x in [str(td.text).split("\n") for td in trlist2][0] if x.strip()]
            
            # print(tdlist1)
            # print(tdlist2)
            
            if len(tdlist2) < len(tdlist1):
                times = len(tdlist1)-len(tdlist2)
                tdlist2.extend("--" for x in range(times))
                
                
            exceptd = dict(zip(tdlist1,tdlist2))
            
            # Extending our FinalDict
            FinalDict = dict(FinalDict, **exceptd)
            tbcount+=1
        
        
        elif tbcount!=2:
            soup = BeautifulSoup(str(i),"html.parser")
            maintable = soup.find_all("table")[1]
            tb = BeautifulSoup(str(maintable),"html.parser")
            trlist = tb.find_all("tr")
            # regular length of table rows will be 4 the last table have 8 which is an exception
            # FinalDict = {}
            for trs in trlist:
                soup = BeautifulSoup(str(trs), "html.parser")
                # list with complete data but we want to convert it into a dictionary so that it can be translated to csv
                complist = [" ".join(str(x.text).split()).split(":")[0] for x in soup.find_all("td")]
                if len(complist)/2==1:
                    FinalDict[complist[0]] = complist[1]
                elif len(complist)/2 > 1:
                    c1 =0
                    c2=1
                    for i in range(len(complist)//2):
                        FinalDict[complist[c1]] = complist[c2]
                        c1 +=2
                        c2+=2
            tbcount+=1
    # we just want that fourth iteration, That will have all the data        
    print(f"tbcount : {tbcount} ", FinalDict)
                    






