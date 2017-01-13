#modules
import requests
from bs4 import BeautifulSoup
import time
import smtplib
#smtplib - library to allow us to email
from email.mime.text import MIMEText
#library - allows to add subject and other various elements

#email
#set the 'from' address,
fromaddr= 'email'
#'to' address
toaddrs = 'email'
#subject
subject = 'New event on bucharest.techhub.com/events/'


#url
url='https://bucharest.techhub.com/events/table/'
#scrape the HTML at url
r_initial=requests.get(url)
#HTML -> BeautifulSoup object
soup_initial=BeautifulSoup(r_initial.text, 'lxml')

#variables to score the data
table_initial=[]

#Object that is class_=table table-striped event-table
table_initial=soup_initial.find(class_="table table-striped event-table")
msg=""
i=0
while i==0:
    time.sleep(43200)
    #scrapes html
    r=requests.get(url)
    #transforms to BeautifulSoup Object
    soup=BeautifulSoup(r.text,'lxml')
    #saves table
    table=soup.find(class_="table table-striped event-table")

    #compares tables
    if table_initial!=table:
        for row in table.find_all('tr')[1:]:
            #each line -> each collumn

            #variable with all <td>
            col=row.find_all('td')

            #collects text between tags
            event=col[0].text
            #event - last character is a newline
            event = event[:-1]
            location=col[1].text
            date=col[2].text
            #above - scrapes data.
            msg=msg+event+'\n'+location+'\n'+date+'\n'+'\n'

            message = 'Subject: %s\n\n%s' % (subject, msg)

        message=message.encode('utf-8')
        # setup the email server,
        server = smtplib.SMTP("smtp.gmail.com", 587)
        # server.starttls()
        server.starttls()
        # add my account login name and password,
        server.login("login_email", "login_email+password")

        # Print the email's msgs
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))


        # send the email
        server.sendmail(fromaddr, toaddrs, message)
        #disconnect from the server
        server.quit()
