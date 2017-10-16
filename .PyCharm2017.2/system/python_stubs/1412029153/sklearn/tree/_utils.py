# encoding: utf-8
# module sklearn.tree._utils
# from D:\ProgramData\Anaconda3\lib\site-packages\sklearn\tree\_utils.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # D:\ProgramData\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def _realloc_test(*args, **kwargs): # real signature unknown
    pass

# classes

class PriorityHeap(object):
    """
    A priority queue implemented as a binary heap.
    
        The heap invariant is that the impurity improvement of the parent record
        is larger then the impurity improvement of the children.
    
        Attributes
        ----------
        capacity : SIZE_t
            The capacity of the heap
    
        heap_ptr : SIZE_t
            The water mark of the heap; the heap grows from left to right in the
            array ``heap_``. The following invariant holds ``heap_ptr < capacity``.
    
        heap_ : PriorityHeapRecord*
            The array of heap records. The maximum element is on the left;
            the heap grows from left to right
    """
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


class Stack(object):
    """
    A LIFO data structure.
    
        Attributes
        ----------
        capacity : SIZE_t
            The elements the stack can hold; if more added then ``self.stack_``
            needs to be resized.
    
        top : SIZE_t
            The number of elements currently on the stack.
    
        stack : StackRecord pointer
            The stack of records (upward in the stack corresponds to the right).
    """
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


class WeightedMedianCalculator(object):
    """
    A class to handle calculation of the weighted median from streams of
        data. To do so, it maintains a parameter ``k`` such that the sum of the
        weights in the range [0,k) is greater than or equal to half of the total
        weight. By minimizing the value of ``k`` that fulfills this constraint,
        calculating the median is done by either taking the value of the sample
        at index ``k-1`` of ``samples`` (samples[k-1].data) or the average of
        the samples at index ``k-1`` and ``k`` of ``samples``
        ((samples[k-1] + samples[k]) / 2).
    
        Attributes
        ----------
        initial_capacity : SIZE_t
            The initial capacity of the WeightedMedianCalculator.
    
        samples : WeightedPQueue
            Holds the samples (consisting of values and their weights) used in the
            weighted median calculation.
    
        total_weight : DOUBLE_t
            The sum of the weights of items in ``samples``. Represents the total
            weight of all samples used in the median calculation.
    
        k : SIZE_t
            Index used to calculate the median.
    
        sum_w_0_k : DOUBLE_t
            The sum of the weights from samples[0:k]. Used in the weighted
            median calculation; minimizing the value of ``k`` such that
            ``sum_w_0_k`` >= ``total_weight / 2`` provides a mechanism for
            calculating the median in constant time.
    """
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


class WeightedPQueue(object):
    """
    A priority queue class, always sorted in increasing order.
    
        Attributes
        ----------
        capacity : SIZE_t
            The capacity of the priority queue.
    
        array_ptr : SIZE_t
            The water mark of the priority queue; the priority queue grows from
            left to right in the array ``array_``. ``array_ptr`` is always
            less than ``capacity``.
    
        array_ : WeightedPQueueRecord*
            The array of priority queue records. The minimum element is on the
            left at index 0, and the maximum element is on the right at index
            ``array_ptr-1``.
    """
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


# variables with complex values

__loader__ = None # (!) real value is ''

__pyx_capi__ = {
    '__pyx_fuse_0safe_realloc': None, # (!) real value is ''
    '__pyx_fuse_10safe_realloc': None, # (!) real value is ''
    '__pyx_fuse_1safe_realloc': None, # (!) real value is ''
    '__pyx_fuse_2safe_realloc': None, # (!) real value is ''
    '__pyx_fuse_3safe_realloc': None, # (!) real value is ''
    '__pyx_fuse_4safe_realloc': None, # (!) real value is ''
    '__pyx_fuse_5safe_realloc': None, # (!) real value is ''
    '__pyx_fuse_6safe_realloc': None, # (!) real value is ''
    '__pyx_fuse_7safe_realloc': None, # (!) real value is ''
    '__pyx_fuse_8safe_realloc': None, # (!) real value is ''
    '__pyx_fuse_9safe_realloc': None, # (!) real value is ''
    'log': None, # (!) real value is ''
    'rand_int': None, # (!) real value is ''
    'rand_uniform': None, # (!) real value is ''
    'sizet_ptr_to_ndarray': None, # (!) real value is ''
}

__spec__ = None # (!) real value is ''

__test__ = {}
