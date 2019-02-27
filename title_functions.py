import unittest
import pandas as pd
#from reddit_access import get_Ten_Titles

new_title = '[US-MA] [H] TX-1800v2 [W] PayPal'
w = 'TX-1800'


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


"""
class TestTitleMethods(unittest.TestCase):

    def test_split_title(self):
        test_title = '[Location][H] Have_String [W] Want_string'
        self.assertTrue(split_title(test_title), ['[Location]', 'Have_String', 'Want_string'])
"""


"""
if __name__ == '__main__':
    unittest.main()
"""
