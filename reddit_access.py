import praw
import pandas as pd
import time

reddit = praw.Reddit(client_id='eY4fcL32M0QJCA',
                     client_secret='nk4_7j9NNIu-t59frkoQk7sMlB4',
                     user_agent='MechScraper v1.0 by /u/mech_scraper')


def split_title(title):

    if '[H]' in title and '[W]' in title:

        split_H = title.split('[H]')
        location_tag = split_H[0].strip(' ')
        split_W = split_H[1].split('[W]')
        have_string = split_W[0].strip(' ')
        want_string = split_W[1].strip(' ')

        split_title_dict = {'Location': location_tag,
                            'User Has': have_string,
                            'User Wants': want_string}

        return split_title_dict

    else:
        split_title_dict = {'Location': 'N/A',
                            'User Has': 'N/A',
                            'User Wants': 'N/A'}

        return split_title_dict


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

        if submission.created_utc <= most_recent_search_UTC:

            pass

        elif submission.created_utc > most_recent_search_UTC:

            for keyword_dict in keyword_list:
                if keyword_dict['Keyword'].lower() in submission.title.lower():

                    split_title_dict = split_title(submission.title)

                    # Creates dictionary for submission information
                    # Will create duplicate dictionary if post has multiple
                    # keywords
                    post_dict = {'Title': submission.title,
                                 'Flair': submission.link_flair_text,
                                 'id': submission.id,
                                 'url': submission.url,
                                 'Time Posted': submission.created_utc,
                                 'Keyword': keyword_dict['Keyword']}

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
#test_df = posts_to_df((user_post_search([{'Keyword': 'GMK', 'Action': 1}, {'Keyword': 'RAMA', 'Action': 2}], 1551752447.0)))

#for index, row in test_df.iterrows():
    #print(row['url'])
