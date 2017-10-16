# encoding: utf-8
# module scipy.optimize._nnls
# from D:\ProgramData\Anaconda3\lib\site-packages\scipy\optimize\_nnls.cp36-win_amd64.pyd
# by generator 1.145
"""
This module '_nnls' is auto-generated with f2py (version:2).
Functions:
  x,rnorm,mode = nnls(a,m,n,b,w,zz,index_bn,mda=shape(a,0),overwrite_a=0,overwrite_b=0)
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def nnls(a, m, n, b, w, zz, index_bn, mda=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,rnorm,mode = nnls(a,m,n,b,w,zz,index_bn,[mda,overwrite_a,overwrite_b])
    
    Wrapper for ``nnls``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (mda,*)
    m : input int
    n : input int
    b : input rank-1 array('d') with bounds (*)
    w : input rank-1 array('d') with bounds (*)
    zz : input rank-1 array('d') with bounds (*)
    index_bn : input rank-1 array('i') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    mda : input int, optional
        Default: shape(a,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-1 array('d') with bounds (n)
    rnorm : float
    mode : int
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

