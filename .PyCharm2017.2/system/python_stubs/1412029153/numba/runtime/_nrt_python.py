# encoding: utf-8
# module numba.runtime._nrt_python
# from D:\ProgramData\Anaconda3\lib\site-packages\numba\runtime\_nrt_python.cp36-win_amd64.pyd
# by generator 1.145
""" No docs """
# no imports

# functions

def meminfo_alloc(*args, **kwargs): # real signature unknown
    pass

def meminfo_alloc_safe(*args, **kwargs): # real signature unknown
    pass

def meminfo_new(*args, **kwargs): # real signature unknown
    pass

def memsys_get_stats_alloc(*args, **kwargs): # real signature unknown
    pass

def memsys_get_stats_free(*args, **kwargs): # real signature unknown
    pass

def memsys_get_stats_mi_alloc(*args, **kwargs): # real signature unknown
    pass

def memsys_get_stats_mi_free(*args, **kwargs): # real signature unknown
    pass

def memsys_set_atomic_cas(*args, **kwargs): # real signature unknown
    pass

def memsys_set_atomic_inc_dec(*args, **kwargs): # real signature unknown
    pass

def memsys_shutdown(*args, **kwargs): # real signature unknown
    pass

def memsys_use_cpython_allocator(*args, **kwargs): # real signature unknown
    pass

# classes

class _MemInfo(object):
    # no doc
    def acquire(self, *args, **kwargs): # real signature unknown
        """ Increment the reference count """
        pass

    def release(self, *args, **kwargs): # real signature unknown
        """ Decrement the reference count """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the data pointer as an integer"""

    refcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the refcount"""



# variables with complex values

c_helpers = {
    'Allocate': 140705112734016,
    'Free': 140705112734064,
    'MemInfo_alloc': 140705112733200,
    'MemInfo_alloc_aligned': 140705112734992,
    'MemInfo_alloc_dtor_safe': 140705112733856,
    'MemInfo_alloc_safe': 140705112734112,
    'MemInfo_alloc_safe_aligned': 140705112734592,
    'MemInfo_call_dtor': 140705112734272,
    'MemInfo_new_varsize': 140705112733472,
    'MemInfo_release': 140705112734368,
    'MemInfo_varsize_alloc': 140705112733632,
    'MemInfo_varsize_free': 140705112734832,
    'MemInfo_varsize_realloc': 140705112734128,
    'adapt_buffer_from_python': 140705112729664,
    'adapt_ndarray_from_python': 140705112730624,
    'adapt_ndarray_to_python': 140705112729968,
}

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

