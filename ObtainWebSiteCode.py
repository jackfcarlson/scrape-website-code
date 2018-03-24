import bs4 as bs
import urllib.request

rawData = urllib.request.urlopen('website URL Here').read()

filteredPage = bs.BeautifulSoup(rawData, 'lxml')

#print(rawData) would contain print(filteredPage) along with /t and /n and other "invisible" characters.
#filteredPage displays/prints what you would see if you went to a website and clicked "View Page Source".
print(filteredPage)
