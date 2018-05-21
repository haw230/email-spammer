import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
from time import sleep
gmail = 'x@gmail.com'
pw = 'password'
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login(gmail, pw)
alpha = 'stuvwxyz'

start = 0
for letter in alpha:
    count = 0
    temp = requests.get("http://universities.hipolabs.com/search?country=United%20States&name=" + letter).json()
    for i in range(start, len(temp)):
        dom = "admissions@" + temp[i]['domains'][0]
        bodyText = "Dear " + temp[i]['name'] + """
        , \n\nI am a high school senior in Canada interested in heading south for college. 
        I am an academically-driven student (top 3% of largest school in the province and 99th percentile SAT) looking for a rigorous 
        education, and " + temp[i]['name'] + " seems like the perfect match. However, being in Canada, it is difficult to find both time 
        and money to travel and take a look at the open house. But if there is anything (swag, brochures, shirts etc) left over, I would 
        love it. My mailing address is X. Postal code is Y.
        """
        bodyText = bodyText + "\n\n Thank you in advance! \n "
        msg = MIMEText(bodyText)
        msg['Subject'] = 'Prospective Canadian High School Student'
        msg['From'] = gmail
        msg['Reply-To'] = gmail
        msg['To'] = dom
        mail.sendmail(gmail, dom, msg.as_string())
        count += 1
        if(count == 35):
            count = 0
            mail.quit()
            sleep(700)
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login(gmail, pw)
        print("Sent")
        sleep(1)
        f = open('log.txt','w')
        f.write(letter + str(i) + "\n")
        f.close()
    start = 0

