# encoding: utf-8
# module bottleneck.nonreduce
# from D:\ProgramData\Anaconda3\lib\site-packages\bottleneck\nonreduce.cp36-win_amd64.pyd
# by generator 1.145
""" Bottleneck nonreducing functions. """
# no imports

# functions

def replace(a, old, new): # real signature unknown; restored from __doc__
    """
    replace(a, old, new)
    
    Replace (inplace) given scalar values of an array with new values.
    
    The equivalent numpy function:
    
        a[a==old] = new
    
    Or in the case where old=np.nan:
    
        a[np.isnan(old)] = new
    
    Parameters
    ----------
    a : numpy.ndarray
        The input array, which is also the output array since this functions
        works inplace.
    old : scalar
        All elements in `a` with this value will be replaced by `new`.
    new : scalar
        All elements in `a` with a value of `old` will be replaced by `new`.
    
    Returns
    -------
    Returns a view of the input array after performing the replacements,
    if any.
    
    Examples
    --------
    Replace zero with 3 (note that the input array is modified):
    
    >>> a = np.array([1, 2, 0])
    >>> bn.replace(a, 0, 3)
    >>> a
    array([1, 2, 3])
    
    Replace np.nan with 0:
    
    >>> a = np.array([1, 2, np.nan])
    >>> bn.replace(a, np.nan, 0)
    >>> a
    array([ 1.,  2.,  0.])
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

