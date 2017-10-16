# encoding: utf-8
# module pandas._libs.parsers
# from D:\ProgramData\Anaconda3\lib\site-packages\pandas\_libs\parsers.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # D:\ProgramData\Anaconda3\lib\warnings.py
import numpy as np # D:\ProgramData\Anaconda3\lib\site-packages\numpy\__init__.py
import pandas._libs.lib as lib # D:\ProgramData\Anaconda3\lib\site-packages\pandas\_libs\lib.cp36-win_amd64.pyd
import pandas.compat as compat # D:\ProgramData\Anaconda3\lib\site-packages\pandas\compat\__init__.py
import time as time # <module 'time' (built-in)>
import os as os # D:\ProgramData\Anaconda3\lib\os.py
import sys as sys # <module 'sys' (built-in)>
import numpy as __numpy
import pandas.core.base as __pandas_core_base
import pandas.core.dtypes.dtypes as __pandas_core_dtypes_dtypes
import pandas.core.strings as __pandas_core_strings


# Variables with simple values

DEFAULT_CHUNKSIZE = 262144

QUOTE_MINIMAL = 0
QUOTE_NONE = 3
QUOTE_NONNUMERIC = 2

# functions

def is_bool_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check whether the provided array or dtype is of a boolean dtype.
    
        Parameters
        ----------
        arr_or_dtype : array-like
            The array or dtype to check.
    
        Returns
        -------
        boolean : Whether or not the array or dtype is of a boolean dtype.
    
        Examples
        --------
        >>> is_bool_dtype(str)
        False
        >>> is_bool_dtype(int)
        False
        >>> is_bool_dtype(bool)
        True
        >>> is_bool_dtype(np.bool)
        True
        >>> is_bool_dtype(np.array(['a', 'b']))
        False
        >>> is_bool_dtype(pd.Series([1, 2]))
        False
        >>> is_bool_dtype(np.array([True, False]))
        True
    """
    pass

def is_categorical_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check whether an array-like or dtype is of the Categorical dtype.
    
        Parameters
        ----------
        arr_or_dtype : array-like
            The array-like or dtype to check.
    
        Returns
        -------
        boolean : Whether or not the array-like or dtype is
                  of the Categorical dtype.
    
        Examples
        --------
        >>> is_categorical_dtype(object)
        False
        >>> is_categorical_dtype(CategoricalDtype())
        True
        >>> is_categorical_dtype([1, 2, 3])
        False
        >>> is_categorical_dtype(pd.Categorical([1, 2, 3]))
        True
        >>> is_categorical_dtype(pd.CategoricalIndex([1, 2, 3]))
        True
    """
    pass

def is_datetime64_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check whether an array-like or dtype is of the datetime64 dtype.
    
        Parameters
        ----------
        arr_or_dtype : array-like
            The array-like or dtype to check.
    
        Returns
        -------
        boolean : Whether or not the array-like or dtype is of
                  the datetime64 dtype.
    
        Examples
        --------
        >>> is_datetime64_dtype(object)
        False
        >>> is_datetime64_dtype(np.datetime64)
        True
        >>> is_datetime64_dtype(np.array([], dtype=int))
        False
        >>> is_datetime64_dtype(np.array([], dtype=np.datetime64))
        True
        >>> is_datetime64_dtype([1, 2, 3])
        False
    """
    pass

def is_float_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check whether the provided array or dtype is of a float dtype.
    
        Parameters
        ----------
        arr_or_dtype : array-like
            The array or dtype to check.
    
        Returns
        -------
        boolean : Whether or not the array or dtype is of a float dtype.
    
        Examples
        --------
        >>> is_float_dtype(str)
        False
        >>> is_float_dtype(int)
        False
        >>> is_float_dtype(float)
        True
        >>> is_float_dtype(np.array(['a', 'b']))
        False
        >>> is_float_dtype(pd.Series([1, 2]))
        False
        >>> is_float_dtype(pd.Index([1, 2.]))
        True
    """
    pass

def is_integer_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check whether the provided array or dtype is of an integer dtype.
    
        Unlike in `in_any_int_dtype`, timedelta64 instances will return False.
    
        Parameters
        ----------
        arr_or_dtype : array-like
            The array or dtype to check.
    
        Returns
        -------
        boolean : Whether or not the array or dtype is of an integer dtype
                  and not an instance of timedelta64.
    
        Examples
        --------
        >>> is_integer_dtype(str)
        False
        >>> is_integer_dtype(int)
        True
        >>> is_integer_dtype(float)
        False
        >>> is_integer_dtype(np.uint64)
        True
        >>> is_integer_dtype(np.datetime64)
        False
        >>> is_integer_dtype(np.timedelta64)
        False
        >>> is_integer_dtype(np.array(['a', 'b']))
        False
        >>> is_integer_dtype(pd.Series([1, 2]))
        True
        >>> is_integer_dtype(np.array([], dtype=np.timedelta64))
        False
        >>> is_integer_dtype(pd.Index([1, 2.]))  # float
        False
    """
    pass

def is_object_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check whether an array-like or dtype is of the object dtype.
    
        Parameters
        ----------
        arr_or_dtype : array-like
            The array-like or dtype to check.
    
        Returns
        -------
        boolean : Whether or not the array-like or dtype is of the object dtype.
    
        Examples
        --------
        >>> is_object_dtype(object)
        True
        >>> is_object_dtype(int)
        False
        >>> is_object_dtype(np.array([], dtype=object))
        True
        >>> is_object_dtype(np.array([], dtype=int))
        False
        >>> is_object_dtype([1, 2, 3])
        False
    """
    pass

def is_string_dtype(arr_or_dtype): # reliably restored by inspect
    """
    Check whether the provided array or dtype is of the string dtype.
    
        Parameters
        ----------
        arr_or_dtype : array-like
            The array or dtype to check.
    
        Returns
        -------
        boolean : Whether or not the array or dtype is of the string dtype.
    
        Examples
        --------
        >>> is_string_dtype(str)
        True
        >>> is_string_dtype(object)
        True
        >>> is_string_dtype(int)
        False
        >>>
        >>> is_string_dtype(np.array(['a', 'b']))
        True
        >>> is_string_dtype(pd.Series([1, 2]))
        False
    """
    pass

def pandas_dtype(dtype): # reliably restored by inspect
    """
    Converts input into a pandas only dtype object or a numpy dtype object.
    
        Parameters
        ----------
        dtype : object to be converted
    
        Returns
        -------
        np.dtype or a pandas dtype
    """
    pass

def take_1d(arr, indexer, axis=0, out=None, fill_value=nan, mask_info=None, allow_fill=True): # reliably restored by inspect
    """
    Specialized Cython take which sets NaN values in one pass
    
        Parameters
        ----------
        arr : ndarray
            Input array
        indexer : ndarray
            1-D array of indices to take, subarrays corresponding to -1 value
            indicies are filed with fill_value
        axis : int, default 0
            Axis to take from
        out : ndarray or None, default None
            Optional output array, must be appropriate type to hold input and
            fill_value together, if indexer has any -1 value entries; call
            _maybe_promote to determine this type for any fill_value
        fill_value : any, default np.nan
            Fill value to replace -1 values with
        mask_info : tuple of (ndarray, boolean)
            If provided, value should correspond to:
                (indexer != -1, (indexer != -1).any())
            If not provided, it will be computed internally if necessary
        allow_fill : boolean, default True
            If False, indexer is assumed to contain no -1 values so no filling
            will be done.  This short-circuits computation of a mask.  Result is
            undefined if allow_fill == False and -1 is present in indexer.
    """
    pass

def union_categoricals(to_union, sort_categories=False, ignore_order=False): # reliably restored by inspect
    """
    Combine list-like of Categorical-like, unioning categories. All
        categories must have the same dtype.
    
        .. versionadded:: 0.19.0
    
        Parameters
        ----------
        to_union : list-like of Categorical, CategoricalIndex,
                   or Series with dtype='category'
        sort_categories : boolean, default False
            If true, resulting categories will be lexsorted, otherwise
            they will be ordered as they appear in the data.
        ignore_order: boolean, default False
            If true, the ordered attribute of the Categoricals will be ignored.
            Results in an unordered categorical.
    
            .. versionadded:: 0.20.0
    
        Returns
        -------
        result : Categorical
    
        Raises
        ------
        TypeError
            - all inputs do not have the same dtype
            - all inputs do not have the same ordered property
            - all inputs are ordered and their categories are not identical
            - sort_categories=True and Categoricals are ordered
        ValueError
            Empty list of categoricals passed
    """
    pass

def _compute_na_values(*args, **kwargs): # real signature unknown
    pass

def _concatenate_chunks(*args, **kwargs): # real signature unknown
    pass

def _ensure_encoded(*args, **kwargs): # real signature unknown
    pass

def _is_file_like(*args, **kwargs): # real signature unknown
    pass

def _maybe_encode(*args, **kwargs): # real signature unknown
    pass

def _maybe_upcast(*args, **kwargs): # real signature unknown
    """  """
    pass

def _to_structured_array(*args, **kwargs): # real signature unknown
    pass

# classes

