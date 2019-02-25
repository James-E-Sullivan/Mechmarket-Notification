import praw

reddit = praw.Reddit(client_id = 'eY4fcL32M0QJCA',
                     client_secret = 'nk4_7j9NNIu-t59frkoQk7sMlB4',
                     user_agent = 'MechScraper v1.0 by /u/mech_scraper')

#print(reddit.read_only)

#for submission in reddit.subreddit('mechmarket').new(limit=10):
#    print(submission.title)


def get_Ten_Titles():
    '''
    Postcondition: Returns the 10 most recent /r/mechmarket post titles
    '''

    recent_titles = []

    for submission in reddit.subreddit('mechmarket').new(limit=10):
        # print(submission.title)
        recent_titles.append(submission.title)

    return recent_titles


def get_Ten_Posts():

    recent_posts = []

    for submission in reddit.subreddit('mechmarket').new(limit=10):

        # Creates dictionary for submission information
        post_dict = {'Title': submission.title,
                     'Flair': submission.link_flair_text,
                     'id': submission.id,
                     'Time': submission.created_utc}

        # Appends submission dictionary to recent post list
        recent_posts.append(post_dict)

    return recent_posts


#get_Ten_Titles()
print(get_Ten_Posts())

def get_New_Title():
    '''
    Postcondition: Returns the newest /r/mechmarket post title
    '''

    newest_title = []

    for submission in reddit.subreddit('mechmarket').new(limit=1):
        newest_title.append(submission.title)

    return newest_title

def get_Attributes():

    attributes_dict = {"title": [], \
                       "url": [], \
                       "id": [], \
                       "created": []}

    for submission in reddit.subreddit('mechmarket').new(limit=1):
        attributes_dict["title"].append(submission.title)
        attributes_dict["url"].append(submission.url)
        attributes_dict["id"].append(submission.id)
        attributes_dict["created"].append(submission.created)

    attributes_data = pd.DataFrame(attributes_dict)
    attributes_data.to_csv('mm_new_posts.csv', index = False)

get_Attributes()