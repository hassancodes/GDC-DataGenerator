import pandas as pd
import pprint
mylist = ["Accomack General District Court",
"Albemarle General District Court",
"Alexandria General District Court",
"Alleghany General District Court",
"Amelia General District Court",
"Amherst General District Court",
"Appomattox General District Court",
"Arlington General District Court",
"Augusta General District Court",
"Bath General District Court",
"Bedford General District Court",
"Bland General District Court",
"Botetourt General District Court",
"Bristol General District Court",
"Brunswick General District Court",
"Buchanan General District Court",
"Buckingham General District Court",
"Buena Vista General District Court",
"Campbell General District Court",
"Caroline General District Court",
"Carroll General District Court",
"Charles City General District Court",
"Charlotte General District Court",
"Charlottesville General District Court",
"Chesapeake General District Court",
"Chesterfield General District Court",
"Clarke General District Court",
"Colonial Heights General District Court",
"Craig General District Court",
"Culpeper General District Court",
"Cumberland General District Court",
"Danville General District Court",
"Dickenson General District Court",
"Dinwiddie General District Court",
"Emporia General District Court",
"Essex General District Court",
"Fairfax City General District Court",
"Fairfax County General District Court",
"Falls Church General District Court",
"Fauquier General District Court",
"Floyd General District Court",
"Fluvanna General District Court",
"Franklin City General District Court",
"Franklin County General District Court",
"Frederick General District Court",
"Fredericksburg General District Court",
"Galax General District Court",
"Giles General District Court",
"Gloucester General District Court",
"Goochland General District Court",
"Grayson General District Court",
"Greene General District Court",
"Greensville General District Court",
"Halifax General District Court",
"Hampton General District Court",
"Hanover General District Court",
"Harrisonburg/Rockingham General District Court",
"Henrico General District Court",
"Henry General District Court",
"Highland General District Court",
"Hopewell General District Court",
"Isle of Wight General District Court",
"King George General District Court",
"King William General District Court",
"King and Queen General District Court",
"Lancaster General District Court",
"Lee General District Court",
"Lexington/Rockbridge General District Court",
"Loudoun General District Court",
"Louisa General District Court",
"Lunenburg General District Court",
"Lynchburg General District Court",
"Madison General District Court",
"Martinsville General District Court",
"Mathews General District Court",
"Mecklenburg General District Court",
"Middlesex General District Court",
"Montgomery/Blacksburg General District Court",
"Montgomery/Christiansburg General District Court",
"Nelson General District Court",
"New Kent General District Court",
"Newport News-Civil General District Court",
"Newport News-Criminal General District Court",
"Newport News-Traffic General District Court",
"Norfolk General District Court",
"Norfolk General District-Criminal Division",
"Norfolk General District-Traffic Division",
"Norfolk General District-Civil Division",
"Northampton General District Court",
"Northumberland General District Court",
"Nottoway General District Court",
"Orange General District Court",
"Page General District Court",
"Patrick General District Court",
"Petersburg General District Court",
"Pittsylvania General District Court",
"Portsmouth General District Court",
"Powhatan General District Court",
"PrinceEdward General District Court",
"PrinceGeorge General District Court",
"PrinceWilliam General District Court",
"Pulaski General District Court",
"Radford General District Court",
"Rappahannock General District Court",
"Richmond County General District Court",
"Richmond City General District Court",
"Richmond-Civil General District Court",
"Richmond-Marsh Criminal/Traffic General District Court at Manchester",
"Richmond-John Marshall Criminal/Traffic General District Court",
"Richmond Manchester General District Court",
"Roanoke City General District Court",
"Roanoke County General District Court",
"Russell General District Court",
"Salem General District Court",
"Scott General District Court",
"Shenandoah General District Court",
"Smyth General District Court",
"Southampton General District Court",
"Spotsylvania General District Court",
"Stafford General District Court",
"Staunton General District Court",
"Suffolk General District Court",
"Surry General District Court",
"Sussex General District Court",
"Tazewell General District Court",
"Virginia Beach General District Court",
"Warren General District Court",
"Washington General District Court",
"Waynesboro General District Court",
"Westmoreland General District Court",
"Williamsburg/James City County General District Court",
"Winchester General District Court",
"Wise/Norton General District Court",
"Wythe General District Court",
"York General District Court"]









