from email_functions import send_Test_Message
from title_functions import splitTitle
from reddit_access import get_New_Titles

def main():

    new_Titles = get_New_Titles()
    #print(new_Titles[0])
    for i in new_Titles:
        #print(i)
        splitTitle(i)


main()