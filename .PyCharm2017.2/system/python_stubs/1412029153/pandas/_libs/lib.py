# encoding: utf-8
# module pandas._libs.lib
# from D:\ProgramData\Anaconda3\lib\site-packages\pandas\_libs\lib.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # D:\ProgramData\Anaconda3\lib\site-packages\numpy\__init__.py
import sys as sys # <module 'sys' (built-in)>
import pandas._libs.tslib as tslib # D:\ProgramData\Anaconda3\lib\site-packages\pandas\_libs\tslib.cp36-win_amd64.pyd
import pandas._libs.interval as interval # D:\ProgramData\Anaconda3\lib\site-packages\pandas\_libs\interval.cp36-win_amd64.pyd
from pandas._libs.interval import Interval

from pandas._libs.tslib import NaT, Timedelta, Timestamp, get_timezone

import datetime as __datetime
import distutils.version as __distutils_version


# Variables with simple values

iNaT = -9223372036854775808

is_numpy_prior_1_6_2 = False

# functions

def apply_frame_axis0(*args, **kwargs): # real signature unknown
    pass

def array_equivalent_object(*args, **kwargs): # real signature unknown
    """
    perform an element by element comparion on 1-d object arrays
            taking into account nan positions
    """
    pass

def array_to_timestamp(*args, **kwargs): # real signature unknown
    pass

def arrmap(*args, **kwargs): # real signature unknown
    pass

def astype_intsafe(*args, **kwargs): # real signature unknown
    pass

def astype_str(*args, **kwargs): # real signature unknown
    pass

def astype_unicode(*args, **kwargs): # real signature unknown
    pass

def checknull(*args, **kwargs): # real signature unknown
    pass

def checknull_old(*args, **kwargs): # real signature unknown
    pass

def clean_index_list(*args, **kwargs): # real signature unknown
    """ Utility used in pandas.core.index._ensure_index """
    pass

def convert_json_to_lines(*args, **kwargs): # real signature unknown
    """
    replace comma separated json with line feeds, paying special attention
        to quotes & brackets
    """
    pass

def convert_sql_column(*args, **kwargs): # real signature unknown
    pass

def convert_timestamps(*args, **kwargs): # real signature unknown
    pass

def count_level_2d(*args, **kwargs): # real signature unknown
    pass

def dicts_to_array(*args, **kwargs): # real signature unknown
    pass

def downcast_int64(*args, **kwargs): # real signature unknown
    pass

def fast_multiget(*args, **kwargs): # real signature unknown
    pass

def fast_unique(*args, **kwargs): # real signature unknown
    pass

def fast_unique_multiple(*args, **kwargs): # real signature unknown
    pass

def fast_unique_multiple_list(*args, **kwargs): # real signature unknown
    pass

def fast_unique_multiple_list_gen(*args, **kwargs): # real signature unknown
    """
    Generate a list of unique values from a generator of lists.
    
        Parameters
        ----------
        gen : generator object
            A generator of lists from which the unique list is created
        sort : boolean
            Whether or not to sort the resulting unique list
    
        Returns
        -------
        unique_list : list of unique values
    """
    pass

def fast_zip(*args, **kwargs): # real signature unknown
    """ For zipping multiple ndarrays into an ndarray of tuples """
    pass

def fast_zip_fillna(*args, **kwargs): # real signature unknown
    """ For zipping multiple ndarrays into an ndarray of tuples """
    pass

def generate_bins_dt64(*args, **kwargs): # real signature unknown
    """ Int64 (datetime64) version of generic python version in groupby.py """
    pass

def generate_slices(*args, **kwargs): # real signature unknown
    pass

def get_blkno_indexers(*args, **kwargs): # real signature unknown
    """
    Enumerate contiguous runs of integers in ndarray.
    
        Iterate over elements of `blknos` yielding ``(blkno, slice(start, stop))``
        pairs for each contiguous run found.
    
        If `group` is True and there is more than one run for a certain blkno,
        ``(blkno, array)`` with an array containing positions of all elements equal
        to blkno.
    
        Returns
        -------
        iter : iterator of (int, slice or array)
    """
    pass

def get_level_sorter(*args, **kwargs): # real signature unknown
    """
    argsort for a single level of a multi-index, keeping the order of higher
        levels unchanged. `starts` points to starts of same-key indices w.r.t
        to leading levels; equivalent to:
            np.hstack([label[starts[i]:starts[i+1]].argsort(kind='mergesort')
                + starts[i] for i in range(len(starts) - 1)])
    """
    pass

def get_reverse_indexer(*args, **kwargs): # real signature unknown
    """
    Reverse indexing operation.
    
        Given `indexer`, make `indexer_inv` of it, such that::
    
            indexer_inv[indexer[x]] = x
    
        .. note:: If indexer is not unique, only first occurrence is accounted.
    """
    pass

def group_count(*args, **kwargs): # real signature unknown
    pass

def has_infs_f4(*args, **kwargs): # real signature unknown
    pass

def has_infs_f8(*args, **kwargs): # real signature unknown
    pass

def indexer_as_slice(*args, **kwargs): # real signature unknown
    pass

def indices_fast(*args, **kwargs): # real signature unknown
    pass

def infer_datetimelike_array(*args, **kwargs): # real signature unknown
    """
    infer if we have a datetime or timedelta array
        - date: we have *only* date and maybe strings, nulls
        - datetime: we have *only* datetimes and maybe strings, nulls
        - timedelta: we have *only* timedeltas and maybe strings, nulls
        - nat: we do not have *any* date, datetimes or timedeltas, but do have
          at least a NaT
        - mixed: other objects (strings or actual objects)
    
        Parameters
        ----------
        arr : object array
    
        Returns
        -------
        string: {datetime, timedelta, date, nat, mixed}
    """
    pass

