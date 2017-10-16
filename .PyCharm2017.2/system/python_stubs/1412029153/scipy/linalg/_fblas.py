# encoding: utf-8
# module scipy.linalg._fblas
# from D:\ProgramData\Anaconda3\lib\site-packages\scipy\linalg\_fblas.cp36-win_amd64.pyd
# by generator 1.145
"""
This module '_fblas' is auto-generated with f2py (version:2).
Functions:
  c,s = srotg(a,b)
  c,s = drotg(a,b)
  c,s = crotg(a,b)
  c,s = zrotg(a,b)
  param = srotmg(d1,d2,x1,y1)
  param = drotmg(d1,d2,x1,y1)
  x,y = srot(x,y,c,s,n=(len(x)-1-offx)/abs(incx)+1,offx=0,incx=1,offy=0,incy=1,overwrite_x=0,overwrite_y=0)
  x,y = drot(x,y,c,s,n=(len(x)-1-offx)/abs(incx)+1,offx=0,incx=1,offy=0,incy=1,overwrite_x=0,overwrite_y=0)
  x,y = csrot(x,y,c,s,n=(len(x)-1-offx)/abs(incx)+1,offx=0,incx=1,offy=0,incy=1,overwrite_x=0,overwrite_y=0)
  x,y = zdrot(x,y,c,s,n=(len(x)-1-offx)/abs(incx)+1,offx=0,incx=1,offy=0,incy=1,overwrite_x=0,overwrite_y=0)
  x,y = srotm(x,y,param,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1,overwrite_x=0,overwrite_y=0)
  x,y = drotm(x,y,param,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1,overwrite_x=0,overwrite_y=0)
  x,y = sswap(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  x,y = dswap(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  x,y = cswap(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  x,y = zswap(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  x = sscal(a,x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  x = dscal(a,x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  x = cscal(a,x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  x = zscal(a,x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  x = csscal(a,x,n=(len(x)-offx)/abs(incx),offx=0,incx=1,overwrite_x=0)
  x = zdscal(a,x,n=(len(x)-offx)/abs(incx),offx=0,incx=1,overwrite_x=0)
  y = scopy(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  y = dcopy(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  y = ccopy(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  y = zcopy(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  z = saxpy(x,y,n=(len(x)-offx)/abs(incx),a=1.0,offx=0,incx=1,offy=0,incy=1)
  z = daxpy(x,y,n=(len(x)-offx)/abs(incx),a=1.0,offx=0,incx=1,offy=0,incy=1)
  z = caxpy(x,y,n=(len(x)-offx)/abs(incx),a=(1.0, 0.0),offx=0,incx=1,offy=0,incy=1)
  z = zaxpy(x,y,n=(len(x)-offx)/abs(incx),a=(1.0, 0.0),offx=0,incx=1,offy=0,incy=1)
  xy = sdot(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  xy = ddot(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  xy = cdotu(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  xy = zdotu(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  xy = cdotc(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  xy = zdotc(x,y,n=(len(x)-offx)/abs(incx),offx=0,incx=1,offy=0,incy=1)
  n2 = snrm2(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  n2 = scnrm2(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  n2 = dnrm2(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  n2 = dznrm2(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  s = sasum(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  s = scasum(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  s = dasum(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  s = dzasum(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  k = isamax(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  k = idamax(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  k = icamax(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  k = izamax(x,n=(len(x)-offx)/abs(incx),offx=0,incx=1)
  y = sgemv(alpha,a,x,beta=0.0,y=,offx=0,incx=1,offy=0,incy=1,trans=0,overwrite_y=0)
  y = dgemv(alpha,a,x,beta=0.0,y=,offx=0,incx=1,offy=0,incy=1,trans=0,overwrite_y=0)
  y = cgemv(alpha,a,x,beta=(0.0, 0.0),y=,offx=0,incx=1,offy=0,incy=1,trans=0,overwrite_y=0)
  y = zgemv(alpha,a,x,beta=(0.0, 0.0),y=,offx=0,incx=1,offy=0,incy=1,trans=0,overwrite_y=0)
  y = ssymv(alpha,a,x,beta=0.0,y=,offx=0,incx=1,offy=0,incy=1,lower=0,overwrite_y=0)
  y = dsymv(alpha,a,x,beta=0.0,y=,offx=0,incx=1,offy=0,incy=1,lower=0,overwrite_y=0)
  y = chemv(alpha,a,x,beta=(0.0, 0.0),y=,offx=0,incx=1,offy=0,incy=1,lower=0,overwrite_y=0)
  y = zhemv(alpha,a,x,beta=(0.0, 0.0),y=,offx=0,incx=1,offy=0,incy=1,lower=0,overwrite_y=0)
  x = strmv(a,x,offx=0,incx=1,lower=0,trans=0,unitdiag=0,overwrite_x=0)
  x = dtrmv(a,x,offx=0,incx=1,lower=0,trans=0,unitdiag=0,overwrite_x=0)
  x = ctrmv(a,x,offx=0,incx=1,lower=0,trans=0,unitdiag=0,overwrite_x=0)
  x = ztrmv(a,x,offx=0,incx=1,lower=0,trans=0,unitdiag=0,overwrite_x=0)
  a = sger(alpha,x,y,incx=1,incy=1,a=0.0,overwrite_x=1,overwrite_y=1,overwrite_a=0)
  a = dger(alpha,x,y,incx=1,incy=1,a=0.0,overwrite_x=1,overwrite_y=1,overwrite_a=0)
  a = cgeru(alpha,x,y,incx=1,incy=1,a=(0.0,0.0),overwrite_x=1,overwrite_y=1,overwrite_a=0)
  a = zgeru(alpha,x,y,incx=1,incy=1,a=(0.0,0.0),overwrite_x=1,overwrite_y=1,overwrite_a=0)
  a = cgerc(alpha,x,y,incx=1,incy=1,a=(0.0,0.0),overwrite_x=1,overwrite_y=1,overwrite_a=0)
  a = zgerc(alpha,x,y,incx=1,incy=1,a=(0.0,0.0),overwrite_x=1,overwrite_y=1,overwrite_a=0)
  a = ssyr(alpha,x,lower=0,incx=1,offx=0,n=(len(x)-1-offx)/abs(incx)+1,a=,overwrite_a=0)
  a = dsyr(alpha,x,lower=0,incx=1,offx=0,n=(len(x)-1-offx)/abs(incx)+1,a=,overwrite_a=0)
  a = csyr(alpha,x,lower=0,incx=1,offx=0,n=(len(x)-1-offx)/abs(incx)+1,a=,overwrite_a=0)
  a = zsyr(alpha,x,lower=0,incx=1,offx=0,n=(len(x)-1-offx)/abs(incx)+1,a=,overwrite_a=0)
  a = cher(alpha,x,lower=0,incx=1,offx=0,n=(len(x)-1-offx)/abs(incx)+1,a=,overwrite_a=0)
  a = zher(alpha,x,lower=0,incx=1,offx=0,n=(len(x)-1-offx)/abs(incx)+1,a=,overwrite_a=0)
  a = ssyr2(alpha,x,y,lower=0,incx=1,offx=0,incy=1,offy=0,n=((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1),a=,overwrite_a=0)
  a = dsyr2(alpha,x,y,lower=0,incx=1,offx=0,incy=1,offy=0,n=((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1),a=,overwrite_a=0)
  a = cher2(alpha,x,y,lower=0,incx=1,offx=0,incy=1,offy=0,n=((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1),a=,overwrite_a=0)
  a = zher2(alpha,x,y,lower=0,incx=1,offx=0,incy=1,offy=0,n=((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1),a=,overwrite_a=0)
  c = sgemm(alpha,a,b,beta=0.0,c=,trans_a=0,trans_b=0,overwrite_c=0)
  c = dgemm(alpha,a,b,beta=0.0,c=,trans_a=0,trans_b=0,overwrite_c=0)
  c = cgemm(alpha,a,b,beta=(0.0, 0.0),c=,trans_a=0,trans_b=0,overwrite_c=0)
  c = zgemm(alpha,a,b,beta=(0.0, 0.0),c=,trans_a=0,trans_b=0,overwrite_c=0)
  c = ssymm(alpha,a,b,beta=0.0,c=,side=0,lower=0,overwrite_c=0)
  c = dsymm(alpha,a,b,beta=0.0,c=,side=0,lower=0,overwrite_c=0)
  c = csymm(alpha,a,b,beta=(0.0, 0.0),c=,side=0,lower=0,overwrite_c=0)
  c = zsymm(alpha,a,b,beta=(0.0, 0.0),c=,side=0,lower=0,overwrite_c=0)
  c = chemm(alpha,a,b,beta=(0.0, 0.0),c=,side=0,lower=0,overwrite_c=0)
  c = zhemm(alpha,a,b,beta=(0.0, 0.0),c=,side=0,lower=0,overwrite_c=0)
  c = ssyrk(alpha,a,beta=0.0,c=,trans=0,lower=0,overwrite_c=0)
  c = dsyrk(alpha,a,beta=0.0,c=,trans=0,lower=0,overwrite_c=0)
  c = csyrk(alpha,a,beta=(0.0, 0.0),c=,trans=0,lower=0,overwrite_c=0)
  c = zsyrk(alpha,a,beta=(0.0, 0.0),c=,trans=0,lower=0,overwrite_c=0)
  c = cherk(alpha,a,beta=(0.0, 0.0),c=,trans=0,lower=0,overwrite_c=0)
  c = zherk(alpha,a,beta=(0.0, 0.0),c=,trans=0,lower=0,overwrite_c=0)
  c = ssyr2k(alpha,a,b,beta=0.0,c=,trans=0,lower=0,overwrite_c=0)
  c = dsyr2k(alpha,a,b,beta=0.0,c=,trans=0,lower=0,overwrite_c=0)
  c = csyr2k(alpha,a,b,beta=(0.0, 0.0),c=,trans=0,lower=0,overwrite_c=0)
  c = zsyr2k(alpha,a,b,beta=(0.0, 0.0),c=,trans=0,lower=0,overwrite_c=0)
  c = cher2k(alpha,a,b,beta=(0.0, 0.0),c=,trans=0,lower=0,overwrite_c=0)
  c = zher2k(alpha,a,b,beta=(0.0, 0.0),c=,trans=0,lower=0,overwrite_c=0)
  b = strmm(alpha,a,b,side=0,lower=0,trans_a=0,diag=0,overwrite_b=0)
  b = dtrmm(alpha,a,b,side=0,lower=0,trans_a=0,diag=0,overwrite_b=0)
  b = ctrmm(alpha,a,b,side=0,lower=0,trans_a=0,diag=0,overwrite_b=0)
  b = ztrmm(alpha,a,b,side=0,lower=0,trans_a=0,diag=0,overwrite_b=0)
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def caxpy(x, y, n=None, a=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    z = caxpy(x,y,[n,a,offx,incx,offy,incy])
    
    Wrapper for ``caxpy``.
    
    Parameters
    ----------
    x : input rank-1 array('F') with bounds (*)
    y : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    a : input complex, optional
        Default: (1.0, 0.0)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    z : rank-1 array('F') with bounds (*) and y storage
    """
    pass

