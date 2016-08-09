# This python program check if something new published on diavgeia
# if something new then it send an email
# 
# Author: Gerardis Ioannis
# Date: 2016-08-09

# Term and Subject that we looking for

##############################################################################

term = 'dipode2'
subject = '%CE%92%CE%B5%CF%81%CE%BF%CE%BB%CE%AF%CE%BD%CE%BF'
me = 'noreply@myhomerpi.gr'
you = 'j.gerardis@gmail.com'

##############################################################################

def check(term, subject, date):
  import urllib.request
  import json
  url = 'https://diavgeia.gov.gr/opendata/search?term='+term+'&from_date='+date+'&subject='+subject
  response = urllib.request.urlopen(url)
  encoding = response.info().get_content_charset('utf8')
  data = json.loads(response.read().decode(encoding))
  return ([data['info']['actualSize'], data])

def mail(me, you, text):
  import smtplib
  from email.mime.text import MIMEText
  msg = MIMEText('Ok! ' + str(text))
  msg['Subject'] = 'New alert! ' + '[' + str(text) + ']' 
  msg['From'] = me
  msg['To'] = you
  s = smtplib.SMTP('localhost')
  s.sendmail(me, [you], msg.as_string()) # For email send you must install postfix or something else you like
  s.quit()

def readvars():
  # Read variables simply stored with | separated
  f = open( '/home/pi/diavgeialert/vars.txt', 'r' )
  vars = f.read()
  f.close
  return vars.split("|")

def writevars(vars):
  # Store variables simply with | separated
  f = open( '/home/pi/diavgeialert/vars.txt', 'w' )
  f.write(vars)
  f.close
  return

###################################################


# Get today date
from datetime import date
d = date.today() # Date for search if today is something new
date = d.isoformat()

# Call the check function
[chk, data] = check(term, subject, date)

# Check if we had something 
if int(chk)>0:
  # Check if this is somthing new
  [fdate, fchk] = readvars()
  if (fdate!=date) or (int(fchk)!=int(chk)):
    writevars(str(date) + '|' + str(chk))
    mail(me, you, chk)
    print('New alert mailed')  
