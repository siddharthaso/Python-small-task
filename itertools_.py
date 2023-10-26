"""don't you dare
https://docs.python.org/3/library/itertools.html#itertools.product
"""
from itertools import groupby


def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
        print("\n",result,"\n")
    for prod in result:
        yield tuple(prod)

print([i for i in product(*[[1,2,3,4],[5,6,7],[100,200]])])



class groupby_mine(object):
    # [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
    # [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
    def __init__(self, iterable, key=None):
        if key is None:
            key = lambda x: x
        self.keyfunc = key
        self.it = iter(iterable)
        self.tgtkey = self.currkey = self.currvalue = object()
    def __iter__(self):
        return self
    def next(self):
        print(self.tgtkey, self.currkey, self.currvalue)
        while self.currkey == self.tgtkey:
            self.currvalue = next(self.it)    # Exit on StopIteration
            self.currkey = self.keyfunc(self.currvalue)
        self.tgtkey = self.currkey
        return (self.currkey, self._grouper(self.tgtkey))
    def _grouper(self, tgtkey):
        while self.currkey == tgtkey:
            yield self.currvalue
            self.currvalue = next(self.it)    # Exit on StopIteration
            self.currkey = self.keyfunc(self.currvalue)


print([(i,list(j)) for i,j in groupby("112223333554411")])


def groupby(iterable, key=None):
    # groupby('AAAABBBCCDAABBB') --> A, A, A, A, B, B, B, C, C, D, A, A, B, B, B
    # groupby('ABBCcAD') --> A, B, B, C, c, A, D
    # Reference: https://docs.python.org/3/library/itertools.html#itertools.groupby

    # Create an iterator from the input iterable
    it = iter(iterable)
    
    # Check if a key function is provided
    if key is None:
        # Define the key function as an identity function
        key = lambda x: x
    
    # Create variables to store the current key and group
    current_key = None
    current_group = []
    
    # Iterate over the input iterable
    for item in it:
        # Compute the key for the current item
        item_key = key(item)
        
        # Check if the key has changed
        if item_key != current_key:
            # Yield the previous key and group
            if current_key is not None:
                yield current_key, current_group
            
            # Start a new group with the current item
            current_key = item_key
            current_group = [item]
        else:
            # Add the current item to the current group
            current_group.append(item)
    
    # Yield the last key and group
    if current_key is not None:
        yield current_key, current_group
