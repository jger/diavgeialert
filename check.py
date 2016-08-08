# This python program check if something new published on diavgeia
#
# the url is in the form of: https://diavgeia.gov.gr/search?query=q:%22KEY_WORD_HERE%22&page=0&sort=recent
# and return the number of result items 


import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()

# print (html)