class basestring(object):
    """
    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str
    
    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.
    """
    def capitalize(self): # real signature unknown; restored from __doc__
        """
        S.capitalize() -> str
        
        Return a capitalized version of S, i.e. make the first character
        have upper case and the rest lower case.
        """
        return ""

    def casefold(self): # real signature unknown; restored from __doc__
        """
        S.casefold() -> str
        
        Return a version of S suitable for caseless comparisons.
        """
        return ""

    def center(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        S.center(width[, fillchar]) -> str
        
        Return S centered in a string of length width. Padding is
        done using the specified fill character (default is a space)
        """
        return ""

    def count(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.count(sub[, start[, end]]) -> int
        
        Return the number of non-overlapping occurrences of substring sub in
        string S[start:end].  Optional arguments start and end are
        interpreted as in slice notation.
        """
        return 0

    def encode(self, encoding='utf-8', errors='strict'): # real signature unknown; restored from __doc__
        """
        S.encode(encoding='utf-8', errors='strict') -> bytes
        
        Encode S using the codec registered for encoding. Default encoding
        is 'utf-8'. errors may be given to set a different error
        handling scheme. Default is 'strict' meaning that encoding errors raise
        a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
        'xmlcharrefreplace' as well as any other name registered with
        codecs.register_error that can handle UnicodeEncodeErrors.
        """
        return b""

    def endswith(self, suffix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.endswith(suffix[, start[, end]]) -> bool
        
        Return True if S ends with the specified suffix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        suffix can also be a tuple of strings to try.
        """
        return False

    def expandtabs(self, tabsize=8): # real signature unknown; restored from __doc__
        """
        S.expandtabs(tabsize=8) -> str
        
        Return a copy of S where all tab characters are expanded using spaces.
        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        return ""

    def find(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.find(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def format(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        S.format(*args, **kwargs) -> str
        
        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""

    def format_map(self, mapping): # real signature unknown; restored from __doc__
        """
        S.format_map(mapping) -> str
        
        Return a formatted version of S, using substitutions from mapping.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""

    def index(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.index(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found, 
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
        """
        return 0

    def isalnum(self): # real signature unknown; restored from __doc__
        """
        S.isalnum() -> bool
        
        Return True if all characters in S are alphanumeric
        and there is at least one character in S, False otherwise.
        """
        return False

    def isalpha(self): # real signature unknown; restored from __doc__
        """
        S.isalpha() -> bool
        
        Return True if all characters in S are alphabetic
        and there is at least one character in S, False otherwise.
        """
        return False

    def isdecimal(self): # real signature unknown; restored from __doc__
        """
        S.isdecimal() -> bool
        
        Return True if there are only decimal characters in S,
        False otherwise.
        """
        return False

    def isdigit(self): # real signature unknown; restored from __doc__
        """
        S.isdigit() -> bool
        
        Return True if all characters in S are digits
        and there is at least one character in S, False otherwise.
        """
        return False

    def isidentifier(self): # real signature unknown; restored from __doc__
        """
        S.isidentifier() -> bool
        
        Return True if S is a valid identifier according
        to the language definition.
        
        Use keyword.iskeyword() to test for reserved identifiers
        such as "def" and "class".
        """
        return False

    def islower(self): # real signature unknown; restored from __doc__
        """
        S.islower() -> bool
        
        Return True if all cased characters in S are lowercase and there is
        at least one cased character in S, False otherwise.
        """
        return False

    def isnumeric(self): # real signature unknown; restored from __doc__
        """
        S.isnumeric() -> bool
        
        Return True if there are only numeric characters in S,
        False otherwise.
        """
        return False

    def isprintable(self): # real signature unknown; restored from __doc__
        """
        S.isprintable() -> bool
        
        Return True if all characters in S are considered
        printable in repr() or S is empty, False otherwise.
        """
        return False

    def isspace(self): # real signature unknown; restored from __doc__
        """
        S.isspace() -> bool
        
        Return True if all characters in S are whitespace
        and there is at least one character in S, False otherwise.
        """
        return False

    def istitle(self): # real signature unknown; restored from __doc__
        """
        S.istitle() -> bool
        
        Return True if S is a titlecased string and there is at least one
        character in S, i.e. upper- and titlecase characters may only
        follow uncased characters and lowercase characters only cased ones.
        Return False otherwise.
        """
        return False

    def isupper(self): # real signature unknown; restored from __doc__
        """
        S.isupper() -> bool
        
        Return True if all cased characters in S are uppercase and there is
        at least one cased character in S, False otherwise.
        """
        return False

    def join(self, iterable): # real signature unknown; restored from __doc__
        """
        S.join(iterable) -> str
        
        Return a string which is the concatenation of the strings in the
        iterable.  The separator between elements is S.
        """
        return ""

    def ljust(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        S.ljust(width[, fillchar]) -> str
        
        Return S left-justified in a Unicode string of length width. Padding is
        done using the specified fill character (default is a space).
        """
        return ""

    def lower(self): # real signature unknown; restored from __doc__
        """
        S.lower() -> str
        
        Return a copy of the string S converted to lowercase.
        """
        return ""

    def lstrip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.lstrip([chars]) -> str
        
        Return a copy of the string S with leading whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        """
        return ""

    def maketrans(self, *args, **kwargs): # real signature unknown
        """
        Return a translation table usable for str.translate().
        
        If there is only one argument, it must be a dictionary mapping Unicode
        ordinals (integers) or characters to Unicode ordinals, strings or None.
        Character keys will be then converted to ordinals.
        If there are two arguments, they must be strings of equal length, and
        in the resulting dictionary, each character in x will be mapped to the
        character at the same position in y. If there is a third argument, it
        must be a string, whose characters will be mapped to None in the result.
        """
        pass

    def partition(self, sep): # real signature unknown; restored from __doc__
        """
        S.partition(sep) -> (head, sep, tail)
        
        Search for the separator sep in S, and return the part before it,
        the separator itself, and the part after it.  If the separator is not
        found, return S and two empty strings.
        """
        pass

    def replace(self, old, new, count=None): # real signature unknown; restored from __doc__
        """
        S.replace(old, new[, count]) -> str
        
        Return a copy of S with all occurrences of substring
        old replaced by new.  If the optional argument count is
        given, only the first count occurrences are replaced.
        """
        return ""

    def rfind(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rfind(sub[, start[, end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def rindex(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rindex(sub[, start[, end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
        """
        return 0

    def rjust(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        S.rjust(width[, fillchar]) -> str
        
        Return S right-justified in a string of length width. Padding is
        done using the specified fill character (default is a space).
        """
        return ""

    def rpartition(self, sep): # real signature unknown; restored from __doc__
        """
        S.rpartition(sep) -> (head, sep, tail)
        
        Search for the separator sep in S, starting at the end of S, and return
        the part before it, the separator itself, and the part after it.  If the
        separator is not found, return two empty strings and S.
        """
        pass

    def rsplit(self, sep=None, maxsplit=-1): # real signature unknown; restored from __doc__
        """
        S.rsplit(sep=None, maxsplit=-1) -> list of strings
        
        Return a list of the words in S, using sep as the
        delimiter string, starting at the end of the string and
        working to the front.  If maxsplit is given, at most maxsplit
        splits are done. If sep is not specified, any whitespace string
        is a separator.
        """
        return []

    def rstrip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.rstrip([chars]) -> str
        
        Return a copy of the string S with trailing whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        """
        return ""

    def split(self, sep=None, maxsplit=-1): # real signature unknown; restored from __doc__
        """
        S.split(sep=None, maxsplit=-1) -> list of strings
        
        Return a list of the words in S, using sep as the
        delimiter string.  If maxsplit is given, at most maxsplit
        splits are done. If sep is not specified or is None, any
        whitespace string is a separator and empty strings are
        removed from the result.
        """
        return []

    def splitlines(self, keepends=None): # real signature unknown; restored from __doc__
        """
        S.splitlines([keepends]) -> list of strings
        
        Return a list of the lines in S, breaking at line boundaries.
        Line breaks are not included in the resulting list unless keepends
        is given and true.
        """
        return []

    def startswith(self, prefix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.startswith(prefix[, start[, end]]) -> bool
        
        Return True if S starts with the specified prefix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        prefix can also be a tuple of strings to try.
        """
        return False

    def strip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.strip([chars]) -> str
        
        Return a copy of the string S with leading and trailing
        whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        """
        return ""

    def swapcase(self): # real signature unknown; restored from __doc__
        """
        S.swapcase() -> str
        
        Return a copy of S with uppercase characters converted to lowercase
        and vice versa.
        """
        return ""

    def title(self): # real signature unknown; restored from __doc__
        """
        S.title() -> str
        
        Return a titlecased version of S, i.e. words start with title case
        characters, all remaining cased characters have lower case.
        """
        return ""

    def translate(self, table): # real signature unknown; restored from __doc__
        """
        S.translate(table) -> str
        
        Return a copy of the string S in which each character has been mapped
        through the given translation table. The table must implement
        lookup/indexing via __getitem__, for instance a dictionary or list,
        mapping Unicode ordinals to Unicode ordinals, strings, or None. If
        this operation raises LookupError, the character is left untouched.
        Characters mapped to None are deleted.
        """
        return ""

    def upper(self): # real signature unknown; restored from __doc__
        """
        S.upper() -> str
        
        Return a copy of S converted to uppercase.
        """
        return ""

    def zfill(self, width): # real signature unknown; restored from __doc__
        """
        S.zfill(width) -> str
        
        Pad a numeric string S with zeros on the left, to fill a field
        of the specified width. The string S is never truncated.
        """
        return ""

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, format_spec): # real signature unknown; restored from __doc__
        """
        S.__format__(format_spec) -> str
        
        Return a formatted version of S as described by format_spec.
        """
        return ""

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
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
        """ Return self*value.n """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ S.__sizeof__() -> size of S in memory, in bytes """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class Categorical(__pandas_core_base.PandasObject):
    """
    Represents a categorical variable in classic R / S-plus fashion
    
        `Categoricals` can only take on only a limited, and usually fixed, number
        of possible values (`categories`). In contrast to statistical categorical
        variables, a `Categorical` might have an order, but numerical operations
        (additions, divisions, ...) are not possible.
    
        All values of the `Categorical` are either in `categories` or `np.nan`.
        Assigning values outside of `categories` will raise a `ValueError`. Order
        is defined by the order of the `categories`, not lexical order of the
        values.
    
        Parameters
        ----------
        values : list-like
            The values of the categorical. If categories are given, values not in
            categories will be replaced with NaN.
        categories : Index-like (unique), optional
            The unique categories for this categorical. If not given, the
            categories are assumed to be the unique values of values.
        ordered : boolean, (default False)
            Whether or not this categorical is treated as a ordered categorical.
            If not given, the resulting categorical will not be ordered.
    
        Attributes
        ----------
        categories : Index
            The categories of this categorical
        codes : ndarray
            The codes (integer positions, which point to the categories) of this
            categorical, read only.
        ordered : boolean
            Whether or not this Categorical is ordered.
    
        Raises
        ------
        ValueError
            If the categories do not validate.
        TypeError
            If an explicit ``ordered=True`` is given but no `categories` and the
            `values` are not sortable.
    
    
        Examples
        --------
        >>> from pandas import Categorical
        >>> Categorical([1, 2, 3, 1, 2, 3])
        [1, 2, 3, 1, 2, 3]
        Categories (3, int64): [1 < 2 < 3]
    
        >>> Categorical(['a', 'b', 'c', 'a', 'b', 'c'])
        [a, b, c, a, b, c]
        Categories (3, object): [a < b < c]
    
        >>> a = Categorical(['a','b','c','a','b','c'], ['c', 'b', 'a'],
                            ordered=True)
        >>> a.min()
        'c'
    """
    def add_categories(self, new_categories, inplace=False): # reliably restored by inspect
        """
        Add new categories.
        
                `new_categories` will be included at the last/highest place in the
                categories and will be unused directly after this call.
        
                Raises
                ------
                ValueError
                    If the new categories include old categories or do not validate as
                    categories
        
                Parameters
                ----------
                new_categories : category or list-like of category
                   The new categories to be included.
                inplace : boolean (default: False)
                   Whether or not to add the categories inplace or return a copy of
                   this categorical with added categories.
        
                Returns
                -------
                cat : Categorical with new categories added or None if inplace.
        
                See also
                --------
                rename_categories
                reorder_categories
                remove_categories
                remove_unused_categories
                set_categories
        """
        pass

    def argsort(self, ascending=True, kind=None, *args, **kwargs): # reliably restored by inspect
        """
        Returns the indices that would sort the Categorical instance if
                'sort_values' was called. This function is implemented to provide
                compatibility with numpy ndarray objects.
        
                While an ordering is applied to the category values, arg-sorting
                in this context refers more to organizing and grouping together
                based on matching category values. Thus, this function can be
                called on an unordered Categorical instance unlike the functions
                'Categorical.min' and 'Categorical.max'.
        
                Returns
                -------
                argsorted : numpy array
        
                See also
                --------
                numpy.ndarray.argsort
        """
        pass

    def astype(self, dtype, copy=True): # reliably restored by inspect
        """
        Coerce this type to another dtype
        
                Parameters
                ----------
                dtype : numpy dtype or pandas type
                copy : bool, default True
                    By default, astype always returns a newly allocated object.
                    If copy is set to False and dtype is categorical, the original
                    object is returned.
        
                    .. versionadded:: 0.19.0
        """
        pass

    def as_ordered(self, inplace=False): # reliably restored by inspect
        """
        Sets the Categorical to be ordered
        
                Parameters
                ----------
                inplace : boolean (default: False)
                   Whether or not to set the ordered attribute inplace or return a copy
                   of this categorical with ordered set to True
        """
        pass

    def as_unordered(self, inplace=False): # reliably restored by inspect
        """
        Sets the Categorical to be unordered
        
                Parameters
                ----------
                inplace : boolean (default: False)
                   Whether or not to set the ordered attribute inplace or return a copy
                   of this categorical with ordered set to False
        """
        pass

    def check_for_ordered(self, op): # reliably restored by inspect
        """ assert that we are ordered """
        pass

    def copy(self): # reliably restored by inspect
        """ Copy constructor. """
        pass

    def describe(self): # reliably restored by inspect
        """
        Describes this Categorical
        
                Returns
                -------
                description: `DataFrame`
                    A dataframe with frequency and counts by category.
        """
        pass

    def dropna(self): # reliably restored by inspect
        """
        Return the Categorical without null values.
        
                Both missing values (-1 in .codes) and NA as a category are detected.
                NA is removed from the categories if present.
        
                Returns
                -------
                valid : Categorical
        """
        pass

    def equals(self, other): # reliably restored by inspect
        """
        Returns True if categorical arrays are equal.
        
                Parameters
                ----------
                other : `Categorical`
        
                Returns
                -------
                are_equal : boolean
        """
        pass

    def fillna(*args, **kwargs): # reliably restored by inspect
        """
        Fill NA/NaN values using the specified method.
        
                Parameters
                ----------
                method : {'backfill', 'bfill', 'pad', 'ffill', None}, default None
                    Method to use for filling holes in reindexed Series
                    pad / ffill: propagate last valid observation forward to next valid
                    backfill / bfill: use NEXT valid observation to fill gap
                value : scalar
                    Value to use to fill holes (e.g. 0)
                limit : int, default None
                    (Not implemented yet for Categorical!)
                    If method is specified, this is the maximum number of consecutive
                    NaN values to forward/backward fill. In other words, if there is
                    a gap with more than this number of consecutive NaNs, it will only
                    be partially filled. If method is not specified, this is the
                    maximum number of entries along the entire axis where NaNs will be
                    filled.
        
                Returns
                -------
                filled : Categorical with NA/NaN filled
        """
        pass

    @classmethod
    def from_array(cls, *args, **kwargs): # real signature unknown
        """
        DEPRECATED: Use ``Categorical`` instead.
        
                Make a Categorical type from a single array-like object.
        
                For internal compatibility with numpy arrays.
        
                Parameters
                ----------
                data : array-like
                    Can be an Index or array-like. The categories are assumed to be
                    the unique values of `data`.
        """
        pass

    @classmethod
    def from_codes(cls, *args, **kwargs): # real signature unknown
        """
        Make a Categorical type from codes and categories arrays.
        
                This constructor is useful if you already have codes and categories and
                so do not need the (computation intensive) factorization step, which is
                usually done on the constructor.
        
                If your data does not follow this convention, please use the normal
                constructor.
        
                Parameters
                ----------
                codes : array-like, integers
                    An integer array, where each integer points to a category in
                    categories or -1 for NaN
                categories : index-like
                    The categories for the categorical. Items need to be unique.
                ordered : boolean, (default False)
                    Whether or not this categorical is treated as a ordered
                    categorical. If not given, the resulting categorical will be
                    unordered.
        """
        pass

    def get_values(self): # reliably restored by inspect
        """
        Return the values.
        
                For internal compatibility with pandas formatting.
        
                Returns
                -------
                values : numpy array
                    A numpy array of the same dtype as categorical.categories.dtype or
                    Index if datetime / periods
        """
        pass

    def isnull(self): # reliably restored by inspect
        """
        Detect missing values
        
                Both missing values (-1 in .codes) and NA as a category are detected.
        
                Returns
                -------
                a boolean array of whether my values are null
        
                See also
                --------
                isnull : pandas version
                Categorical.notnull : boolean inverse of Categorical.isnull
        """
        pass

    def is_dtype_equal(self, other): # reliably restored by inspect
        """
        Returns True if categoricals are the same dtype
                  same categories, and same ordered
        
                Parameters
                ----------
                other : Categorical
        
                Returns
                -------
                are_equal : boolean
        """
        pass

    def map(self, mapper): # reliably restored by inspect
        """
        Apply mapper function to its categories (not codes).
        
                Parameters
                ----------
                mapper : callable
                    Function to be applied. When all categories are mapped
                    to different categories, the result will be Categorical which has
                    the same order property as the original. Otherwise, the result will
                    be np.ndarray.
        
                Returns
                -------
                applied : Categorical or Index.
        """
        pass

    def max(self, numeric_only=None, **kwargs): # reliably restored by inspect
        """
        The maximum value of the object.
        
                Only ordered `Categoricals` have a maximum!
        
                Raises
                ------
                TypeError
                    If the `Categorical` is not `ordered`.
        
                Returns
                -------
                max : the maximum of this `Categorical`
        """
        pass

    def memory_usage(self, deep=False): # reliably restored by inspect
        """
        Memory usage of my values
        
                Parameters
                ----------
                deep : bool
                    Introspect the data deeply, interrogate
                    `object` dtypes for system-level memory consumption
        
                Returns
                -------
                bytes used
        
                Notes
                -----
                Memory usage does not include memory consumed by elements that
                are not components of the array if deep=False
        
                See Also
                --------
                numpy.ndarray.nbytes
        """
        pass

    def min(self, numeric_only=None, **kwargs): # reliably restored by inspect
        """
        The minimum value of the object.
        
                Only ordered `Categoricals` have a minimum!
        
                Raises
                ------
                TypeError
                    If the `Categorical` is not `ordered`.
        
                Returns
                -------
                min : the minimum of this `Categorical`
        """
        pass

    def mode(self): # reliably restored by inspect
        """
        Returns the mode(s) of the Categorical.
        
                Always returns `Categorical` even if only one value.
        
                Returns
                -------
                modes : `Categorical` (sorted)
        """
        pass

    def notnull(self): # reliably restored by inspect
        """
        Reverse of isnull
        
                Both missing values (-1 in .codes) and NA as a category are detected as
                null.
        
                Returns
                -------
                a boolean array of whether my values are not null
        
                See also
                --------
                notnull : pandas version
                Categorical.isnull : boolean inverse of Categorical.notnull
        """
        pass

    def order(self, inplace=False, ascending=True, na_position=None): # reliably restored by inspect
        """
        DEPRECATED: use :meth:`Categorical.sort_values`. That function
                is entirely equivalent to this one.
        
                See Also
                --------
                Categorical.sort_values
        """
        pass

    def put(self, *args, **kwargs): # reliably restored by inspect
        """ Replace specific elements in the Categorical with given values. """
        pass

    def ravel(self, order=None): # reliably restored by inspect
        """
        Return a flattened (numpy) array.
        
                For internal compatibility with numpy arrays.
        
                Returns
                -------
                raveled : numpy array
        """
        pass

    def remove_categories(self, removals, inplace=False): # reliably restored by inspect
        """
        Removes the specified categories.
        
                `removals` must be included in the old categories. Values which were in
                the removed categories will be set to NaN
        
                Raises
                ------
                ValueError
                    If the removals are not contained in the categories
        
                Parameters
                ----------
                removals : category or list of categories
                   The categories which should be removed.
                inplace : boolean (default: False)
                   Whether or not to remove the categories inplace or return a copy of
                   this categorical with removed categories.
        
                Returns
                -------
                cat : Categorical with removed categories or None if inplace.
        
                See also
                --------
                rename_categories
                reorder_categories
                add_categories
                remove_unused_categories
                set_categories
        """
        pass

    def remove_unused_categories(self, inplace=False): # reliably restored by inspect
        """
        Removes categories which are not used.
        
                Parameters
                ----------
                inplace : boolean (default: False)
                   Whether or not to drop unused categories inplace or return a copy of
                   this categorical with unused categories dropped.
        
                Returns
                -------
                cat : Categorical with unused categories dropped or None if inplace.
        
                See also
                --------
                rename_categories
                reorder_categories
                add_categories
                remove_categories
                set_categories
        """
        pass

    def rename_categories(self, new_categories, inplace=False): # reliably restored by inspect
        """
        Renames categories.
        
                The new categories has to be a list-like object. All items must be
                unique and the number of items in the new categories must be the same
                as the number of items in the old categories.
        
                Raises
                ------
                ValueError
                    If the new categories do not have the same number of items than the
                    current categories or do not validate as categories
        
                Parameters
                ----------
                new_categories : Index-like
                   The renamed categories.
                inplace : boolean (default: False)
                   Whether or not to rename the categories inplace or return a copy of
                   this categorical with renamed categories.
        
                Returns
                -------
                cat : Categorical with renamed categories added or None if inplace.
        
                See also
                --------
                reorder_categories
                add_categories
                remove_categories
                remove_unused_categories
                set_categories
        """
        pass

    def reorder_categories(self, new_categories, ordered=None, inplace=False): # reliably restored by inspect
        """
        Reorders categories as specified in new_categories.
        
                `new_categories` need to include all old categories and no new category
                items.
        
                Raises
                ------
                ValueError
                    If the new categories do not contain all old category items or any
                    new ones
        
                Parameters
                ----------
                new_categories : Index-like
                   The categories in new order.
                ordered : boolean, optional
                   Whether or not the categorical is treated as a ordered categorical.
                   If not given, do not change the ordered information.
                inplace : boolean (default: False)
                   Whether or not to reorder the categories inplace or return a copy of
                   this categorical with reordered categories.
        
                Returns
                -------
                cat : Categorical with reordered categories or None if inplace.
        
                See also
                --------
                rename_categories
                add_categories
                remove_categories
                remove_unused_categories
                set_categories
        """
        pass

    def repeat(self, repeats, *args, **kwargs): # reliably restored by inspect
        """
        Repeat elements of a Categorical.
        
                See also
                --------
                numpy.ndarray.repeat
        """
        pass

    def reshape(self, new_shape, *args, **kwargs): # reliably restored by inspect
        """
        DEPRECATED: calling this method will raise an error in a
                future release.
        
                An ndarray-compatible method that returns `self` because
                `Categorical` instances cannot actually be reshaped.
        
                Parameters
                ----------
                new_shape : int or tuple of ints
                    A 1-D array of integers that correspond to the new
                    shape of the `Categorical`. For more information on
                    the parameter, please refer to `np.reshape`.
        """
        pass

    def searchsorted(*args, **kwargs): # reliably restored by inspect
        """
        Find indices where elements should be inserted to maintain order.
        
                Find the indices into a sorted Categorical `self` such that, if the
                corresponding elements in `value` were inserted before the indices,
                the order of `self` would be preserved.
        
                Parameters
                ----------
                value : array_like
                    Values to insert into `self`.
                side : {'left', 'right'}, optional
                    If 'left', the index of the first suitable location found is given.
                    If 'right', return the last such index.  If there is no suitable
                    index, return either 0 or N (where N is the length of `self`).
                sorter : 1-D array_like, optional
                    Optional array of integer indices that sort `self` into ascending
                    order. They are typically the result of ``np.argsort``.
        
                Returns
                -------
                indices : array of ints
                    Array of insertion points with the same shape as `value`.
        
                See Also
                --------
                numpy.searchsorted
        
                Notes
                -----
                Binary search is used to find the required insertion points.
        
                Examples
                --------
        
                >>> x = pd.Series([1, 2, 3])
                >>> x
                0    1
                1    2
                2    3
                dtype: int64
        
                >>> x.searchsorted(4)
                array([3])
        
                >>> x.searchsorted([0, 4])
                array([0, 3])
        
                >>> x.searchsorted([1, 3], side='left')
                array([0, 2])
        
                >>> x.searchsorted([1, 3], side='right')
                array([1, 3])
        
                >>> x = pd.Categorical(['apple', 'bread', 'bread', 'cheese', 'milk' ])
                [apple, bread, bread, cheese, milk]
                Categories (4, object): [apple < bread < cheese < milk]
        
                >>> x.searchsorted('bread')
                array([1])     # Note: an array, not a scalar
        
                >>> x.searchsorted(['bread'])
                array([1])
        
                >>> x.searchsorted(['bread', 'eggs'])
                array([1, 4])
        
                >>> x.searchsorted(['bread', 'eggs'], side='right')
                array([3, 4])    # eggs before milk
        """
        pass

    def set_categories(self, new_categories, ordered=None, rename=False, inplace=False): # reliably restored by inspect
        """
        Sets the categories to the specified new_categories.
        
                `new_categories` can include new categories (which will result in
                unused categories) or remove old categories (which results in values
                set to NaN). If `rename==True`, the categories will simple be renamed
                (less or more items than in old categories will result in values set to
                NaN or in unused categories respectively).
        
                This method can be used to perform more than one action of adding,
                removing, and reordering simultaneously and is therefore faster than
                performing the individual steps via the more specialised methods.
        
                On the other hand this methods does not do checks (e.g., whether the
                old categories are included in the new categories on a reorder), which
                can result in surprising changes, for example when using special string
                dtypes on python3, which does not considers a S1 string equal to a
                single char python string.
        
                Raises
                ------
                ValueError
                    If new_categories does not validate as categories
        
                Parameters
                ----------
                new_categories : Index-like
                   The categories in new order.
                ordered : boolean, (default: False)
                   Whether or not the categorical is treated as a ordered categorical.
                   If not given, do not change the ordered information.
                rename : boolean (default: False)
                   Whether or not the new_categories should be considered as a rename
                   of the old  categories or as reordered categories.
                inplace : boolean (default: False)
                   Whether or not to reorder the categories inplace or return a copy of
                   this categorical with reordered categories.
        
                Returns
                -------
                cat : Categorical with reordered categories or None if inplace.
        
                See also
                --------
                rename_categories
                reorder_categories
                add_categories
                remove_categories
                remove_unused_categories
        """
        pass

    def set_ordered(self, value, inplace=False): # reliably restored by inspect
        """
        Sets the ordered attribute to the boolean value
        
                Parameters
                ----------
                value : boolean to set whether this categorical is ordered (True) or
                   not (False)
                inplace : boolean (default: False)
                   Whether or not to set the ordered attribute inplace or return a copy
                   of this categorical with ordered set to the value
        """
        pass

    def shift(self, periods): # reliably restored by inspect
        """
        Shift Categorical by desired number of periods.
        
                Parameters
                ----------
                periods : int
                    Number of periods to move, can be positive or negative
        
                Returns
                -------
                shifted : Categorical
        """
        pass

    def sort(self, inplace=True, ascending=True, na_position=None, **kwargs): # reliably restored by inspect
        """
        DEPRECATED: use :meth:`Categorical.sort_values`. That function
                is just like this one, except that a new Categorical is returned
                by default, so make sure to pass in 'inplace=True' to get
                inplace sorting.
        
                See Also
                --------
                Categorical.sort_values
        """
        pass

    def sort_values(self, inplace=False, ascending=True, na_position=None): # reliably restored by inspect
        """
        Sorts the Categorical by category value returning a new
                Categorical by default.
        
                While an ordering is applied to the category values, sorting in this
                context refers more to organizing and grouping together based on
                matching category values. Thus, this function can be called on an
                unordered Categorical instance unlike the functions 'Categorical.min'
                and 'Categorical.max'.
        
                Parameters
                ----------
                inplace : boolean, default False
                    Do operation in place.
                ascending : boolean, default True
                    Order ascending. Passing False orders descending. The
                    ordering parameter provides the method by which the
                    category values are organized.
                na_position : {'first', 'last'} (optional, default='last')
                    'first' puts NaNs at the beginning
                    'last' puts NaNs at the end
        
                Returns
                -------
                y : Categorical or None
        
                See Also
                --------
                Categorical.sort
                Series.sort_values
        
                Examples
                --------
                >>> c = pd.Categorical([1, 2, 2, 1, 5])
                >>> c
                [1, 2, 2, 1, 5]
                Categories (3, int64): [1, 2, 5]
                >>> c.sort_values()
                [1, 1, 2, 2, 5]
                Categories (3, int64): [1, 2, 5]
                >>> c.sort_values(ascending=False)
                [5, 2, 2, 1, 1]
                Categories (3, int64): [1, 2, 5]
        
                Inplace sorting can be done as well:
        
                >>> c.sort_values(inplace=True)
                >>> c
                [1, 1, 2, 2, 5]
                Categories (3, int64): [1, 2, 5]
                >>>
                >>> c = pd.Categorical([1, 2, 2, 1, 5])
        
                'sort_values' behaviour with NaNs. Note that 'na_position'
                is independent of the 'ascending' parameter:
        
                >>> c = pd.Categorical([np.nan, 2, 2, np.nan, 5])
                >>> c
                [NaN, 2.0, 2.0, NaN, 5.0]
                Categories (2, int64): [2, 5]
                >>> c.sort_values()
                [2.0, 2.0, 5.0, NaN, NaN]
                Categories (2, int64): [2, 5]
                >>> c.sort_values(ascending=False)
                [5.0, 2.0, 2.0, NaN, NaN]
                Categories (2, int64): [2, 5]
                >>> c.sort_values(na_position='first')
                [NaN, NaN, 2.0, 2.0, 5.0]
                Categories (2, int64): [2, 5]
                >>> c.sort_values(ascending=False, na_position='first')
                [NaN, NaN, 5.0, 2.0, 2.0]
                Categories (2, int64): [2, 5]
        """
        pass

    def take(self, indexer, allow_fill=True, fill_value=None): # reliably restored by inspect
        """
        Take the codes by the indexer, fill with the fill_value.
        
                For internal compatibility with numpy arrays.
        """
        pass

    def take_nd(self, indexer, allow_fill=True, fill_value=None): # reliably restored by inspect
        """
        Take the codes by the indexer, fill with the fill_value.
        
                For internal compatibility with numpy arrays.
        """
        pass

    def to_dense(self): # reliably restored by inspect
        """
        Return my 'dense' representation
        
                For internal compatibility with numpy arrays.
        
                Returns
                -------
                dense : array
        """
        pass

    def unique(self): # reliably restored by inspect
        """
        Return the ``Categorical`` which ``categories`` and ``codes`` are
                unique. Unused categories are NOT returned.
        
                - unordered category: values and categories are sorted by appearance
                  order.
                - ordered category: values are sorted by appearance order, categories
                  keeps existing order.
        
                Returns
                -------
                unique values : ``Categorical``
        
                Examples
                --------
                An unordered Categorical will return categories in the
                order of appearance.
        
                >>> pd.Categorical(list('baabc'))
                [b, a, c]
                Categories (3, object): [b, a, c]
        
                >>> pd.Categorical(list('baabc'), categories=list('abc'))
                [b, a, c]
                Categories (3, object): [b, a, c]
        
                An ordered Categorical preserves the category ordering.
        
                >>> pd.Categorical(list('baabc'),
                ...                categories=list('abc'),
                ...                ordered=True)
                [b, a, c]
                Categories (3, object): [a < b < c]
        
                See Also
                --------
                unique
                CategoricalIndex.unique
                Series.unique
        """
        pass

    def value_counts(self, dropna=True): # reliably restored by inspect
        """
        Returns a Series containing counts of each category.
        
                Every category will have an entry, even those with a count of 0.
        
                Parameters
                ----------
                dropna : boolean, default True
                    Don't include counts of NaN, even if NaN is a category.
        
                Returns
                -------
                counts : Series
        
                See Also
                --------
                Series.value_counts
        """
        pass

    def view(self): # reliably restored by inspect
        """
        Return a view of myself.
        
                For internal compatibility with numpy arrays.
        
                Returns
                -------
                view : Categorical
                   Returns `self`!
        """
        pass

    def _codes_for_groupby(self, sort): # reliably restored by inspect
        """
        If sort=False, return a copy of self, coded with categories as
                returned by .unique(), followed by any categories not appearing in
                the data. If sort=True, return self.
        
                This method is needed solely to ensure the categorical index of the
                GroupBy result has categories in the order of appearance in the data
                (GH-8868).
        
                Parameters
                ----------
                sort : boolean
                    The value of the sort paramter groupby was called with.
        
                Returns
                -------
                Categorical
                    If sort=False, the new categories are set to the order of
                    appearance in codes (unless ordered=True, in which case the
                    original order is preserved), followed by any unrepresented
                    categories in the original order.
        """
        pass

    def _get_categories(self): # reliably restored by inspect
        """ Gets the categories """
        pass

    def _get_codes(self): # reliably restored by inspect
        """
        Get the codes.
        
                Returns
                -------
                codes : integer array view
                    A non writable view of the `codes` array.
        """
        pass

    def _get_labels(self): # reliably restored by inspect
        """
        Get the category labels (deprecated).
        
                Deprecated, use .codes!
        """
        pass

    def _get_ordered(self): # reliably restored by inspect
        """ Gets the ordered attribute """
        pass

    def _get_repr(self, length=True, na_rep=None, footer=True): # reliably restored by inspect
        # no doc
        pass

    def _maybe_coerce_indexer(self, indexer): # reliably restored by inspect
        """ return an indexer coerced to the codes dtype """
        pass

    def _reduce(self, op, name, axis=0, skipna=True, numeric_only=None, filter_type=None, **kwds): # reliably restored by inspect
        """ perform the reduction type operation """
        pass

    def _repr_categories(self): # reliably restored by inspect
        """ return the base repr for the categories """
        pass

    def _repr_categories_info(self): # reliably restored by inspect
        """ Returns a string representation of the footer. """
        pass

    def _repr_footer(self): # reliably restored by inspect
        # no doc
        pass

    def _reverse_indexer(self): # reliably restored by inspect
        """
        Compute the inverse of a categorical, returning
                a dict of categories -> indexers.
        
                *This is an internal function*
        
                Returns
                -------
                dict of categories -> indexers
        
                Example
                -------
                In [1]: c = pd.Categorical(list('aabca'))
        
                In [2]: c
                Out[2]:
                [a, a, b, c, a]
                Categories (3, object): [a, b, c]
        
                In [3]: c.categories
                Out[3]: Index([u'a', u'b', u'c'], dtype='object')
        
                In [4]: c.codes
                Out[4]: array([0, 0, 1, 2, 0], dtype=int8)
        
                In [5]: c._reverse_indexer()
                Out[5]: {'a': array([0, 1, 4]), 'b': array([2]), 'c': array([3])}
        """
        pass

    def _set_categories(self, categories, fastpath=False): # reliably restored by inspect
        """
        Sets new categories
        
                Parameters
                ----------
                fastpath : boolean (default: False)
                   Don't perform validation of the categories for uniqueness or nulls
        """
        pass

    def _set_codes(self, codes): # reliably restored by inspect
        """ Not settable by the user directly """
        pass

    def _slice(self, slicer): # reliably restored by inspect
        """
        Return a slice of myself.
        
                For internal compatibility with numpy arrays.
        """
        pass

    def _tidy_repr(self, max_vals=10, footer=True): # reliably restored by inspect
        """
        a short repr displaying only max_vals and an optional (but default
                footer)
        """
        pass

    @classmethod
    def _validate_categories(cls, *args, **kwargs): # real signature unknown
        """
        Validates that we have good categories
        
                Parameters
                ----------
                fastpath : boolean (default: False)
                   Don't perform validation of the categories for uniqueness or nulls
        """
        pass

    @classmethod
    def _validate_ordered(cls, *args, **kwargs): # real signature unknown
        """
        Validates that we have a valid ordered parameter. If
                it is not a boolean, a TypeError will be raised.
        
                Parameters
                ----------
                ordered : object
                    The parameter to be verified.
        
                Raises
                ------
                TypeError
                    If 'ordered' is not a boolean.
        """
        pass

    def _values_for_rank(self): # reliably restored by inspect
        """
        For correctly ranking ordered categorical data. See GH#15420
        
                Ordered categorical data should be ranked on the basis of
                codes with -1 translated to NaN.
        
                Returns
                -------
                numpy array
        """
        pass

    def __array__(self, dtype=None): # reliably restored by inspect
        """
        The numpy array interface.
        
                Returns
                -------
                values : numpy array
                    A numpy array of either the specified dtype or,
                    if dtype==None (default), the same dtype as
                    categorical.categories.dtype
        """
        pass

    def __dir__(self): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __getitem__(self, key): # reliably restored by inspect
        """ Return an item. """
        pass

    def __ge__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __gt__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, values, categories=None, ordered=False, fastpath=False): # reliably restored by inspect
        # no doc
        pass

    def __iter__(self): # reliably restored by inspect
        """ Returns an Iterator over the values of this Categorical. """
        pass

    def __len__(self): # reliably restored by inspect
        """ The length of this Categorical. """
        pass

    def __le__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __lt__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __setitem__(self, key, value): # reliably restored by inspect
        """
        Item assignment.
        
        
                Raises
                ------
                ValueError
                    If (one or more) Value is not in categories or if a assigned
                    `Categorical` does not have the same categories
        """
        pass

    def __setstate__(self, state): # reliably restored by inspect
        """ Necessary for making this object picklable """
        pass

    def __unicode__(self): # reliably restored by inspect
        """ Unicode representation. """
        pass

    base = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ compat, we are always our own object """

    categories = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The categories of this categorical.

Setting assigns new values to each category (effectively a rename of
each individual category).

The assigned value has to be a list-like object. All items must be unique and
the number of items in the new categories must be the same as the number of
items in the old categories.

Assigning to `categories` is a inplace operation!

Raises
------
ValueError
    If the new categories do not validate as categories or if the number of new
    categories is unequal the number of old categories

See also
--------
rename_categories
reorder_categories
add_categories
remove_categories
remove_unused_categories
set_categories
"""

    codes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The category codes of this categorical.

Level codes are an array if integer which are the positions of the real
values in the categories array.

There is not setter, use the other categorical methods and the normal item
setter to change values in the categorical.
"""

    labels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get the category labels (deprecated).

        Deprecated, use .codes!
        """

    nbytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ordered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Gets the ordered attribute """

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Shape of the Categorical.

        For internal compatibility with numpy arrays.

        Returns
        -------
        shape : tuple
        """

    T = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _constructor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    dtype = None # (!) real value is ''
    itemsize = None
    ndim = None
    size = None
    _categories = None
    _codes = None
    _ordered = None
    _typ = 'categorical'
    __array_priority__ = 1000
    __hash__ = None


class CategoricalDtype(__pandas_core_dtypes_dtypes.ExtensionDtype):
    """
    A np.dtype duck-typed class, suitable for holding a custom categorical
        dtype.
    
        THIS IS NOT A REAL NUMPY DTYPE, but essentially a sub-class of np.object
    """
    @classmethod
    def construct_from_string(cls, *args, **kwargs): # real signature unknown
        """
        attempt to construct this type from a string, raise a TypeError if
                it's not possible
        """
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __hash__(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls): # reliably restored by inspect
        # no doc
        pass

    base = None # (!) real value is ''
    kind = 'O'
    name = 'category'
    str = '|O08'
    type = None # (!) real value is ''
    _cache = {
        'category': None, # (!) real value is ''
    }
    _metadata = []


class ParserError(ValueError):
    """ Exception that is thrown by an error is encountered in `pd.read_csv` """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



CParserError = ParserError


class DtypeWarning(Warning):
    """
    Warning that is raised for a dtype incompatiblity. This is
        can happen whenever `pd.read_csv` encounters non-
        uniform dtypes in a column(s) of a given CSV file
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class EmptyDataError(ValueError):
    """
    Exception that is thrown in `pd.read_csv` (by both the C and
        Python engines) when empty data or header is encountered
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Index(__pandas_core_base.IndexOpsMixin, __pandas_core_strings.StringAccessorMixin, __pandas_core_base.PandasObject):
    """
    Immutable ndarray implementing an ordered, sliceable set. The basic object
        storing axis labels for all pandas objects
    
        Parameters
        ----------
        data : array-like (1-dimensional)
        dtype : NumPy dtype (default: object)
        copy : bool
            Make a copy of input ndarray
        name : object
            Name to be stored in the index
        tupleize_cols : bool (default: True)
            When True, attempt to create a MultiIndex if possible
    
        Notes
        -----
        An Index instance can **only** contain hashable objects
    """
    def all(self, *args, **kwargs): # reliably restored by inspect
        """
        Return whether all elements are True
        
        Parameters
        ----------
        All arguments to numpy.all are accepted.
        
        Returns
        -------
        all : bool or array_like (if axis is specified)
            A single element array_like may be converted to bool.
        """
        pass

    def any(self, *args, **kwargs): # reliably restored by inspect
        """
        Return whether any element is True
        
        Parameters
        ----------
        All arguments to numpy.any are accepted.
        
        Returns
        -------
        any : bool or array_like (if axis is specified)
            A single element array_like may be converted to bool.
        """
        pass

    def append(self, other): # reliably restored by inspect
        """
        Append a collection of Index options together
        
                Parameters
                ----------
                other : Index or list/tuple of indices
        
                Returns
                -------
                appended : Index
        """
        pass

    def argsort(self, *args, **kwargs): # reliably restored by inspect
        """
        Returns the indices that would sort the index and its
                underlying data.
        
                Returns
                -------
                argsorted : numpy array
        
                See also
                --------
                numpy.ndarray.argsort
        """
        pass

    def asof(self, label): # reliably restored by inspect
        """
        For a sorted index, return the most recent label up to and including
                the passed label. Return NaN if not found.
        
                See also
                --------
                get_loc : asof is a thin wrapper around get_loc with method='pad'
        """
        pass

    def asof_locs(self, where, mask): # reliably restored by inspect
        """
        where : array of timestamps
                mask : array of booleans where data is not NA
        """
        pass

    def astype(self, dtype, copy=True): # reliably restored by inspect
        """
        Create an Index with values cast to dtypes. The class of a new Index
        is determined by dtype. When conversion is impossible, a ValueError
        exception is raised.
        
        Parameters
        ----------
        dtype : numpy dtype or pandas type
        copy : bool, default True
            By default, astype always returns a newly allocated object.
            If copy is set to False and internal requirements on dtype are
            satisfied, the original data is used to create a new Index
            or the original Index is returned.
        
            .. versionadded:: 0.19.0
        """
        pass

    def contains(self, key): # reliably restored by inspect
        """
        return a boolean if this key is IN the index
        
        Parameters
        ----------
        key : object
        
        Returns
        -------
        boolean
        """
        pass

    def copy(self, name=None, deep=False, dtype=None, **kwargs): # reliably restored by inspect
        """
        Make a copy of this object.  Name and dtype sets those attributes on
        the new object.
        
        Parameters
        ----------
        name : string, optional
        deep : boolean, default False
        dtype : numpy dtype or pandas type
        
        Returns
        -------
        copy : Index
        
        Notes
        -----
        In most cases, there should be no functional difference from using
        ``deep``, but if ``deep`` is passed it will attempt to deepcopy.
        """
        pass

    def delete(self, loc): # reliably restored by inspect
        """
        Make new Index with passed location(-s) deleted
        
                Returns
                -------
                new_index : Index
        """
        pass

    def difference(self, other): # reliably restored by inspect
        """
        Return a new Index with elements from the index that are not in
                `other`.
        
                This is the set difference of two Index objects.
                It's sorted if sorting is possible.
        
                Parameters
                ----------
                other : Index or array-like
        
                Returns
                -------
                difference : Index
        
                Examples
                --------
        
                >>> idx1 = pd.Index([1, 2, 3, 4])
                >>> idx2 = pd.Index([3, 4, 5, 6])
                >>> idx1.difference(idx2)
                Int64Index([1, 2], dtype='int64')
        """
        pass

    def drop(self, labels, errors=None): # reliably restored by inspect
        """
        Make new Index with passed list of labels deleted
        
                Parameters
                ----------
                labels : array-like
                errors : {'ignore', 'raise'}, default 'raise'
                    If 'ignore', suppress error and existing labels are dropped.
        
                Returns
                -------
                dropped : Index
        """
        pass

    def dropna(self, how=None): # reliably restored by inspect
        """
        Return Index without NA/NaN values
        
        Parameters
        ----------
        how :  {'any', 'all'}, default 'any'
            If the Index is a MultiIndex, drop the value when any or all levels
            are NaN.
        
        Returns
        -------
        valid : Index
        """
        pass

    def drop_duplicates(self, keep=None): # reliably restored by inspect
        """
        Return Index with duplicate values removed
        
                Parameters
                ----------
        
                keep : {'first', 'last', False}, default 'first'
                    - ``first`` : Drop duplicates except for the first occurrence.
                    - ``last`` : Drop duplicates except for the last occurrence.
                    - False : Drop all duplicates.
        
        
                Returns
                -------
                deduplicated : Index
        """
        pass

    def duplicated(self, keep=None): # reliably restored by inspect
        """
        Return boolean np.ndarray denoting duplicate values
        
                Parameters
                ----------
                keep : {'first', 'last', False}, default 'first'
                    - ``first`` : Mark duplicates as ``True`` except for the first
                      occurrence.
                    - ``last`` : Mark duplicates as ``True`` except for the last
                      occurrence.
                    - False : Mark all duplicates as ``True``.
        
                Returns
                -------
                duplicated : np.ndarray
        """
        pass

    def equals(self, other): # reliably restored by inspect
        """ Determines if two Index objects contain the same elements. """
        pass

    def fillna(self, value=None, downcast=None): # reliably restored by inspect
        """
        Fill NA/NaN values with the specified value
        
        Parameters
        ----------
        value : scalar
            Scalar value to use to fill holes (e.g. 0).
            This value cannot be a list-likes.
        downcast : dict, default is None
            a dict of item->dtype of what to downcast if possible,
            or the string 'infer' which will try to downcast to an appropriate
            equal type (e.g. float64 to int64 if possible)
        
        Returns
        -------
        filled : %(klass)s
        """
        pass

    def format(self, name=False, formatter=None, **kwargs): # reliably restored by inspect
        """ Render a string representation of the Index """
        pass

    def get_duplicates(self): # reliably restored by inspect
        # no doc
        pass

    def get_indexer(self, target, method=None, limit=None, tolerance=None): # reliably restored by inspect
        """
        Compute indexer and mask for new index given the current index. The
        indexer should be then used as an input to ndarray.take to align the
        current data to the new index.
        
        Parameters
        ----------
        target : Index
        method : {None, 'pad'/'ffill', 'backfill'/'bfill', 'nearest'}, optional
            * default: exact matches only.
            * pad / ffill: find the PREVIOUS index value if no exact match.
            * backfill / bfill: use NEXT index value if no exact match
            * nearest: use the NEAREST index value if no exact match. Tied
              distances are broken by preferring the larger index value.
        limit : int, optional
            Maximum number of consecutive labels in ``target`` to match for
            inexact matches.
        tolerance : optional
            Maximum distance between original and new labels for inexact
            matches. The values of the index at the matching locations most
            satisfy the equation ``abs(index[indexer] - target) <= tolerance``.
        
            .. versionadded:: 0.17.0
        
        Examples
        --------
        >>> indexer = index.get_indexer(new_index)
        >>> new_values = cur_values.take(indexer)
        
        Returns
        -------
        indexer : ndarray of int
            Integers from 0 to n - 1 indicating that the index at these
            positions matches the corresponding target values. Missing values
            in the target are marked by -1.
        """
        pass

    def get_indexer_for(self, target, **kwargs): # reliably restored by inspect
        """
        guaranteed return of an indexer even when non-unique
                This dispatches to get_indexer or get_indexer_nonunique as appropriate
        """
        pass

    def get_indexer_non_unique(self, target): # reliably restored by inspect
        """
        Compute indexer and mask for new index given the current index. The
        indexer should be then used as an input to ndarray.take to align the
        current data to the new index.
        
        Parameters
        ----------
        target : Index
        
        Returns
        -------
        indexer : ndarray of int
            Integers from 0 to n - 1 indicating that the index at these
            positions matches the corresponding target values. Missing values
            in the target are marked by -1.
        missing : ndarray of int
            An indexer into the target of the values not found.
            These correspond to the -1 in the indexer array
        """
        pass

    def get_level_values(self, level): # reliably restored by inspect
        """
        Return an Index of values for requested level, equal to the length
                of the index
        
                Parameters
                ----------
                level : int
        
                Returns
                -------
                values : Index
        """
        pass

    def get_loc(self, key, method=None, tolerance=None): # reliably restored by inspect
        """
        Get integer location for requested label.
        
        Parameters
        ----------
        key : label
        method : {None, 'pad'/'ffill', 'backfill'/'bfill', 'nearest'}, optional
            * default: exact matches only.
            * pad / ffill: find the PREVIOUS index value if no exact match.
            * backfill / bfill: use NEXT index value if no exact match
            * nearest: use the NEAREST index value if no exact match. Tied
              distances are broken by preferring the larger index value.
        tolerance : optional
            Maximum distance from index value for inexact matches. The value of
            the index at the matching location most satisfy the equation
            ``abs(index[loc] - key) <= tolerance``.
        
            .. versionadded:: 0.17.0
        
        Returns
        -------
        loc : int if unique index, possibly slice or mask if not
        """
        pass

    def get_slice_bound(self, label, side, kind): # reliably restored by inspect
        """
        Calculate slice bound that corresponds to given label.
        
                Returns leftmost (one-past-the-rightmost if ``side=='right'``) position
                of given label.
        
                Parameters
                ----------
                label : object
                side : {'left', 'right'}
                kind : {'ix', 'loc', 'getitem'}
        """
        pass

    def get_value(self, series, key): # reliably restored by inspect
        """
        Fast lookup of value from 1-dimensional ndarray. Only use this if you
                know what you're doing
        """
        pass

    def get_values(self): # reliably restored by inspect
        """ return the underlying data as an ndarray """
        pass

    def groupby(self, values): # reliably restored by inspect
        """
        Group the index labels by a given array of values.
        
                Parameters
                ----------
                values : array
                    Values used to determine the groups.
        
                Returns
                -------
                groups : dict
                    {group name -> group labels}
        """
        pass

    def holds_integer(self): # reliably restored by inspect
        # no doc
        pass

    def identical(self, other): # reliably restored by inspect
        """
        Similar to equals, but check that other comparable attributes are
                also equal
        """
        pass

    def insert(self, loc, item): # reliably restored by inspect
        """
        Make new Index inserting new item at location. Follows
                Python list.append semantics for negative values
        
                Parameters
                ----------
                loc : int
                item : object
        
                Returns
                -------
                new_index : Index
        """
        pass

    def intersection(self, other): # reliably restored by inspect
        """
        Form the intersection of two Index objects.
        
                This returns a new Index with elements common to the index and `other`,
                preserving the order of the calling index.
        
                Parameters
                ----------
                other : Index or array-like
        
                Returns
                -------
                intersection : Index
        
                Examples
                --------
        
                >>> idx1 = pd.Index([1, 2, 3, 4])
                >>> idx2 = pd.Index([3, 4, 5, 6])
                >>> idx1.intersection(idx2)
                Int64Index([3, 4], dtype='int64')
        """
        pass

    def isin(self, values, level=None): # reliably restored by inspect
        """
        Compute boolean array of whether each index value is found in the
                passed set of values.
        
                Parameters
                ----------
                values : set or list-like
                    Sought values.
        
                    .. versionadded:: 0.18.1
        
                    Support for values as a set
        
                level : str or int, optional
                    Name or position of the index level to use (if the index is a
                    MultiIndex).
        
                Notes
                -----
                If `level` is specified:
        
                - if it is the name of one *and only one* index level, use that level;
                - otherwise it should be a number indicating level position.
        
                Returns
                -------
                is_contained : ndarray (boolean dtype)
        """
        pass

    def isnull(self): # reliably restored by inspect
        """
        Detect missing values
        
                .. versionadded:: 0.20.0
        
                Returns
                -------
                a boolean array of whether my values are null
        
                See also
                --------
                pandas.isnull : pandas version
        """
        pass

    def is_(self, other): # reliably restored by inspect
        """
        More flexible, faster check like ``is`` but that works through views
        
                Note: this is *not* the same as ``Index.identical()``, which checks
                that metadata is also the same.
        
                Parameters
                ----------
                other : object
                    other object to compare against.
        
                Returns
                -------
                True if both have same underlying data, False otherwise : bool
        """
        pass

    def is_boolean(self): # reliably restored by inspect
        # no doc
        pass

    def is_categorical(self): # reliably restored by inspect
        # no doc
        pass

    def is_floating(self): # reliably restored by inspect
        # no doc
        pass

    def is_integer(self): # reliably restored by inspect
        # no doc
        pass

    def is_interval(self): # reliably restored by inspect
        # no doc
        pass

    def is_lexsorted_for_tuple(self, tup): # reliably restored by inspect
        # no doc
        pass

    def is_mixed(self): # reliably restored by inspect
        # no doc
        pass

    def is_numeric(self): # reliably restored by inspect
        # no doc
        pass

    def is_object(self): # reliably restored by inspect
        # no doc
        pass

    def is_type_compatible(self, kind): # reliably restored by inspect
        # no doc
        pass

    def join(self, other, how=None, level=None, return_indexers=False, sort=False): # reliably restored by inspect
        """
        *this is an internal non-public method*
        
        Compute join_index and indexers to conform data
        structures to the new index.
        
        Parameters
        ----------
        other : Index
        how : {'left', 'right', 'inner', 'outer'}
        level : int or level name, default None
        return_indexers : boolean, default False
        sort : boolean, default False
            Sort the join keys lexicographically in the result Index. If False,
            the order of the join keys depends on the join type (how keyword)
        
            .. versionadded:: 0.20.0
        
        Returns
        -------
        join_index, (left_indexer, right_indexer)
        """
        pass

    def map(self, mapper): # reliably restored by inspect
        """
        Apply mapper function to an index.
        
                Parameters
                ----------
                mapper : callable
                    Function to be applied.
        
                Returns
                -------
                applied : Union[Index, MultiIndex], inferred
                    The output of the mapping function applied to the index.
                    If the function returns a tuple with more than one element
                    a MultiIndex will be returned.
        """
        pass

    def memory_usage(self, deep=False): # reliably restored by inspect
        """
        Memory usage of my values
        
        Parameters
        ----------
        deep : bool
            Introspect the data deeply, interrogate
            `object` dtypes for system-level memory consumption
        
        Returns
        -------
        bytes used
        
        Notes
        -----
        Memory usage does not include memory consumed by elements that
        are not components of the array if deep=False
        
        See Also
        --------
        numpy.ndarray.nbytes
        """
        pass

    def notnull(self): # reliably restored by inspect
        """
        Reverse of isnull
        
                .. versionadded:: 0.20.0
        
                Returns
                -------
                a boolean array of whether my values are not null
        
                See also
                --------
                pandas.notnull : pandas version
        """
        pass

    def putmask(self, mask, value): # reliably restored by inspect
        """
        return a new Index of the values set with the mask
        
                See also
                --------
                numpy.ndarray.putmask
        """
        pass

    def ravel(self, order=None): # reliably restored by inspect
        """
        return an ndarray of the flattened values of the underlying data
        
                See also
                --------
                numpy.ndarray.ravel
        """
        pass

    def reindex(self, target, method=None, level=None, limit=None, tolerance=None): # reliably restored by inspect
        """
        Create index with target's values (move/add/delete values as necessary)
        
                Parameters
                ----------
                target : an iterable
        
                Returns
                -------
                new_index : pd.Index
                    Resulting index
                indexer : np.ndarray or None
                    Indices of output values in original index
        """
        pass

    def rename(self, name, inplace=False): # reliably restored by inspect
        """
        Set new names on index. Defaults to returning new index.
        
                Parameters
                ----------
                name : str or list
                    name to set
                inplace : bool
                    if True, mutates in place
        
                Returns
                -------
                new index (of same type and class...etc) [if inplace, returns None]
        """
        pass

    def repeat(*args, **kwargs): # reliably restored by inspect
        """
        Repeat elements of an Index. Refer to `numpy.ndarray.repeat`
                for more information about the `repeats` argument.
        
                See also
                --------
                numpy.ndarray.repeat
        """
        pass

    def reshape(self, *args, **kwargs): # reliably restored by inspect
        """
        NOT IMPLEMENTED: do not call this method, as reshaping is not
                supported for Index objects and will raise an error.
        
                Reshape an Index.
        """
        pass

    def set_names(self, names, level=None, inplace=False): # reliably restored by inspect
        """
        Set new names on index. Defaults to returning new index.
        
                Parameters
                ----------
                names : str or sequence
                    name(s) to set
                level : int, level name, or sequence of int/level names (default None)
                    If the index is a MultiIndex (hierarchical), level(s) to set (None
                    for all levels).  Otherwise level must be None
                inplace : bool
                    if True, mutates in place
        
                Returns
                -------
                new index (of same type and class...etc) [if inplace, returns None]
        
                Examples
                --------
                >>> Index([1, 2, 3, 4]).set_names('foo')
                Int64Index([1, 2, 3, 4], dtype='int64')
                >>> Index([1, 2, 3, 4]).set_names(['foo'])
                Int64Index([1, 2, 3, 4], dtype='int64')
                >>> idx = MultiIndex.from_tuples([(1, u'one'), (1, u'two'),
                                                  (2, u'one'), (2, u'two')],
                                                  names=['foo', 'bar'])
                >>> idx.set_names(['baz', 'quz'])
                MultiIndex(levels=[[1, 2], [u'one', u'two']],
                           labels=[[0, 0, 1, 1], [0, 1, 0, 1]],
                           names=[u'baz', u'quz'])
                >>> idx.set_names('baz', level=0)
                MultiIndex(levels=[[1, 2], [u'one', u'two']],
                           labels=[[0, 0, 1, 1], [0, 1, 0, 1]],
                           names=[u'baz', u'bar'])
        """
        pass

    def set_value(self, arr, key, value): # reliably restored by inspect
        """
        Fast lookup of value from 1-dimensional ndarray. Only use this if you
                know what you're doing
        """
        pass

    def shift(self, periods=1, freq=None): # reliably restored by inspect
        """
        Shift Index containing datetime objects by input number of periods and
                DateOffset
        
                Returns
                -------
                shifted : Index
        """
        pass

    def slice_indexer(self, start=None, end=None, step=None, kind=None): # reliably restored by inspect
        """
        For an ordered Index, compute the slice indexer for input labels and
                step
        
                Parameters
                ----------
                start : label, default None
                    If None, defaults to the beginning
                end : label, default None
                    If None, defaults to the end
                step : int, default None
                kind : string, default None
        
                Returns
                -------
                indexer : ndarray or slice
        
                Notes
                -----
                This function assumes that the data is sorted, so use at your own peril
        """
        pass

    def slice_locs(self, start=None, end=None, step=None, kind=None): # reliably restored by inspect
        """
        Compute slice locations for input labels.
        
                Parameters
                ----------
                start : label, default None
                    If None, defaults to the beginning
                end : label, default None
                    If None, defaults to the end
                step : int, defaults None
                    If None, defaults to 1
                kind : {'ix', 'loc', 'getitem'} or None
        
                Returns
                -------
                start, end : int
        """
        pass

    def sort(self, *args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def sortlevel(self, level=None, ascending=True, sort_remaining=None): # reliably restored by inspect
        """
        For internal compatibility with with the Index API
        
                Sort the Index. This is for compat with MultiIndex
        
                Parameters
                ----------
                ascending : boolean, default True
                    False to sort in descending order
        
                level, sort_remaining are compat parameters
        
                Returns
                -------
                sorted_index : Index
        """
        pass

    def sort_values(self, return_indexer=False, ascending=True): # reliably restored by inspect
        """ Return sorted copy of Index """
        pass

    def summary(self, name=None): # reliably restored by inspect
        # no doc
        pass

    def symmetric_difference(self, other, result_name=None): # reliably restored by inspect
        """
        Compute the symmetric difference of two Index objects.
                It's sorted if sorting is possible.
        
                Parameters
                ----------
                other : Index or array-like
                result_name : str
        
                Returns
                -------
                symmetric_difference : Index
        
                Notes
                -----
                ``symmetric_difference`` contains elements that appear in either
                ``idx1`` or ``idx2`` but not both. Equivalent to the Index created by
                ``idx1.difference(idx2) | idx2.difference(idx1)`` with duplicates
                dropped.
        
                Examples
                --------
                >>> idx1 = Index([1, 2, 3, 4])
                >>> idx2 = Index([2, 3, 4, 5])
                >>> idx1.symmetric_difference(idx2)
                Int64Index([1, 5], dtype='int64')
        
                You can also use the ``^`` operator:
        
                >>> idx1 ^ idx2
                Int64Index([1, 5], dtype='int64')
        """
        pass

    def sym_diff(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def take(self, indices, axis=0, allow_fill=True, fill_value=None, **kwargs): # reliably restored by inspect
        """
        return a new Index of the values selected by the indices
        
        For internal compatibility with numpy arrays.
        
        Parameters
        ----------
        indices : list
            Indices to be taken
        axis : int, optional
            The axis over which to select values, always 0.
        allow_fill : bool, default True
        fill_value : bool, default None
            If allow_fill=True and fill_value is not None, indices specified by
            -1 is regarded as NA. If Index doesn't hold NA, raise ValueError
        
        See also
        --------
        numpy.ndarray.take
        """
        pass

    def tolist(self): # reliably restored by inspect
        """ return a list of the Index values """
        pass

    def to_datetime(self, dayfirst=False): # reliably restored by inspect
        """
        DEPRECATED: use :meth:`pandas.to_datetime` instead.
        
                For an Index containing strings or datetime.datetime objects, attempt
                conversion to DatetimeIndex
        """
        pass

    def to_native_types(self, slicer=None, **kwargs): # reliably restored by inspect
        """
        Format specified values of `self` and return them.
        
                Parameters
                ----------
                slicer : int, array-like
                    An indexer into `self` that specifies which values
                    are used in the formatting process.
                kwargs : dict
                    Options for specifying how the values should be formatted.
                    These options include the following:
        
                    1) na_rep : str
                        The value that serves as a placeholder for NULL values
                    2) quoting : bool or None
                        Whether or not there are quoted values in `self`
                    3) date_format : str
                        The format used to represent date-like values
        """
        pass

    def to_series(self, **kwargs): # reliably restored by inspect
        """
        Create a Series with both index and values equal to the index keys
                useful with map for returning an indexer based on an index
        
                Returns
                -------
                Series : dtype will be based on the type of the Index values.
        """
        pass

    def union(self, other): # reliably restored by inspect
        """
        Form the union of two Index objects and sorts if possible.
        
                Parameters
                ----------
                other : Index or array-like
        
                Returns
                -------
                union : Index
        
                Examples
                --------
        
                >>> idx1 = pd.Index([1, 2, 3, 4])
                >>> idx2 = pd.Index([3, 4, 5, 6])
                >>> idx1.union(idx2)
                Int64Index([1, 2, 3, 4, 5, 6], dtype='int64')
        """
        pass

    def unique(self): # reliably restored by inspect
        """
        Return unique values in the object. Uniques are returned in order
        of appearance, this does NOT sort. Hash table-based unique.
        
        Parameters
        ----------
        values : 1d array-like
        
        Returns
        -------
        unique values.
          - If the input is an Index, the return is an Index
          - If the input is a Categorical dtype, the return is a Categorical
          - If the input is a Series/ndarray, the return will be an ndarray
        
        See Also
        --------
        unique
        Index.unique
        Series.unique
        """
        pass

    def view(self, cls=None): # reliably restored by inspect
        # no doc
        pass

    def where(self, cond, other=None): # reliably restored by inspect
        """
        .. versionadded:: 0.19.0
        
        Return an Index of same shape as self and whose corresponding
        entries are from self where cond is True and otherwise are from
        other.
        
        Parameters
        ----------
        cond : boolean array-like with the same length as self
        other : scalar, or array-like
        """
        pass

    @classmethod
    def _add_comparison_methods(cls, *args, **kwargs): # real signature unknown
        """ add in comparison methods """
        pass

    @classmethod
    def _add_logical_methods(cls, *args, **kwargs): # real signature unknown
        """ add in logical methods """
        pass

    @classmethod
    def _add_logical_methods_disabled(cls, *args, **kwargs): # real signature unknown
        """ add in logical methods to disable """
        pass

    @classmethod
    def _add_numeric_methods(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _add_numeric_methods_add_sub_disabled(cls, *args, **kwargs): # real signature unknown
        """ add in the numeric add/sub methods to disable """
        pass

    @classmethod
    def _add_numeric_methods_binary(cls, *args, **kwargs): # real signature unknown
        """ add in numeric methods """
        pass

    @classmethod
    def _add_numeric_methods_disabled(cls, *args, **kwargs): # real signature unknown
        """ add in numeric methods to disable other than add/sub """
        pass

    @classmethod
    def _add_numeric_methods_unary(cls, *args, **kwargs): # real signature unknown
        """ add in numeric unary methods """
        pass

    def _append_same_dtype(self, to_concat, name): # reliably restored by inspect
        """ Concatenate to_concat which has the same class """
        pass

    def _arrmap(self, *args, **kwargs): # real signature unknown
        pass

    def _assert_can_do_op(self, value): # reliably restored by inspect
        """ Check value is valid for scalar op """
        pass

    def _assert_can_do_setop(self, other): # reliably restored by inspect
        # no doc
        pass

    def _assert_take_fillable(self, values, indices, allow_fill=True, fill_value=None, na_value=nan): # reliably restored by inspect
        """ Internal method to handle NA filling of take """
        pass

    def _can_reindex(self, indexer): # reliably restored by inspect
        """
        *this is an internal non-public method*
        
                Check if we are allowing reindexing with this particular indexer
        
                Parameters
                ----------
                indexer : an integer indexer
        
                Raises
                ------
                ValueError if its a duplicate axis
        """
        pass

    def _cleanup(self): # reliably restored by inspect
        # no doc
        pass

    def _coerce_scalar_to_index(self, item): # reliably restored by inspect
        """
        we need to coerce a scalar to a compat for our index type
        
                Parameters
                ----------
                item : scalar item to coerce
        """
        pass

    @classmethod
    def _coerce_to_ndarray(cls, *args, **kwargs): # real signature unknown
        """
        coerces data to ndarray, raises on scalar data. Converts other
                iterables to list first and then to array. Does not touch ndarrays.
        """
        pass

    def _convert_arr_indexer(self, keyarr): # reliably restored by inspect
        """
        Convert an array-like indexer to the appropriate dtype.
        
        Parameters
        ----------
        keyarr : array-like
            Indexer to convert.
        
        Returns
        -------
        converted_keyarr : array-like
        """
        pass

    def _convert_can_do_setop(self, other): # reliably restored by inspect
        # no doc
        pass

    def _convert_for_op(self, value): # reliably restored by inspect
        """ Convert value to be insertable to ndarray """
        pass

    def _convert_index_indexer(self, keyarr): # reliably restored by inspect
        """
        Convert an Index indexer to the appropriate dtype.
        
        Parameters
        ----------
        keyarr : Index (or sub-class)
            Indexer to convert.
        
        Returns
        -------
        converted_keyarr : Index (or sub-class)
        """
        pass

    def _convert_listlike_indexer(self, keyarr, kind=None): # reliably restored by inspect
        """
        Parameters
                ----------
                keyarr : list-like
                    Indexer to convert.
        
                Returns
                -------
                tuple (indexer, keyarr)
                    indexer is an ndarray or None if cannot convert
                    keyarr are tuple-safe keys
        """
        pass

    def _convert_list_indexer(self, keyarr, kind=None): # reliably restored by inspect
        """
        Convert a list-like indexer to the appropriate dtype.
        
        Parameters
        ----------
        keyarr : Index (or sub-class)
            Indexer to convert.
        kind : iloc, ix, loc, optional
        
        Returns
        -------
        positional indexer or None
        """
        pass

    def _convert_scalar_indexer(self, key, kind=None): # reliably restored by inspect
        """
        Convert a scalar indexer.
        
        Parameters
        ----------
        key : label of the slice bound
        kind : {'ix', 'loc', 'getitem', 'iloc'} or None
        """
        pass

    def _convert_slice_indexer(self, key, kind=None): # reliably restored by inspect
        """
        Convert a slice indexer.
        
        By definition, these are labels unless 'iloc' is passed in.
        Floats are not allowed as the start, step, or stop of the slice.
        
        Parameters
        ----------
        key : label of the slice bound
        kind : {'ix', 'loc', 'getitem', 'iloc'} or None
        """
        pass

    def _convert_tolerance(self, tolerance): # reliably restored by inspect
        # no doc
        pass

    def _deepcopy_if_needed(self, orig, copy=False): # reliably restored by inspect
        """
        .. versionadded:: 0.19.0
        
                Make a copy of self if data coincides (in memory) with orig.
                Subclasses should override this if self._base is not an ndarray.
        
                Parameters
                ----------
                orig : ndarray
                    other ndarray to compare self._data against
                copy : boolean, default False
                    when False, do not run any check, just return self
        
                Returns
                -------
                A copy of self if needed, otherwise self : Index
        """
        pass

    def _evaluate_with_datetime_like(self, other, op, opstr): # reliably restored by inspect
        # no doc
        pass

    def _evaluate_with_timedelta_like(self, other, op, opstr): # reliably restored by inspect
        # no doc
        pass

    def _evalute_compare(self, op): # reliably restored by inspect
        # no doc
        pass

    def _filter_indexer_tolerance(self, target, indexer, tolerance): # reliably restored by inspect
        # no doc
        pass

    def _format_attrs(self): # reliably restored by inspect
        """ Return a list of tuples of the (attr,formatted_value) """
        pass

    def _format_data(self): # reliably restored by inspect
        """ Return the formatted data as a unicode string """
        pass

    def _format_native_types(self, na_rep=None, quoting=None, **kwargs): # reliably restored by inspect
        """ actually format my specific types """
        pass

    def _format_space(self): # reliably restored by inspect
        # no doc
        pass

    def _format_with_header(self, header, na_rep=None, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def _get_attributes_dict(self): # reliably restored by inspect
        """ return an attributes dict for my class """
        pass

    def _get_consensus_name(self, other): # reliably restored by inspect
        """
        Given 2 indexes, give a consensus name meaning
                we take the not None one, or None if the names differ.
                Return a new object if we are resetting the name
        """
        pass

    def _get_duplicates(self): # reliably restored by inspect
        # no doc
        pass

    def _get_fill_indexer(self, target, method, limit=None, tolerance=None): # reliably restored by inspect
        # no doc
        pass

    def _get_fill_indexer_searchsorted(self, target, method, limit=None): # reliably restored by inspect
        """
        Fallback pad/backfill get_indexer that works for monotonic decreasing
                indexes and non-monotonic targets
        """
        pass

    def _get_grouper_for_level(self, mapper, level=None): # reliably restored by inspect
        """
        Get index grouper corresponding to an index level
        
        Parameters
        ----------
        mapper: Group mapping function or None
            Function mapping index values to groups
        level : int or None
            Index level
        
        Returns
        -------
        grouper : Index
            Index of values to group on
        labels : ndarray of int or None
            Array of locations in level_index
        uniques : Index or None
            Index of unique values for level
        """
        pass

    def _get_level_number(self, level): # reliably restored by inspect
        # no doc
        pass

    def _get_level_values(self, level): # reliably restored by inspect
        """
        Return an Index of values for requested level, equal to the length
                of the index
        
                Parameters
                ----------
                level : int
        
                Returns
                -------
                values : Index
        """
        pass

    def _get_loc_only_exact_matches(self, key): # reliably restored by inspect
        """
        This is overriden on subclasses (namely, IntervalIndex) to control
                get_slice_bound.
        """
        pass

    def _get_names(self): # reliably restored by inspect
        # no doc
        pass

    def _get_nearest_indexer(self, target, limit, tolerance): # reliably restored by inspect
        """
        Get the indexer for the nearest index labels; requires an index with
                values that can be subtracted from each other (e.g., not strings or
                tuples).
        """
        pass

    def _get_string_slice(self, key, use_lhs=True, use_rhs=True): # reliably restored by inspect
        # no doc
        pass

    def _get_unique_index(self, dropna=False): # reliably restored by inspect
        """
        Returns an index containing unique values.
        
                Parameters
                ----------
                dropna : bool
                    If True, NaN values are dropped.
        
                Returns
                -------
                uniques : index
        """
        pass

    def _inner_indexer(self, *args, **kwargs): # real signature unknown
        """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
        pass

    def _invalid_indexer(self, form, key): # reliably restored by inspect
        """ consistent invalid indexer message """
        pass

    def _is_memory_usage_qualified(self): # reliably restored by inspect
        """ return a boolean if we need a qualified .info display """
        pass

    def _join_level(self, other, level, how=None, return_indexers=False, keep_order=True): # reliably restored by inspect
        """
        The join method *only* affects the level of the resulting
                MultiIndex. Otherwise it just exactly aligns the Index data to the
                labels of the level in the MultiIndex. If `keep_order` == True, the
                order of the data indexed by the MultiIndex will not be changed;
                otherwise, it will tie out with `other`.
        """
        pass

    def _join_monotonic(self, other, how=None, return_indexers=False): # reliably restored by inspect
        # no doc
        pass

    def _join_multi(self, other, how, return_indexers=True): # reliably restored by inspect
        # no doc
        pass

    def _join_non_unique(self, other, how=None, return_indexers=False): # reliably restored by inspect
        # no doc
        pass

    def _left_indexer(self, *args, **kwargs): # real signature unknown
        """ Two-pass algorithm for monotonic indexes. Handles many-to-one merges """
        pass

    def _left_indexer_unique(self, *args, **kwargs): # real signature unknown
        pass

    def _maybe_cast_indexer(self, key): # reliably restored by inspect
        """
        If we have a float key and are not a floating index
                then try to cast to an int if equivalent
        """
        pass

    def _maybe_cast_slice_bound(self, label, side, kind): # reliably restored by inspect
        """
        This function should be overloaded in subclasses that allow non-trivial
        casting on label-slice bounds, e.g. datetime-like indices allowing
        strings containing formatted datetimes.
        
        Parameters
        ----------
        label : object
        side : {'left', 'right'}
        kind : {'ix', 'loc', 'getitem'}
        
        Returns
        -------
        label :  object
        
        Notes
        -----
        Value of `side` parameter should be validated in caller.
        """
        pass

    def _maybe_promote(self, other): # reliably restored by inspect
        # no doc
        pass

    def _maybe_update_attributes(self, attrs): # reliably restored by inspect
        """ Update Index attributes (e.g. freq) depending on op """
        pass

    def _mpl_repr(self): # reliably restored by inspect
        # no doc
        pass

    def _outer_indexer(self, *args, **kwargs): # real signature unknown
        pass

    def _reindex_non_unique(self, target): # reliably restored by inspect
        """
        *this is an internal non-public method*
        
                Create a new index with target's values (move/add/delete values as
                necessary) use with non-unique Index and a possibly non-unique target
        
                Parameters
                ----------
                target : an iterable
        
                Returns
                -------
                new_index : pd.Index
                    Resulting index
                indexer : np.ndarray or None
                    Indices of output values in original index
        """
        pass

    def _reset_identity(self): # reliably restored by inspect
        """ Initializes or resets ``_id`` attribute with new object """
        pass

    @classmethod
    def _scalar_data_error(cls, *args, **kwargs): # real signature unknown
        pass

    def _searchsorted_monotonic(self, label, side=None): # reliably restored by inspect
        # no doc
        pass

    def _set_names(self, values, level=None): # reliably restored by inspect
        # no doc
        pass

    def _shallow_copy(self, values=None, **kwargs): # reliably restored by inspect
        """
        create a new Index with the same class as the caller, don't copy the
        data, use the same object attributes with passed in attributes taking
        precedence
        
        *this is an internal non-public method*
        
        Parameters
        ----------
        values : the values to create the new Index, optional
        kwargs : updates the default attributes for this Index
        """
        pass

    def _shallow_copy_with_infer(self, values=None, **kwargs): # reliably restored by inspect
        """
        create a new Index inferring the class with passed value, don't copy
                the data, use the same object attributes with passed in attributes
                taking precedence
        
                *this is an internal non-public method*
        
                Parameters
                ----------
                values : the values to create the new Index, optional
                kwargs : updates the default attributes for this Index
        """
        pass

    @classmethod
    def _simple_new(cls, *args, **kwargs): # real signature unknown
        """
        we require the we have a dtype compat for the values
                if we are passed a non-dtype compat, then coerce using the constructor
        
                Must be careful not to recurse.
        """
        pass

    def _sort_levels_monotonic(self): # reliably restored by inspect
        """ compat with MultiIndex """
        pass

    @classmethod
    def _string_data_error(cls, *args, **kwargs): # real signature unknown
        pass

    def _to_embed(self, keep_tz=False): # reliably restored by inspect
        """
        *this is an internal non-public method*
        
                return an array repr of this object, potentially casting to object
        """
        pass

    def _to_safe_for_reshape(self): # reliably restored by inspect
        """ convert to object if we are a categorical """
        pass

    @classmethod
    def _try_convert_to_int_index(cls, *args, **kwargs): # real signature unknown
        """
        Attempt to convert an array of data into an integer index.
        
                Parameters
                ----------
                data : The data to convert.
                copy : Whether to copy the data or not.
                name : The name of the index returned.
        
                Returns
                -------
                int_index : data converted to either an Int64Index or a
                            UInt64Index
        
                Raises
                ------
                ValueError if the conversion was not successful.
        """
        pass

    def _unpickle_compat(self, state): # reliably restored by inspect
        """ Necessary for making this object picklable """
        pass

    def _update_inplace(self, result, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def _validate_for_numeric_binop(self, other, op, opstr): # reliably restored by inspect
        """
        return valid other, evaluate or raise TypeError
                if we are not of the appropriate type
        
                internal method called by ops
        """
        pass

    def _validate_for_numeric_unaryop(self, op, opstr): # reliably restored by inspect
        """ validate if we can perform a numeric unary operation """
        pass

    def _validate_indexer(self, form, key, kind): # reliably restored by inspect
        """
        if we are positional indexer
                validate that we have appropriate typed bounds
                must be an integer
        """
        pass

    def _validate_index_level(self, level): # reliably restored by inspect
        """
        Validate index level.
        
                For single-level Index getting level number is a no-op, but some
                verification must be done like in MultiIndex.
        """
        pass

    def _validate_names(self, name=None, names=None, deep=False): # reliably restored by inspect
        """
        Handles the quirks of having a singular 'name' parameter for general
                Index and plural 'names' parameter for MultiIndex.
        """
        pass

    def _wrap_joined_index(self, joined, other): # reliably restored by inspect
        # no doc
        pass

    def _wrap_union_result(self, other, result): # reliably restored by inspect
        # no doc
        pass

    def __abs__(self, other=None): # reliably restored by inspect
        # no doc
        pass

    def __add__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __and__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __array_wrap__(self, result, context=None): # reliably restored by inspect
        """ Gets called after a ufunc """
        pass

    def __array__(self, dtype=None): # reliably restored by inspect
        """ the array interface, return my values """
        pass

    def __bool__(self): # reliably restored by inspect
        # no doc
        pass

    def __contains__(self, key): # reliably restored by inspect
        """
        return a boolean if this key is IN the index
        
        Parameters
        ----------
        key : object
        
        Returns
        -------
        boolean
        """
        pass

    def __copy__(self, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __deepcopy__(self, memo=None): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __floordiv__(self, other=None): # reliably restored by inspect
        # no doc
        pass

    def __getitem__(self, key): # reliably restored by inspect
        """
        Override numpy.ndarray's __getitem__ method to work as desired.
        
                This function adds lists and Series as valid boolean indexers
                (ndarrays only supports ndarray with dtype=bool).
        
                If resulting ndim != 1, plain ndarray is returned instead of
                corresponding `Index` subclass.
        """
        pass

    def __ge__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __gt__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __hash__(self): # reliably restored by inspect
        # no doc
        pass

    def __iadd__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __inv__(self, other=None): # reliably restored by inspect
        # no doc
        pass

    def __iter__(self): # reliably restored by inspect
        # no doc
        pass

    def __len__(self): # reliably restored by inspect
        """ return the length of the Index """
        pass

    def __le__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __lt__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __mul__(self, other=None): # reliably restored by inspect
        # no doc
        pass

    def __neg__(self, other=None): # reliably restored by inspect
        # no doc
        pass

    @staticmethod # known case of __new__
    def __new__(cls, data=None, dtype=None, copy=False, name=None, fastpath=False, tupleize_cols=True, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __nonzero__(self): # reliably restored by inspect
        # no doc
        pass

    def __or__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __pos__(self, other=None): # reliably restored by inspect
        # no doc
        pass

    def __pow__(self, other=None): # reliably restored by inspect
        # no doc
        pass

    def __radd__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __reduce__(self): # reliably restored by inspect
        # no doc
        pass

    def __rfloordiv__(self, other=None): # reliably restored by inspect
        # no doc
        pass

    def __rmul__(self, other=None): # reliably restored by inspect
        # no doc
        pass

    def __rpow__(self, other=None): # reliably restored by inspect
        # no doc
        pass

    def __rtruediv__(self, other=None): # reliably restored by inspect
        # no doc
        pass

    def __setitem__(self, key, value): # reliably restored by inspect
        # no doc
        pass

    def __setstate__(self, state): # reliably restored by inspect
        """ Necessary for making this object picklable """
        pass

    def __sub__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __truediv__(self, other=None): # reliably restored by inspect
        # no doc
        pass

    def __unicode__(self): # reliably restored by inspect
        """
        Return a string representation for this object.
        
                Invoked by unicode(df) in py2 only. Yields a Unicode String in both
                py2/py3.
        """
        pass

    def __xor__(self, other): # reliably restored by inspect
        # no doc
        pass

    has_duplicates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_monotonic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ alias for is_monotonic_increasing (deprecated) """

    is_monotonic_decreasing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        return if the index is monotonic decreasing (only equal or
        decreasing) values.

        Examples
        --------
        >>> Index([3, 2, 1]).is_monotonic_decreasing
        True
        >>> Index([3, 2, 2]).is_monotonic_decreasing
        True
        >>> Index([3, 1, 2]).is_monotonic_decreasing
        False
        """

    is_monotonic_increasing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        return if the index is monotonic increasing (only equal or
        increasing) values.

        Examples
        --------
        >>> Index([1, 2, 3]).is_monotonic_increasing
        True
        >>> Index([1, 2, 2]).is_monotonic_increasing
        True
        >>> Index([1, 3, 2]).is_monotonic_increasing
        False
        """

    names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nlevels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ return the underlying data as an ndarray """

    _formatter_func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the formatted data as a unicode string
        """

    _has_complex_internals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _is_strictly_monotonic_decreasing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """return if the index is strictly monotonic decreasing
        (only decreasing) values

        Examples
        --------
        >>> Index([3, 2, 1])._is_strictly_monotonic_decreasing
        True
        >>> Index([3, 2, 2])._is_strictly_monotonic_decreasing
        False
        >>> Index([3, 1, 2])._is_strictly_monotonic_decreasing
        False
        """

    _is_strictly_monotonic_increasing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """return if the index is strictly monotonic increasing
        (only increasing) values

        Examples
        --------
        >>> Index([1, 2, 3])._is_strictly_monotonic_increasing
        True
        >>> Index([1, 2, 2])._is_strictly_monotonic_increasing
        False
        >>> Index([1, 3, 2])._is_strictly_monotonic_increasing
        False
        """


    asi8 = None
    dtype = None
    dtype_str = None
    hasnans = None
    inferred_type = None
    is_all_dates = None
    is_unique = None
    name = None
    _allow_datetime_index_ops = False
    _allow_index_ops = True
    _allow_period_index_ops = False
    _attributes = [
        'name',
    ]
    _box_scalars = False
    _can_hold_na = True
    _comparables = [
        'name',
    ]
    _constructor = None
    _data = None
    _defer_to_indexing = False
    _engine = None
    _engine_type = None # (!) real value is ''
    _id = None
    _infer_as_myclass = False
    _isnan = None
    _is_numeric_dtype = False
    _join_precedence = 1
    _nan_idxs = None
    _na_value = nan
    _typ = 'index'


class k(__numpy.generic):
    """ Any Python object.  Character code: 'O'. """
    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
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

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Implement self+=value. """
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Implement self*=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value.n """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass


class ParserWarning(Warning):
    """
    Warning that is raised in `pd.read_csv` whenever it is necessary
        to change parsers (generally from 'c' to 'python') contrary to the
        one specified by the user due to lack of support or functionality for
        parsing particular attributes of a CSV file with the requsted engine
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class TextReader(object):
    """ # source: StringIO or file object """
    def close(self, *args, **kwargs): # real signature unknown
        pass

    def debug_print(self, *args, **kwargs): # real signature unknown
        pass

    def read(self, *args, **kwargs): # real signature unknown
        """ rows=None --> read all rows """
        pass

    def remove_noconvert(self, *args, **kwargs): # real signature unknown
        pass

    def set_error_bad_lines(self, *args, **kwargs): # real signature unknown
        pass

    def set_noconvert(self, *args, **kwargs): # real signature unknown
        pass

    def _convert_column_data(self, *args, **kwargs): # real signature unknown
        pass

    def _get_converter(self, *args, **kwargs): # real signature unknown
        pass

    def _set_quoting(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    allow_leading_cols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    as_recarray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    buffer_lines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    compact_ints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    compression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delimiter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delim_whitespace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dtype_cast_order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    header_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    header_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    index_col = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leading_cols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    low_memory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mangle_dupe_cols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    memory_map = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    na_values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    noconvert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    orig_header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skipfooter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skiprows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    table_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tupleize_cols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    usecols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_unsigned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


# variables with complex values

na_values = {
    np.double: 
        nan
    ,
    np.intp: 
        -9223372036854775808
    ,
    np.int32: 
        -2147483648
    ,
    np.short: 
        -32768
    ,
    np.byte: 
        -128
    ,
    np.uintp: 
        18446744073709551615
    ,
    np.uint: 
        4294967295
    ,
    np.ushort: 
        65535
    ,
    np.ubyte: 
        255
    ,
    np.bool8: 
        255
    ,
    np.object0: 
        nan
    ,
    None:  # (!) real value is ''
        nan
    ,
    None:  # (!) real value is ''
        -9223372036854775808
    ,
    None:  # (!) real value is ''
        -2147483648
    ,
    None:  # (!) real value is ''
        -32768
    ,
    None:  # (!) real value is ''
        -128
    ,
    None:  # (!) real value is ''
        18446744073709551615
    ,
    None:  # (!) real value is ''
        4294967295
    ,
    None:  # (!) real value is ''
        65535
    ,
    None:  # (!) real value is ''
        255
    ,
    None:  # (!) real value is ''
        255
    ,
    None:  # (!) real value is ''
        nan
    ,
}

_NA_VALUES = [
    b'-1.#IND',
    b'1.#QNAN',
    b'1.#IND',
    b'-1.#QNAN',
    b'#N/A N/A',
    b'NA',
    b'#NA',
    b'NULL',
    b'NaN',
    b'nan',
    b'',
]

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

