# Import smtplib to send email
import smtplib

# Import necessary email modules
from email.message import EmailMessage

def email_Package_Test():

    # Open a text file
    with open('title_file', 'r') as fp:

        msg = EmailMessage()
        msg.set_content(fp.read())

    # From and To can use input() when used in final function
    msg['Subject'] = 'Email Package Test'
    msg['From'] = 'silicaowl@gmail.com'
    msg['To'] = 'silicaowl@gmail.com'

    # Send the message via SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)

    user_name = input('Email Username: ')
    user_password = input('Email Password: ')

    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(user_name, user_password)
    server.send_message(msg)

    server.quit()

def send_Test_Message():

    user_name = input("Please enter your gmail username: ")
    user_password = input("Please enter your gmail password: ")
    from_address = input("Please enter your email address: ")
    to_address = input("Please enter the intended recipient's email address: ")

    text_source = open('title_file', 'r')

    with open('title_file', 'r') as message_file:

        my_message = message_file.read().replace('\n', ' ')

    text_source.close()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(user_name, user_password)
    server.sendmail(
        from_address,
        to_address,
        my_message
    )

    server.quit()

# Test email_Package_Test function
email_Package_Test()