mainurl= "https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=001&curentFipsCode="
mydict = {}
rawdict = {}

col_list = ["County FIPS Code", "GU Name"]
df = pd.read_csv("data.csv",usecols=col_list)




lollist =  []
for i in range(len(df["GU Name"])):
    rawdict[df["GU Name"][i]] = df["County FIPS Code"][i]



for i in range(len(mylist)):
    global finalurl
    if  mylist[i].split()[0] in rawdict:
        urlformed = str(rawdict[mylist[i].split()[0]])
        if len(str(urlformed)) ==1:
            urlformed = "00" + str(urlformed)
        elif len(urlformed) ==2:
            urlformed = "0" + str(urlformed)
        elif len(urlformed) ==3:
            urlformed = str(urlformed)
            
        finalurl = f"https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode={urlformed}&curentFipsCode={urlformed}"
        
        lollist.append(finalurl)    
        formeddict = {i :{
            mylist[i] : urlformed,
            "url" : finalurl
            
        }}
        
        # print(formeddict[i]['url'])
        mydict.update(formeddict)
        # mydict[i][mylist[i]] = rawdict[mylist[i].split()[0]]
        # mydict[i]["url"] = mainurl + str(rawdict[mylist[i].split()[0]])

        # print(True)
    else:
        # print(False)
        pass

with open("districtcourturl.txt", "w") as fp:
    for i in lollist:
        fp.write(i+ "\n")
pprint.pprint(mydict)
# print(mylist)



# =================================== Data Created ===================================================





