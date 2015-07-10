__author__ = 'TeodorZ'

from repository.storage import Storage

class MemoryStorage(Storage):
    def __init__(self, listname=None):
        self._listname = []

    @property
    def listname(self):
        return self._listname

    @listname.setter
    def listname(self, new_listname):
        self._listname = new_listname

    def store(self, s=None):
        self._listname.append(s)

    def load(self):
        return self._listname

def test_memory_storage():
    ms = MemoryStorage()
    ms.store('alabala')
    #print(ms.load())
    assert  ms.load() == ['alabala']

if __name__ == '__main__':
    test_memory_storage()