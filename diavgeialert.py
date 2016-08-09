# This python program check if something new published on diavgeia
# if something new then it send an email
# 
# Author: Gerardis Ioannis
# Date: 2016-08-09

# Term and Subject that we looking for
term = 'dipode2'
subject = '%CE%92%CE%B5%CF%81%CE%BF%CE%BB%CE%AF%CE%BD%CE%BF'
me = 'noreply@myhomerpi.gr'
you = 'j.gerardis@gmail.com'

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

def mail(me, you, text):
  import smtplib
  from email.mime.text import MIMEText
  msg = MIMEText('Ok!' + str(text))
  msg['Subject'] = 'You have a new alert!'
  msg['From'] = me
  msg['To'] = you
  s = smtplib.SMTP('localhost')
  s.sendmail(me, [you], msg.as_string()) # For email send you must install postfix or something else you like
  s.quit()

def readvars():
  # Read variables simply stored with | separated
  f = open( 'vars.txt', 'r' )
  vars = f.read()
  f.close
  return vars.split("|")

# Call the check function
[chk, data] = check(term, subject)

# Check if we had something 
if int(chk)>0:
  # Check if this is somthing new
  vars = readvars()
  print (vars[0])
  print (vars[1])
  #mail(me, you, chk)
  
