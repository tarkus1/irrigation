import subprocess
import csv
import re


from time import sleep
from datetime import datetime


emailSent=False


def timeToWater(dateS):

     
    # Import smtplib for the actual sending function
    import smtplib
    import os


    # Import the email modules we'll need

    from email.mime.text import MIMEText

    # Define email addresses to use
    addr_to = 'mark_perrin@hotmail.com'
    addr_from = 'mark_perrin@hotmail.com'

    # Define SMTP email server details
    smtp_server = 'smtp-mail.outlook.com'
    smtp_user='mark_perrin@hotmail.com'
    smtp_pass='Tuk3uTuk4u'

    msgStr='Time to water the plant in the office as of '+dateS
    print(msgStr)

    msg = MIMEText(msgStr)

    msg['To'] = addr_to
    msg['From'] = addr_from
    msg['Subject'] = 'Time to water the plant From RPi'

    # Send the message via an SMTP server
    s = smtplib.SMTP(smtp_server)
    s.starttls()
    s.login(smtp_user,smtp_pass)
    s.sendmail(addr_from, addr_to, msg.as_string())
    s.quit()


while True:
# if True:

    try:
            
        p = subprocess.Popen(["owwrite", "26.241E9D010000/date", "0"])

        p = subprocess.Popen(["owread", "26.241E9D010000/date"], stdout=subprocess.PIPE)

        (date,errcode) = p.communicate()
        dateObj = datetime.strptime(date.decode(),'%a %b %d %H:%M:%S %Y')
        dateS = datetime.strftime(dateObj,'%Y-%m-%d %X')
        # print(datetime.strftime(dateObj,'%Y%m%d %X'))

        print("Time: ",dateS)

        p = subprocess.Popen(["owread", "26.241E9D010000/temperature"], stdout=subprocess.PIPE)

        (temp,errcode) = p.communicate()
        print("Temp: ", float(temp))

        p = subprocess.Popen(["owread", "26.241E9D010000/humidity"], stdout=subprocess.PIPE)

        (output,errcode) = p.communicate()
        #print(output)

        humid = float(output)
        print("Moisture: ", humid)

        if humid < 200 and humid > 10:
            print('okay')
            # red.off()
            # gr.on()
            emailSent=False
        else :
            print('dry');
            # gr.off();
            # red.on()
            if not emailSent :
                timeToWater(dateS)
                emailSent=True

        therow=(dateS,float(temp),float(humid))
        # print(therow)
        
        f = open('officePlant.csv', 'a', newline='')
        writer = csv.writer(f)
        writer.writerow(therow)
        f.close()

    except Exception as e:
        print (e)

    finally:    
        sleep(60)

