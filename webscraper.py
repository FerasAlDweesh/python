from urllib.request import urlopen as newurl
from bs4 import BeautifulSoup as soup

bank_list = ["KFH", "NBK", "BOUBYAN", "CBK", "KIB", "WARBA"]

for bank in bank_list:
	choice = bank_list.index(bank) + 1 
	print(choice, bank)

option = input("Choose a bank from the list: ")

KFH = "https://english.mubasher.info/markets/BK/stocks/KFH"
NBK = "https://english.mubasher.info/markets/BK/stocks/NBK"
BOUBYAN = "https://english.mubasher.info/markets/BK/stocks/BOUBYAN"
CBK = "https://english.mubasher.info/markets/BK/stocks/CBK"
KIB = "https://english.mubasher.info/markets/BK/stocks/KIB"
WARBA = "https://english.mubasher.info/markets/BK/stocks/WARBABANK"

if option == "1":
	url = "https://english.mubasher.info/markets/BK/stocks/KFH"
if option == "2":
	url = "https://english.mubasher.info/markets/BK/stocks/NBK"
if option == "3":
	url = "https://english.mubasher.info/markets/BK/stocks/BOUBYAN"
if option == "4":
	url = "https://english.mubasher.info/markets/BK/stocks/CBK"
if option == "5":
	url = "https://english.mubasher.info/markets/BK/stocks/KIB"
if option == "6":
	url = "https://english.mubasher.info/markets/BK/stocks/WARBABANK"


webpage = newurl(url)
page_html = webpage.read()
webpage.close()

page_soup = soup(page_html, "html.parser")
summary = page_soup.findAll("div", {"class" : "market-summary"})

# print(summary[0])

for parse in summary:
	print("")
	parse = summary[0].text.strip()
	print(parse)