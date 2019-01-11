import praw

reddit = praw.Reddit(client_id = 'eY4fcL32M0QJCA',
                     client_secret = 'nk4_7j9NNIu-t59frkoQk7sMlB4',
                     user_agent = 'MechScraper v1.0 by /u/mech_scraper')

print(reddit.read_only)

#for submission in reddit.subreddit('mechmarket').new(limit=10):
#    print(submission.title)

def get_New_Titles():
    '''
    Postcondition: Returns the 10 most recent /r/mechmarket post titles
    '''


    for submission in reddit.subreddit('mechmarket').new(limit=10):
        print(submission.title)

get_New_Titles()