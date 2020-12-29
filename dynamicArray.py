# Dynamic Array example
# list is a predefined dynamic array in python
# here we will create a dynamic array for our understanding
import sys
import ctypes

class DynamicArray(object):
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.makearray(self.capacity)

    # special method
    def __len__(self):
        return self.n

    # special method
    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError('K is out of bounds.')

        return self.A[k]

    def append(self, element):
        if self.n == self.capacity:
            # This statement will increase the cpaacity by 2 times if the capacity is not enough.
            self._resize(2*self.capacity)

        self.A[self.n] = element
        self.n += 1

    # private method
    def _resize(self, new_capacity):
        B = self.makearray(new_capacity)
        for k in range(self.n):
            # re-referencing everything from A to B
            B[k] = self.A[k]

        # Now assigning B to A reference ( Now A will be taken away by garbage collector in python)
        self.A = B
        self.capacity = new_capacity

    def makearray(self, new_capacity):
        # use ctyped library to make a raw array for our example.
        return (new_capacity * ctypes.py_object)()

# After appending multiple objects keep checking the size of array to determine when the DynamicArray in this example resize itself. See how it changes and doubles its size to accomodate new elements.
    def dynamic_arr_size(self):
        return sys.getsizeof(DynamicArray)


d = DynamicArray()
# d.append(0)
# print('\nTotal number of elements in the Dynamic Array :', len(d))
# print('Total size of Dynamic Array :', sys.getsizeof(d),'bytes')
n = 10
for i in range(40):
    a = len(d)
    b = sys.getsizeof(d)
    print('Length : {0:3d} ; Size in bytes : {1:4d}'.format(a, b))
    d.append(n)

# print('\nAfter multiple insertion of elements, Total number of elements count in the Dynamic Array :', len(d))
# print('Post append, new size of Dynamic Array :', sys.getsizeof(d),'bytes\n')