def infer_dtype(foo=None, bar=None): # real signature unknown; restored from __doc__
    """
    Effeciently infer the type of a passed val, or list-like
        array of values. Return a string describing the type.
    
        Parameters
        ----------
        value : scalar, list, ndarray, or pandas type
    
        Returns
        -------
        string describing the common type of the input data.
        Results can include:
    
        - string
        - unicode
        - bytes
        - floating
        - integer
        - mixed-integer
        - mixed-integer-float
        - complex
        - categorical
        - boolean
        - datetime64
        - datetime
        - date
        - timedelta64
        - timedelta
        - time
        - period
        - mixed
    
        Raises
        ------
        TypeError if ndarray-like but cannot infer the dtype
    
        Notes
        -----
        - 'mixed' is the catchall for anything that is not otherwise
          specialized
        - 'mixed-integer-float' are floats and integers
        - 'mixed-integer' are integers mixed with non-integers
    
        Examples
        --------
        >>> infer_dtype(['foo', 'bar'])
        'string'
    
        >>> infer_dtype([b'foo', b'bar'])
        'bytes'
    
        >>> infer_dtype([1, 2, 3])
        'integer'
    
        >>> infer_dtype([1, 2, 3.5])
        'mixed-integer-float'
    
        >>> infer_dtype([1.0, 2.0, 3.5])
        'floating'
    
        >>> infer_dtype(['a', 1])
        'mixed-integer'
    
        >>> infer_dtype([True, False])
        'boolean'
    
        >>> infer_dtype([True, False, np.nan])
        'mixed'
    
        >>> infer_dtype([pd.Timestamp('20130101')])
        'datetime'
    
        >>> infer_dtype([datetime.date(2013, 1, 1)])
        'date'
    
        >>> infer_dtype([np.datetime64('2013-01-01')])
        'datetime64'
    
        >>> infer_dtype([datetime.timedelta(0, 1, 1)])
        'timedelta'
    
        >>> infer_dtype(pd.Series(list('aabc')).astype('category'))
        'categorical'
    """
    pass

