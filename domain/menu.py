__author__ = 'TeodorZ'

from repository.fileStorage import FileStorage

class Menu(FileStorage):
    def __init__(self, menu_name, meals=None, **kwargs):
        super().__init__(**kwargs)
        self._menu_name = menu_name
        self._meals = []
        self._meals = super(Menu, self).load()

    @property
    def meals(self):
        return self._meals

    @property
    def menu_name(self):
        return self._menu_name

def test_create_menu():
    mn = Menu('meniul zilei', filename='test2.txt')
    assert mn._meals == ['cartofi prajiti\n', 'gratar de pui']

if __name__ == '__main__':
    test_create_menu()

