import csv
def storeData(src,court_name):        
    '''
    storedata.py function will store the dictionary into its specific directory according to the courtname
    MAINFOLDER =  data
    '''
    
    headers = ['Case Number ', 'Filed Date ', 'Locality ', 'Name ', 
               'Status ', 'Defense Attorney ', 'Address ', 'AKA1 ', 
               'AKA2 ', 'Gender ', 'Race ', 'DOB ', 'Charge ', 'Code Section ',
               'Case Type ', 'Class ', 'Offense Date ', 'Arrest Date ', 'Complainant ', 
               'Amended Charge ', 'Amended Code ', 'Amended Case Type ', 'Date',
               'Time', 'Result', 'Hearing Type', 'Courtroom', 'Plea', 
               'Continuance Code', '', 'Final Disposition ', 'Sentence Time ', 
               'Sentence Suspended Time ', 'Probation Type ', 'Probation Time ', 
               'Probation Starts ', 'Operator License Suspension Time ', 
               'Restriction Effective Date ', 'Operator License Restriction Codes ', 
               'Fine ', 'Costs ', 'Fine/Costs Due ', 'Fine/Costs Paid ', 
               'Fine/Costs Paid Date ', 'VASAP ', 'searchDate']
    
    
    
      
    
    file_name = court_name.replace(" ","")
    with open(f"data/{file_name}.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = headers)
        writer.writeheader()
        writer.writerows(src)
        

# my_dict = [{'Case Number ': 'GC19011449-00', 'Filed Date ': '12/20/2019', 'Locality ': 'COMMONWEALTH OF VA', 'Name ': 'WASHINGTON, TORREAN', 'Status ': 'Custody', 'Defense Attorney ': 'BUNDICK, C', 'Address ': 'BIRDSNEST, VA 23307', 'AKA1 ': '', 'AKA2 ': '', 'Gender ': 'Male', 'Race ': 'Black', 'DOB ': '06/09/****', 'Charge ': 'USE FIREARM IN FELONY 1ST OFF', 'Code Section ': '18.2-53.1', 'Case Type ': 'Felony', 'Class ': 'U', 'Offense Date ': '01/20/2019', 'Arrest Date ': '12/19/2019', 'Complainant ': 'CASTIGLIA, S', 'Amended Charge ': '', 'Amended Code ': '', 'Amended Case Type ': '', 'Date': '02/24/2020', 'Time': '01:30 PM', 'Result': 'Finalized', 'Hearing Type': '--', 'Courtroom': '--', 'Plea': '--', 'Continuance Code': '--', '': '', 'Final Disposition ': 'Certified To Grand Jury - For final case disposition, see Circuit Court Case Information', 'Sentence Time ': '00Months 000Days 00Hours', 'Sentence Suspended Time ': '00Months 000Days 00Hours', 'Probation Type ': '', 'Probation Time ': '00Years 00Months 000Days', 'Probation Starts ': '', 'Operator License Suspension Time ': '00Years 00Months 000Days', 'Restriction Effective Date ': '', 'Operator License Restriction Codes ': '', 'Fine ': '', 'Costs ': '', 'Fine/Costs Due ': '', 'Fine/Costs Paid ': '', 'Fine/Costs Paid Date ': '', 'VASAP ': '', 'searchDate': '01-02-2020'},
# {'Case Number ': 'GC19011450-00', 'Filed Date ': '12/20/2019', 'Locality ': 'COMMONWEALTH OF VA', 'Name ': 'WASHINGTON, TORREAN', 'Status ': 'Custody', 'Defense Attorney ': 'BUNDICK, C', 'Address ': 'BIRDSNEST, VA 23307', 'AKA1 ': '', 'AKA2 ': '', 'Gender ': 'Male', 'Race ': 'Black', 'DOB ': '06/09/****', 'Charge ': 'ROBBERY', 'Code Section ': '18.2-58', 'Case Type ': 'Felony', 'Class ': 'U', 'Offense Date ': '01/20/2019', 'Arrest Date ': '12/19/2019', 'Complainant ': 'CASTIGLIA, S', 'Amended Charge ': '', 'Amended Code ': '', 'Amended Case Type ': '', 'Date': '02/24/2020', 'Time': '01:30 PM', 'Result': 'Finalized', 'Hearing Type': '--', 'Courtroom': '--', 'Plea': '--', 'Continuance Code': '--', '': '', 'Final Disposition ': 'Certified To Grand Jury - For final case disposition, see Circuit Court Case Information', 'Sentence Time ': '00Months 000Days 00Hours', 'Sentence Suspended Time ': '00Months 000Days 00Hours', 'Probation Type ': '', 'Probation Time ': '00Years 00Months 000Days', 'Probation Starts ': '', 'Operator License Suspension Time ': '00Years 00Months 000Days', 'Restriction Effective Date ': '', 'Operator License Restriction Codes ': '', 'Fine ': '', 'Costs ': '', 'Fine/Costs Due ': '', 'Fine/Costs Paid ': '', 'Fine/Costs Paid Date ': '', 'VASAP ': '', 'searchDate': '01-02-2020'},
# {'Case Number ': 'GC19011451-00', 'Filed Date ': '12/20/2019', 'Locality ': 'COMMONWEALTH OF VA', 'Name ': 'WASHINGTON, TORREAN', 'Status ': 'Custody', 'Defense Attorney ': 'BUNDICK, C', 'Address ': 'BIRDSNEST, VA 23307', 'AKA1 ': '', 'AKA2 ': '', 'Gender ': 'Male', 'Race ': 'Black', 'DOB ': '06/09/****', 'Charge ': 'GRND LARCENY', 'Code Section ': '18.2-95', 'Case Type ': 'Felony', 'Class ': 'U', 'Offense Date ': '01/20/2019', 'Arrest Date ': '12/19/2019', 'Complainant ': 'CASTILIA, S', 'Amended Charge ': '', 'Amended Code ': '', 'Amended Case Type ': '', 'Date': '02/24/2020', 'Time': '01:30 PM', 'Result': 'Finalized', 'Hearing Type': '--', 'Courtroom': '--', 'Plea': '--', 'Continuance Code': '--', '': '', 'Final Disposition ': 'Certified To Grand Jury - For final case disposition, see Circuit Court Case Information', 'Sentence Time ': '00Months 000Days 00Hours', 'Sentence Suspended Time ': '00Months 000Days 00Hours', 'Probation Type ': '', 'Probation Time ': '00Years 00Months 000Days', 'Probation Starts ': '', 'Operator License Suspension Time ': '00Years 00Months 000Days', 'Restriction Effective Date ': '', 'Operator License Restriction Codes ': '', 'Fine ': '', 'Costs ': '', 'Fine/Costs Due ': '', 'Fine/Costs Paid ': '', 'Fine/Costs Paid Date ': '', 'VASAP ': '', 'searchDate': '01-02-2020'}]
# storeData(my_dict , "Accomack General District Court")