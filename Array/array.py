import ctypes


class _ArrayIterator:
    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__(self):
        return self 

    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            item = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return item 
        else:
            raise StopIteration

class Array:
    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self._size = size 

        # Creating the array structure using the ctypes module
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()

        # Initializing each element to 0
        self.clear(None)

    def __len__(self):
        return self._size 

    # Method Gets the Content of the index element
    def __getitem__(self, index):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[index]

    # Method Sets value of element at the give index to the value given 
    def __setitem__(self, index, value):
        assert index >=0 and index < len(self), "Array subscript out of range"
        self._elements[index] = value 

    def __iter__(self):
        return _ArrayIterator(self._elements)

    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value


if __name__ == "__main__":
    import pdb; pdb.set_trace()