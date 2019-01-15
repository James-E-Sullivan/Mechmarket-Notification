def send_Test_Message():
    import smtplib

    user_name = input("Please enter your gmail username: ")
    user_password = input("Please enter your gmail password: ")
    from_address = input("Please enter your email address: ")
    to_address = input("Please enter the intended recipient's email address: ")

    text_source = open('textfile', 'r')

    with open('textfile', 'r') as message_file:

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