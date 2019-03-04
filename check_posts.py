from email_functions import send_Test_Message
from title_functions import split_title
from reddit_access import user_post_search, posts_to_df
from user_information import User, create_new_user


def main():

    user_list = []
    user1 = create_new_user()
    user_list.append(user1)

    for user in user_list:
        user_post_search(user.get_keywords(), user.get_most_recent_post())



main()
