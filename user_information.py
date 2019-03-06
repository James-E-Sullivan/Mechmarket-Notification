import time


class User:
    """
    User class stores information about the user, including email address,
    a list of keywords of items they want to buy, sell, or trade on reddit,
    and the time of the most recent post that was returned to them by the
    program.
    """
    def __init__(self, email, keyword_list):
        self.__email = email
        self.keyword_list = keyword_list
        self.most_recent_post = time.time()  # initialized with current time

    def add_keyword(self, new_keyword):
        self.keyword_list.append(new_keyword)

    def get_keywords(self):
        return self.keyword_list

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        self.__email = new_email

    def get_most_recent_post(self):
        return self.most_recent_post

    def set_most_recent_post(self, post_time):
        self.most_recent_post = post_time

    def __repr__(self):
        return "Email: " + repr(self.__email) + "Most recent post: " + \
               repr(self.most_recent_post) + \
               "Keyword List: " + repr(self.keyword_list)

    def prompt_user_keyword(self):
        user_keyword = input('Please enter an item you wish to '
                             'buy/sell/trade: ').strip()
        self.keyword_list.append(user_keyword)

    def prompt_additional_keyword(self):
        while True:
            additional_keyword = input('Do you want to enter an additional '
                                       'keyword? Yes or No:').strip().lower()
            if additional_keyword == 'yes' or additional_keyword == 'y':
                self.prompt_user_keyword()
                self.prompt_additional_keyword()
                break
            elif additional_keyword == 'no' or additional_keyword == 'n':
                break
            else:
                print('Please enter Yes or No. Y or N is also acceptable.')
                continue


def prompt_user_email():
    while True:

        user_email = input('Enter your email address: ')

        if '@' not in user_email:
            print('Invalid email address. Please try again.')
            continue
        else:
            return user_email
