# encoding: utf-8
# module cytoolz.recipes
# from D:\ProgramData\Anaconda3\lib\site-packages\cytoolz\recipes.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from itertools import groupby


# functions

def countby(key, seq): # real signature unknown; restored from __doc__
    """
    countby(key, seq)
    
        Count elements of a collection by a key function
    
        >>> countby(len, ['cat', 'mouse', 'dog'])
        {3: 2, 5: 1}
    
        >>> def iseven(x): return x % 2 == 0
        >>> countby(iseven, [1, 2, 3])  # doctest:+SKIP
        {True: 1, False: 2}
    
        See Also:
            groupby
    """
    pass

# classes

class map(object):
    """
    map(func, *iterables) --> map object
    
    Make an iterator that computes the function using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.
    """
    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, func, *iterables): # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling. """
        pass


class partitionby(object):
    """
    partitionby(func, seq)
    
        Partition a sequence according to a function
    
        Partition `s` into a sequence of lists such that, when traversing
        `s`, every time the output of `func` changes a new list is started
        and that and subsequent items are collected into that list.
    
        >>> is_space = lambda c: c == " "
        >>> list(partitionby(is_space, "I have space"))
        [('I',), (' ',), ('h', 'a', 'v', 'e'), (' ',), ('s', 'p', 'a', 'c', 'e')]
    
        >>> is_large = lambda x: x > 10
        >>> list(partitionby(is_large, [1, 2, 1, 99, 88, 33, 99, -1, 5]))
        [(1, 2, 1), (99, 88, 33, 99), (-1, 5)]
    
        See also:
            partition
            groupby
            itertools.groupby
    """
    def __init__(self, func, seq): # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

__all__ = [
    'countby',
    'partitionby',
]

__loader__ = None # (!) real value is ''

__pyx_capi__ = {
    'countby': None, # (!) real value is ''
}

__spec__ = None # (!) real value is ''

__test__ = {
    'countby (line 11)': "\n    Count elements of a collection by a key function\n\n    >>> countby(len, ['cat', 'mouse', 'dog'])\n    {3: 2, 5: 1}\n\n    >>> def iseven(x): return x % 2 == 0\n    >>> countby(iseven, [1, 2, 3])  # doctest:+SKIP\n    {True: 1, False: 2}\n\n    See Also:\n        groupby\n    ",
}

