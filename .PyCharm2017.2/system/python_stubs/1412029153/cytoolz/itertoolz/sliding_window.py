# encoding: utf-8
# module cytoolz.itertoolz
# from D:\ProgramData\Anaconda3\lib\site-packages\cytoolz\itertoolz.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from itertools import chain, islice, zip_longest

from _heapq import heapify, heappop, heapreplace

import _random as ___random


from .object import object

class sliding_window(object):
    """
    sliding_window(n, seq)
    
        A sequence of overlapping subsequences
    
        >>> list(sliding_window(2, [1, 2, 3, 4]))
        [(1, 2), (2, 3), (3, 4)]
    
        This function creates a sliding window suitable for transformations like
        sliding means / smoothing
    
        >>> mean = lambda seq: float(sum(seq)) / len(seq)
        >>> list(map(mean, sliding_window(2, [1, 2, 3, 4])))
        [1.5, 2.5, 3.5]
    """
    def __init__(self, n, seq): # real signature unknown; restored from __doc__
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


