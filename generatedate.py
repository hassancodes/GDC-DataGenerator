import datetime
import pandas as pd
from datetime import datetime
from datetime import date


def generateDateList():
    '''
    this function return a list of the possible dates 
    including the leap days i.e  from 2020 till current date
    '''
    today=date.today()

    d1 = datetime.strptime('2020/01/01', "%Y/%m/%d")
    d2 = datetime.strptime(today.strftime("%Y/%m/%d"), "%Y/%m/%d")
    # difference between dates in timedelta
    delta = d2 - d1

    # print(type(delta.days))

    start = datetime.strptime("01-01-2020", "%m-%d-%Y")
    date_generated = pd.date_range(start, periods=delta.days)
    date_list = list(date_generated.strftime("%m-%d-%Y"))
    if len(date_list)%2 != 0:
        date_list= date_list[:-1]
        print(len(date_list))
    elif len(date_list)%2==0:
        pass
    
    return date_list







def getSublists(mainlist,n):
    subListLength = len(mainlist) // n
    list_of_sublists = []
    for i in range(0, len(mainlist), subListLength):
        list_of_sublists.append(mainlist[i:i+subListLength])
    return list_of_sublists

# a  = getSublists(generateDateList(),8)
# print(a)

# for i in a:
#     print(i)
#     print("\n \n \n")



    


