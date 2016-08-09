# This python program check if something new published on diavgeia
#
# the url is in the form of:
# https://diavgeia.gov.gr/opendata/search?term=KEYWORD&from_date=DATE&subject=SUBJECT
# and return the number of result items 

import urllib.request
from datetime import date
import xml.etree.ElementTree as etree 
import json



d = date.today()
date = d.isoformat() 

term = 'dipode2'
subject = '%CE%92%CE%B5%CF%81%CE%BF%CE%BB%CE%AF%CE%BD%CE%BF'
url = 'https://diavgeia.gov.gr/opendata/search?term='+term+'&from_date='+date+'&subject='+subject


#with urllib.request.urlopen(url) as response:
#   json = response.read()

#print(json)
response = urllib.request.urlopen(url)
encoding = response.info().get_content_charset('utf8')
data = json.loads(response.read().decode(encoding))
