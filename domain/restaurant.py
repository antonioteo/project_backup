__author__ = 'TeodorZ'

from repository.fileStorage import FileStorage
from domain.menuFinder import MenuFinder
import os

MENUS_FOLDER = 'menus'

class Restaurant:
    def __init__(self, menu_finder, menus=None, **kwargs):
        self._menu_finder = menu_finder

    @property
    def menu_finder(self):
        return self._menu_finder

    def get_complete_menu(self, menu_type, **kwargs):
        file_name = os.path.join(os.path.dirname(__file__), MENUS_FOLDER)
        return (self.menu_finder).search(menu_type, file_name).meals

def test_create_restaurant():
    mf = MenuFinder()
    r = Restaurant(mf)
    #assert r._menus == ['mediu\n', 'mare']
    file_name = os.path.join(os.path.dirname(__file__), MENUS_FOLDER)
    assert r._menu_finder.search('example', file_name) == None

def test_get_complete_menu():
    mf = MenuFinder
    r = Restaurant(mf)
    assert r.get_complete_menu('bigMc') != None

if __name__ == '__main__':
    test_create_restaurant()
    test_get_complete_menu()