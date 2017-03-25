from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv

hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

site = "https://freedomhouse.org/report/freedom-press/2016/united-states"

def open_page(site, hdr):
    """
    Opens a URL using the header info and creates a BeautifulSoup object.
    """
    req = Request(site, headers=hdr)
    try:
        html = urlopen(req)
    except HTTPError as e:
        print(e.reason)
    bsObj = BeautifulSoup(html.read(), "html.parser")
    return bsObj

bsObj = open_page(site, hdr)

pages =[]
content = []

"""
name of the country

names = bsObj.findAll("h2", {"class":"pane-title"})

names of the categories
"""
'''
pstatuses = bsObj.findAll("div", {"class":"field-label"}) [1::9]
legalenvs = bsObj.findAll("div", {"class":"field-label"}) [2::9]
polienvs = bsObj.findAll("div", {"class":"field-label"}) [3::9]
econenvs = bsObj.findAll("div", {"class":"field-label"}) [4::9]
pressfrees = bsObj.findAll("div", {"class":"field-label"}) [5::9]
pops = bsObj.findAll("div", {"class":"field-label"}) [6::9]
netfrees = bsObj.findAll("div", {"class":"field-label"}) [7::9]
freeworlds =  bsObj.findAll("div", {"class":"field-label"}) [8::9]
netpenetrations = bsObj.findAll("div", {"class":"field-label"}) [9::9]
'''
"""
data
"""

names = bsObj.findAll("h2", {"class":"pane-title"}),
pressstatuses = bsObj.findAll("div", {"class":"field-items"})[4::12]
legals = bsObj.findAll("div", {"class":"field-items"})[5::12]
politicals = bsObj.findAll("div", {"class":"field-items"})[6::12]
economics = bsObj.findAll("div", {"class":"field-items"})[7::12]
pressscores = bsObj.findAll("div", {"class":"field-items"})[8::12]
populations = bsObj.findAll("div", {"class":"field-items"})[9::12]
netfreedoms = bsObj.findAll("div", {"class":"field-items"})[10::12]
freedomworlds = bsObj.findAll("div", {"class":"field-items"})[11::12]
internets = bsObj.findAll("div", {"class":"field-items"})[12::12]



"""
loops
"""
'''
for name in names:
    print(name.get_text())

for pstatus in pstatuses:
    print(pstatus.get_text())

for legalenv in legalenvs:
    print(legalenv.get_text())

for polienv in polienvs:
    print(polienv.get_text())

for econenv in econenvs:
    print(econenv.get_text())

for pressfree in pressfrees:
    print(pressfree.get_text())

for pop in pops:
    print(pop.get_text())

for netfree in netfrees:
    print(netfree.get_text())

for freeworld in freeworlds:
    print(freeworld.get_text())

for netpenetration in netpenetrations:
    print(netpenetration.get_text())
'''
"""
end of categories beginning of data
"""
'''
for pressstatus in pressstatuses:
    print(pressstatus.get_text())

for legal in legals:
    print(legal.get_text())

for political in politicals:
    print(political.get_text())

for economic in economics:
    print(economic.get_text())

for pressscore in pressscores:
    print(pressscore.get_text())

for population in populations:
    print(population.get_text())

for netfreedom in netfreedoms:
    print(netfreedom.get_text())

for freedomworld in freedomworlds:
    print(freedomworld.get_text())

for internet in internets:
    print(internet.get_text())
'''

def CSV(content):
    filename = "freedomhouse.csv"
    with open(filename, 'w') as output_file:
        fieldnames = [ 'names', 'pressstatuses', 'legals', 'politicals', 'economics', 'pressscores', 'populations', 'netfreedoms', 'freedomworlds', 'internets' ]
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(content)



getDetails(pages)
CSV(content)
