# encoding: utf-8
# module mkl.service
# from D:\ProgramData\Anaconda3\lib\site-packages\mkl\service.cp36-win_amd64.pyd
# by generator 1.145
""" Extension module providing service functions for the MKL library """
# no imports

# functions

def get_cpu_clocks(): # real signature unknown; restored from __doc__
    """
    get_cpu_clocks() -> int
    
    Return the CPU clocks as an integer.
    """
    return 0

def get_cpu_frequency(): # real signature unknown; restored from __doc__
    """
    get_cpu_frequency() -> float
    
    Return CPU frequency in GHz as a float.
    """
    return 0.0

def get_max_threads(): # real signature unknown; restored from __doc__
    """
    get_max_threads() -> int
    
    Return the number of threads Intel MKL is targeting for parallelism.
    """
    return 0

def get_version_string(): # real signature unknown; restored from __doc__
    """
    get_version_string() -> str
    
    Return the MKL library version information as a string.
    """
    return ""

def mem_stat(): # real signature unknown; restored from __doc__
    """
    mem_stat() -> (int, int)
    
    Returns a tuple (bytes, count) containing memory usage statistics of the
    MKL allocator
    - number of bytes allocated (bytes).
    - number of allocated blocks (count).
    """
    pass

def set_num_threads(n): # real signature unknown; restored from __doc__
    """
    set_num_threads(n)
    
    Set the number of threads MKL should use.  This is only a hint, and no
    guaranteed is made this number of threads will actually be used.
    This function takes precedence over the environment variable
    MKL_NUM_THREADS.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

