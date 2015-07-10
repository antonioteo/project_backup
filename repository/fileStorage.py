__author__ = 'TeodorZ'

from repository.memoryStorage import MemoryStorage
from os.path import isfile
from utils import create_file

class FileStorage(MemoryStorage):
    def __init__(self, filename):
        self._filename = filename

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, filename):
        self._filename = filename

    def store(self, s):
        if not isfile(self._filename):
            create_file(self._filename)
        f = open(self._filename, 'r')
        lines = f.readlines()
        f.close()
        with open(self._filename, 'w') as f:
            for line in lines:
                f.write(line)
            f.write(s)

    def load(self):
        if not isfile(self._filename):
            create_file(self._filename)
        with open(self._filename, 'r') as f:
            l = []
            for line in f:
                l.append(line)
        return l

def test_file_storage():
    fs = FileStorage('test.txt')
    fs.store('alabala\n')
    assert fs.load() == ['alabala\n']
'''
if __name__ == '__main__':
    test_file_storage()
'''