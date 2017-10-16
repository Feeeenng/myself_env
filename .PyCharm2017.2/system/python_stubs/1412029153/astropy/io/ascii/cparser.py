# encoding: utf-8
# module astropy.io.ascii.cparser
# from D:\ProgramData\Anaconda3\lib\site-packages\astropy\io\ascii\cparser.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import csv as csv # D:\ProgramData\Anaconda3\lib\csv.py
import os as os # D:\ProgramData\Anaconda3\lib\os.py
import math as math # <module 'math' (built-in)>
import multiprocessing as multiprocessing # D:\ProgramData\Anaconda3\lib\multiprocessing\__init__.py
import mmap as mmap # <module 'mmap' (built-in)>
import warnings as warnings # D:\ProgramData\Anaconda3\lib\warnings.py
import numpy as np # D:\ProgramData\Anaconda3\lib\site-packages\numpy\__init__.py
import numpy.ma as ma # D:\ProgramData\Anaconda3\lib\site-packages\numpy\ma\__init__.py
import astropy.table.pprint as pprint # D:\ProgramData\Anaconda3\lib\site-packages\astropy\table\pprint.py
import astropy.extern.six as six # D:\ProgramData\Anaconda3\lib\site-packages\astropy\extern\bundled\six.py
import astropy.io.ascii.core as core # D:\ProgramData\Anaconda3\lib\site-packages\astropy\io\ascii\core.py
import queue as Queue # D:\ProgramData\Anaconda3\lib\queue.py

# functions

def get_fill_values(*args, **kwargs): # real signature unknown
    pass

def get_readable_fileobj(*args, **kwds): # reliably restored by inspect
    """
    Given a filename, pathlib.Path object or a readable file-like object, return a context
        manager that yields a readable file-like object.
    
        This supports passing filenames, URLs, and readable file-like objects,
        any of which can be compressed in gzip, bzip2 or lzma (xz) if the
        appropriate compression libraries are provided by the Python installation.
    
        Notes
        -----
    
        This function is a context manager, and should be used for example
        as::
    
            with get_readable_fileobj('file.dat') as f:
                contents = f.read()
    
        Parameters
        ----------
        name_or_obj : str or file-like object
            The filename of the file to access (if given as a string), or
            the file-like object to access.
    
            If a file-like object, it must be opened in binary mode.
    
        encoding : str, optional
            When `None` (default), returns a file-like object with a
            ``read`` method that on Python 2.x returns `bytes` objects and
            on Python 3.x returns `str` (``unicode``) objects, using
            `locale.getpreferredencoding` as an encoding.  This matches
            the default behavior of the built-in `open` when no ``mode``
            argument is provided.
    
            When ``'binary'``, returns a file-like object where its ``read``
            method returns `bytes` objects.
    
            When another string, it is the name of an encoding, and the
            file-like object's ``read`` method will return `str` (``unicode``)
            objects, decoded from binary using the given encoding.
    
        cache : bool, optional
            Whether to cache the contents of remote URLs.
    
        show_progress : bool, optional
            Whether to display a progress bar if the file is downloaded
            from a remote server.  Default is `True`.
    
        remote_timeout : float
            Timeout for remote requests in seconds (default is the configurable
            `astropy.utils.data.Conf.remote_timeout`, which is 3s by default)
    
        Returns
        -------
        file : readable file-like object
    """
    pass

def _copy_cparser(*args, **kwargs): # real signature unknown
    pass

def _read_chunk(*args, **kwargs): # real signature unknown
    pass

# classes

class AstropyWarning(Warning):
    """
    The base warning class from which all Astropy warnings should inherit.
    
        Any warning inheriting from this class is handled by the Astropy logger.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class CParser(object):
    """
    A fast Cython parser class which uses underlying C code
        for tokenization.
    """
    def get_header_names(self, *args, **kwargs): # real signature unknown
        pass

    def get_names(self, *args, **kwargs): # real signature unknown
        pass

    def read(self, *args, **kwargs): # real signature unknown
        pass

    def read_header(self, *args, **kwargs): # real signature unknown
        pass

    def setup_tokenizer(self, *args, **kwargs): # real signature unknown
        pass

    def set_names(self, *args, **kwargs): # real signature unknown
        pass

    def _read_parallel(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    header_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class CParserError(Exception):
    """
    An instance of this class is thrown when an error occurs
        during C parsing.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class FastWriter(object):
    """
    A fast Cython writing class for writing tables
        as ASCII data.
    """
    def write(self, *args, **kwargs): # real signature unknown
        pass

    def _write_header(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class FileString(object):
    """ A wrapper class for a memory-mapped file pointer. """
    def splitlines(self, *args, **kwargs): # real signature unknown
        """ Return a generator yielding lines from the memory map. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

ERR_CODES = {
    0: 'no error',
    1: 'invalid line supplied',
    2: None, # (!) real value is ''
    3: None, # (!) real value is ''
    4: 'type conversion error',
    5: 'overflow error',
}

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

