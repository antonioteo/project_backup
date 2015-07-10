__author__ = 'TeodorZ'

class Meal():
    def __init__(self, quantity, name):
        self._quantity = quantity
        self._name = name

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

def test_create_meal():
    m = Meal(50, "cartofi prajiti")
    #print(m.name)
    #print(m.quantity)
    assert m.name == "cartofi prajiti" and m.quantity == 50
    m.quantity = 40
    assert m.quantity == 40

test_create_meal()