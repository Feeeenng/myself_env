# encoding: utf-8
# module sklearn.utils.weight_vector
# from D:\ProgramData\Anaconda3\lib\site-packages\sklearn\utils\weight_vector.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # D:\ProgramData\Anaconda3\lib\site-packages\numpy\__init__.py

# no functions
# classes

class WeightVector(object):
    """
    Dense vector represented by a scalar and a numpy array.
    
        The class provides methods to ``add`` a sparse vector
        and scale the vector.
        Representing a vector explicitly as a scalar times a
        vector allows for efficient scaling operations.
    
        Attributes
        ----------
        w : ndarray, dtype=double, order='C'
            The numpy array which backs the weight vector.
        aw : ndarray, dtype=double, order='C'
            The numpy array which backs the average_weight vector.
        w_data_ptr : double*
            A pointer to the data of the numpy array.
        wscale : double
            The scale of the vector.
        n_features : int
            The number of features (= dimensionality of ``w``).
        sq_norm : double
            The squared norm of ``w``.
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


# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

