# encoding: utf-8
# module scipy.linalg._solve_toeplitz
# from D:\ProgramData\Anaconda3\lib\site-packages\scipy\linalg\_solve_toeplitz.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from numpy.core.multiarray import zeros

import numpy as __numpy


# functions

def asarray(a, dtype=None, order=None): # reliably restored by inspect
    """
    Convert the input to an array.
    
        Parameters
        ----------
        a : array_like
            Input data, in any form that can be converted to an array.  This
            includes lists, lists of tuples, tuples, tuples of tuples, tuples
            of lists and ndarrays.
        dtype : data-type, optional
            By default, the data-type is inferred from the input data.
        order : {'C', 'F'}, optional
            Whether to use row-major (C-style) or
            column-major (Fortran-style) memory representation.
            Defaults to 'C'.
    
        Returns
        -------
        out : ndarray
            Array interpretation of `a`.  No copy is performed if the input
            is already an ndarray with matching dtype and order.  If `a` is a
            subclass of ndarray, a base class ndarray is returned.
    
        See Also
        --------
        asanyarray : Similar function which passes through subclasses.
        ascontiguousarray : Convert input to a contiguous array.
        asfarray : Convert input to a floating point ndarray.
        asfortranarray : Convert input to an ndarray with column-major
                         memory order.
        asarray_chkfinite : Similar function which checks input for NaNs and Infs.
        fromiter : Create an array from an iterator.
        fromfunction : Construct an array by executing a function on grid
                       positions.
    
        Examples
        --------
        Convert a list into an array:
    
        >>> a = [1, 2]
        >>> np.asarray(a)
        array([1, 2])
    
        Existing arrays are not copied:
    
        >>> a = np.array([1, 2])
        >>> np.asarray(a) is a
        True
    
        If `dtype` is set, array is copied only if dtype does not match:
    
        >>> a = np.array([1, 2], dtype=np.float32)
        >>> np.asarray(a, dtype=np.float32) is a
        True
        >>> np.asarray(a, dtype=np.float64) is a
        False
    
        Contrary to `asanyarray`, ndarray subclasses are not passed through:
    
        >>> issubclass(np.matrix, np.ndarray)
        True
        >>> a = np.matrix([[1, 2]])
        >>> np.asarray(a) is a
        False
        >>> np.asanyarray(a) is a
        True
    """
    pass

def levinson(*args, **kwargs): # real signature unknown
    """
    Solve a linear Toeplitz system using Levinson recursion.
    
        Parameters
        ----------
        a : array, dtype=double or complex128, shape=(2n-1,)
            The first column of the matrix in reverse order (without the diagonal)
            followed by the first (see below)
        b : array, dtype=double  or complex128, shape=(n,)
            The right hand side vector. Both a and b must have the same type
            (double or complex128).
    
        Notes
        -----
        For example, the 5x5 toeplitz matrix below should be represented as
        the linear array ``a`` on the right ::
    
            [ a0    a1   a2  a3  a4 ]
            [ a-1   a0   a1  a2  a3 ]
            [ a-2  a-1   a0  a1  a2 ] -> [a-4  a-3  a-2  a-1  a0  a1  a2  a3  a4]
            [ a-3  a-2  a-1  a0  a1 ]
            [ a-4  a-3  a-2  a-1 a0 ]
    
        Returns
        -------
        x : arrray, shape=(n,)
            The solution vector
        reflection_coeff : array, shape=(n+1,)
            Toeplitz reflection coefficients. When a is symmetric Toeplitz and
            ``b`` is ``a[n:]``, as in the solution of autoregressive systems,
            then ``reflection_coeff`` also correspond to the partial
            autocorrelation function.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class complex128(__numpy.complexfloating, complex):
    """ Composed of two 64 bit floats """
    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass


class float64(__numpy.floating, float):
    """ 64-bit floating-point number. Character code 'd'. Python float compatible. """
    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass


class LinAlgError(Exception):
    """
    Generic Python-exception-derived object raised by linalg functions.
    
        General purpose exception class, derived from Python's exception.Exception
        class, programmatically raised in linalg functions when a Linear
        Algebra-related condition would prevent further correct execution of the
        function.
    
        Parameters
        ----------
        None
    
        Examples
        --------
        >>> from numpy import linalg as LA
        >>> LA.inv(np.zeros((2,2)))
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "...linalg.py", line 350,
            in inv return wrap(solve(a, identity(a.shape[0], dtype=a.dtype)))
          File "...linalg.py", line 249,
            in solve
            raise LinAlgError('Singular matrix')
        numpy.linalg.LinAlgError: Singular matrix
    """
    def __init__(self, Singular_matrix): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

