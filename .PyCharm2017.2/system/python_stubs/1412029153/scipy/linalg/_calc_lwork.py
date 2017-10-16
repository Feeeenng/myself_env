# encoding: utf-8
# module scipy.linalg._calc_lwork
# from D:\ProgramData\Anaconda3\lib\site-packages\scipy\linalg\_calc_lwork.cp36-win_amd64.pyd
# by generator 1.145
"""
This module '_calc_lwork' is auto-generated with f2py (version:2).
Functions:
  minwrk,maxwrk = gehrd(prefix,n,lo,hi)
  minwrk,maxwrk = gesdd(prefix,m,n,compute_uv)
  minwrk,maxwrk = gelss(prefix,m,n,nrhs)
  minwrk,maxwrk = getri(prefix,n)
  minwrk,maxwrk = geev(prefix,n,compute_vl=1,compute_vr=1)
  minwrk,maxwrk = heev(prefix,n,lower=0)
  minwrk,maxwrk = syev(prefix,n,lower=0)
  minwrk,maxwrk = gees(prefix,n,compute_v=1)
  minwrk,maxwrk = geqrf(prefix,m,n)
  minwrk,maxwrk = gqr(prefix,m,n)
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def gees(prefix, n, compute_v=None): # real signature unknown; restored from __doc__
    """
    minwrk,maxwrk = gees(prefix,n,[compute_v])
    
    Wrapper for ``gees``.
    
    Parameters
    ----------
    prefix : input string(len=1)
    n : input int
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    
    Returns
    -------
    minwrk : int
    maxwrk : int
    """
    pass

def geev(prefix, n, compute_vl=None, compute_vr=None): # real signature unknown; restored from __doc__
    """
    minwrk,maxwrk = geev(prefix,n,[compute_vl,compute_vr])
    
    Wrapper for ``geev``.
    
    Parameters
    ----------
    prefix : input string(len=1)
    n : input int
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    
    Returns
    -------
    minwrk : int
    maxwrk : int
    """
    pass

def gehrd(prefix, n, lo, hi): # real signature unknown; restored from __doc__
    """
    minwrk,maxwrk = gehrd(prefix,n,lo,hi)
    
    Wrapper for ``gehrd``.
    
    Parameters
    ----------
    prefix : input string(len=1)
    n : input int
    lo : input int
    hi : input int
    
    Returns
    -------
    minwrk : int
    maxwrk : int
    """
    pass

def gelss(prefix, m, n, nrhs): # real signature unknown; restored from __doc__
    """
    minwrk,maxwrk = gelss(prefix,m,n,nrhs)
    
    Wrapper for ``gelss``.
    
    Parameters
    ----------
    prefix : input string(len=1)
    m : input int
    n : input int
    nrhs : input int
    
    Returns
    -------
    minwrk : int
    maxwrk : int
    """
    pass

def geqrf(prefix, m, n): # real signature unknown; restored from __doc__
    """
    minwrk,maxwrk = geqrf(prefix,m,n)
    
    Wrapper for ``geqrf``.
    
    Parameters
    ----------
    prefix : input string(len=1)
    m : input int
    n : input int
    
    Returns
    -------
    minwrk : int
    maxwrk : int
    """
    pass

def gesdd(prefix, m, n, compute_uv): # real signature unknown; restored from __doc__
    """
    minwrk,maxwrk = gesdd(prefix,m,n,compute_uv)
    
    Wrapper for ``gesdd``.
    
    Parameters
    ----------
    prefix : input string(len=1)
    m : input int
    n : input int
    compute_uv : input int
    
    Returns
    -------
    minwrk : int
    maxwrk : int
    """
    pass

def getri(prefix, n): # real signature unknown; restored from __doc__
    """
    minwrk,maxwrk = getri(prefix,n)
    
    Wrapper for ``getri``.
    
    Parameters
    ----------
    prefix : input string(len=1)
    n : input int
    
    Returns
    -------
    minwrk : int
    maxwrk : int
    """
    pass

def gqr(prefix, m, n): # real signature unknown; restored from __doc__
    """
    minwrk,maxwrk = gqr(prefix,m,n)
    
    Wrapper for ``gqr``.
    
    Parameters
    ----------
    prefix : input string(len=1)
    m : input int
    n : input int
    
    Returns
    -------
    minwrk : int
    maxwrk : int
    """
    pass

def heev(prefix, n, lower=None): # real signature unknown; restored from __doc__
    """
    minwrk,maxwrk = heev(prefix,n,[lower])
    
    Wrapper for ``heev``.
    
    Parameters
    ----------
    prefix : input string(len=1)
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    minwrk : int
    maxwrk : int
    """
    pass

def syev(prefix, n, lower=None): # real signature unknown; restored from __doc__
    """
    minwrk,maxwrk = syev(prefix,n,[lower])
    
    Wrapper for ``syev``.
    
    Parameters
    ----------
    prefix : input string(len=1)
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    minwrk : int
    maxwrk : int
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