def isnan(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    isnan(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    Test element-wise for NaN and return result as a boolean array.
    
    Parameters
    ----------
    x : array_like
        Input array.
    out : ndarray, None, or tuple of ndarray and None, optional
        A location into which the result is stored. If provided, it must have
        a shape that the inputs broadcast to. If not provided or `None`,
        a freshly-allocated array is returned. A tuple (possible only as a
        keyword argument) must have length equal to the number of outputs.
    where : array_like, optional
        Values of True indicate to calculate the ufunc at that position, values
        of False indicate to leave the value in the output alone.
    **kwargs
        For other keyword-only arguments, see the
        :ref:`ufunc docs <ufuncs.kwargs>`.
    
    Returns
    -------
    y : ndarray or bool
        For scalar input, the result is a new boolean with value True if
        the input is NaN; otherwise the value is False.
    
        For array input, the result is a boolean array of the same
        dimensions as the input and the values are True if the
        corresponding element of the input is NaN; otherwise the values are
        False.
    
    See Also
    --------
    isinf, isneginf, isposinf, isfinite, isnat
    
    Notes
    -----
    NumPy uses the IEEE Standard for Binary Floating-Point for Arithmetic
    (IEEE 754). This means that Not a Number is not equivalent to infinity.
    
    Examples
    --------
    >>> np.isnan(np.nan)
    True
    >>> np.isnan(np.inf)
    False
    >>> np.isnan([np.log(-1.),1.,np.log(0)])
    array([ True, False, False], dtype=bool)
    """
    pass

def isneginf_scalar(*args, **kwargs): # real signature unknown
    pass

def isnullobj(*args, **kwargs): # real signature unknown
    pass

def isnullobj2d(*args, **kwargs): # real signature unknown
    pass

def isnullobj2d_old(*args, **kwargs): # real signature unknown
    pass

def isnullobj_old(*args, **kwargs): # real signature unknown
    pass

def isposinf_scalar(*args, **kwargs): # real signature unknown
    pass

def isscalar(*args, **kwargs): # real signature unknown
    """
    Return True if given value is scalar.
    
        This includes:
        - numpy array scalar (e.g. np.int64)
        - Python builtin numerics
        - Python builtin byte arrays and strings
        - None
        - instances of datetime.datetime
        - instances of datetime.timedelta
        - Period
        - instances of decimal.Decimal
        - Interval
    """
    pass

def is_bool(*args, **kwargs): # real signature unknown
    pass

def is_bool_array(*args, **kwargs): # real signature unknown
    pass

def is_bytes_array(*args, **kwargs): # real signature unknown
    pass

def is_complex(*args, **kwargs): # real signature unknown
    pass

def is_datetime64_array(*args, **kwargs): # real signature unknown
    pass

def is_datetime_array(*args, **kwargs): # real signature unknown
    pass

def is_datetime_with_singletz_array(*args, **kwargs): # real signature unknown
    """
    Check values have the same tzinfo attribute.
        Doesn't check values are datetime-like types.
    """
    pass

def is_date_array(*args, **kwargs): # real signature unknown
    pass

def is_decimal(*args, **kwargs): # real signature unknown
    pass

def is_float(*args, **kwargs): # real signature unknown
    pass

def is_float_array(*args, **kwargs): # real signature unknown
    pass

def is_integer(*args, **kwargs): # real signature unknown
    pass

def is_integer_array(*args, **kwargs): # real signature unknown
    pass

def is_integer_float_array(*args, **kwargs): # real signature unknown
    pass

def is_interval(*args, **kwargs): # real signature unknown
    pass

def is_interval_array(*args, **kwargs): # real signature unknown
    pass

def is_lexsorted(*args, **kwargs): # real signature unknown
    pass

def is_period(*args, **kwargs): # real signature unknown
    """ Return a boolean if this is a Period object """
    pass

def is_period_array(*args, **kwargs): # real signature unknown
    pass

def is_string_array(*args, **kwargs): # real signature unknown
    pass

def is_timedelta64_array(*args, **kwargs): # real signature unknown
    pass

def is_timedelta_array(*args, **kwargs): # real signature unknown
    pass

def is_timedelta_or_timedelta64_array(*args, **kwargs): # real signature unknown
    """ infer with timedeltas and/or nat/none """
    pass

def is_time_array(*args, **kwargs): # real signature unknown
    pass

def is_unicode_array(*args, **kwargs): # real signature unknown
    pass

def item_from_zerodim(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    If the value is a zerodim array, return the item it contains.
    
        Examples
        --------
        >>> item_from_zerodim(1)
        1
        >>> item_from_zerodim('foobar')
        'foobar'
        >>> item_from_zerodim(np.array(1))
        1
        >>> item_from_zerodim(np.array([1]))
        array([1])
    """
    pass

def list_to_object_array(*args, **kwargs): # real signature unknown
    """
    Convert list to object ndarray. Seriously can't believe
        I had to write this function.
    """
    pass

def lookup_values(*args, **kwargs): # real signature unknown
    pass

def map_indices_list(*args, **kwargs): # real signature unknown
    """
    Produce a dict mapping the values of the input array to their respective
        locations.
    
        Example:
            array(['hi', 'there']) --> {'hi' : 0 , 'there' : 1}
    
        Better to do this with Cython because of the enormous speed boost.
    """
    pass

def map_infer(*args, **kwargs): # real signature unknown
    """
    Substitute for np.vectorize with pandas-friendly dtype inference
    
        Parameters
        ----------
        arr : ndarray
        f : function
    
        Returns
        -------
        mapped : ndarray
    """
    pass

def map_infer_mask(*args, **kwargs): # real signature unknown
    """
    Substitute for np.vectorize with pandas-friendly dtype inference
    
        Parameters
        ----------
        arr : ndarray
        f : function
    
        Returns
        -------
        mapped : ndarray
    """
    pass

def max_len_string_array(*args, **kwargs): # real signature unknown
    """ return the maximum size of elements in a 1-dim string array """
    pass

def maybe_booleans_to_slice(*args, **kwargs): # real signature unknown
    pass

def maybe_convert_bool(*args, **kwargs): # real signature unknown
    pass

def maybe_convert_numeric(*args, **kwargs): # real signature unknown
    """
    Convert object array to a numeric array if possible.
    
        Parameters
        ----------
        values : ndarray
            Array of object elements to convert.
        na_values : set
            Set of values that should be interpreted as NaN.
        convert_empty : bool, default True
            If an empty array-like object is encountered, whether to interpret
            that element as NaN or not. If set to False, a ValueError will be
            raised if such an element is encountered and 'coerce_numeric' is False.
        coerce_numeric : bool, default False
            If initial attempts to convert to numeric have failed, whether to
            force conversion to numeric via alternative methods or by setting the
            element to NaN. Otherwise, an Exception will be raised when such an
            element is encountered.
    
            This boolean also has an impact on how conversion behaves when a
            numeric array has no suitable numerical dtype to return (i.e. uint64,
            int32, uint8). If set to False, the original object array will be
            returned. Otherwise, a ValueError will be raised.
    
        Returns
        -------
        numeric_array : array of converted object values to numerical ones
    """
    pass

def maybe_convert_objects(*args, **kwargs): # real signature unknown
    """ Type inference function-- convert object array to proper dtype """
    pass

def maybe_indices_to_slice(*args, **kwargs): # real signature unknown
    pass

def memory_usage_of_objects(*args, **kwargs): # real signature unknown
    """
    return the memory usage of an object array in bytes,
        does not include the actual bytes of the pointers
    """
    pass

def reduce(*args, **kwargs): # real signature unknown
    """
    Parameters
        -----------
        arr : NDFrame object
        f : function
        axis : integer axis
        dummy : type of reduced output (series)
        labels : Index or None
    """
    pass

def row_bool_subset(*args, **kwargs): # real signature unknown
    pass

def row_bool_subset_object(*args, **kwargs): # real signature unknown
    pass

def sanitize_objects(*args, **kwargs): # real signature unknown
    pass

def scalar_binop(*args, **kwargs): # real signature unknown
    pass

def scalar_compare(*args, **kwargs): # real signature unknown
    pass

def slice_canonize(*args, **kwargs): # real signature unknown
    """ Convert slice to canonical bounded form. """
    pass

def slice_getitem(*args, **kwargs): # real signature unknown
    pass

def slice_get_indices_ex(*args, **kwargs): # real signature unknown
    """
    Get (start, stop, step, length) tuple for a slice.
    
        If `objlen` is not specified, slice must be bounded, otherwise the result
        will be wrong.
    """
    pass

def slice_len(*args, **kwargs): # real signature unknown
    """
    Get length of a bounded slice.
    
        The slice must not have any "open" bounds that would create dependency on
        container size, i.e.:
        - if ``s.step is None or s.step > 0``, ``s.stop`` is not ``None``
        - if ``s.step < 0``, ``s.start`` is not ``None``
    
        Otherwise, the result is unreliable.
    """
    pass

def string_array_replace_from_nan_rep(*args, **kwargs): # real signature unknown
    """
    Replace the values in the array with 'replacement' if
        they are 'nan_rep'. Return the same array.
    """
    pass

def time64_to_datetime(*args, **kwargs): # real signature unknown
    pass

def to_datetime(*args, **kwargs): # real signature unknown
    pass

def to_object_array(*args, **kwargs): # real signature unknown
    """
    Convert a list of lists into an object array.
    
        Parameters
        ----------
        rows : 2-d array (N, K)
            A list of lists to be converted into an array
        min_width : int
            The minimum width of the object array. If a list
            in `rows` contains fewer than `width` elements,
            the remaining elements in the corresponding row
            will all be `NaN`.
    
        Returns
        -------
        obj_array : numpy array of the object dtype
    """
    pass

def to_object_array_tuples(*args, **kwargs): # real signature unknown
    pass

def to_timestamp(*args, **kwargs): # real signature unknown
    pass

def try_parse_dates(*args, **kwargs): # real signature unknown
    pass

def try_parse_datetime_components(*args, **kwargs): # real signature unknown
    pass

def try_parse_date_and_time(*args, **kwargs): # real signature unknown
    pass

def try_parse_year_month_day(*args, **kwargs): # real signature unknown
    pass

def tuples_to_object_array(*args, **kwargs): # real signature unknown
    pass

def values_from_object(*args, **kwargs): # real signature unknown
    """ return my values or the object if we are say an ndarray """
    pass

def vec_binop(*args, **kwargs): # real signature unknown
    pass

def vec_compare(*args, **kwargs): # real signature unknown
    pass

def write_csv_rows(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_AxisProperty(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_BlockPlacement(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_cache_readonly(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Reducer(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_SeriesBinGrouper(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_SeriesGrouper(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Slider(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle__PandasNull(*args, **kwargs): # real signature unknown
    pass

# classes

class AxisProperty(object):
    # no doc
    def __delete__(self, *args, **kwargs): # real signature unknown
        """ Delete an attribute of instance. """
        pass

    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
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

    def __set__(self, *args, **kwargs): # real signature unknown
        """ Set an attribute of instance to value. """
        pass


class BlockPlacement(object):
    # no doc
    def add(self, *args, **kwargs): # real signature unknown
        pass

    def append(self, *args, **kwargs): # real signature unknown
        pass

    def delete(self, *args, **kwargs): # real signature unknown
        pass

    def isin(self, *args, **kwargs): # real signature unknown
        pass

    def sub(self, *args, **kwargs): # real signature unknown
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    as_array = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    as_slice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    indexer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_slice_like = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class BlockSlider(object):
    """ Only capable of sliding on axis=0 """
    def move(self, *args, **kwargs): # real signature unknown
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

    blocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    idx_slider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nblocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class cache_readonly(object):
    # no doc
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __delete__(self, *args, **kwargs): # real signature unknown
        """ Delete an attribute of instance. """
        pass

    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
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

    def __set__(self, *args, **kwargs): # real signature unknown
        """ Set an attribute of instance to value. """
        pass

    allow_setting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Decimal(object):
    """
    Construct a new Decimal object. 'value' can be an integer, string, tuple,
    or another Decimal object. If no value is given, return Decimal('0'). The
    context does not affect the conversion and is only passed to determine if
    the InvalidOperation trap is active.
    """
    def adjusted(self, *args, **kwargs): # real signature unknown
        """ Return the adjusted exponent of the number.  Defined as exp + digits - 1. """
        pass

    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Decimal.as_integer_ratio() -> (int, int)
        
        Return a pair of integers, whose ratio is exactly equal to the original
        Decimal and with a positive denominator. The ratio is in lowest terms.
        Raise OverflowError on infinities and a ValueError on NaNs.
        """
        pass

    def as_tuple(self, *args, **kwargs): # real signature unknown
        """ Return a tuple representation of the number. """
        pass

    def canonical(self, *args, **kwargs): # real signature unknown
        """
        Return the canonical encoding of the argument.  Currently, the encoding
        of a Decimal instance is always canonical, so this operation returns its
        argument unchanged.
        """
        pass

    def compare(self, *args, **kwargs): # real signature unknown
        """
        Compare self to other.  Return a decimal value:
        
            a or b is a NaN ==> Decimal('NaN')
            a < b           ==> Decimal('-1')
            a == b          ==> Decimal('0')
            a > b           ==> Decimal('1')
        """
        pass

    def compare_signal(self, *args, **kwargs): # real signature unknown
        """ Identical to compare, except that all NaNs signal. """
        pass

    def compare_total(self, Decimal, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Compare two operands using their abstract representation rather than
        their numerical value.  Similar to the compare() method, but the result
        gives a total ordering on Decimal instances.  Two Decimal instances with
        the same numeric value but different representations compare unequal
        in this ordering:
        
            >>> Decimal('12.0').compare_total(Decimal('12'))
            Decimal('-1')
        
        Quiet and signaling NaNs are also included in the total ordering. The result
        of this function is Decimal('0') if both operands have the same representation,
        Decimal('-1') if the first operand is lower in the total order than the second,
        and Decimal('1') if the first operand is higher in the total order than the
        second operand. See the specification for details of the total order.
        
        This operation is unaffected by context and is quiet: no flags are changed
        and no rounding is performed. As an exception, the C version may raise
        InvalidOperation if the second operand cannot be converted exactly.
        """
        pass

    def compare_total_mag(self, y): # real signature unknown; restored from __doc__
        """
        Compare two operands using their abstract representation rather than their
        value as in compare_total(), but ignoring the sign of each operand.
        
        x.compare_total_mag(y) is equivalent to x.copy_abs().compare_total(y.copy_abs()).
        
        This operation is unaffected by context and is quiet: no flags are changed
        and no rounding is performed. As an exception, the C version may raise
        InvalidOperation if the second operand cannot be converted exactly.
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Return self. """
        pass

    def copy_abs(self, *args, **kwargs): # real signature unknown
        """
        Return the absolute value of the argument.  This operation is unaffected by
        context and is quiet: no flags are changed and no rounding is performed.
        """
        pass

    def copy_negate(self, *args, **kwargs): # real signature unknown
        """
        Return the negation of the argument.  This operation is unaffected by context
        and is quiet: no flags are changed and no rounding is performed.
        """
        pass

    def copy_sign(self, Decimal, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Return a copy of the first operand with the sign set to be the same as the
        sign of the second operand. For example:
        
            >>> Decimal('2.3').copy_sign(Decimal('-1.5'))
            Decimal('-2.3')
        
        This operation is unaffected by context and is quiet: no flags are changed
        and no rounding is performed. As an exception, the C version may raise
        InvalidOperation if the second operand cannot be converted exactly.
        """
        pass

    def exp(self, *args, **kwargs): # real signature unknown
        """
        Return the value of the (natural) exponential function e**x at the given
        number.  The function always uses the ROUND_HALF_EVEN mode and the result
        is correctly rounded.
        """
        pass

    def fma(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Fused multiply-add.  Return self*other+third with no rounding of the
        intermediate product self*other.
        
            >>> Decimal(2).fma(3, 5)
            Decimal('11')
        """
        pass

    @classmethod
    def from_float(cls, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Class method that converts a float to a decimal number, exactly.
        Since 0.1 is not exactly representable in binary floating point,
        Decimal.from_float(0.1) is not the same as Decimal('0.1').
        
            >>> Decimal.from_float(0.1)
            Decimal('0.1000000000000000055511151231257827021181583404541015625')
            >>> Decimal.from_float(float('nan'))
            Decimal('NaN')
            >>> Decimal.from_float(float('inf'))
            Decimal('Infinity')
            >>> Decimal.from_float(float('-inf'))
            Decimal('-Infinity')
        """
        pass

    def is_canonical(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is canonical and False otherwise.  Currently,
        a Decimal instance is always canonical, so this operation always returns
        True.
        """
        pass

    def is_finite(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is a finite number, and False if the argument
        is infinite or a NaN.
        """
        pass

    def is_infinite(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is either positive or negative infinity and
        False otherwise.
        """
        pass

    def is_nan(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is a (quiet or signaling) NaN and False
        otherwise.
        """
        pass

    def is_normal(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is a normal finite non-zero number with an
        adjusted exponent greater than or equal to Emin. Return False if the
        argument is zero, subnormal, infinite or a NaN.
        """
        pass

    def is_qnan(self, *args, **kwargs): # real signature unknown
        """ Return True if the argument is a quiet NaN, and False otherwise. """
        pass

    def is_signed(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument has a negative sign and False otherwise.
        Note that both zeros and NaNs can carry signs.
        """
        pass

    def is_snan(self, *args, **kwargs): # real signature unknown
        """ Return True if the argument is a signaling NaN and False otherwise. """
        pass

    def is_subnormal(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is subnormal, and False otherwise. A number is
        subnormal if it is non-zero, finite, and has an adjusted exponent less
        than Emin.
        """
        pass

    def is_zero(self, *args, **kwargs): # real signature unknown
        """
        Return True if the argument is a (positive or negative) zero and False
        otherwise.
        """
        pass

    def ln(self, *args, **kwargs): # real signature unknown
        """
        Return the natural (base e) logarithm of the operand. The function always
        uses the ROUND_HALF_EVEN mode and the result is correctly rounded.
        """
        pass

    def log10(self, *args, **kwargs): # real signature unknown
        """
        Return the base ten logarithm of the operand. The function always uses the
        ROUND_HALF_EVEN mode and the result is correctly rounded.
        """
        pass

    def logb(self, *args, **kwargs): # real signature unknown
        """
        For a non-zero number, return the adjusted exponent of the operand as a
        Decimal instance.  If the operand is a zero, then Decimal('-Infinity') is
        returned and the DivisionByZero condition is raised. If the operand is
        an infinity then Decimal('Infinity') is returned.
        """
        pass

    def logical_and(self, *args, **kwargs): # real signature unknown
        """ Return the digit-wise 'and' of the two (logical) operands. """
        pass

    def logical_invert(self, *args, **kwargs): # real signature unknown
        """ Return the digit-wise inversion of the (logical) operand. """
        pass

    def logical_or(self, *args, **kwargs): # real signature unknown
        """ Return the digit-wise 'or' of the two (logical) operands. """
        pass

    def logical_xor(self, *args, **kwargs): # real signature unknown
        """ Return the digit-wise 'exclusive or' of the two (logical) operands. """
        pass

    def max(self, *args, **kwargs): # real signature unknown
        """
        Maximum of self and other.  If one operand is a quiet NaN and the other is
        numeric, the numeric operand is returned.
        """
        pass

    def max_mag(self, *args, **kwargs): # real signature unknown
        """
        Similar to the max() method, but the comparison is done using the absolute
        values of the operands.
        """
        pass

    def min(self, *args, **kwargs): # real signature unknown
        """
        Minimum of self and other. If one operand is a quiet NaN and the other is
        numeric, the numeric operand is returned.
        """
        pass

    def min_mag(self, *args, **kwargs): # real signature unknown
        """
        Similar to the min() method, but the comparison is done using the absolute
        values of the operands.
        """
        pass

    def next_minus(self, *args, **kwargs): # real signature unknown
        """
        Return the largest number representable in the given context (or in the
        current default context if no context is given) that is smaller than the
        given operand.
        """
        pass

    def next_plus(self, *args, **kwargs): # real signature unknown
        """
        Return the smallest number representable in the given context (or in the
        current default context if no context is given) that is larger than the
        given operand.
        """
        pass

    def next_toward(self, *args, **kwargs): # real signature unknown
        """
        If the two operands are unequal, return the number closest to the first
        operand in the direction of the second operand.  If both operands are
        numerically equal, return a copy of the first operand with the sign set
        to be the same as the sign of the second operand.
        """
        pass

    def normalize(self, *args, **kwargs): # real signature unknown
        """
        Normalize the number by stripping the rightmost trailing zeros and
        converting any result equal to Decimal('0') to Decimal('0e0').  Used
        for producing canonical values for members of an equivalence class.
        For example, Decimal('32.100') and Decimal('0.321000e+2') both normalize
        to the equivalent value Decimal('32.1').
        """
        pass

    def number_class(self, *args, **kwargs): # real signature unknown
        """
        Return a string describing the class of the operand.  The returned value
        is one of the following ten strings:
        
            * '-Infinity', indicating that the operand is negative infinity.
            * '-Normal', indicating that the operand is a negative normal number.
            * '-Subnormal', indicating that the operand is negative and subnormal.
            * '-Zero', indicating that the operand is a negative zero.
            * '+Zero', indicating that the operand is a positive zero.
            * '+Subnormal', indicating that the operand is positive and subnormal.
            * '+Normal', indicating that the operand is a positive normal number.
            * '+Infinity', indicating that the operand is positive infinity.
            * 'NaN', indicating that the operand is a quiet NaN (Not a Number).
            * 'sNaN', indicating that the operand is a signaling NaN.
        """
        pass

    def quantize(self, Decimal, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Return a value equal to the first operand after rounding and having the
        exponent of the second operand.
        
            >>> Decimal('1.41421356').quantize(Decimal('1.000'))
            Decimal('1.414')
        
        Unlike other operations, if the length of the coefficient after the quantize
        operation would be greater than precision, then an InvalidOperation is signaled.
        This guarantees that, unless there is an error condition, the quantized exponent
        is always equal to that of the right-hand operand.
        
        Also unlike other operations, quantize never signals Underflow, even if the
        result is subnormal and inexact.
        
        If the exponent of the second operand is larger than that of the first, then
        rounding may be necessary. In this case, the rounding mode is determined by the
        rounding argument if given, else by the given context argument; if neither
        argument is given, the rounding mode of the current thread's context is used.
        """
        pass

    def radix(self, base): # real signature unknown; restored from __doc__
        """
        Return Decimal(10), the radix (base) in which the Decimal class does
        all its arithmetic. Included for compatibility with the specification.
        """
        pass

    def remainder_near(self, *args, **kwargs): # real signature unknown
        """
        Return the remainder from dividing self by other.  This differs from
        self % other in that the sign of the remainder is chosen so as to minimize
        its absolute value. More precisely, the return value is self - n * other
        where n is the integer nearest to the exact value of self / other, and
        if two integers are equally near then the even one is chosen.
        
        If the result is zero then its sign will be the sign of self.
        """
        pass

    def rotate(self, *args, **kwargs): # real signature unknown
        """
        Return the result of rotating the digits of the first operand by an amount
        specified by the second operand.  The second operand must be an integer in
        the range -precision through precision. The absolute value of the second
        operand gives the number of places to rotate. If the second operand is
        positive then rotation is to the left; otherwise rotation is to the right.
        The coefficient of the first operand is padded on the left with zeros to
        length precision if necessary. The sign and exponent of the first operand are
        unchanged.
        """
        pass

    def same_quantum(self, *args, **kwargs): # real signature unknown
        """
        Test whether self and other have the same exponent or whether both are NaN.
        
        This operation is unaffected by context and is quiet: no flags are changed
        and no rounding is performed. As an exception, the C version may raise
        InvalidOperation if the second operand cannot be converted exactly.
        """
        pass

    def scaleb(self, *args, **kwargs): # real signature unknown
        """
        Return the first operand with the exponent adjusted the second.  Equivalently,
        return the first operand multiplied by 10**other. The second operand must be
        an integer.
        """
        pass

    def shift(self, *args, **kwargs): # real signature unknown
        """
        Return the result of shifting the digits of the first operand by an amount
        specified by the second operand.  The second operand must be an integer in
        the range -precision through precision. The absolute value of the second
        operand gives the number of places to shift. If the second operand is
        positive, then the shift is to the left; otherwise the shift is to the
        right. Digits shifted into the coefficient are zeros. The sign and exponent
        of the first operand are unchanged.
        """
        pass

    def sqrt(self, *args, **kwargs): # real signature unknown
        """
        Return the square root of the argument to full precision. The result is
        correctly rounded using the ROUND_HALF_EVEN rounding mode.
        """
        pass

    def to_eng_string(self, *args, **kwargs): # real signature unknown
        """
        Convert to an engineering-type string.  Engineering notation has an exponent
        which is a multiple of 3, so there are up to 3 digits left of the decimal
        place. For example, Decimal('123E+1') is converted to Decimal('1.23E+3').
        
        The value of context.capitals determines whether the exponent sign is lower
        or upper case. Otherwise, the context does not affect the operation.
        """
        pass

    def to_integral(self): # real signature unknown; restored from __doc__
        """
        Identical to the to_integral_value() method.  The to_integral() name has been
        kept for compatibility with older versions.
        """
        pass

    def to_integral_exact(self, *args, **kwargs): # real signature unknown
        """
        Round to the nearest integer, signaling Inexact or Rounded as appropriate if
        rounding occurs.  The rounding mode is determined by the rounding parameter
        if given, else by the given context. If neither parameter is given, then the
        rounding mode of the current default context is used.
        """
        pass

    def to_integral_value(self, *args, **kwargs): # real signature unknown
        """
        Round to the nearest integer without signaling Inexact or Rounded.  The
        rounding mode is determined by the rounding parameter if given, else by
        the given context. If neither parameter is given, then the rounding mode
        of the current default context is used.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        pass

    def __complex__(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        pass

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class InvalidApply(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class LooseVersion(__distutils_version.Version):
    """
    Version numbering for anarchists and software realists.
        Implements the standard interface for version number classes as
        described above.  A version number consists of a series of numbers,
        separated by either periods or strings of letters.  When comparing
        version numbers, the numeric components will be compared
        numerically, and the alphabetic components lexically.  The following
        are all valid version numbers, in no particular order:
    
            1.5.1
            1.5.2b2
            161
            3.10a
            8.02
            3.4j
            1996.07.12
            3.2.pl0
            3.1.1.6
            2g6
            11g
            0.960923
            2.2beta29
            1.13++
            5.5.kw
            2.0b1pl0
    
        In fact, there is no such thing as an invalid version number under
        this scheme; the rules for comparison are simple and predictable,
        but may not always give the results you want (for some definition
        of "want").
    """
    def parse(self, vstring): # reliably restored by inspect
        # no doc
        pass

    def _cmp(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, vstring=None): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    component_re = None # (!) real value is ''


class pydate(object):
    """ date(year, month, day) --> date object """
    def ctime(self): # real signature unknown; restored from __doc__
        """ Return ctime() style string. """
        pass

    @classmethod
    def fromordinal(cls, *args, **kwargs): # real signature unknown
        """ int -> date corresponding to a proleptic Gregorian ordinal. """
        pass

    @classmethod
    def fromtimestamp(cls, *args, **kwargs): # real signature unknown
        """ timestamp -> local date from a POSIX timestamp (like time.time()). """
        pass

    def isocalendar(self, *args, **kwargs): # real signature unknown
        """ Return a 3-tuple containing ISO year, week number, and weekday. """
        pass

    def isoformat(self, *args, **kwargs): # real signature unknown
        """ Return string in ISO 8601 format, YYYY-MM-DD. """
        pass

    def isoweekday(self, *args, **kwargs): # real signature unknown
        """
        Return the day of the week represented by the date.
        Monday == 1 ... Sunday == 7
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """ Return date with new specified fields. """
        pass

    def strftime(self): # real signature unknown; restored from __doc__
        """ format -> strftime() style string. """
        pass

    def timetuple(self, *args, **kwargs): # real signature unknown
        """ Return time tuple, compatible with time.localtime(). """
        pass

    @classmethod
    def today(cls, *args, **kwargs): # real signature unknown
        """ Current date or datetime:  same as self.__class__.fromtimestamp(time.time()). """
        pass

    def toordinal(self, *args, **kwargs): # real signature unknown
        """ Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1. """
        pass

    def weekday(self, *args, **kwargs): # real signature unknown
        """
        Return the day of the week represented by the date.
        Monday == 0 ... Sunday == 6
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Formats self with strftime. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ __reduce__() -> (cls, state) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    max = None # (!) real value is ''
    min = None # (!) real value is ''
    resolution = None # (!) real value is ''


class pydatetime(__datetime.date):
    """
    datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
    
    The year, month and day arguments are required. tzinfo may be None, or an
    instance of a tzinfo subclass. The remaining arguments may be ints.
    """
    def astimezone(self, *args, **kwargs): # real signature unknown
        """ tz -> convert to local time in new timezone tz """
        pass

    @classmethod
    def combine(cls, *args, **kwargs): # real signature unknown
        """ date, time -> datetime with same date and time fields """
        pass

    def ctime(self): # real signature unknown; restored from __doc__
        """ Return ctime() style string. """
        pass

    def date(self, *args, **kwargs): # real signature unknown
        """ Return date object with same year, month and day. """
        pass

    def dst(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.dst(self). """
        pass

    @classmethod
    def fromtimestamp(cls, *args, **kwargs): # real signature unknown
        """ timestamp[, tz] -> tz's local time from POSIX timestamp. """
        pass

    def isoformat(self, *args, **kwargs): # real signature unknown
        """
        [sep] -> string in ISO 8601 format, YYYY-MM-DDT[HH[:MM[:SS[.mmm[uuu]]]]][+HH:MM].
        sep is used to separate the year from the time, and defaults to 'T'.
        timespec specifies what components of the time to include (allowed values are 'auto', 'hours', 'minutes', 'seconds', 'milliseconds', and 'microseconds').
        """
        pass

    @classmethod
    def now(cls, *args, **kwargs): # real signature unknown
        """
        Returns new datetime object representing current time local to tz.
        
          tz
            Timezone object.
        
        If no tz is specified, uses local timezone.
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """ Return datetime with new specified fields. """
        pass

    @classmethod
    def strptime(cls): # real signature unknown; restored from __doc__
        """ string, format -> new datetime parsed from a string (like time.strptime()). """
        pass

    def time(self, *args, **kwargs): # real signature unknown
        """ Return time object with same time but with tzinfo=None. """
        pass

    def timestamp(self, *args, **kwargs): # real signature unknown
        """ Return POSIX timestamp as float. """
        pass

    def timetuple(self, *args, **kwargs): # real signature unknown
        """ Return time tuple, compatible with time.localtime(). """
        pass

    def timetz(self, *args, **kwargs): # real signature unknown
        """ Return time object with same time and tzinfo. """
        pass

    def tzname(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.tzname(self). """
        pass

    @classmethod
    def utcfromtimestamp(cls, *args, **kwargs): # real signature unknown
        """ Construct a naive UTC datetime from a POSIX timestamp. """
        pass

    @classmethod
    def utcnow(cls, *args, **kwargs): # real signature unknown
        """ Return a new datetime representing UTC day and time. """
        pass

    def utcoffset(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.utcoffset(self). """
        pass

    def utctimetuple(self, *args, **kwargs): # real signature unknown
        """ Return UTC time tuple, compatible with time.localtime(). """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce_ex__(self, proto): # real signature unknown; restored from __doc__
        """ __reduce_ex__(proto) -> (cls, state) """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ __reduce__() -> (cls, state) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    fold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    microsecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    second = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tzinfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    max = None # (!) real value is ''
    min = None # (!) real value is ''
    resolution = None # (!) real value is ''


class Reducer(object):
    """
    Performs generic reduction operation on a C or Fortran-contiguous ndarray
        while avoiding ndarray construction overhead
    """
    def get_result(self, *args, **kwargs): # real signature unknown
        pass

    def _check_dummy(self, *args, **kwargs): # real signature unknown
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


class Seen(object):
    """
    Class for keeping track of the types of elements
        encountered when trying to perform type conversions.
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

    is_bool = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_float_or_complex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    numeric_ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class SeriesBinGrouper(object):
    """ Performs grouping operation according to bin edges, rather than labels """
    def get_result(self, *args, **kwargs): # real signature unknown
        pass

    def _check_dummy(self, *args, **kwargs): # real signature unknown
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

    arr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bins = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy_arr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ityp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    typ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class SeriesGrouper(object):
    """
    Performs generic grouping operation while avoiding ndarray construction
        overhead
    """
    def get_result(self, *args, **kwargs): # real signature unknown
        pass

    def _check_dummy(self, *args, **kwargs): # real signature unknown
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

    arr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy_arr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ityp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    labels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    typ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Slider(object):
    """ Only handles contiguous data for now """
    def advance(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def set_length(self, *args, **kwargs): # real signature unknown
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


class _PandasNull(object):
    # no doc
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

pandas_null = None # (!) real value is ''

_TYPE_MAP = {
    'M': 'datetime64',
    'S': 'bytes',
    'U': 'string',
    'b': 'boolean',
    'bool': 'boolean',
    'c': 'complex',
    'categorical': 'categorical',
    'category': 'categorical',
    'complex128': 'complex',
    'datetime64[ns]': 'datetime64',
    'f': 'floating',
    'float16': 'floating',
    'float32': 'floating',
    'float64': 'floating',
    'i': 'integer',
    'int16': 'integer',
    'int32': 'integer',
    'int64': 'integer',
    'int8': 'integer',
    'm': 'timedelta64',
    'string': 'bytes',
    'timedelta64[ns]': 'timedelta64',
    'u': 'integer',
    'uint16': 'integer',
    'uint32': 'integer',
    'uint64': 'integer',
    'uint8': 'integer',
    'unicode': 'string',
}

__loader__ = None # (!) real value is ''

__pyx_capi__ = {
    'is_null_datetimelike': None, # (!) real value is ''
    'is_period': None, # (!) real value is ''
}

__spec__ = None # (!) real value is ''

__test__ = {
    'infer_dtype (line 225)': "\n    Effeciently infer the type of a passed val, or list-like\n    array of values. Return a string describing the type.\n\n    Parameters\n    ----------\n    value : scalar, list, ndarray, or pandas type\n\n    Returns\n    -------\n    string describing the common type of the input data.\n    Results can include:\n\n    - string\n    - unicode\n    - bytes\n    - floating\n    - integer\n    - mixed-integer\n    - mixed-integer-float\n    - complex\n    - categorical\n    - boolean\n    - datetime64\n    - datetime\n    - date\n    - timedelta64\n    - timedelta\n    - time\n    - period\n    - mixed\n\n    Raises\n    ------\n    TypeError if ndarray-like but cannot infer the dtype\n\n    Notes\n    -----\n    - 'mixed' is the catchall for anything that is not otherwise\n      specialized\n    - 'mixed-integer-float' are floats and integers\n    - 'mixed-integer' are integers mixed with non-integers\n\n    Examples\n    --------\n    >>> infer_dtype(['foo', 'bar'])\n    'string'\n\n    >>> infer_dtype([b'foo', b'bar'])\n    'bytes'\n\n    >>> infer_dtype([1, 2, 3])\n    'integer'\n\n    >>> infer_dtype([1, 2, 3.5])\n    'mixed-integer-float'\n\n    >>> infer_dtype([1.0, 2.0, 3.5])\n    'floating'\n\n    >>> infer_dtype(['a', 1])\n    'mixed-integer'\n\n    >>> infer_dtype([True, False])\n    'boolean'\n\n    >>> infer_dtype([True, False, np.nan])\n    'mixed'\n\n    >>> infer_dtype([pd.Timestamp('20130101')])\n    'datetime'\n\n    >>> infer_dtype([datetime.date(2013, 1, 1)])\n    'date'\n\n    >>> infer_dtype([np.datetime64('2013-01-01')])\n    'datetime64'\n\n    >>> infer_dtype([datetime.timedelta(0, 1, 1)])\n    'timedelta'\n\n    >>> infer_dtype(pd.Series(list('aabc')).astype('category'))\n    'categorical'\n\n    ",
    'item_from_zerodim (line 268)': "\n    If the value is a zerodim array, return the item it contains.\n\n    Examples\n    --------\n    >>> item_from_zerodim(1)\n    1\n    >>> item_from_zerodim('foobar')\n    'foobar'\n    >>> item_from_zerodim(np.array(1))\n    1\n    >>> item_from_zerodim(np.array([1]))\n    array([1])\n\n    ",
}

