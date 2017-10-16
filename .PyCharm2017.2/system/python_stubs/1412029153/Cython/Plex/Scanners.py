# encoding: utf-8
# module Cython.Plex.Scanners
# from D:\ProgramData\Anaconda3\lib\site-packages\Cython\Plex\Scanners.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import Cython.Plex.Errors as Errors # D:\ProgramData\Anaconda3\lib\site-packages\Cython\Plex\Errors.py

# functions

def __pyx_unpickle_Scanner(*args, **kwargs): # real signature unknown
    pass

def __reduce_cython__(*args, **kwargs): # real signature unknown
    pass

def __setstate_cython__(*args, **kwargs): # real signature unknown
    pass

# classes

class Scanner(object):
    """
    A Scanner is used to read tokens from a stream of characters
        using the token set specified by a Plex.Lexicon.
    
        Constructor:
    
          Scanner(lexicon, stream, name = '')
    
            See the docstring of the __init__ method for details.
    
        Methods:
    
          See the docstrings of the individual methods for more
          information.
    
          read() --> (value, text)
            Reads the next lexical token from the stream.
    
          position() --> (name, line, col)
            Returns the position of the last token read using the
            read() method.
    
          begin(state_name)
            Causes scanner to change state.
    
          produce(value [, text])
            Causes return of a token value to the caller of the
            Scanner.
    """
    def eof(self, *args, **kwargs): # real signature unknown
        """
        Override this method if you want something to be done at
                end of file.
        """
        pass

    def get_position(self, *args, **kwargs): # real signature unknown
        """ Python accessible wrapper around position(), only for error reporting. """
        pass

    def read(self, *args, **kwargs): # real signature unknown
        """
        Read the next lexical token from the stream and return a
                tuple (value, text), where |value| is the value associated with
                the token as specified by the Lexicon, and |text| is the actual
                string read from the stream. Returns (None, '') on end of file.
        """
        pass

    def __init__(self, lexicon, stream, name=''): # real signature unknown; restored from __doc__
        """
        Scanner(lexicon, stream, name = '')
        
                  |lexicon| is a Plex.Lexicon instance specifying the lexical tokens
                  to be recognised.
        
                  |stream| can be a file object or anything which implements a
                  compatible read() method.
        
                  |name| is optional, and may be the name of the file being
                  scanned or any other identifying string.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    buf_start_pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cur_char = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cur_line = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cur_line_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cur_pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    input_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lexicon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next_pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    queue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_col = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_line = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    trace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}
