 
# Import smtplib for the actual sending function
import smtplib
import os


# Import the email modules we'll need

from email.message import EmailMessage

# Define email addresses to use
addr_to = 'mark_perrin@hotmail.com'
addr_from = 'mark_perrin@hotmail.com'

# Define SMTP email server details
smtp_server = 'smtp-mail.outlook.com'
smtp_user='mark_perrin@hotmail.com'
smtp_pass='Tuk3uTuk4u'

# Construct email

textfile = ("/home/pi/testemail.csv")
            
            

# Open the plain text file whose name is in textfile for reading.
with open(textfile) as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())


msg['To'] = addr_to
msg['From'] = addr_from
msg['Subject'] = 'Test Email From RPi'

# Send the message via an SMTP server
s = smtplib.SMTP(smtp_server)
s.starttls()
s.login(smtp_user,smtp_pass)
s.sendmail(addr_from, addr_to, msg.as_string())
s.quit()

