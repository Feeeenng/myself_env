# encoding: utf-8
# module h5py.h5t
# from D:\ProgramData\Anaconda3\lib\site-packages\h5py\h5t.cp36-win_amd64.pyd
# by generator 1.145
"""
HDF5 "H5T" data-type API

    This module contains the datatype identifier class TypeID, and its
    subclasses which represent things like integer/float/compound identifiers.
    The majority of the H5T API is presented as methods on these identifiers.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import operator as operator # D:\ProgramData\Anaconda3\lib\operator.py
import numpy as np # D:\ProgramData\Anaconda3\lib\site-packages\numpy\__init__.py
import platform as platform # D:\ProgramData\Anaconda3\lib\platform.py
import warnings as warnings # D:\ProgramData\Anaconda3\lib\warnings.py
from h5py._objects import (array_create, check_dtype, convert, create, decode, 
    enum_create, find, open, special_dtype, vlen_create, with_phil)

import h5py._objects as __h5py__objects
import numpy as __numpy


# Variables with simple values

ARRAY = 10

BITFIELD = 4

BKG_NO = 0
BKG_TEMP = 1
BKG_YES = 2

COMPOUND = 6

CSET_ASCII = 0
CSET_UTF8 = 1

DIR_ASCEND = 1
DIR_DEFAULT = 0
DIR_DESCEND = 2

ENUM = 8

FLOAT = 1

INTEGER = 0

MACHINE = 'AMD64'

NORM_IMPLIED = 0
NORM_MSBSET = 1
NORM_NONE = 2

NO_CLASS = -1

OPAQUE = 5

ORDER_BE = 1
ORDER_LE = 0
ORDER_NATIVE = 0
ORDER_NONE = 4
ORDER_VAX = 2

PAD_BACKGROUND = 2
PAD_ONE = 1
PAD_ZERO = 0

PY3 = True

REFERENCE = 7

SGN_2 = 1
SGN_NONE = 0

STRING = 3

STR_NULLPAD = 1
STR_NULLTERM = 0
STR_SPACEPAD = 2

TIME = 2

VARIABLE = 18446744073709551615

VLEN = 9

# functions

def get_config(*args, **kwargs): # real signature unknown
    """
    () => H5PYConfig
    
        Get a reference to the global library configuration object.
    """
    pass

def py_create(*args, **kwargs): # real signature unknown
    """
    (OBJECT dtype_in, BOOL logical=False) => TypeID
    
        Given a Numpy dtype object, generate a byte-for-byte memory-compatible
        HDF5 datatype object.  The result is guaranteed to be transient and
        unlocked.
    
        Argument dtype_in may be a dtype object, or anything which can be
        converted to a dtype, including strings like '<i4'.
    
        logical
            If this flag is set, instead of returning a byte-for-byte identical
            representation of the type, the function returns the closest logically
            appropriate HDF5 type.  For example, in the case of a "hinted" dtype
            of kind "O" representing a string, it would return an HDF5 variable-
            length string type.
    """
    pass

def py_get_enum(*args, **kwargs): # real signature unknown
    """
    (DTYPE dt_in) => DICT
    
        Deprecated; use check_dtype() instead.
    """
    pass

def py_get_vlen(*args, **kwargs): # real signature unknown
    """
    (OBJECT dt_in) => TYPE
    
        Deprecated; use check_dtype() instead.
    """
    pass

def py_new_enum(*args, **kwargs): # real signature unknown
    """
    (DTYPE dt_in, DICT enum_vals) => DTYPE
    
        Deprecated; use special_dtype() instead.
    """
    pass

def py_new_vlen(*args, **kwargs): # real signature unknown
    """
    (OBJECT kind) => DTYPE
    
        Deprecated; use special_dtype() instead.
    """
    pass

def typewrap(*args, **kwargs): # real signature unknown
    pass

# classes

class ftype(bytes, __numpy.character):
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class TypeID(__h5py__objects.ObjectID):
    """
    Base class for type identifiers (implements common operations)
    
            * Hashable: If committed; in HDF5 1.8.X, also if locked
            * Equality: Logical H5T comparison
    """
    def commit(self, *args, **kwargs): # real signature unknown
        """
        (ObjectID group, STRING name, PropID lcpl=None)
        
                Commit this (transient) datatype to a named datatype in a file.
                If present, lcpl may be a link creation property list.
        """
        pass

    def committed(self, *args, **kwargs): # real signature unknown
        """
        () => BOOL is_comitted
        
                Determine if a given type object is named (T) or transient (F).
        """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        """
        () => TypeID
        
                Create a copy of this type object.
        """
        pass

    def detect_class(self, *args, **kwargs): # real signature unknown
        """
        (INT classtype) => BOOL class_is_present
        
                Determine if a member of the given class exists in a compound
                datatype.  The search is recursive.
        """
        pass

    def encode(self, *args, **kwargs): # real signature unknown
        """
        () => STRING
        
                Serialize an HDF5 type.  Bear in mind you can also use the
                native Python pickle/unpickle machinery to do this.  The
                returned string may contain binary values, including NULLs.
        """
        pass

    def equal(self, *args, **kwargs): # real signature unknown
        """
        (TypeID typeid) => BOOL
        
                Logical comparison between datatypes.  Also called by
                Python's "==" operator.
        """
        pass

    def get_class(self, *args, **kwargs): # real signature unknown
        """
        () => INT classcode
        
                Determine the datatype's class code.
        """
        pass

    def get_size(self, *args, **kwargs): # real signature unknown
        """
        () => INT size
        
                    Determine the total size of a datatype, in bytes.
        """
        pass

    def get_super(self, *args, **kwargs): # real signature unknown
        """
        () => TypeID
        
                Determine the parent type of an array, enumeration or vlen datatype.
        """
        pass

    def lock(self, *args, **kwargs): # real signature unknown
        """
        ()
        
                Lock this datatype, which makes it immutable and indestructible.
                Once locked, it can't be unlocked.
        """
        pass

    def set_size(self, *args, **kwargs): # real signature unknown
        """
        (UINT size)
        
                Set the total size of the datatype, in bytes.
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

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

    dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ A Numpy-style dtype object representing this object.
        """


    __pyx_vtable__ = None # (!) real value is ''


class TypeArrayID(TypeID):
    """ Represents an array datatype """
    def get_array_dims(self, *args, **kwargs): # real signature unknown
        """
        () => TUPLE dimensions
        
                Get the dimensions of the given array datatype as
                a tuple of integers.
        """
        pass

    def get_array_ndims(self, *args, **kwargs): # real signature unknown
        """
        () => INT rank
        
                Get the rank of the given array datatype.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class TypeAtomicID(TypeID):
    """ Base class for atomic datatypes (float or integer) """
    def get_offset(self, *args, **kwargs): # real signature unknown
        """
        () => INT offset
        
                Get the offset of the first significant bit.
        """
        pass

    def get_order(self, *args, **kwargs): # real signature unknown
        """
        () => INT order
        
                Obtain the byte order of the datatype; one of:
        
                - ORDER_LE
                - ORDER_BE
        """
        pass

    def get_pad(self, *args, **kwargs): # real signature unknown
        """
        () => (INT lsb_pad_code, INT msb_pad_code)
        
                Determine the padding type.  Possible values are:
        
                - PAD_ZERO
                - PAD_ONE
                - PAD_BACKGROUND
        """
        pass

    def get_precision(self, *args, **kwargs): # real signature unknown
        """
        () => UINT precision
        
                Get the number of significant bits (excludes padding).
        """
        pass

    def set_offset(self, *args, **kwargs): # real signature unknown
        """
        (UINT offset)
        
                Set the offset of the first significant bit.
        """
        pass

    def set_order(self, *args, **kwargs): # real signature unknown
        """
        (INT order)
        
                Set the byte order of the datatype; one of:
        
                - ORDER_LE
                - ORDER_BE
        """
        pass

    def set_pad(self, *args, **kwargs): # real signature unknown
        """
        (INT lsb_pad_code, INT msb_pad_code)
        
                Set the padding type.  Possible values are:
        
                - PAD_ZERO
                - PAD_ONE
                - PAD_BACKGROUND
        """
        pass

    def set_precision(self, *args, **kwargs): # real signature unknown
        """
        (UINT precision)
                    
                Set the number of significant bits (excludes padding).
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class TypeBitfieldID(TypeID):
    """ HDF5 bitfield type """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class TypeCompositeID(TypeID):
    """ Base class for enumerated and compound types. """
    def get_member_index(self, *args, **kwargs): # real signature unknown
        """
        (STRING name) => INT index
        
                Determine the index of a member of a compound or enumerated datatype
                identified by a string name.
        """
        pass

    def get_member_name(self, *args, **kwargs): # real signature unknown
        """
        (INT member) => STRING name
                
                Determine the name of a member of a compound or enumerated type,
                identified by its index (0 <= member < nmembers).
        """
        pass

    def get_nmembers(self, *args, **kwargs): # real signature unknown
        """
        () => INT number_of_members
        
                Determine the number of members in a compound or enumerated type.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class TypeCompoundID(TypeCompositeID):
    """ Represents a compound datatype """
    def get_member_class(self, *args, **kwargs): # real signature unknown
        """
        (INT member) => INT class
        
                Determine the datatype class of the member of a compound type,
                identified by its index (0 <= member < nmembers).
        """
        pass

    def get_member_offset(self, *args, **kwargs): # real signature unknown
        """
        (INT member) => INT offset
        
                Determine the offset, in bytes, of the beginning of the specified
                member of a compound datatype.
        """
        pass

    def get_member_type(self, *args, **kwargs): # real signature unknown
        """
        (INT member) => TypeID
        
                Create a copy of a member of a compound datatype, identified by its
                index.
        """
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        """
        (STRING name, UINT offset, TypeID field)
        
                Add a named member datatype to a compound datatype.  The parameter
                offset indicates the offset from the start of the compound datatype,
                in bytes.
        """
        pass

    def pack(self, *args, **kwargs): # real signature unknown
        """
        ()
        
                Recursively removes padding (introduced on account of e.g. compiler
                alignment rules) from a compound datatype.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class TypeEnumID(TypeCompositeID):
    """ Represents an enumerated type """
    def enum_insert(self, *args, **kwargs): # real signature unknown
        """
        (STRING name, INT/LONG value)
        
                Define a new member of an enumerated type.  The value will be
                automatically converted to the base type defined for this enum.  If
                the conversion results in overflow, the value will be silently 
                clipped.
        """
        pass

    def enum_nameof(self, *args, **kwargs): # real signature unknown
        """
        (LONG value) => STRING name
        
                Determine the name associated with the given value.  Due to a
                limitation of the HDF5 library, this can only retrieve names up to
                1023 characters in length.
        """
        pass

    def enum_valueof(self, *args, **kwargs): # real signature unknown
        """
        (STRING name) => LONG value
        
                Get the value associated with an enum name.
        """
        pass

    def get_member_value(self, *args, **kwargs): # real signature unknown
        """
        (UINT index) => LONG value
        
                Determine the value for the member at the given zero-based index.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class TypeFloatID(TypeAtomicID):
    """ Floating-point atomic datatypes """
    def get_ebias(self, *args, **kwargs): # real signature unknown
        """
        () => UINT ebias
        
                Get the exponent bias.
        """
        pass

    def get_fields(self, *args, **kwargs): # real signature unknown
        """
        () => TUPLE field_info
        
                Get information about floating-point bit fields.  See the HDF5
                docs for a full description.  Tuple has the following members:
        
                0. UINT spos
                1. UINT epos
                2. UINT esize
                3. UINT mpos
                4. UINT msize
        """
        pass

    def get_inpad(self, *args, **kwargs): # real signature unknown
        """
        () => INT pad_code
        
                Determine the internal padding strategy.  Legal values are:
        
                - PAD_ZERO
                - PAD_ONE
                - PAD_BACKGROUND
        """
        pass

    def get_norm(self, *args, **kwargs): # real signature unknown
        """
        () => INT normalization_code
        
                Get the normalization strategy.  Legal values are:
        
                - NORM_IMPLIED
                - NORM_MSBSET
                - NORM_NONE
        """
        pass

    def set_ebias(self, *args, **kwargs): # real signature unknown
        """
        (UINT ebias)
        
                Set the exponent bias.
        """
        pass

    def set_fields(self, *args, **kwargs): # real signature unknown
        """
        (UINT spos, UINT epos, UINT esize, UINT mpos, UINT msize)
        
                Set floating-point bit fields.  Refer to the HDF5 docs for
                argument definitions.
        """
        pass

    def set_inpad(self, *args, **kwargs): # real signature unknown
        """
        (INT pad_code)
        
                Set the internal padding strategy.  Legal values are:
        
                - PAD_ZERO
                - PAD_ONE
                - PAD_BACKGROUND
        """
        pass

    def set_norm(self, *args, **kwargs): # real signature unknown
        """
        (INT normalization_code)
        
                Set the normalization strategy.  Legal values are:
        
                - NORM_IMPLIED
                - NORM_MSBSET
                - NORM_NONE
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class TypeIntegerID(TypeAtomicID):
    """ Integer atomic datatypes """
    def get_sign(self, *args, **kwargs): # real signature unknown
        """
        () => INT sign
        
                Get the "signedness" of the datatype; one of:
        
                SGN_NONE
                    Unsigned
        
                SGN_2
                    Signed 2's complement
        """
        pass

    def set_sign(self, *args, **kwargs): # real signature unknown
        """
        (INT sign)
        
                Set the "signedness" of the datatype; one of:
        
                SGN_NONE
                    Unsigned
        
                SGN_2
                    Signed 2's complement
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class TypeOpaqueID(TypeID):
    """ Represents an opaque type """
    def get_tag(self, *args, **kwargs): # real signature unknown
        """
        () => STRING tag
        
                Get the tag associated with an opaque datatype.
        """
        pass

    def set_tag(self, *args, **kwargs): # real signature unknown
        """
        (STRING tag)
        
                Set a string describing the contents of an opaque datatype.
                Limited to 256 characters.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class TypeReferenceID(TypeID):
    """ HDF5 object or region reference """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class TypeStringID(TypeID):
    """ String datatypes, both fixed and vlen. """
    def get_cset(self, *args, **kwargs): # real signature unknown
        """
        () => INT character_set
        
                Retrieve the character set used for a string.
        """
        pass

    def get_strpad(self, *args, **kwargs): # real signature unknown
        """
        () => INT padding_type
        
                Get the padding type.  Legal values are:
        
                STR_NULLTERM
                    NULL termination only (C style)
        
                STR_NULLPAD
                    Pad buffer with NULLs
        
                STR_SPACEPAD
                    Pad buffer with spaces (FORTRAN style)
        """
        pass

    def is_variable_str(self, *args, **kwargs): # real signature unknown
        """
        () => BOOL is_variable
        
                Determine if the given string datatype is a variable-length string.
        """
        pass

    def set_cset(self, *args, **kwargs): # real signature unknown
        """
        (INT character_set)
        
                Set the character set used for a string.
        """
        pass

    def set_strpad(self, *args, **kwargs): # real signature unknown
        """
        (INT pad)
        
                Set the padding type.  Legal values are:
        
                STR_NULLTERM
                    NULL termination only (C style)
        
                STR_NULLPAD
                    Pad buffer with NULLs
        
                STR_SPACEPAD
                    Pad buffer with spaces (FORTRAN style)
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class TypeTimeID(TypeID):
    """ Unix-style time_t (deprecated) """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class TypeVlenID(TypeID):
    """ Non-string vlen datatypes. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


# variables with complex values

available_ftypes = {
    2: None, # (!) real value is ''
    4: None, # (!) real value is ''
    8: None, # (!) real value is ''
}

cfg = None # (!) real value is ''

C_S1 = None # (!) real value is ''

FORTRAN_S1 = None # (!) real value is ''

IEEE_F16BE = None # (!) real value is ''

IEEE_F16LE = None # (!) real value is ''

IEEE_F32BE = None # (!) real value is ''

IEEE_F32LE = None # (!) real value is ''

IEEE_F64BE = None # (!) real value is ''

IEEE_F64LE = None # (!) real value is ''

NATIVE_DOUBLE = None # (!) real value is ''

NATIVE_FLOAT = None # (!) real value is ''

NATIVE_INT16 = None # (!) real value is ''

NATIVE_INT32 = None # (!) real value is ''

NATIVE_INT64 = None # (!) real value is ''

NATIVE_INT8 = None # (!) real value is ''

NATIVE_LDOUBLE = None # (!) real value is ''

NATIVE_UINT16 = None # (!) real value is ''

NATIVE_UINT32 = None # (!) real value is ''

NATIVE_UINT64 = None # (!) real value is ''

NATIVE_UINT8 = None # (!) real value is ''

phil = None # (!) real value is ''

PYTHON_OBJECT = None # (!) real value is ''

STD_I16BE = None # (!) real value is ''

STD_I16LE = None # (!) real value is ''

STD_I32BE = None # (!) real value is ''

STD_I32LE = None # (!) real value is ''

STD_I64BE = None # (!) real value is ''

STD_I64LE = None # (!) real value is ''

STD_I8BE = None # (!) real value is ''

STD_I8LE = None # (!) real value is ''

STD_REF_DSETREG = None # (!) real value is ''

STD_REF_OBJ = None # (!) real value is ''

STD_U16BE = None # (!) real value is ''

STD_U16LE = None # (!) real value is ''

STD_U32BE = None # (!) real value is ''

STD_U32LE = None # (!) real value is ''

STD_U64BE = None # (!) real value is ''

STD_U64LE = None # (!) real value is ''

STD_U8BE = None # (!) real value is ''

STD_U8LE = None # (!) real value is ''

UNIX_D32BE = None # (!) real value is ''

UNIX_D32LE = None # (!) real value is ''

UNIX_D64BE = None # (!) real value is ''

UNIX_D64LE = None # (!) real value is ''

__loader__ = None # (!) real value is ''

__pyx_capi__ = {
    'H5PY_OBJ': None, # (!) real value is ''
    'py_create': None, # (!) real value is ''
    'typewrap': None, # (!) real value is ''
}

__spec__ = None # (!) real value is ''

__test__ = {}

