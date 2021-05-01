import requests
import re
import smtplib
from bs4 import BeautifulSoup
import lxml
source = requests.get('https://www.punchng.com').text #source is punchng
soup = BeautifulSoup(source,'html.parser')
headline=soup.find_all('h3', class_='entry-title')
list=[]
cnt=1
for news in headline:
    list.append((news.a.text))
    cnt=cnt+1
    #print(list)
print(list)
newlist =''.join(list) # create a string
print (newlist)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("kingolaribigbe@gmail.com", "Saheed22")
#list.encode("ascii", errors="replace")
send="kingolaribigbe@gmail.com"
rec="kingolaribigbe@gmail.com"
encodedNewList=newlist.encode("ascii",errors="ignore") #encode the string
msg = "From: %s\r\nTo: %s\r\n\r\n %s" %(send,rec,encodedNewList)
print(encodedNewList)
server.sendmail(
  "kingolaribigbe@gmail.com",
  "kingolaribigbe@gmail.com",
    msg)#smtplib only doesnt allow certain asci hence we have to encode
server.quit()
#print(source.content)


