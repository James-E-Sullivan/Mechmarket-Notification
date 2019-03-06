# Import smtplib to send email
import smtplib

# Import necessary email modules
from email.message import EmailMessage

# Import email password from secrets.py file
from secrets import MM_PASSWORD


def send_matching_posts(user_email, post_df):

    # Creates first line of email body. List items will be joined.
    email_body_list = ['Mechmarket posts matching your keywords are listed '
                       'below:\n']

    # iterate through rows in the post DataFrame
    # appends Keyword, Title, and url of each row to email_body_list
    for index, row in post_df.iterrows():
        email_body_list.append('Keyword: ' + row['Keyword'])
        email_body_list.append('Title: ' + row['Title'])
        email_body_list.append('url: ' + row['url'] + '\n')

    # Join each post paragraph into one string to create email_body
    email_body = '\n'.join(email_body_list)

    # Set the content of the message to the email_body string
    msg = EmailMessage()
    msg.set_content(email_body)

    # Set Subject, From, and To fields for the email
    msg['Subject'] = 'Mechmarket Notification'
    msg['From'] = 'mechmarket.notification@gmail.com'
    msg['To'] = user_email

    # Password for Gmail account that will be sending email
    user_password = MM_PASSWORD

    # Send the message via SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(msg['From'], user_password)
    server.send_message(msg)
    server.quit()
