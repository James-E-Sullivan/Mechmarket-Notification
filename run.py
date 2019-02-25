from email_functions import send_Test_Message
from title_functions import split_title, write_title_to_text, append_title_to_text
from reddit_access import get_Ten_Titles


def main():

    new_Titles = get_Ten_Titles()
    #print(new_Titles[0])
    for i in new_Titles:
        #print(i)
        tenTitles = split_title(i)
        append_title_to_text(str(tenTitles))

    send_Test_Message()

main()