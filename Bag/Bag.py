# An Implementation of the BAG ADT using the list Data structure available
# in python
# A Bag is a Data Structure that stores items without taking into consideration
# the order of the items. Also it stores a reference to the items added so that
# the items can be retrieved back when needed


class _BagIterator:
    def __init__(self, theList):
        self._bagItems = theList
        self._curItem = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curItem < len(self._bagItems):
            item = self._bagItems[self._curItem]
            self._curItem += 1
            return item
        else:
            raise StopIteration


class Bag:
    def __init__(self):
        self._theItems = list()

    def __len__(self):
        return len(self._theItems)

    def __contains__(self, item):
        return item in self._theItems

    def add(self, item):
        self._theItems.append(item)

    def remove(self, item):
        assert item in self._theItems, "The item must be in the bag"
        ndx = self._theItems.index(item)
        return self._theItems.pop(ndx)

    def __iter__(self):
        return _BagIterator(self._theItems)

    def __str__(self):
        repr = "{item}".format(item= [i for i in self._theItems])
        repr = "{=> " + repr[1:] + '\b <=}'
        return repr


if __name__ == "__main__":
    import pdb; pdb.set_trace()