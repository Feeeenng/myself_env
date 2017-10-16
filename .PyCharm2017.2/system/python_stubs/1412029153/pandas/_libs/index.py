# encoding: utf-8
# module pandas._libs.index
# from D:\ProgramData\Anaconda3\lib\site-packages\pandas\_libs\index.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # D:\ProgramData\Anaconda3\lib\site-packages\numpy\__init__.py
import pandas._libs.tslib as tslib # D:\ProgramData\Anaconda3\lib\site-packages\pandas\_libs\tslib.cp36-win_amd64.pyd
import pandas._libs.algos as algos # D:\ProgramData\Anaconda3\lib\site-packages\pandas\_libs\algos.cp36-win_amd64.pyd
import pandas._libs.hashtable as _hash # D:\ProgramData\Anaconda3\lib\site-packages\pandas\_libs\hashtable.cp36-win_amd64.pyd
import pytz as pytz # D:\ProgramData\Anaconda3\lib\site-packages\pytz\__init__.py
from pandas._libs.tslib import Timedelta, Timestamp

import datetime as __datetime


# Variables with simple values

have_pytz = True

_SIZE_CUTOFF = 1000000

# functions

def convert_scalar(*args, **kwargs): # real signature unknown
    pass

def get_value_at(*args, **kwargs): # real signature unknown
    pass

def set_value_at(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_DatetimeEngine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Float64Engine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_IndexEngine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Int64Engine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_MultiIndexHashEngine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_MultiIndexObjectEngine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_ObjectEngine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_TimedeltaEngine(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_UInt64Engine(*args, **kwargs): # real signature unknown
    pass

# classes

class IndexEngine(object):
    # no doc
    def clear_mapping(self, *args, **kwargs): # real signature unknown
        pass

    def get_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_indexer_non_unique(self, *args, **kwargs): # real signature unknown
        """
        return an indexer suitable for takng from a non unique index
                    return the labels in the same order ast the target
                    and a missing indexer into the targets (which correspond
                    to the -1 indicies in the results
        """
        pass

    def get_loc(self, *args, **kwargs): # real signature unknown
        pass

    def get_value(self, *args, **kwargs): # real signature unknown
        """ arr : 1-dimensional ndarray """
        pass

    def set_value(self, *args, **kwargs): # real signature unknown
        """ arr : 1-dimensional ndarray """
        pass

    def sizeof(self, *args, **kwargs): # real signature unknown
        """ return the sizeof our mapping """
        pass

    def _call_monotonic(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
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

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        pass

    is_mapping_populated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_monotonic_decreasing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_monotonic_increasing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_unique = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    over_size_threshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vgetter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class Int64Engine(IndexEngine):
    # no doc
    def get_backfill_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_pad_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def _call_monotonic(self, *args, **kwargs): # real signature unknown
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


class DatetimeEngine(Int64Engine):
    # no doc
    def get_backfill_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_loc(self, *args, **kwargs): # real signature unknown
        pass

    def get_pad_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def _call_monotonic(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
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


class Float64Engine(IndexEngine):
    # no doc
    def get_backfill_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_pad_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def _call_monotonic(self, *args, **kwargs): # real signature unknown
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


class ObjectEngine(IndexEngine):
    # no doc
    def get_backfill_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_pad_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def _call_monotonic(self, *args, **kwargs): # real signature unknown
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


class MultiIndexHashEngine(ObjectEngine):
    """
    Use a hashing based MultiIndex impl
        but use the IndexEngine for computation
    
        This provides good performance with larger MI's
    """
    def get_backfill_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_loc(self, *args, **kwargs): # real signature unknown
        pass

    def get_pad_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def _call_monotonic(self, *args, **kwargs): # real signature unknown
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


class MultiIndexObjectEngine(ObjectEngine):
    """
    provide the same interface as the MultiIndexEngine
        but use the IndexEngine for computation
    
        This provides good performance with samller MI's
    """
    def get_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_loc(self, *args, **kwargs): # real signature unknown
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


class TimedeltaEngine(DatetimeEngine):
    # no doc
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


class UInt64Engine(IndexEngine):
    # no doc
    def get_backfill_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def get_pad_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def _call_monotonic(self, *args, **kwargs): # real signature unknown
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


class _du_utc(__datetime.tzinfo):
    """ This is a tzinfo object that represents the UTC time zone. """
    def dst(self, dt): # reliably restored by inspect
        # no doc
        pass

    def fromutc(self, dt): # reliably restored by inspect
        """
        Fast track version of fromutc() returns the original ``dt`` object for
                any valid :py:class:`datetime.datetime` object.
        """
        pass

    def is_ambiguous(self, dt): # reliably restored by inspect
        """
        Whether or not the "wall time" of a given datetime is ambiguous in this
                zone.
        
                :param dt:
                    A :py:class:`datetime.datetime`, naive or time zone aware.
        
        
                :return:
                    Returns ``True`` if ambiguous, ``False`` otherwise.
        
                .. versionadded:: 2.6.0
        """
        pass

    def tzname(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def utcoffset(self, dt): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ helper for pickle """
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __hash__ = None


# variables with complex values

UTC = tslib.UTC

_backfill_functions = {
    'float64': algos.backfill_float64,
    'int64': algos.backfill_int64,
    'object': algos.backfill_object,
}

_pad_functions = {
    'float64': algos.pad_float64,
    'int64': algos.pad_int64,
    'object': algos.pad_object,
}

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

