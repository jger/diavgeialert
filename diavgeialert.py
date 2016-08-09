# This python program check if something new published on diavgeia
# if something new then it send an email
# and return as result the number of items 
# 
# Author: Gerardis Ioannis
# Date: 2016-08-09

# Term and Subject that we looking for
term = 'dipode2'
subject = '%CE%92%CE%B5%CF%81%CE%BF%CE%BB%CE%AF%CE%BD%CE%BF'

def check(term, subject):
  import urllib.request
  from datetime import date
  import json
  d = date.today() # Date for search if today is something new
  date = d.isoformat() 
  url = 'https://diavgeia.gov.gr/opendata/search?term='+term+'&from_date='+date+'&subject='+subject
  response = urllib.request.urlopen(url)
  encoding = response.info().get_content_charset('utf8')
  data = json.loads(response.read().decode(encoding))
  return ([data['info']['actualSize'], data])