def ccopy(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    y = ccopy(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``ccopy``.
    
    Parameters
    ----------
    x : input rank-1 array('F') with bounds (*)
    y : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    y : rank-1 array('F') with bounds (*)
    """
    pass

def cdotc(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    xy = cdotc(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``cdotc``.
    
    Parameters
    ----------
    x : input rank-1 array('F') with bounds (*)
    y : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    xy : complex
    """
    pass

def cdotu(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    xy = cdotu(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``cdotu``.
    
    Parameters
    ----------
    x : input rank-1 array('F') with bounds (*)
    y : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    xy : complex
    """
    pass

def cgemm(alpha, a, b, beta=None, c=None, trans_a=None, trans_b=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = cgemm(alpha,a,b,[beta,c,trans_a,trans_b,overwrite_c])
    
    Wrapper for ``cgemm``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('F') with bounds (lda,ka)
    b : input rank-2 array('F') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('F') with bounds (m,n)
    overwrite_c : input int, optional
        Default: 0
    trans_a : input int, optional
        Default: 0
    trans_b : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('F') with bounds (m,n)
    """
    pass

def cgemv(alpha, a, x, beta=None, y=None, offx=None, incx=None, offy=None, incy=None, trans=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    y = cgemv(alpha,a,x,[beta,y,offx,incx,offy,incy,trans,overwrite_y])
    
    Wrapper for ``cgemv``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('F') with bounds (m,n)
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    y : input rank-1 array('F') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    trans : input int, optional
        Default: 0
    
    Returns
    -------
    y : rank-1 array('F') with bounds (ly)
    """
    pass

def cgerc(alpha, x, y, incx=None, incy=None, a=None, overwrite_x=None, overwrite_y=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = cgerc(alpha,x,y,[incx,incy,a,overwrite_x,overwrite_y,overwrite_a])
    
    Wrapper for ``cgerc``.
    
    Parameters
    ----------
    alpha : input complex
    x : input rank-1 array('F') with bounds (m)
    y : input rank-1 array('F') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 1
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 1
    incy : input int, optional
        Default: 1
    a : input rank-2 array('F') with bounds (m,n), optional
        Default: (0.0,0.0)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('F') with bounds (m,n)
    """
    pass

def cgeru(alpha, x, y, incx=None, incy=None, a=None, overwrite_x=None, overwrite_y=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = cgeru(alpha,x,y,[incx,incy,a,overwrite_x,overwrite_y,overwrite_a])
    
    Wrapper for ``cgeru``.
    
    Parameters
    ----------
    alpha : input complex
    x : input rank-1 array('F') with bounds (m)
    y : input rank-1 array('F') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 1
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 1
    incy : input int, optional
        Default: 1
    a : input rank-2 array('F') with bounds (m,n), optional
        Default: (0.0,0.0)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('F') with bounds (m,n)
    """
    pass

def chemm(alpha, a, b, beta=None, c=None, side=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = chemm(alpha,a,b,[beta,c,side,lower,overwrite_c])
    
    Wrapper for ``chemm``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('F') with bounds (lda,ka)
    b : input rank-2 array('F') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('F') with bounds (m,n)
    overwrite_c : input int, optional
        Default: 0
    side : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('F') with bounds (m,n)
    """
    pass

def chemv(alpha, a, x, beta=None, y=None, offx=None, incx=None, offy=None, incy=None, lower=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    y = chemv(alpha,a,x,[beta,y,offx,incx,offy,incy,lower,overwrite_y])
    
    Wrapper for ``chemv``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('F') with bounds (n,n)
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    y : input rank-1 array('F') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    y : rank-1 array('F') with bounds (ly)
    """
    pass

def cher(alpha, x, lower=None, incx=None, offx=None, n=None, a=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = cher(alpha,x,[lower,incx,offx,n,a,overwrite_a])
    
    Wrapper for ``cher``.
    
    Parameters
    ----------
    alpha : input complex
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    n : input int, optional
        Default: (len(x)-1-offx)/abs(incx)+1
    a : input rank-2 array('F') with bounds (n,n)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('F') with bounds (n,n)
    """
    pass

def cher2(alpha, x, y, lower=None, incx=None, offx=None, incy=None, offy=None, n=None, a=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = cher2(alpha,x,y,[lower,incx,offx,incy,offy,n,a,overwrite_a])
    
    Wrapper for ``cher2``.
    
    Parameters
    ----------
    alpha : input complex
    x : input rank-1 array('F') with bounds (*)
    y : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    n : input int, optional
        Default: ((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1)
    a : input rank-2 array('F') with bounds (n,n)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('F') with bounds (n,n)
    """
    pass

def cher2k(alpha, a, b, beta=None, c=None, trans=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = cher2k(alpha,a,b,[beta,c,trans,lower,overwrite_c])
    
    Wrapper for ``cher2k``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('F') with bounds (lda,ka)
    b : input rank-2 array('F') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('F') with bounds (n,n)
    overwrite_c : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('F') with bounds (n,n)
    """
    pass

def cherk(alpha, a, beta=None, c=None, trans=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = cherk(alpha,a,[beta,c,trans,lower,overwrite_c])
    
    Wrapper for ``cherk``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('F') with bounds (lda,ka)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('F') with bounds (n,n)
    overwrite_c : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('F') with bounds (n,n)
    """
    pass

def crotg(a, b): # real signature unknown; restored from __doc__
    """
    c,s = crotg(a,b)
    
    Wrapper for ``crotg``.
    
    Parameters
    ----------
    a : input complex
    b : input complex
    
    Returns
    -------
    c : complex
    s : complex
    """
    pass

def cscal(a, x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    x = cscal(a,x,[n,offx,incx])
    
    Wrapper for ``cscal``.
    
    Parameters
    ----------
    a : input complex
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('F') with bounds (*)
    """
    pass

def csrot(x, y, c, s, n=None, offx=None, incx=None, offy=None, incy=None, overwrite_x=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    x,y = csrot(x,y,c,s,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])
    
    Wrapper for ``csrot``.
    
    Parameters
    ----------
    x : input rank-1 array('F') with bounds (*)
    y : input rank-1 array('F') with bounds (*)
    c : input float
    s : input float
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-1-offx)/abs(incx)+1
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 0
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('F') with bounds (*)
    y : rank-1 array('F') with bounds (*)
    """
    pass

def csscal(a, x, n=None, offx=None, incx=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    x = csscal(a,x,[n,offx,incx,overwrite_x])
    
    Wrapper for ``csscal``.
    
    Parameters
    ----------
    a : input float
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('F') with bounds (*)
    """
    pass

def cswap(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    x,y = cswap(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``cswap``.
    
    Parameters
    ----------
    x : input rank-1 array('F') with bounds (*)
    y : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('F') with bounds (*)
    y : rank-1 array('F') with bounds (*)
    """
    pass

def csymm(alpha, a, b, beta=None, c=None, side=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = csymm(alpha,a,b,[beta,c,side,lower,overwrite_c])
    
    Wrapper for ``csymm``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('F') with bounds (lda,ka)
    b : input rank-2 array('F') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('F') with bounds (m,n)
    overwrite_c : input int, optional
        Default: 0
    side : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('F') with bounds (m,n)
    """
    pass

def csyr(alpha, x, lower=None, incx=None, offx=None, n=None, a=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = csyr(alpha,x,[lower,incx,offx,n,a,overwrite_a])
    
    Wrapper for ``csyr``.
    
    Parameters
    ----------
    alpha : input complex
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    n : input int, optional
        Default: (len(x)-1-offx)/abs(incx)+1
    a : input rank-2 array('F') with bounds (n,n)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('F') with bounds (n,n)
    """
    pass

def csyr2k(alpha, a, b, beta=None, c=None, trans=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = csyr2k(alpha,a,b,[beta,c,trans,lower,overwrite_c])
    
    Wrapper for ``csyr2k``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('F') with bounds (lda,ka)
    b : input rank-2 array('F') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('F') with bounds (n,n)
    overwrite_c : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('F') with bounds (n,n)
    """
    pass

def csyrk(alpha, a, beta=None, c=None, trans=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = csyrk(alpha,a,[beta,c,trans,lower,overwrite_c])
    
    Wrapper for ``csyrk``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('F') with bounds (lda,ka)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('F') with bounds (n,n)
    overwrite_c : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('F') with bounds (n,n)
    """
    pass

def ctrmm(alpha, a, b, side=None, lower=None, trans_a=None, diag=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    b = ctrmm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])
    
    Wrapper for ``ctrmm``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('F') with bounds (lda,k)
    b : input rank-2 array('F') with bounds (ldb,n)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    side : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans_a : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    b : rank-2 array('F') with bounds (ldb,n)
    """
    pass

def ctrmv(a, x, offx=None, incx=None, lower=None, trans=None, unitdiag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    x = ctrmv(a,x,[offx,incx,lower,trans,unitdiag,overwrite_x])
    
    Wrapper for ``ctrmv``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    unitdiag : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-1 array('F') with bounds (*)
    """
    pass

def dasum(x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    s = dasum(x,[n,offx,incx])
    
    Wrapper for ``dasum``.
    
    Parameters
    ----------
    x : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    s : float
    """
    pass

def daxpy(x, y, n=None, a=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    z = daxpy(x,y,[n,a,offx,incx,offy,incy])
    
    Wrapper for ``daxpy``.
    
    Parameters
    ----------
    x : input rank-1 array('d') with bounds (*)
    y : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    a : input float, optional
        Default: 1.0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    z : rank-1 array('d') with bounds (*) and y storage
    """
    pass

def dcopy(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    y = dcopy(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``dcopy``.
    
    Parameters
    ----------
    x : input rank-1 array('d') with bounds (*)
    y : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    y : rank-1 array('d') with bounds (*)
    """
    pass

def ddot(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    xy = ddot(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``ddot``.
    
    Parameters
    ----------
    x : input rank-1 array('d') with bounds (*)
    y : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    xy : float
    """
    pass

def dgemm(alpha, a, b, beta=None, c=None, trans_a=None, trans_b=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = dgemm(alpha,a,b,[beta,c,trans_a,trans_b,overwrite_c])
    
    Wrapper for ``dgemm``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('d') with bounds (lda,ka)
    b : input rank-2 array('d') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input float, optional
        Default: 0.0
    c : input rank-2 array('d') with bounds (m,n)
    overwrite_c : input int, optional
        Default: 0
    trans_a : input int, optional
        Default: 0
    trans_b : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('d') with bounds (m,n)
    """
    pass

def dgemv(alpha, a, x, beta=None, y=None, offx=None, incx=None, offy=None, incy=None, trans=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    y = dgemv(alpha,a,x,[beta,y,offx,incx,offy,incy,trans,overwrite_y])
    
    Wrapper for ``dgemv``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('d') with bounds (m,n)
    x : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    beta : input float, optional
        Default: 0.0
    y : input rank-1 array('d') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    trans : input int, optional
        Default: 0
    
    Returns
    -------
    y : rank-1 array('d') with bounds (ly)
    """
    pass

def dger(alpha, x, y, incx=None, incy=None, a=None, overwrite_x=None, overwrite_y=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = dger(alpha,x,y,[incx,incy,a,overwrite_x,overwrite_y,overwrite_a])
    
    Wrapper for ``dger``.
    
    Parameters
    ----------
    alpha : input float
    x : input rank-1 array('d') with bounds (m)
    y : input rank-1 array('d') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 1
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 1
    incy : input int, optional
        Default: 1
    a : input rank-2 array('d') with bounds (m,n), optional
        Default: 0.0
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('d') with bounds (m,n)
    """
    pass

def dnrm2(x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    n2 = dnrm2(x,[n,offx,incx])
    
    Wrapper for ``dnrm2``.
    
    Parameters
    ----------
    x : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    n2 : float
    """
    pass

def drot(x, y, c, s, n=None, offx=None, incx=None, offy=None, incy=None, overwrite_x=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    x,y = drot(x,y,c,s,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])
    
    Wrapper for ``drot``.
    
    Parameters
    ----------
    x : input rank-1 array('d') with bounds (*)
    y : input rank-1 array('d') with bounds (*)
    c : input float
    s : input float
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-1-offx)/abs(incx)+1
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 0
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('d') with bounds (*)
    y : rank-1 array('d') with bounds (*)
    """
    pass

def drotg(a, b): # real signature unknown; restored from __doc__
    """
    c,s = drotg(a,b)
    
    Wrapper for ``drotg``.
    
    Parameters
    ----------
    a : input float
    b : input float
    
    Returns
    -------
    c : float
    s : float
    """
    pass

def drotm(x, y, param, n=None, offx=None, incx=None, offy=None, incy=None, overwrite_x=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    x,y = drotm(x,y,param,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])
    
    Wrapper for ``drotm``.
    
    Parameters
    ----------
    x : input rank-1 array('d') with bounds (*)
    y : input rank-1 array('d') with bounds (*)
    param : input rank-1 array('d') with bounds (5)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 0
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('d') with bounds (*)
    y : rank-1 array('d') with bounds (*)
    """
    pass

def drotmg(d1, d2, x1, y1): # real signature unknown; restored from __doc__
    """
    param = drotmg(d1,d2,x1,y1)
    
    Wrapper for ``drotmg``.
    
    Parameters
    ----------
    d1 : input float
    d2 : input float
    x1 : input float
    y1 : input float
    
    Returns
    -------
    param : rank-1 array('d') with bounds (5)
    """
    pass

def dscal(a, x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    x = dscal(a,x,[n,offx,incx])
    
    Wrapper for ``dscal``.
    
    Parameters
    ----------
    a : input float
    x : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('d') with bounds (*)
    """
    pass

def dswap(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    x,y = dswap(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``dswap``.
    
    Parameters
    ----------
    x : input rank-1 array('d') with bounds (*)
    y : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('d') with bounds (*)
    y : rank-1 array('d') with bounds (*)
    """
    pass

def dsymm(alpha, a, b, beta=None, c=None, side=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = dsymm(alpha,a,b,[beta,c,side,lower,overwrite_c])
    
    Wrapper for ``dsymm``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('d') with bounds (lda,ka)
    b : input rank-2 array('d') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input float, optional
        Default: 0.0
    c : input rank-2 array('d') with bounds (m,n)
    overwrite_c : input int, optional
        Default: 0
    side : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('d') with bounds (m,n)
    """
    pass

def dsymv(alpha, a, x, beta=None, y=None, offx=None, incx=None, offy=None, incy=None, lower=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    y = dsymv(alpha,a,x,[beta,y,offx,incx,offy,incy,lower,overwrite_y])
    
    Wrapper for ``dsymv``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('d') with bounds (n,n)
    x : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    beta : input float, optional
        Default: 0.0
    y : input rank-1 array('d') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    y : rank-1 array('d') with bounds (ly)
    """
    pass

def dsyr(alpha, x, lower=None, incx=None, offx=None, n=None, a=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = dsyr(alpha,x,[lower,incx,offx,n,a,overwrite_a])
    
    Wrapper for ``dsyr``.
    
    Parameters
    ----------
    alpha : input float
    x : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    n : input int, optional
        Default: (len(x)-1-offx)/abs(incx)+1
    a : input rank-2 array('d') with bounds (n,n)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('d') with bounds (n,n)
    """
    pass

def dsyr2(alpha, x, y, lower=None, incx=None, offx=None, incy=None, offy=None, n=None, a=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = dsyr2(alpha,x,y,[lower,incx,offx,incy,offy,n,a,overwrite_a])
    
    Wrapper for ``dsyr2``.
    
    Parameters
    ----------
    alpha : input float
    x : input rank-1 array('d') with bounds (*)
    y : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    n : input int, optional
        Default: ((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1)
    a : input rank-2 array('d') with bounds (n,n)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('d') with bounds (n,n)
    """
    pass

def dsyr2k(alpha, a, b, beta=None, c=None, trans=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = dsyr2k(alpha,a,b,[beta,c,trans,lower,overwrite_c])
    
    Wrapper for ``dsyr2k``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('d') with bounds (lda,ka)
    b : input rank-2 array('d') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input float, optional
        Default: 0.0
    c : input rank-2 array('d') with bounds (n,n)
    overwrite_c : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('d') with bounds (n,n)
    """
    pass

def dsyrk(alpha, a, beta=None, c=None, trans=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = dsyrk(alpha,a,[beta,c,trans,lower,overwrite_c])
    
    Wrapper for ``dsyrk``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('d') with bounds (lda,ka)
    
    Other Parameters
    ----------------
    beta : input float, optional
        Default: 0.0
    c : input rank-2 array('d') with bounds (n,n)
    overwrite_c : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('d') with bounds (n,n)
    """
    pass

def dtrmm(alpha, a, b, side=None, lower=None, trans_a=None, diag=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    b = dtrmm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])
    
    Wrapper for ``dtrmm``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('d') with bounds (lda,k)
    b : input rank-2 array('d') with bounds (ldb,n)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    side : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans_a : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    b : rank-2 array('d') with bounds (ldb,n)
    """
    pass

def dtrmv(a, x, offx=None, incx=None, lower=None, trans=None, unitdiag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    x = dtrmv(a,x,[offx,incx,lower,trans,unitdiag,overwrite_x])
    
    Wrapper for ``dtrmv``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    x : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    unitdiag : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-1 array('d') with bounds (*)
    """
    pass

def dzasum(x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    s = dzasum(x,[n,offx,incx])
    
    Wrapper for ``dzasum``.
    
    Parameters
    ----------
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    s : float
    """
    pass

def dznrm2(x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    n2 = dznrm2(x,[n,offx,incx])
    
    Wrapper for ``dznrm2``.
    
    Parameters
    ----------
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    n2 : float
    """
    pass

def icamax(x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    k = icamax(x,[n,offx,incx])
    
    Wrapper for ``icamax``.
    
    Parameters
    ----------
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    k : int
    """
    pass

def idamax(x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    k = idamax(x,[n,offx,incx])
    
    Wrapper for ``idamax``.
    
    Parameters
    ----------
    x : input rank-1 array('d') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    k : int
    """
    pass

def isamax(x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    k = isamax(x,[n,offx,incx])
    
    Wrapper for ``isamax``.
    
    Parameters
    ----------
    x : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    k : int
    """
    pass

def izamax(x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    k = izamax(x,[n,offx,incx])
    
    Wrapper for ``izamax``.
    
    Parameters
    ----------
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    k : int
    """
    pass

def sasum(x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    s = sasum(x,[n,offx,incx])
    
    Wrapper for ``sasum``.
    
    Parameters
    ----------
    x : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    s : float
    """
    pass

def saxpy(x, y, n=None, a=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    z = saxpy(x,y,[n,a,offx,incx,offy,incy])
    
    Wrapper for ``saxpy``.
    
    Parameters
    ----------
    x : input rank-1 array('f') with bounds (*)
    y : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    a : input float, optional
        Default: 1.0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    z : rank-1 array('f') with bounds (*) and y storage
    """
    pass

def scasum(x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    s = scasum(x,[n,offx,incx])
    
    Wrapper for ``scasum``.
    
    Parameters
    ----------
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    s : float
    """
    pass

def scnrm2(x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    n2 = scnrm2(x,[n,offx,incx])
    
    Wrapper for ``scnrm2``.
    
    Parameters
    ----------
    x : input rank-1 array('F') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    n2 : float
    """
    pass

def scopy(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    y = scopy(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``scopy``.
    
    Parameters
    ----------
    x : input rank-1 array('f') with bounds (*)
    y : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    y : rank-1 array('f') with bounds (*)
    """
    pass

def sdot(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    xy = sdot(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``sdot``.
    
    Parameters
    ----------
    x : input rank-1 array('f') with bounds (*)
    y : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    xy : float
    """
    pass

def sgemm(alpha, a, b, beta=None, c=None, trans_a=None, trans_b=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = sgemm(alpha,a,b,[beta,c,trans_a,trans_b,overwrite_c])
    
    Wrapper for ``sgemm``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('f') with bounds (lda,ka)
    b : input rank-2 array('f') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input float, optional
        Default: 0.0
    c : input rank-2 array('f') with bounds (m,n)
    overwrite_c : input int, optional
        Default: 0
    trans_a : input int, optional
        Default: 0
    trans_b : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('f') with bounds (m,n)
    """
    pass

def sgemv(alpha, a, x, beta=None, y=None, offx=None, incx=None, offy=None, incy=None, trans=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    y = sgemv(alpha,a,x,[beta,y,offx,incx,offy,incy,trans,overwrite_y])
    
    Wrapper for ``sgemv``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('f') with bounds (m,n)
    x : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    beta : input float, optional
        Default: 0.0
    y : input rank-1 array('f') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    trans : input int, optional
        Default: 0
    
    Returns
    -------
    y : rank-1 array('f') with bounds (ly)
    """
    pass

def sger(alpha, x, y, incx=None, incy=None, a=None, overwrite_x=None, overwrite_y=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = sger(alpha,x,y,[incx,incy,a,overwrite_x,overwrite_y,overwrite_a])
    
    Wrapper for ``sger``.
    
    Parameters
    ----------
    alpha : input float
    x : input rank-1 array('f') with bounds (m)
    y : input rank-1 array('f') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 1
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 1
    incy : input int, optional
        Default: 1
    a : input rank-2 array('f') with bounds (m,n), optional
        Default: 0.0
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('f') with bounds (m,n)
    """
    pass

def snrm2(x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    n2 = snrm2(x,[n,offx,incx])
    
    Wrapper for ``snrm2``.
    
    Parameters
    ----------
    x : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    n2 : float
    """
    pass

def srot(x, y, c, s, n=None, offx=None, incx=None, offy=None, incy=None, overwrite_x=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    x,y = srot(x,y,c,s,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])
    
    Wrapper for ``srot``.
    
    Parameters
    ----------
    x : input rank-1 array('f') with bounds (*)
    y : input rank-1 array('f') with bounds (*)
    c : input float
    s : input float
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-1-offx)/abs(incx)+1
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 0
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('f') with bounds (*)
    y : rank-1 array('f') with bounds (*)
    """
    pass

def srotg(a, b): # real signature unknown; restored from __doc__
    """
    c,s = srotg(a,b)
    
    Wrapper for ``srotg``.
    
    Parameters
    ----------
    a : input float
    b : input float
    
    Returns
    -------
    c : float
    s : float
    """
    pass

def srotm(x, y, param, n=None, offx=None, incx=None, offy=None, incy=None, overwrite_x=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    x,y = srotm(x,y,param,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])
    
    Wrapper for ``srotm``.
    
    Parameters
    ----------
    x : input rank-1 array('f') with bounds (*)
    y : input rank-1 array('f') with bounds (*)
    param : input rank-1 array('f') with bounds (5)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 0
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('f') with bounds (*)
    y : rank-1 array('f') with bounds (*)
    """
    pass

def srotmg(d1, d2, x1, y1): # real signature unknown; restored from __doc__
    """
    param = srotmg(d1,d2,x1,y1)
    
    Wrapper for ``srotmg``.
    
    Parameters
    ----------
    d1 : input float
    d2 : input float
    x1 : input float
    y1 : input float
    
    Returns
    -------
    param : rank-1 array('f') with bounds (5)
    """
    pass

def sscal(a, x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    x = sscal(a,x,[n,offx,incx])
    
    Wrapper for ``sscal``.
    
    Parameters
    ----------
    a : input float
    x : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('f') with bounds (*)
    """
    pass

def sswap(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    x,y = sswap(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``sswap``.
    
    Parameters
    ----------
    x : input rank-1 array('f') with bounds (*)
    y : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('f') with bounds (*)
    y : rank-1 array('f') with bounds (*)
    """
    pass

def ssymm(alpha, a, b, beta=None, c=None, side=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = ssymm(alpha,a,b,[beta,c,side,lower,overwrite_c])
    
    Wrapper for ``ssymm``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('f') with bounds (lda,ka)
    b : input rank-2 array('f') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input float, optional
        Default: 0.0
    c : input rank-2 array('f') with bounds (m,n)
    overwrite_c : input int, optional
        Default: 0
    side : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('f') with bounds (m,n)
    """
    pass

def ssymv(alpha, a, x, beta=None, y=None, offx=None, incx=None, offy=None, incy=None, lower=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    y = ssymv(alpha,a,x,[beta,y,offx,incx,offy,incy,lower,overwrite_y])
    
    Wrapper for ``ssymv``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('f') with bounds (n,n)
    x : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    beta : input float, optional
        Default: 0.0
    y : input rank-1 array('f') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    y : rank-1 array('f') with bounds (ly)
    """
    pass

def ssyr(alpha, x, lower=None, incx=None, offx=None, n=None, a=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = ssyr(alpha,x,[lower,incx,offx,n,a,overwrite_a])
    
    Wrapper for ``ssyr``.
    
    Parameters
    ----------
    alpha : input float
    x : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    n : input int, optional
        Default: (len(x)-1-offx)/abs(incx)+1
    a : input rank-2 array('f') with bounds (n,n)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('f') with bounds (n,n)
    """
    pass

def ssyr2(alpha, x, y, lower=None, incx=None, offx=None, incy=None, offy=None, n=None, a=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = ssyr2(alpha,x,y,[lower,incx,offx,incy,offy,n,a,overwrite_a])
    
    Wrapper for ``ssyr2``.
    
    Parameters
    ----------
    alpha : input float
    x : input rank-1 array('f') with bounds (*)
    y : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    n : input int, optional
        Default: ((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1)
    a : input rank-2 array('f') with bounds (n,n)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('f') with bounds (n,n)
    """
    pass

def ssyr2k(alpha, a, b, beta=None, c=None, trans=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = ssyr2k(alpha,a,b,[beta,c,trans,lower,overwrite_c])
    
    Wrapper for ``ssyr2k``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('f') with bounds (lda,ka)
    b : input rank-2 array('f') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input float, optional
        Default: 0.0
    c : input rank-2 array('f') with bounds (n,n)
    overwrite_c : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('f') with bounds (n,n)
    """
    pass

def ssyrk(alpha, a, beta=None, c=None, trans=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = ssyrk(alpha,a,[beta,c,trans,lower,overwrite_c])
    
    Wrapper for ``ssyrk``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('f') with bounds (lda,ka)
    
    Other Parameters
    ----------------
    beta : input float, optional
        Default: 0.0
    c : input rank-2 array('f') with bounds (n,n)
    overwrite_c : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('f') with bounds (n,n)
    """
    pass

def strmm(alpha, a, b, side=None, lower=None, trans_a=None, diag=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    b = strmm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])
    
    Wrapper for ``strmm``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-2 array('f') with bounds (lda,k)
    b : input rank-2 array('f') with bounds (ldb,n)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    side : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans_a : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    b : rank-2 array('f') with bounds (ldb,n)
    """
    pass

def strmv(a, x, offx=None, incx=None, lower=None, trans=None, unitdiag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    x = strmv(a,x,[offx,incx,lower,trans,unitdiag,overwrite_x])
    
    Wrapper for ``strmv``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    x : input rank-1 array('f') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    unitdiag : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-1 array('f') with bounds (*)
    """
    pass

def zaxpy(x, y, n=None, a=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    z = zaxpy(x,y,[n,a,offx,incx,offy,incy])
    
    Wrapper for ``zaxpy``.
    
    Parameters
    ----------
    x : input rank-1 array('D') with bounds (*)
    y : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    a : input complex, optional
        Default: (1.0, 0.0)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    z : rank-1 array('D') with bounds (*) and y storage
    """
    pass

def zcopy(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    y = zcopy(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``zcopy``.
    
    Parameters
    ----------
    x : input rank-1 array('D') with bounds (*)
    y : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    y : rank-1 array('D') with bounds (*)
    """
    pass

def zdotc(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    xy = zdotc(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``zdotc``.
    
    Parameters
    ----------
    x : input rank-1 array('D') with bounds (*)
    y : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    xy : complex
    """
    pass

def zdotu(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    xy = zdotu(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``zdotu``.
    
    Parameters
    ----------
    x : input rank-1 array('D') with bounds (*)
    y : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    xy : complex
    """
    pass

def zdrot(x, y, c, s, n=None, offx=None, incx=None, offy=None, incy=None, overwrite_x=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    x,y = zdrot(x,y,c,s,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])
    
    Wrapper for ``zdrot``.
    
    Parameters
    ----------
    x : input rank-1 array('D') with bounds (*)
    y : input rank-1 array('D') with bounds (*)
    c : input float
    s : input float
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-1-offx)/abs(incx)+1
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 0
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('D') with bounds (*)
    y : rank-1 array('D') with bounds (*)
    """
    pass

def zdscal(a, x, n=None, offx=None, incx=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    x = zdscal(a,x,[n,offx,incx,overwrite_x])
    
    Wrapper for ``zdscal``.
    
    Parameters
    ----------
    a : input float
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('D') with bounds (*)
    """
    pass

def zgemm(alpha, a, b, beta=None, c=None, trans_a=None, trans_b=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = zgemm(alpha,a,b,[beta,c,trans_a,trans_b,overwrite_c])
    
    Wrapper for ``zgemm``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('D') with bounds (lda,ka)
    b : input rank-2 array('D') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('D') with bounds (m,n)
    overwrite_c : input int, optional
        Default: 0
    trans_a : input int, optional
        Default: 0
    trans_b : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('D') with bounds (m,n)
    """
    pass

def zgemv(alpha, a, x, beta=None, y=None, offx=None, incx=None, offy=None, incy=None, trans=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    y = zgemv(alpha,a,x,[beta,y,offx,incx,offy,incy,trans,overwrite_y])
    
    Wrapper for ``zgemv``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('D') with bounds (m,n)
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    y : input rank-1 array('D') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    trans : input int, optional
        Default: 0
    
    Returns
    -------
    y : rank-1 array('D') with bounds (ly)
    """
    pass

def zgerc(alpha, x, y, incx=None, incy=None, a=None, overwrite_x=None, overwrite_y=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = zgerc(alpha,x,y,[incx,incy,a,overwrite_x,overwrite_y,overwrite_a])
    
    Wrapper for ``zgerc``.
    
    Parameters
    ----------
    alpha : input complex
    x : input rank-1 array('D') with bounds (m)
    y : input rank-1 array('D') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 1
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 1
    incy : input int, optional
        Default: 1
    a : input rank-2 array('D') with bounds (m,n), optional
        Default: (0.0,0.0)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('D') with bounds (m,n)
    """
    pass

def zgeru(alpha, x, y, incx=None, incy=None, a=None, overwrite_x=None, overwrite_y=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = zgeru(alpha,x,y,[incx,incy,a,overwrite_x,overwrite_y,overwrite_a])
    
    Wrapper for ``zgeru``.
    
    Parameters
    ----------
    alpha : input complex
    x : input rank-1 array('D') with bounds (m)
    y : input rank-1 array('D') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 1
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 1
    incy : input int, optional
        Default: 1
    a : input rank-2 array('D') with bounds (m,n), optional
        Default: (0.0,0.0)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('D') with bounds (m,n)
    """
    pass

def zhemm(alpha, a, b, beta=None, c=None, side=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = zhemm(alpha,a,b,[beta,c,side,lower,overwrite_c])
    
    Wrapper for ``zhemm``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('D') with bounds (lda,ka)
    b : input rank-2 array('D') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('D') with bounds (m,n)
    overwrite_c : input int, optional
        Default: 0
    side : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('D') with bounds (m,n)
    """
    pass

def zhemv(alpha, a, x, beta=None, y=None, offx=None, incx=None, offy=None, incy=None, lower=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    y = zhemv(alpha,a,x,[beta,y,offx,incx,offy,incy,lower,overwrite_y])
    
    Wrapper for ``zhemv``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('D') with bounds (n,n)
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    y : input rank-1 array('D') with bounds (ly)
    overwrite_y : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    y : rank-1 array('D') with bounds (ly)
    """
    pass

def zher(alpha, x, lower=None, incx=None, offx=None, n=None, a=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = zher(alpha,x,[lower,incx,offx,n,a,overwrite_a])
    
    Wrapper for ``zher``.
    
    Parameters
    ----------
    alpha : input complex
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    n : input int, optional
        Default: (len(x)-1-offx)/abs(incx)+1
    a : input rank-2 array('D') with bounds (n,n)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('D') with bounds (n,n)
    """
    pass

def zher2(alpha, x, y, lower=None, incx=None, offx=None, incy=None, offy=None, n=None, a=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = zher2(alpha,x,y,[lower,incx,offx,incy,offy,n,a,overwrite_a])
    
    Wrapper for ``zher2``.
    
    Parameters
    ----------
    alpha : input complex
    x : input rank-1 array('D') with bounds (*)
    y : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    n : input int, optional
        Default: ((len(x)-1-offx)/abs(incx)+1 <=(len(y)-1-offy)/abs(incy)+1 ?(len(x)-1-offx)/abs(incx)+1 :(len(y)-1-offy)/abs(incy)+1)
    a : input rank-2 array('D') with bounds (n,n)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('D') with bounds (n,n)
    """
    pass

def zher2k(alpha, a, b, beta=None, c=None, trans=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = zher2k(alpha,a,b,[beta,c,trans,lower,overwrite_c])
    
    Wrapper for ``zher2k``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('D') with bounds (lda,ka)
    b : input rank-2 array('D') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('D') with bounds (n,n)
    overwrite_c : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('D') with bounds (n,n)
    """
    pass

def zherk(alpha, a, beta=None, c=None, trans=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = zherk(alpha,a,[beta,c,trans,lower,overwrite_c])
    
    Wrapper for ``zherk``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('D') with bounds (lda,ka)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('D') with bounds (n,n)
    overwrite_c : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('D') with bounds (n,n)
    """
    pass

def zrotg(a, b): # real signature unknown; restored from __doc__
    """
    c,s = zrotg(a,b)
    
    Wrapper for ``zrotg``.
    
    Parameters
    ----------
    a : input complex
    b : input complex
    
    Returns
    -------
    c : complex
    s : complex
    """
    pass

def zscal(a, x, n=None, offx=None, incx=None): # real signature unknown; restored from __doc__
    """
    x = zscal(a,x,[n,offx,incx])
    
    Wrapper for ``zscal``.
    
    Parameters
    ----------
    a : input complex
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('D') with bounds (*)
    """
    pass

def zswap(x, y, n=None, offx=None, incx=None, offy=None, incy=None): # real signature unknown; restored from __doc__
    """
    x,y = zswap(x,y,[n,offx,incx,offy,incy])
    
    Wrapper for ``zswap``.
    
    Parameters
    ----------
    x : input rank-1 array('D') with bounds (*)
    y : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (len(x)-offx)/abs(incx)
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('D') with bounds (*)
    y : rank-1 array('D') with bounds (*)
    """
    pass

def zsymm(alpha, a, b, beta=None, c=None, side=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = zsymm(alpha,a,b,[beta,c,side,lower,overwrite_c])
    
    Wrapper for ``zsymm``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('D') with bounds (lda,ka)
    b : input rank-2 array('D') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('D') with bounds (m,n)
    overwrite_c : input int, optional
        Default: 0
    side : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('D') with bounds (m,n)
    """
    pass

def zsyr(alpha, x, lower=None, incx=None, offx=None, n=None, a=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = zsyr(alpha,x,[lower,incx,offx,n,a,overwrite_a])
    
    Wrapper for ``zsyr``.
    
    Parameters
    ----------
    alpha : input complex
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    offx : input int, optional
        Default: 0
    n : input int, optional
        Default: (len(x)-1-offx)/abs(incx)+1
    a : input rank-2 array('D') with bounds (n,n)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('D') with bounds (n,n)
    """
    pass

def zsyr2k(alpha, a, b, beta=None, c=None, trans=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = zsyr2k(alpha,a,b,[beta,c,trans,lower,overwrite_c])
    
    Wrapper for ``zsyr2k``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('D') with bounds (lda,ka)
    b : input rank-2 array('D') with bounds (ldb,kb)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('D') with bounds (n,n)
    overwrite_c : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('D') with bounds (n,n)
    """
    pass

def zsyrk(alpha, a, beta=None, c=None, trans=None, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = zsyrk(alpha,a,[beta,c,trans,lower,overwrite_c])
    
    Wrapper for ``zsyrk``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('D') with bounds (lda,ka)
    
    Other Parameters
    ----------------
    beta : input complex, optional
        Default: (0.0, 0.0)
    c : input rank-2 array('D') with bounds (n,n)
    overwrite_c : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('D') with bounds (n,n)
    """
    pass

def ztrmm(alpha, a, b, side=None, lower=None, trans_a=None, diag=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    b = ztrmm(alpha,a,b,[side,lower,trans_a,diag,overwrite_b])
    
    Wrapper for ``ztrmm``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-2 array('D') with bounds (lda,k)
    b : input rank-2 array('D') with bounds (ldb,n)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    side : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    trans_a : input int, optional
        Default: 0
    diag : input int, optional
        Default: 0
    
    Returns
    -------
    b : rank-2 array('D') with bounds (ldb,n)
    """
    pass

def ztrmv(a, x, offx=None, incx=None, lower=None, trans=None, unitdiag=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    x = ztrmv(a,x,[offx,incx,lower,trans,unitdiag,overwrite_x])
    
    Wrapper for ``ztrmv``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    x : input rank-1 array('D') with bounds (*)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    unitdiag : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-1 array('D') with bounds (*)
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

