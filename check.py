# This python program check if something new published on diavgeia
#
# the url is in the form of:
# https://diavgeia.gov.gr/opendata/search?term=KEYWORD&from_date=DATE&subject=SUBJECT
# and return the number of result items 

import urllib.request
from datetime import date
#from xml.dom.minidom import parse
#import xml.dom.minidom
import xml.etree.ElementTree as etree 




d = date.today()
date = d.isoformat() 

term = 'dipode2'
subject = '%CE%92%CE%B5%CF%81%CE%BF%CE%BB%CE%AF%CE%BD%CE%BF'
url = 'https://diavgeia.gov.gr/opendata/search?term='+term+'&from_date='+date+'&subject='+subject


with urllib.request.urlopen(url) as response:
   json = response.read()

# Open XML document using minidom parser
#DOMTree = xml.dom.minidom.parse(xml)
#decisions = DOMTree.documentElement
#info = decisions.getElementsByTagName("info")

#print (info.childNodes[0].data)
#print (info.childNodes[1].data)


print(json)
#tree = etree.ElementTree(etree.fromstring(xml))
