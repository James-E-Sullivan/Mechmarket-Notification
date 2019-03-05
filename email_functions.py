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


def send_matching_posts(user_email, post_df):

    email_body_list = ['Mechmarket posts matching your keywords are listed '
                       'below:\n']

    # iterate through rows in the post DataFrame
    for index, row in post_df.iterrows():
        email_body_list.append('Keyword: ' + row['Keyword'])
        email_body_list.append('Title: ' + row['Title'])
        email_body_list.append('url: ' + row['url'] + '\n')

    # Join each post paragraph into one string to create email body
    email_body = '\n'.join(email_body_list)

    # Set the content of the message to the email_body string
    msg = EmailMessage()
    msg.set_content(email_body)

    # Set Subject, From, and To fields for the email
    msg['Subject'] = 'Mechmarket Notification'
    msg['From'] = 'mechmarket.notification@gmail.com'
    msg['To'] = user_email

    # Send the message via SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)

    # Prompt user for password - this must change before submission
    user_password = input('Enter email password: ')  # Need a constant here

    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(msg['From'], user_password)
    server.send_message(msg)
    server.quit()
