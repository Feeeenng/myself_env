# encoding: utf-8
# module scipy.optimize._slsqp
# from D:\ProgramData\Anaconda3\lib\site-packages\scipy\optimize\_slsqp.cp36-win_amd64.pyd
# by generator 1.145
"""
This module '_slsqp' is auto-generated with f2py (version:2).
Functions:
  slsqp(m,meq,x,xl,xu,f,c,g,a,acc,iter,mode,w,jw,la=len(c),n=len(x),l_w=len(w),l_jw=len(jw))
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def slsqp(m, meq, x, xl, xu, f, c, g, a, acc, iter, mode, w, jw, la=None, n=None, l_w=None, l_jw=None): # real signature unknown; restored from __doc__
    """
    slsqp(m,meq,x,xl,xu,f,c,g,a,acc,iter,mode,w,jw,[la,n,l_w,l_jw])
    
    Wrapper for ``slsqp``.
    
    Parameters
    ----------
    m : input int
    meq : input int
    x : in/output rank-1 array('d') with bounds (n)
    xl : input rank-1 array('d') with bounds (n)
    xu : input rank-1 array('d') with bounds (n)
    f : input float
    c : input rank-1 array('d') with bounds (la)
    g : input rank-1 array('d') with bounds (n + 1)
    a : input rank-2 array('d') with bounds (la,n + 1)
    acc : in/output rank-0 array(float,'d')
    iter : in/output rank-0 array(int,'i')
    mode : in/output rank-0 array(int,'i')
    w : input rank-1 array('d') with bounds (l_w)
    jw : input rank-1 array('i') with bounds (l_jw)
    
    Other Parameters
    ----------------
    la : input int, optional
        Default: len(c)
    n : input int, optional
        Default: len(x)
    l_w : input int, optional
        Default: len(w)
    l_jw : input int, optional
        Default: len(jw)
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

