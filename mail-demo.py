import os
import smtplib

# EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

with smtplib.SMTP('localhost', 1027) as smtp:
    # smtp.ehlo()
    # smtp.starttls()
    # smtp.ehlo()
        
    # smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Check the smtplib in python'
    body = 'It is successful experiment.'
    msg = f'Subject: {subject} \n\n{body}'

    smtp.sendmail('siddharth.a@simformsolutions.com','siddharth.a@simformsolutions.com',msg)                                       


""" siddharthasodariya@sf-cpu-213:~$ python3 -m smtpd -c DebuggingServer -n localhost:1027
---------- MESSAGE FOLLOWS ----------
b'This is a plain text email'
------------ END MESSAGE ------------
---------- MESSAGE FOLLOWS ----------
b'Subject: Check the smtplib in python '
b'X-Peer: 127.0.0.1'
b''
b'It is successful experiment.'
------------ END MESSAGE ------------ """


# ------------------------------------------------------------SMTP_SSL()--------------------------------------------------------------

import smtplib, ssl

port = 465  # For SSL
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("my@gmail.com", password)
    # TODO: Send email here



""" There are two ways to start a secure connection with your email server:

    Start an SMTP connection that is secured from the beginning using SMTP_SSL().
    Start an unsecured SMTP connection that can then be encrypted using .starttls(). """


# ------------------------------------------------------------.starttls()--------------------------------------------------------------

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "my@gmail.com"
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    # TODO: Send email here
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 




# 'siddharth.a@simformsolutions.com'
# import os
# import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['YourAddress@gmail.com', 'test@example.com']

msg = EmailMessage()
msg['Subject'] = 'Check out Bronx as a puppy!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'YourAddress@gmail.com'

msg.set_content('This is a plain text email')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)