# encoding: utf-8
# module astropy.convolution.boundary_wrap
# from D:\ProgramData\Anaconda3\lib\site-packages\astropy\convolution\boundary_wrap.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # D:\ProgramData\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def convolve1d_boundary_wrap(*args, **kwargs): # real signature unknown
    pass

def convolve2d_boundary_wrap(*args, **kwargs): # real signature unknown
    pass

def convolve3d_boundary_wrap(*args, **kwargs): # real signature unknown
    pass

# classes

class DTYPE(object):
    """
    float(x) -> floating point number
    
    Convert a string or number to a floating point number, if possible.
    """
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        float.as_integer_ratio() -> (int, int)
        
        Return a pair of integers, whose ratio is exactly equal to the original
        float and with a positive denominator.
        Raise OverflowError on infinities and a ValueError on NaNs.
        
        >>> (10.0).as_integer_ratio()
        (10, 1)
        >>> (0.0).as_integer_ratio()
        (0, 1)
        >>> (-.25).as_integer_ratio()
        (-1, 4)
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Return self, the complex conjugate of any float. """
        pass

    @classmethod
    def fromhex(cls, string): # real signature unknown; restored from __doc__
        """
        float.fromhex(string) -> float
        
        Create a floating-point number from a hexadecimal string.
        >>> float.fromhex('0x1.ffffp10')
        2047.984375
        >>> float.fromhex('-0x1p-1074')
        -5e-324
        """
        return 0.0

    def hex(self): # real signature unknown; restored from __doc__
        """
        float.hex() -> string
        
        Return a hexadecimal representation of a floating-point number.
        >>> (-0.1).hex()
        '-0x1.999999999999ap-4'
        >>> 3.14159.hex()
        '0x1.921f9f01b866ep+1'
        """
        return ""

    def is_integer(self, *args, **kwargs): # real signature unknown
        """ Return True if the float is an integer. """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
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

    def __format__(self, format_spec): # real signature unknown; restored from __doc__
        """
        float.__format__(format_spec) -> string
        
        Formats the float according to format_spec.
        """
        return ""

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    @classmethod
    def __getformat__(cls, typestr): # real signature unknown; restored from __doc__
        """
        float.__getformat__(typestr) -> string
        
        You probably don't want to use this function.  It exists mainly to be
        used in Python's test suite.
        
        typestr must be 'double' or 'float'.  This function returns whichever of
        'unknown', 'IEEE, big-endian' or 'IEEE, little-endian' best describes the
        format of floating point numbers used by the C type named by typestr.
        """
        return ""

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
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

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
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

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Return the Integral closest to x, rounding half toward even.
        When an argument is passed, work like built-in round(x, ndigits).
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    @classmethod
    def __setformat__(cls, typestr, fmt): # real signature unknown; restored from __doc__
        """
        float.__setformat__(typestr, fmt) -> None
        
        You probably don't want to use this function.  It exists mainly to be
        used in Python's test suite.
        
        typestr must be 'double' or 'float'.  fmt must be one of 'unknown',
        'IEEE, big-endian' or 'IEEE, little-endian', and in addition can only be
        one of the latter two if it appears to match the underlying C reality.
        
        Override the automatic determination of C-level floating point type.
        This affects how floats are converted to and from binary strings.
        """
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

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Return the Integral closest to x between 0 and x. """
        pass

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""



# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

