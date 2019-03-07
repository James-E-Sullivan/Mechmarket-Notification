from reddit_access import user_post_search, posts_to_df, df_to_csv
from user_information import prompt_user_email, User
from email_functions import send_matching_posts
import time
import sys
import pandas as pd


def check_posts(user):

    post_list = user_post_search(user.get_keywords(),
                                 user.get_most_recent_post())
    post_df = posts_to_df(post_list)

    # if the dataframe contains any data, do the following
    if post_df.shape[0] > 0:

        # Set user's most recent post time to equal the most recent post's time
        user.set_most_recent_post(post_df.loc[0, 'Time Posted'])

        # Send email to user's email address with matching post data
        send_matching_posts(user.get_email(), post_df)
        print('Sent matching posts to', user.get_email())

    # if the dataframe is empty (no matching posts) return nothing
    else:
        pass

    return post_df


def main():

    # Prompt user for email address
    user_email = prompt_user_email()

    # Empty string created for user_keywords
    user_keywords = []

    # Instantiate new User object using user_email and user_keywords
    user1 = User(user_email, user_keywords)

    # Prompt user for initial keyword, and any additional keywords
    user1.prompt_user_keyword()
    user1.prompt_additional_keyword()

    # Post_log is set to an empty pandas DataFrame
    post_log = pd.DataFrame()

    while True:
        try:
            # Checks for new matching posts, emails user if there are matches
            # new_posts references DataFrame of matching post information
            new_posts = check_posts(user1)

            # Concatenate new_posts and post_log
            post_log = pd.concat([post_log, new_posts])
            time.sleep(60)  # Waits 1 minute before checking again

        # If user performs KeyboardInterrupt (ctrl+c), post_log output to .csv
        # and system exits
        except KeyboardInterrupt:
            print('\nExiting Program \n')
            df_to_csv(post_log)  # Outputs runtime matching posts to .csv
            sys.exit()


main()
