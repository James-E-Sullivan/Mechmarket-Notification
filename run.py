from email_functions import send_Test_Message
from title_functions import splitTitle, writeTitle, appendTitle
from reddit_access import get_Ten_Titles, get_New_Title

def email_New_Title():
    '''
    Postcondition: Emails newest /r/mechmarket title to specified email address
    '''

    new_Title = get_New_Title()
    writeTitle(str(new_Title[0]))
    send_Test_Message()


def email_Ten_Titles():
    '''
    Postcondition: Emails 10 newest /r/mechmarket titles to specified email address
    '''

    new_Titles = get_Ten_Titles()

    for i in new_Titles:

        tenTitles = splitTitle(i)
        appendTitle(str(tenTitles))

    send_Test_Message()


def main():

    email_New_Title()

main()