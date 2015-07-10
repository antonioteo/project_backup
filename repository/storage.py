__author__ = 'TeodorZ'

from abc import ABCMeta, abstractmethod

class Storage(metaclass=ABCMeta):
    @abstractmethod
    def store(self, s=None):
        pass

    @abstractmethod
    def load(self):
        pass

def test_storage():
    pass