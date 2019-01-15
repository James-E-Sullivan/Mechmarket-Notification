import praw

reddit = praw.Reddit(client_id = 'eY4fcL32M0QJCA',
                     client_secret = 'nk4_7j9NNIu-t59frkoQk7sMlB4',
                     user_agent = 'MechScraper v1.0 by /u/mech_scraper')

def get_Ten_Titles():
    '''
    Postcondition: Returns the 10 most recent /r/mechmarket post titles
    '''

    recent_titles = []


    for submission in reddit.subreddit('mechmarket').new(limit=10):
        recent_titles.append(submission.title)

    return recent_titles

def get_New_Title():
    '''
    Postcondition: Returns the newest /r/mechmarket post title
    '''

    newest_title = []

    for submission in reddit.subreddit('mechmarket').new(limit=1):
        newest_title.append(submission.title)

    return newest_title