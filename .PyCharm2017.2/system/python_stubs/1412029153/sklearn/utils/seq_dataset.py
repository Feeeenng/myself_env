# encoding: utf-8
# module sklearn.utils.seq_dataset
# from D:\ProgramData\Anaconda3\lib\site-packages\sklearn\utils\seq_dataset.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # D:\ProgramData\Anaconda3\lib\site-packages\numpy\__init__.py

# no functions
# classes

class SequentialDataset(object):
    """ Base class for datasets with sequential data access. """
    def _next_py(self, *args, **kwargs): # real signature unknown
        """ python function used for easy testing """
        pass

    def _random_py(self, *args, **kwargs): # real signature unknown
        """ python function used for easy testing """
        pass

    def _sample_py(self, *args, **kwargs): # real signature unknown
        """ python function used for easy testing """
        pass

    def _shuffle_py(self, *args, **kwargs): # real signature unknown
        """ python function used for easy testing """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is ''


class ArrayDataset(SequentialDataset):
    """
    Dataset backed by a two-dimensional numpy array.
    
        The dtype of the numpy array is expected to be ``np.float64`` (double)
        and C-style memory layout.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is ''


class CSRDataset(SequentialDataset):
    """ A ``SequentialDataset`` backed by a scipy sparse CSR matrix. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is ''


# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