# {0: {'Accomack General District Court': '001',
#      'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=001&curentFipsCode=001'},
#  1: {'Albemarle General District Court': '003',
#      'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=003&curentFipsCode=003'},
#  2: {'Alexandria General District Court': '510',
#      'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=510&curentFipsCode=510'},
#  3: {'Alleghany General District Court': '005',
#      'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=005&curentFipsCode=005'},
#  4: {'Amelia General District Court': '007',
#      'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=007&curentFipsCode=007'},
#  5: {'Amherst General District Court': '009',
#      'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=009&curentFipsCode=009'},
#  6: {'Appomattox General District Court': '011',
#      'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=011&curentFipsCode=011'},
#  7: {'Arlington General District Court': '013',
#      'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=013&curentFipsCode=013'},
#  8: {'Augusta General District Court': '015',
#      'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=015&curentFipsCode=015'},
#  9: {'Bath General District Court': '017',
#      'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=017&curentFipsCode=017'},
#  10: {'Bedford General District Court': '019',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=019&curentFipsCode=019'},
#  11: {'Bland General District Court': '021',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=021&curentFipsCode=021'},
#  12: {'Botetourt General District Court': '023',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=023&curentFipsCode=023'},
#  13: {'Bristol General District Court': '520',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=520&curentFipsCode=520'},
#  14: {'Brunswick General District Court': '025',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=025&curentFipsCode=025'},
#  15: {'Buchanan General District Court': '023',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=023&curentFipsCode=023'},
#  16: {'Buckingham General District Court': '029',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=029&curentFipsCode=029'},
#  18: {'Campbell General District Court': '031',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=031&curentFipsCode=031'},
#  19: {'Caroline General District Court': '033',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=033&curentFipsCode=033'},
#  20: {'Carroll General District Court': '035',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=035&curentFipsCode=035'},
#  22: {'Charlotte General District Court': '037',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=037&curentFipsCode=037'},
#  23: {'Charlottesville General District Court': '540',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=540&curentFipsCode=540'},
#  24: {'Chesapeake General District Court': '550',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=550&curentFipsCode=550'},
#  25: {'Chesterfield General District Court': '041',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=041&curentFipsCode=041'},
#  26: {'Clarke General District Court': '043',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=043&curentFipsCode=043'},
#  28: {'Craig General District Court': '045',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=045&curentFipsCode=045'},
#  29: {'Culpeper General District Court': '047',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=047&curentFipsCode=047'},
#  30: {'Cumberland General District Court': '049',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=049&curentFipsCode=049'},
#  31: {'Danville General District Court': '590',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=590&curentFipsCode=590'},
#  32: {'Dickenson General District Court': '051',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=051&curentFipsCode=051'},
#  33: {'Dinwiddie General District Court': '053',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=053&curentFipsCode=053'},
#  34: {'Emporia General District Court': '595',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=595&curentFipsCode=595'},
#  35: {'Essex General District Court': '057',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=057&curentFipsCode=057'},
#  36: {'Fairfax City General District Court': '059',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=059&curentFipsCode=059'},
#  37: {'Fairfax County General District Court': '059',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=059&curentFipsCode=059'},
#  39: {'Fauquier General District Court': '061',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=061&curentFipsCode=061'},
#  40: {'Floyd General District Court': '063',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=063&curentFipsCode=063'},
#  41: {'Fluvanna General District Court': '065',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=065&curentFipsCode=065'},
#  42: {'Franklin City General District Court': '067',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=067&curentFipsCode=067'},
#  43: {'Franklin County General District Court': '067',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=067&curentFipsCode=067'},
#  44: {'Frederick General District Court': '069',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=069&curentFipsCode=069'},
#  45: {'Fredericksburg General District Court': '630',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=630&curentFipsCode=630'},
#  46: {'Galax General District Court': '640',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=640&curentFipsCode=640'},
#  47: {'Giles General District Court': '071',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=071&curentFipsCode=071'},
#  48: {'Gloucester General District Court': '073',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=073&curentFipsCode=073'},
#  49: {'Goochland General District Court': '075',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=075&curentFipsCode=075'},
#  50: {'Grayson General District Court': '077',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=077&curentFipsCode=077'},
#  51: {'Greene General District Court': '079',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=079&curentFipsCode=079'},
#  52: {'Greensville General District Court': '081',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=081&curentFipsCode=081'},
#  53: {'Halifax General District Court': '083',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=083&curentFipsCode=083'},
#  54: {'Hampton General District Court': '650',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=650&curentFipsCode=650'},
#  55: {'Hanover General District Court': '085',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=085&curentFipsCode=085'},
#  57: {'Henrico General District Court': '087',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=087&curentFipsCode=087'},
#  58: {'Henry General District Court': '089',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=089&curentFipsCode=089'},
#  59: {'Highland General District Court': '091',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=091&curentFipsCode=091'},
#  60: {'Hopewell General District Court': '670',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=670&curentFipsCode=670'},
#  65: {'Lancaster General District Court': '103',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=103&curentFipsCode=103'},
#  66: {'Lee General District Court': '105',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=105&curentFipsCode=105'},
#  68: {'Loudoun General District Court': '107',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=107&curentFipsCode=107'},
#  69: {'Louisa General District Court': '109',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=109&curentFipsCode=109'},
#  70: {'Lunenburg General District Court': '111',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=111&curentFipsCode=111'},
#  71: {'Lynchburg General District Court': '680',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=680&curentFipsCode=680'},
#  72: {'Madison General District Court': '113',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=113&curentFipsCode=113'},
#  73: {'Martinsville General District Court': '690',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=690&curentFipsCode=690'},
#  74: {'Mathews General District Court': '115',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=115&curentFipsCode=115'},
#  75: {'Mecklenburg General District Court': '117',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=117&curentFipsCode=117'},
#  76: {'Middlesex General District Court': '119',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=119&curentFipsCode=119'},
#  79: {'Nelson General District Court': '125',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=125&curentFipsCode=125'},
#  84: {'Norfolk General District Court': '710',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=710&curentFipsCode=710'},
#  85: {'Norfolk General District-Criminal Division': '710',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=710&curentFipsCode=710'},
#  86: {'Norfolk General District-Traffic Division': '710',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=710&curentFipsCode=710'},
#  87: {'Norfolk General District-Civil Division': '710',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=710&curentFipsCode=710'},
#  88: {'Northampton General District Court': '131',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=131&curentFipsCode=131'},
#  89: {'Northumberland General District Court': '133',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=133&curentFipsCode=133'},
#  90: {'Nottoway General District Court': '135',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=135&curentFipsCode=135'},
#  91: {'Orange General District Court': '137',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=137&curentFipsCode=137'},
#  92: {'Page General District Court': '139',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=139&curentFipsCode=139'},
#  93: {'Patrick General District Court': '141',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=141&curentFipsCode=141'},
#  94: {'Petersburg General District Court': '730',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=730&curentFipsCode=730'},
#  95: {'Pittsylvania General District Court': '143',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=143&curentFipsCode=143'},
#  96: {'Portsmouth General District Court': '740',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=740&curentFipsCode=740'},
#  97: {'Powhatan General District Court': '145',
#       'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=145&curentFipsCode=145'},
#  101: {'Pulaski General District Court': '155',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=155&curentFipsCode=155'},
#  102: {'Radford General District Court': '750',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=750&curentFipsCode=750'},
#  103: {'Rappahannock General District Court': '157',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=157&curentFipsCode=157'},
#  104: {'Richmond County General District Court': '159',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=159&curentFipsCode=159'},
#  105: {'Richmond City General District Court': '159',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=159&curentFipsCode=159'},
#  109: {'Richmond Manchester General District Court': '159',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=159&curentFipsCode=159'},
#  110: {'Roanoke City General District Court': '161',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=161&curentFipsCode=161'},
#  111: {'Roanoke County General District Court': '161',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=161&curentFipsCode=161'},
#  112: {'Russell General District Court': '167',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=167&curentFipsCode=167'},
#  113: {'Salem General District Court': '775',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=775&curentFipsCode=775'},
#  114: {'Scott General District Court': '169',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=169&curentFipsCode=169'},
#  115: {'Shenandoah General District Court': '139',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=139&curentFipsCode=139'},
#  116: {'Smyth General District Court': '173',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=173&curentFipsCode=173'},
#  117: {'Southampton General District Court': '175',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=175&curentFipsCode=175'},
#  118: {'Spotsylvania General District Court': '177',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=177&curentFipsCode=177'},
#  119: {'Stafford General District Court': '179',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=179&curentFipsCode=179'},
#  120: {'Staunton General District Court': '790',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=790&curentFipsCode=790'},
#  121: {'Suffolk General District Court': '800',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=800&curentFipsCode=800'},
#  122: {'Surry General District Court': '181',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=181&curentFipsCode=181'},
#  123: {'Sussex General District Court': '183',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=183&curentFipsCode=183'},
#  124: {'Tazewell General District Court': '185',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=185&curentFipsCode=185'},
#  125: {'Virginia Beach General District Court': '000',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=000&curentFipsCode=000'},
#  126: {'Warren General District Court': '187',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=187&curentFipsCode=187'},
#  127: {'Washington General District Court': '157',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=157&curentFipsCode=157'},
#  128: {'Waynesboro General District Court': '820',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=820&curentFipsCode=820'},
#  129: {'Westmoreland General District Court': '193',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=193&curentFipsCode=193'},
#  131: {'Winchester General District Court': '840',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=840&curentFipsCode=840'},
#  133: {'Wythe General District Court': '197',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=197&curentFipsCode=197'},
#  134: {'York General District Court': '199',
#        'url': 'https://eapps.courts.state.va.us/gdcourts/caseSearch.do?fromSidebar=true&searchLanding=searchLanding&searchType=hearingDate&searchDivision=T&searchFipsCode=199&curentFipsCode=199'}}





