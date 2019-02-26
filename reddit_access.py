import praw
from title_functions import split_title
import pandas as pd
import time

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


def get_posts():

    recent_posts = []

    for submission in reddit.subreddit('mechmarket').new():

        # Looks for posts only within past 24 hours
        if time.time() - submission.created_utc < 86400:

            split_title_dict = split_title(submission.title)

            # Creates dictionary for submission information
            post_dict = {'Title': submission.title,
                         'Flair': submission.link_flair_text,
                         'id': submission.id,
                         'Time': submission.created_utc}

            merged_dict = {**split_title_dict, **post_dict}

            # Appends submission dictionary to recent post list
            recent_posts.append(merged_dict)

        else:
            break

    return recent_posts


def posts_to_df(post_list):

    post_df = pd.DataFrame(posts for posts in post_list)
    post_df.to_csv('mm_new_posts.csv', index=False)

    return post_df



print(posts_to_df(get_posts()))


#get_Ten_Titles()
#print(get_Ten_Posts())


def get_New_Title():
    '''
    Postcondition: Returns the newest /r/mechmarket post title
    '''

    newest_title = []

    for submission in reddit.subreddit('mechmarket').new(limit=1):
        newest_title.append(submission.title)

    return newest_title

def get_Attributes():

    attributes_dict = {"title": [],
                       "url": [],
                       "id": [],
                       "created": []}

    for submission in reddit.subreddit('mechmarket').new(limit=1):
        attributes_dict["title"].append(submission.title)
        attributes_dict["url"].append(submission.url)
        attributes_dict["id"].append(submission.id)
        attributes_dict["created"].append(submission.created)

    attributes_data = pd.DataFrame(attributes_dict)
    attributes_data.to_csv('mm_new_posts.csv', index = False)
