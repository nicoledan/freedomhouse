from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv

hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

site = "https://freedomhouse.org"

countries = ["/report/freedom-press/2016/united-states",
"/report/freedom-press/2016/canada",
"/report/freedom-press/2016/denmark",
"/report/freedom-press/2016/mexico",
"/report/freedom-press/2016/guatemala",
"/report/freedom-press/2016/belize",
"/report/freedom-press/2016/afghanistan",
"/report/freedom-press/2016/albania",
"/report/freedom-press/2016/algeria",
"/report/freedom-press/2016/angola",
"/report/freedom-press/2016/antigua-and-barbuda",
"/report/freedom-press/2016/argentina",
"/report/freedom-press/2016/armenia",
"/report/freedom-press/2016/australia",
"/report/freedom-press/2016/austria",
"/report/freedom-press/2016/azerbaijan",
"/report/freedom-press/2016/bahamas",
"/report/freedom-press/2016/bahrain",
"/report/freedom-press/2016/bangladesh",
"/report/freedom-press/2016/barbados",
"/report/freedom-press/2016/belarus",
"/report/freedom-press/2016/belgium",
"/report/freedom-press/2016/benin",
"/report/freedom-press/2016/bhutan",
"/report/freedom-press/2016/bolivia",
"/report/freedom-press/2016/bosnia-and-herzegovina",
"/report/freedom-press/2016/botswana",
"/report/freedom-press/2016/brazil",
"/report/freedom-press/2016/brunei",
"/report/freedom-press/2016/bulgaria",
"/report/freedom-press/2016/burkina-faso",
"/report/freedom-press/2016/burundi",
"/report/freedom-press/2016/cambodia",
"/report/freedom-press/2016/cameroon",
"/report/freedom-press/2016/cape-verde",
"/report/freedom-press/2016/central-african-republic",
"/report/freedom-press/2016/chad",
"/report/freedom-press/2016/chile",
"/report/freedom-press/2016/china",
"/report/freedom-press/2016/colombia",
"/report/freedom-press/2016/comoros",
"/report/freedom-press/2016/congo-democratic-republic-kinshasa",
"/report/freedom-press/2016/congo-republic-brazzaville",
"/report/freedom-press/2016/costa-rica",
"/report/freedom-press/2016/c-te-divoire",
"/report/freedom-press/2016/crimea",
"/report/freedom-press/2016/croatia",
"/report/freedom-press/2016/cuba",
"/report/freedom-press/2016/cyprus",
"/report/freedom-press/2016/czech-republic",
"/report/freedom-press/2016/djibouti",
"/report/freedom-press/2016/dominica",
"/report/freedom-press/2016/dominican-republic",
"/report/freedom-press/2016/ecuador",
"/report/freedom-press/2016/egypt",
"/report/freedom-press/2016/el-salvador",
"/report/freedom-press/2016/equatorial-guinea",
"/report/freedom-press/2016/eritrea",
"/report/freedom-press/2016/estonia",
"/report/freedom-press/2016/ethiopia",
"/report/freedom-press/2016/fiji",
"/report/freedom-press/2016/finland",
"/report/freedom-press/2016/france",
"/report/freedom-press/2016/gabon",
"/report/freedom-press/2016/gambia",
"/report/freedom-press/2016/georgia",
"/report/freedom-press/2016/germany",
"/report/freedom-press/2016/ghana",
"/report/freedom-press/2016/greece",
"/report/freedom-press/2016/grenada",
"report/freedom-press/2016/guinea",
"/report/freedom-press/2016/guinea-bissau",
"/report/freedom-press/2016/guyana",
"/report/freedom-press/2016/haiti",
"/report/freedom-press/2016/honduras",
"/report/freedom-press/2016/hungary",
"/report/freedom-press/2016/hong-kong",
"/report/freedom-press/2016/iceland",
"/report/freedom-press/2016/india",
"/report/freedom-press/2016/indonesia",
"/report/freedom-press/2016/iran",
"/report/freedom-press/2016/iraq",
"/report/freedom-press/2016/ireland",
"/report/freedom-press/2016/israel",
"/report/freedom-press/2016/italy",
"/report/freedom-press/2016/jamaica",
"/report/freedom-press/2016/japan",
"/report/freedom-press/2016/jordan",
"/report/freedom-press/2016/kazakhstan",
"/report/freedom-press/2016/kenya",
"/report/freedom-press/2016/kiribati",
"/report/freedom-press/2016/kosovo",
"/report/freedom-press/2016/kuwait",
"/report/freedom-press/2016/kyrgyzstan",
"/report/freedom-press/2016/laos",
"/report/freedom-press/2016/latvia",
"/report/freedom-press/2016/lebanon",
"/report/freedom-press/2016/lesotho",
"/report/freedom-press/2016/liberia",
"/report/freedom-press/2016/libya",
"/report/freedom-press/2016/liechtenstein",
"/report/freedom-press/2016/lithuania",
"/report/freedom-press/2016/luxembourg",
"/report/freedom-press/2016/macedonia",
"/report/freedom-press/2016/madegascar",
"/report/freedom-press/2016/malawi",
"/report/freedom-press/2016/malaysia",
"/report/freedom-press/2016/maldives",
"/report/freedom-press/2016/mali",
"/report/freedom-press/2016/malta",
"/report/freedom-press/2016/marshall-islands",
"/report/freedom-press/2016/mauritania",
"/report/freedom-press/2016/mauritius",
"/report/freedom-press/2016/mexico",
"/report/freedom-press/2016/micronesia",
"/report/freedom-press/2016/moldova",
"/report/freedom-press/2016/monaco",
"/report/freedom-press/2016/mongolia",
"/report/freedom-press/2016/montenegro",
"/report/freedom-press/2016/morocco",
"/report/freedom-press/2016/mozambique",
"/report/freedom-press/2016/myanmar",
"/report/freedom-press/2016/namibia",
"report/freedom-press/2016/nauru",
"/report/freedom-press/2016/nepal",
"/report/freedom-press/2016/netherlands",
"/report/freedom-press/2016/new-zealand",
"/report/freedom-press/2016/nicaragua",
"/report/freedom-press/2016/niger",
"/report/freedom-press/2016/nigeria",
"/report/freedom-press/2016/north-korea",
"/report/freedom-press/2016/norway",
"/report/freedom-press/2016/oman",
"/report/freedom-press/2016/pakistan",
"/report/freedom-press/2016/palau",
"/report/freedom-press/2016/panama",
"/report/freedom-press/2016/papua-new-guinea",
"/report/freedom-press/2016/paraguay",
"/report/freedom-press/2016/peru",
"/report/freedom-press/2016/phillippines",
"/report/freedom-press/2016/poland",
"/report/freedom-press/2016/portugal",
"/report/freedom-press/2016/qatar",
"/report/freedom-press/2016/romania",
"/report/freedom-press/2016/russia",
"/report/freedom-press/2016/rwanda",
"/report/freedom-press/2016/samoa",
"/report/freedom-press/2016/san-marino",
"/report/freedom-press/2016/s-o-tom-and-pr-ncipe",
"/report/freedom-press/2016/saudi-arabia",
"/report/freedom-press/2016/senegal",
"/report/freedom-press/2016/serbia",
"/report/freedom-press/2016/seychelles",
"/report/freedom-press/2016/sierra-leone",
"/report/freedom-press/2016/singapore",
"/report/freedom-press/2016/slovakia",
"/report/freedom-press/2016/slovenia",
"/report/freedom-press/2016/solomon-islands",
"/report/freedom-press/2016/somalia",
"/report/freedom-press/2016/somaliland",
"/report/freedom-press/2016/south-africa",
"/report/freedom-press/2016/south-korea",
"/report/freedom-press/2016/south-sudan",
"/report/freedom-press/2016/spain",
"/report/freedom-press/2016/sri-lanka",
"/report/freedom-press/2016/st-kitts-and-nevis",
"/report/freedom-press/2016/st-lucia",
"/report/freedom-press/2016/st-vincent-and-grenadines",
"/report/freedom-press/2016/sudan",
"/report/freedom-press/2016/suriname",
"/report/freedom-press/2016/swaziland",
"/report/freedom-press/2016/sweden",
"/report/freedom-press/2016/switzerland",
"/report/freedom-press/2016/syria",
"/report/freedom-press/2016/taiwan",
"/report/freedom-press/2016/tajikistan",
"/report/freedom-press/2016/tanzania",
"/report/freedom-press/2016/thailand",
"/report/freedom-press/2016/timor-leste",
"/report/freedom-press/2016/togo",
"/report/freedom-press/2016/tonga",
"/report/freedom-press/2016/trinidad-and-tobago",
"/report/freedom-press/2016/tunisia",
"/report/freedom-press/2016/turkey",
"/report/freedom-press/2016/turkmenistan",
"/report/freedom-press/2016/tuvalu",
"/report/freedom-press/2016/uganda",
"/report/freedom-press/2016/ukraine",
"/report/freedom-press/2016/united-arab-emirates",
"/report/freedom-press/2016/united-kingdom",
"/report/freedom-press/2016/uruguay",
"/report/freedom-press/2016/uzbekistan",
"/report/freedom-press/2016/vanuatu",
"/report/freedom-press/2016/venezuela",
"/report/freedom-press/2016/vietnam",
"/report/freedom-press/2016/west-bank-and-gaza-strip",
"/report/freedom-press/2016/yemen",
"/report/freedom-press/2016/zambia",
"/report/freedom-press/2016/zimbabwe"
 ]

def open_page(site, hdr):
    """
    Opens a URL using the header info and creates a BeautifulSoup object.
    """
    new_url = site + str(countries)
    req = Request(new_url, headers=hdr)
    try:
        html = urlopen(req)
    except HTTPError as e:
        print(e.reason)
    bsObj = BeautifulSoup(html.read(), "html.parser")
    return bsObj

bsObj = open_page(new_url, hdr)

pages =[]
content = []

def getDetails(pages):
    global content
    for value in pages:
        html = urlopen(value)
        bsObj = BeatifulSoup(html, "html.parser")
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


def CSV(content):
    filename = "freedomhouse.csv"
    with open(filename, 'w') as output_file:
        fieldnames = [ 'names', 'pressstatuses', 'legals', 'politicals', 'economics', 'pressscores', 'populations', 'netfreedoms', 'freedomworlds', 'internets' ]
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(content)



getDetails(pages)
CSV(content)
