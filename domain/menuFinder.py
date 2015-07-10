__author__ = 'TeodorZ'

import glob, os
from domain.menu import Menu

class MenuFinder():
    @classmethod
    def search(self, tip, path):
        for root, dirs, files in os.walk(path):
            dirs=[]
            #print(files)
            filename = 'menu_%s' % tip
            if filename in files:
                pt = os.path.join(root, filename)
                return Menu(tip, filename=pt)

def test_menu_finder():
    mf = MenuFinder()
    fn = os.path.join(os.path.dirname(__file__), 'menus')
    #print(fn)
    #print(mf.search('bigMc', fn))

if __name__ == '__main__':
    test_menu_finder()