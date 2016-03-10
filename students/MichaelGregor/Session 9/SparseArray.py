

class SparseArray(object):

    def __init__(self, array=[]):
        self._array = array

    @property
    def array(self):
        return self.array

    @array.setter
    def array(self, item):
        self.array.append(item)

    @array.deleter
    def array(self, index):
        self.array.pop[index]


def main():

    sa = SparseArray([1, 2, 3, 4])




if __name__ == "__main__":
    main()


