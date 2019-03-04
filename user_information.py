

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
        self.most_recent_post = 0.0

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


def prompt_user_email():
    while True:

        user_email = input('Enter your email address: ')

        if '@' not in user_email:
            print('Invalid email address. Please try again.')
            continue
        else:
            return user_email


def prompt_user_keyword():

    while True:
        try:
            user_action = int(input('Please enter an integer corresponding to'
                                    ' one of the following options\n'
                                    '1. Buy\n'
                                    '2. Sell\n'
                                    '3. Trade'))

            if user_action not in range(1, 4):
                print('Invalid input. Value outside of range.')
                continue

            else:
                break

        except ValueError:
            print('Invalid input. Not an integer.')
            continue

    user_keyword = input('Please enter the item you wish to buy/sell/trade')

    keyword_dict = {'Keyword': user_keyword,
                    'Action': user_action}
    return keyword_dict


def create_new_user():

    user_email = prompt_user_email()
    keyword_list = []

    while True:

        keyword = prompt_user_keyword()
        keyword_list.append(keyword)
        additional_keyword = input('Do you want to enter another keyword? Yes or No?')

        if additional_keyword.lower() == 'yes' or additional_keyword.lower() == 'y':
            continue

        elif additional_keyword.lower() == 'no' or additional_keyword.lower() == 'n':
            break

        else:
            print('Invalid input. Please enter Yes or No.')

    new_account = User(user_email, keyword_list)

    return new_account


def test_create_new_user():

    user1 = create_new_user()
    print(user1.get_email())
    print(user1.get_keywords())
    print(user1.__repr__())


#test_create_new_user()
