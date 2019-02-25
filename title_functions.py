import unittest
import pandas as pd
from reddit_access import get_Ten_Titles

new_title = '[US-MA] [H] TX-1800v2 [W] PayPal'
w = 'TX-1800'


class MechMarketPost:

    def __init__(self, title):
        self.title = title




    """
    def split_title(self, title):
        title_list = []

        if '[H]' in title and '[W]' in title:

            split_h = title.split('[H]')
            location_tag = split_h[0].strip(' ')
            split_w = split_h[1].split('[W]')
            have_string = split_w[0].strip(' ')
            want_string = split_w[1].strip(' ')

            title_list.append(location_tag)
            title_list.append(have_string)
            title_list.append(want_string)

            return title_list

        else:
            pass
    """

def split_title(title):

    title_list = []

    if '[H]' in title and '[W]' in title:

        split_H = title.split('[H]')
        location_tag = split_H[0].strip(' ')
        split_W = split_H[1].split('[W]')
        have_string = split_W[0].strip(' ')
        want_string = split_W[1].strip(' ')

        title_list.append(location_tag)
        title_list.append(have_string)
        title_list.append(want_string)

        return title_list

    else:
        pass


def titles_to_df(split_titles):

    column_headers = ['Location', 'User Has', 'User Wants']
    title_df = pd.DataFrame([split_titles], columns=column_headers)
    return title_df


def write_title_to_text(title):

    title_file = open("textfile", "w")
    title_file.write(title)
    title_file.close()


def append_title_to_text(title):

    title_file = open("textfile", "a")
    title_file.write(title + "\n")
    title_file.close()


print(split_title(new_title))
print(titles_to_df(split_title(new_title)))

test_list = [1, 2, 3]
test_headers = ['Loc', 'Has', 'Wants']
test_df = pd.DataFrame(test_list, test_headers)
print(test_df)


class TestTitleMethods(unittest.TestCase):

    def test_split_title(self):
        test_title = '[Location][H] Have_String [W] Want_string'
        self.assertTrue(split_title(test_title), ['[Location]', 'Have_String', 'Want_string'])


if __name__ == '__main__':
    unittest.main()
