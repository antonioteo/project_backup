__author__ = 'TeodorZ'

from urllib.parse import urlparse

class PathHandler:
    def __init__(self, restaurant):
        self._path_dictionary = {"/get_menu" : restaurant.get_complete_menu}

    @property
    def path_dictionary(self):
        return self._path_dictionary

    def handle_it(self, requested_path):
        query_params = {}
        #parse the path.. and fill up query_params
        parse_result = urlparse(requested_path)
        s = parse_result.query
        # s is of query type now..
        query_params = dict((param.rsplit('=') for param in s.rsplit('&')))
        #ok done
        request_type = parse_result.path #the dictionary key
        menu_list = self.path_dictionary[request_type](**query_params)
        return str(menu_list)