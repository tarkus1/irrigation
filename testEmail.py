 
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
smtp_pass='Tuk1uTuk2u'

msg = MIMEText('test')
msg['To'] = addr_to
msg['From'] = addr_from
msg['Subject'] = 'Test Email Really From RPi'

# Send the message via an SMTP server
s = smtplib.SMTP(smtp_server)
s.starttls()
s.login(smtp_user,smtp_pass)
s.sendmail(addr_from, addr_to, msg.as_string())
s.quit()

