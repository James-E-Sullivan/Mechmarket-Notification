from reddit_access import user_post_search, posts_to_df, df_to_csv
from user_information import create_new_user
from email_functions import send_matching_posts
import time
import sys
import pandas as pd


def check_posts(user_list):

    for user in user_list:
        post_dict = user_post_search(user.get_keywords(), user.get_most_recent_post())
        post_df = posts_to_df(post_dict)

        if post_df.shape[0] > 0:
            # Set user's most recent post time to equal the most recent post's time
            user.set_most_recent_post(post_df.iloc[0, 3])
            send_matching_posts(user.get_email(), post_df)
            print('Sent matching posts to', user.get_email())

        else:
            pass

        return post_df


def main():

    user_list = []
    user1 = create_new_user()
    user_list.append(user1)

    post_log = pd.DataFrame()

    while True:

        try:
            new_posts = check_posts(user_list)
            post_log.append(new_posts)
            time.sleep(60)

        except KeyboardInterrupt:
            print('Exiting Program \n')
            df_to_csv(post_log)
            sys.exit()


main()
