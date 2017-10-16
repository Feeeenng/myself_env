# encoding: utf-8
# module scipy.linalg.cython_blas
# from D:\ProgramData\Anaconda3\lib\site-packages\scipy\linalg\cython_blas.cp36-win_amd64.pyd
# by generator 1.145
"""
BLAS Functions for Cython
=========================

Usable from Cython via::

    cimport scipy.linalg.cython_blas

These wrappers do not check for alignment of arrays.
Alignment should be checked before these wrappers are used.

Raw function pointers (Fortran-style pointer arguments):

- caxpy
- ccopy
- cdotc
- cdotu
- cgbmv
- cgemm
- cgemv
- cgerc
- cgeru
- chbmv
- chemm
- chemv
- cher
- cher2
- cher2k
- cherk
- chpmv
- chpr
- chpr2
- crotg
- cscal
- csrot
- csscal
- cswap
- csymm
- csyr2k
- csyrk
- ctbmv
- ctbsv
- ctpmv
- ctpsv
- ctrmm
- ctrmv
- ctrsm
- ctrsv
- dasum
- daxpy
- dcabs1
- dcopy
- ddot
- dgbmv
- dgemm
- dgemv
- dger
- dnrm2
- drot
- drotg
- drotm
- drotmg
- dsbmv
- dscal
- dsdot
- dspmv
- dspr
- dspr2
- dswap
- dsymm
- dsymv
- dsyr
- dsyr2
- dsyr2k
- dsyrk
- dtbmv
- dtbsv
- dtpmv
- dtpsv
- dtrmm
- dtrmv
- dtrsm
- dtrsv
- dzasum
- dznrm2
- icamax
- idamax
- isamax
- izamax
- lsame
- sasum
- saxpy
- scasum
- scnrm2
- scopy
- sdot
- sdsdot
- sgbmv
- sgemm
- sgemv
- sger
- snrm2
- srot
- srotg
- srotm
- srotmg
- ssbmv
- sscal
- sspmv
- sspr
- sspr2
- sswap
- ssymm
- ssymv
- ssyr
- ssyr2
- ssyr2k
- ssyrk
- stbmv
- stbsv
- stpmv
- stpsv
- strmm
- strmv
- strsm
- strsv
- zaxpy
- zcopy
- zdotc
- zdotu
- zdrot
- zdscal
- zgbmv
- zgemm
- zgemv
- zgerc
- zgeru
- zhbmv
- zhemm
- zhemv
- zher
- zher2
- zher2k
- zherk
- zhpmv
- zhpr
- zhpr2
- zrotg
- zscal
- zswap
- zsymm
- zsyr2k
- zsyrk
- ztbmv
- ztbsv
- ztpmv
- ztpsv
- ztrmm
- ztrmv
- ztrsm
- ztrsv
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def _test_cdotc(*args, **kwargs): # real signature unknown
    pass

def _test_cdotu(*args, **kwargs): # real signature unknown
    pass

def _test_dasum(*args, **kwargs): # real signature unknown
    pass

def _test_ddot(*args, **kwargs): # real signature unknown
    pass

def _test_dgemm(*args, **kwargs): # real signature unknown
    pass

def _test_dnrm2(*args, **kwargs): # real signature unknown
    pass

def _test_dzasum(*args, **kwargs): # real signature unknown
    pass

def _test_dznrm2(*args, **kwargs): # real signature unknown
    pass

def _test_icamax(*args, **kwargs): # real signature unknown
    pass

def _test_idamax(*args, **kwargs): # real signature unknown
    pass

def _test_isamax(*args, **kwargs): # real signature unknown
    pass

def _test_izamax(*args, **kwargs): # real signature unknown
    pass

def _test_sasum(*args, **kwargs): # real signature unknown
    pass

def _test_scasum(*args, **kwargs): # real signature unknown
    pass

def _test_scnrm2(*args, **kwargs): # real signature unknown
    pass

def _test_sdot(*args, **kwargs): # real signature unknown
    pass

def _test_snrm2(*args, **kwargs): # real signature unknown
    pass

def _test_zdotc(*args, **kwargs): # real signature unknown
    pass

def _test_zdotu(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__pyx_capi__ = {
    'caxpy': None, # (!) real value is ''
    'ccopy': None, # (!) real value is ''
    'cdotc': None, # (!) real value is ''
    'cdotu': None, # (!) real value is ''
    'cgbmv': None, # (!) real value is ''
    'cgemm': None, # (!) real value is ''
    'cgemv': None, # (!) real value is ''
    'cgerc': None, # (!) real value is ''
    'cgeru': None, # (!) real value is ''
    'chbmv': None, # (!) real value is ''
    'chemm': None, # (!) real value is ''
    'chemv': None, # (!) real value is ''
    'cher': None, # (!) real value is ''
    'cher2': None, # (!) real value is ''
    'cher2k': None, # (!) real value is ''
    'cherk': None, # (!) real value is ''
    'chpmv': None, # (!) real value is ''
    'chpr': None, # (!) real value is ''
    'chpr2': None, # (!) real value is ''
    'crotg': None, # (!) real value is ''
    'cscal': None, # (!) real value is ''
    'csrot': None, # (!) real value is ''
    'csscal': None, # (!) real value is ''
    'cswap': None, # (!) real value is ''
    'csymm': None, # (!) real value is ''
    'csyr2k': None, # (!) real value is ''
    'csyrk': None, # (!) real value is ''
    'ctbmv': None, # (!) real value is ''
    'ctbsv': None, # (!) real value is ''
    'ctpmv': None, # (!) real value is ''
    'ctpsv': None, # (!) real value is ''
    'ctrmm': None, # (!) real value is ''
    'ctrmv': None, # (!) real value is ''
    'ctrsm': None, # (!) real value is ''
    'ctrsv': None, # (!) real value is ''
    'dasum': None, # (!) real value is ''
    'daxpy': None, # (!) real value is ''
    'dcabs1': None, # (!) real value is ''
    'dcopy': None, # (!) real value is ''
    'ddot': None, # (!) real value is ''
    'dgbmv': None, # (!) real value is ''
    'dgemm': None, # (!) real value is ''
    'dgemv': None, # (!) real value is ''
    'dger': None, # (!) real value is ''
    'dnrm2': None, # (!) real value is ''
    'drot': None, # (!) real value is ''
    'drotg': None, # (!) real value is ''
    'drotm': None, # (!) real value is ''
    'drotmg': None, # (!) real value is ''
    'dsbmv': None, # (!) real value is ''
    'dscal': None, # (!) real value is ''
    'dsdot': None, # (!) real value is ''
    'dspmv': None, # (!) real value is ''
    'dspr': None, # (!) real value is ''
    'dspr2': None, # (!) real value is ''
    'dswap': None, # (!) real value is ''
    'dsymm': None, # (!) real value is ''
    'dsymv': None, # (!) real value is ''
    'dsyr': None, # (!) real value is ''
    'dsyr2': None, # (!) real value is ''
    'dsyr2k': None, # (!) real value is ''
    'dsyrk': None, # (!) real value is ''
    'dtbmv': None, # (!) real value is ''
    'dtbsv': None, # (!) real value is ''
    'dtpmv': None, # (!) real value is ''
    'dtpsv': None, # (!) real value is ''
    'dtrmm': None, # (!) real value is ''
    'dtrmv': None, # (!) real value is ''
    'dtrsm': None, # (!) real value is ''
    'dtrsv': None, # (!) real value is ''
    'dzasum': None, # (!) real value is ''
    'dznrm2': None, # (!) real value is ''
    'icamax': None, # (!) real value is ''
    'idamax': None, # (!) real value is ''
    'isamax': None, # (!) real value is ''
    'izamax': None, # (!) real value is ''
    'lsame': None, # (!) real value is ''
    'sasum': None, # (!) real value is ''
    'saxpy': None, # (!) real value is ''
    'scasum': None, # (!) real value is ''
    'scnrm2': None, # (!) real value is ''
    'scopy': None, # (!) real value is ''
    'sdot': None, # (!) real value is ''
    'sdsdot': None, # (!) real value is ''
    'sgbmv': None, # (!) real value is ''
    'sgemm': None, # (!) real value is ''
    'sgemv': None, # (!) real value is ''
    'sger': None, # (!) real value is ''
    'snrm2': None, # (!) real value is ''
    'srot': None, # (!) real value is ''
    'srotg': None, # (!) real value is ''
    'srotm': None, # (!) real value is ''
    'srotmg': None, # (!) real value is ''
    'ssbmv': None, # (!) real value is ''
    'sscal': None, # (!) real value is ''
    'sspmv': None, # (!) real value is ''
    'sspr': None, # (!) real value is ''
    'sspr2': None, # (!) real value is ''
    'sswap': None, # (!) real value is ''
    'ssymm': None, # (!) real value is ''
    'ssymv': None, # (!) real value is ''
    'ssyr': None, # (!) real value is ''
    'ssyr2': None, # (!) real value is ''
    'ssyr2k': None, # (!) real value is ''
    'ssyrk': None, # (!) real value is ''
    'stbmv': None, # (!) real value is ''
    'stbsv': None, # (!) real value is ''
    'stpmv': None, # (!) real value is ''
    'stpsv': None, # (!) real value is ''
    'strmm': None, # (!) real value is ''
    'strmv': None, # (!) real value is ''
    'strsm': None, # (!) real value is ''
    'strsv': None, # (!) real value is ''
    'zaxpy': None, # (!) real value is ''
    'zcopy': None, # (!) real value is ''
    'zdotc': None, # (!) real value is ''
    'zdotu': None, # (!) real value is ''
    'zdrot': None, # (!) real value is ''
    'zdscal': None, # (!) real value is ''
    'zgbmv': None, # (!) real value is ''
    'zgemm': None, # (!) real value is ''
    'zgemv': None, # (!) real value is ''
    'zgerc': None, # (!) real value is ''
    'zgeru': None, # (!) real value is ''
    'zhbmv': None, # (!) real value is ''
    'zhemm': None, # (!) real value is ''
    'zhemv': None, # (!) real value is ''
    'zher': None, # (!) real value is ''
    'zher2': None, # (!) real value is ''
    'zher2k': None, # (!) real value is ''
    'zherk': None, # (!) real value is ''
    'zhpmv': None, # (!) real value is ''
    'zhpr': None, # (!) real value is ''
    'zhpr2': None, # (!) real value is ''
    'zrotg': None, # (!) real value is ''
    'zscal': None, # (!) real value is ''
    'zswap': None, # (!) real value is ''
    'zsymm': None, # (!) real value is ''
    'zsyr2k': None, # (!) real value is ''
    'zsyrk': None, # (!) real value is ''
    'ztbmv': None, # (!) real value is ''
    'ztbsv': None, # (!) real value is ''
    'ztpmv': None, # (!) real value is ''
    'ztpsv': None, # (!) real value is ''
    'ztrmm': None, # (!) real value is ''
    'ztrmv': None, # (!) real value is ''
    'ztrsm': None, # (!) real value is ''
    'ztrsv': None, # (!) real value is ''
}

__spec__ = None # (!) real value is ''

__test__ = {}

