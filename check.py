# This python program check if something new published on diavgeia
#
# the url is in the form of:
# https://diavgeia.gov.gr/opendata/search?term=KEYWORD&from_date=DATE&subject=SUBJECT
# and return as result the number of items 
# 
# Author: Gerardis Ioannis
# Date: 2016-08-09

import urllib.request
from datetime import date
import json

d = date.today()
date = d.isoformat() 
term = 'dipode2' # example
subject = '%CE%92%CE%B5%CF%81%CE%BF%CE%BB%CE%AF%CE%BD%CE%BF' # example
url = 'https://diavgeia.gov.gr/opendata/search?term='+term+'&from_date='+date+'&subject='+subject
response = urllib.request.urlopen(url)
encoding = response.info().get_content_charset('utf8')
data = json.loads(response.read().decode(encoding))

print(data['info']['actualSize'])
