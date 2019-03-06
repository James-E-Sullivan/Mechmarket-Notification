import praw
import pandas as pd
from secrets import PRAW_CLIENT_SECRET

reddit = praw.Reddit(client_id='eY4fcL32M0QJCA',
                     client_secret=PRAW_CLIENT_SECRET,
                     user_agent='MechScraper v1.0 by /u/mech_scraper')


def posts_to_df(post_list):
    """
    :param post_list: A list of dictionaries (containing post info)
    :return post_df: Returns a DataFrame w/ data from the dictionaries
    """

    # Create a pandas DataFrame using post_list data.
    # post_list dictionary keywords will be column headers
    post_df = pd.DataFrame(posts for posts in post_list)

    return post_df


def df_to_csv(post_df):

    post_df.to_csv('mm_new_posts.csv', index=False)


def user_post_search(keyword_list, most_recent_search_utc):

    recent_posts = []

    # Iterates through /r/mechmarket posts, starting at the most recent
    for submission in reddit.subreddit('mechmarket').new():

        # If the post is older (or the same) as the most recent post sent to
        # user, then the function ends and does not return anything
        if submission.created_utc <= most_recent_search_utc:
            pass

        # If the post is newer than the most recent post sent to user, post
        # information is recorded in a dictionary
        elif submission.created_utc > most_recent_search_utc:

            # Iterates through keyword dictionaries (containing keyword, and
            # action (buy/sell/trade) within the user's keyword_list
            for keyword in keyword_list:

                if keyword.lower() in submission.title.lower():

                    # Creates dictionary for submission information
                    # Will create duplicate dictionary if post has multiple
                    # keywords
                    post_dict = {'Title': submission.title,
                                 'Flair': submission.link_flair_text,
                                 'id': submission.id,
                                 'url': submission.url,
                                 'Time Posted': submission.created_utc,
                                 'Keyword': keyword}

                    # Appends post dictionary to recent post list
                    recent_posts.append(post_dict)

                else:
                    continue

        else:
            break

    return recent_posts
