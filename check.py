# This python program check if something new published on diavgeia
#
# the url is in the form of:
# https://diavgeia.gov.gr/opendata/search?term=dipode2&from_date=2016-08-08&subject=%CE%92%CE%B5%CF%81%CE%BF%CE%BB%CE%AF%CE%BD%CE%BF
# and return the number of result items 

import urllib.request

url = 'https://diavgeia.gov.gr/opendata/search?term=dipode2&from_date=2016-08-08&subject=%CE%92%CE%B5%CF%81%CE%BF%CE%BB%CE%AF%CE%BD%CE%BF'


with urllib.request.urlopen(url) as response:
   html = response.read()

print (html)
