import praw
from title_functions import split_title
import pandas as pd
import time

reddit = praw.Reddit(client_id='eY4fcL32M0QJCA',
                     client_secret='nk4_7j9NNIu-t59frkoQk7sMlB4',
                     user_agent='MechScraper v1.0 by /u/mech_scraper')


def get_posts():
    """
    Iterates through newest posts from reddit.com/r/mechmarket.
    Maximum age of post is 24 hrs (86400s since unix epoch).
    Splits the title using split_title(), creating a dictionary.
    post_dict stores other related info. Dictionaries merged into merged_dict.
    :return recent posts: returns list of post dictionaries
    """
    recent_posts = []

    for submission in reddit.subreddit('mechmarket').new():

        # Looks for posts only within past 24 hours
        if time.time() - submission.created_utc < 86400:

            split_title_dict = split_title(submission.title)

            # Creates dictionary for submission information
            post_dict = {'Title': submission.title,
                         'Flair': submission.link_flair_text,
                         'id': submission.id,
                         'Time Posted': submission.created_utc}

            # Merges Split title info with other post information
            merged_dict = {**split_title_dict, **post_dict}

            # Appends merged submission dictionary to recent post list
            recent_posts.append(merged_dict)

        else:
            break

    return recent_posts


def posts_to_df(post_list):
    """
    :param post_list: A list of dictionaries (containing post info)
    :return post_df: Returns a DataFrame w/ data from the dictionaries
    """

    post_df = pd.DataFrame(posts for posts in post_list)
    post_df.to_csv('mm_new_posts.csv', index=False)

    return post_df


def user_post_search(keyword_list, most_recent_search_UTC):

    recent_posts = []

    for submission in reddit.subreddit('mechmarket').new():

        if submission.created_utc > most_recent_search_UTC:

            for keyword in keyword_list:
                if keyword.lower() in submission.title.lower():

                    split_title_dict = split_title(submission.title)

                    # Creates dictionary for submission information
                    post_dict = {'Title': submission.title,
                                 'Flair': submission.link_flair_text,
                                 'id': submission.id,
                                 'Time Posted': submission.created_utc}

                    # Merges Split title info with other post information
                    merged_dict = {**split_title_dict, **post_dict}

                    # Appends merged submission dictionary to recent post list
                    recent_posts.append(merged_dict)

                else:
                    continue

        else:
            break

    return recent_posts


#print(posts_to_df(get_posts()))
print(posts_to_df((user_post_search(['rama', 'JTK'], 1551565058.0))))
