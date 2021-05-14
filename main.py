import pandas as pd
import smtplib as sm
your_email = "pooja2000pm@gmail.com"
your_password = "poojapm@170"
  
# establishing connection with gmail
server = sm.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(your_email, your_password)
  
# reading the spreadsheet
email_list = pd.read_excel('C:/test.xlsx')
  
# getting the names and the emails
names = email_list['name']
emails = email_list['email']
print(emails)
  
# iterate through the records
for i in range(len(emails)):
  
    # for every record get the name and the email addresses
    name = names[i]
    email = emails[i]
  
    # the message to be emailed
    message = "Hello " + name 
  
    # sending the email
    server.sendmail(your_email, [email], message)
 
# close the smtp server
server.close()