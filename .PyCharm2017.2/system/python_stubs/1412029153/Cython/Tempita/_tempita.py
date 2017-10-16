# encoding: utf-8
# module Cython.Tempita._tempita
# from D:\ProgramData\Anaconda3\lib\site-packages\Cython\Tempita\_tempita.cp36-win_amd64.pyd
# by generator 1.145
"""
A small templating language

This implements a small templating language.  This language implements
if/elif/else, for/continue/break, expressions, and blocks of Python
code.  The syntax is::

  {{any expression (function calls etc)}}
  {{any expression | filter}}
  {{for x in y}}...{{endfor}}
  {{if x}}x{{elif y}}y{{else}}z{{endif}}
  {{py:x=1}}
  {{py:
  def foo(bar):
      return 'baz'
  }}
  {{default var = default_value}}
  {{# comment}}

You use this with the ``Template`` class or the ``sub`` shortcut.
The ``Template`` class takes the template string and the name of
the template (for errors) and a default namespace.  Then (like
``string.Template``) you can call the ``tmpl.substitute(**kw)``
method to make a substitution (or ``tmpl.substitute(a_dict)``).

``sub(content, **kw)`` substitutes the template immediately.  You
can use ``__name='tmpl.html'`` to set the name of the template.

If there are syntax errors ``TemplateError`` will be raised.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import re as re # D:\ProgramData\Anaconda3\lib\re.py
import sys as sys # <module 'sys' (built-in)>
import cgi as cgi # D:\ProgramData\Anaconda3\lib\cgi.py
import os as os # D:\ProgramData\Anaconda3\lib\os.py
import tokenize as tokenize # D:\ProgramData\Anaconda3\lib\tokenize.py
from _io import StringIO


# Variables with simple values

_fill_command_usage = '%prog [OPTIONS] TEMPLATE arg=value\n\nUse py:arg=value to set a Python value; otherwise all values are\nstrings.\n'

# functions

def attr(*args, **kwargs): # real signature unknown
    pass

def coerce_text(v): # reliably restored by inspect
    # no doc
    pass

def Empty(*args, **kwargs): # real signature unknown
    pass

def fill_command(*args, **kwargs): # real signature unknown
    pass

def find_position(*args, **kwargs): # real signature unknown
    """ Given a string and index, return (line, column) """
    pass

def get_file_template(*args, **kwargs): # real signature unknown
    pass

def html_quote(*args, **kwargs): # real signature unknown
    pass

def isolate_expression(*args, **kwargs): # real signature unknown
    pass

def is_unicode(obj): # reliably restored by inspect
    # no doc
    pass

def lex(hey): # real signature unknown; restored from __doc__
    """
    Lex a string into chunks:
    
            >>> lex('hey')
            ['hey']
            >>> lex('hey {{you}}')
            ['hey ', ('you', (1, 7))]
            >>> lex('hey {{')
            Traceback (most recent call last):
                ...
            TemplateError: No }} to finish last expression at line 1 column 7
            >>> lex('hey }}')
            Traceback (most recent call last):
                ...
            TemplateError: }} outside expression at line 1 column 7
            >>> lex('hey {{ {{')
            Traceback (most recent call last):
                ...
            TemplateError: {{ inside expression at line 1 column 10
    """
    pass

def next(iterator, default=None): # real signature unknown; restored from __doc__
    """
    next(iterator[, default])
    
    Return the next item from the iterator. If default is given and the iterator
    is exhausted, it is returned instead of raising StopIteration.
    """
    pass

def parse(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Parses a string into a kind of AST
    
            >>> parse('{{x}}')
            [('expr', (1, 3), 'x')]
            >>> parse('foo')
            ['foo']
            >>> parse('{{if x}}test{{endif}}')
            [('cond', (1, 3), ('if', (1, 3), 'x', ['test']))]
            >>> parse('series->{{for x in y}}x={{x}}{{endfor}}')
            ['series->', ('for', (1, 11), ('x',), 'y', ['x=', ('expr', (1, 27), 'x')])]
            >>> parse('{{for x, y in z:}}{{continue}}{{endfor}}')
            [('for', (1, 3), ('x', 'y'), 'z', [('continue', (1, 21))])]
            >>> parse('{{py:x=1}}')
            [('py', (1, 3), 'x=1')]
            >>> parse('{{if x}}a{{elif y}}b{{else}}c{{endif}}')
            [('cond', (1, 3), ('if', (1, 3), 'x', ['a']), ('elif', (1, 12), 'y', ['b']), ('else', (1, 23), None, ['c']))]
    
        Some exceptions::
    
            >>> parse('{{continue}}')
            Traceback (most recent call last):
                ...
            TemplateError: continue outside of for loop at line 1 column 3
            >>> parse('{{if x}}foo')
            Traceback (most recent call last):
                ...
            TemplateError: No {{endif}} at line 1 column 3
            >>> parse('{{else}}')
            Traceback (most recent call last):
                ...
            TemplateError: else outside of an if block at line 1 column 3
            >>> parse('{{if x}}{{for x in y}}{{endif}}{{endfor}}')
            Traceback (most recent call last):
                ...
            TemplateError: Unexpected endif at line 1 column 25
            >>> parse('{{if}}{{endif}}')
            Traceback (most recent call last):
                ...
            TemplateError: if with no expression at line 1 column 3
            >>> parse('{{for x y}}{{endfor}}')
            Traceback (most recent call last):
                ...
            TemplateError: Bad for (no "in") in 'x y' at line 1 column 3
            >>> parse('{{py:x=1\ny=2}}')
            Traceback (most recent call last):
                ...
            TemplateError: Multi-line py blocks must start with a newline at line 1 column 3
    """
    pass

def parse_cond(*args, **kwargs): # real signature unknown
    pass

def parse_def(*args, **kwargs): # real signature unknown
    pass

def parse_default(*args, **kwargs): # real signature unknown
    pass

def parse_expr(*args, **kwargs): # real signature unknown
    pass

def parse_for(*args, **kwargs): # real signature unknown
    pass

def parse_inherit(*args, **kwargs): # real signature unknown
    pass

def parse_one_cond(*args, **kwargs): # real signature unknown
    pass

def parse_signature(*args, **kwargs): # real signature unknown
    pass

def paste_script_template_renderer(*args, **kwargs): # real signature unknown
    pass

def sub(*args, **kwargs): # real signature unknown
    pass

def sub_html(*args, **kwargs): # real signature unknown
    pass

def trim_lex(tokens): # real signature unknown; restored from __doc__
    """
    Takes a lexed set of tokens, and removes whitespace when there is
        a directive on a line by itself:
    
           >>> tokens = lex('{{if x}}\nx\n{{endif}}\ny', trim_whitespace=False)
           >>> tokens
           [('if x', (1, 3)), '\nx\n', ('endif', (3, 3)), '\ny']
           >>> trim_lex(tokens)
           [('if x', (1, 3)), 'x\n', ('endif', (3, 3)), 'y']
    """
    pass

def url(*args, **kwargs): # real signature unknown
    pass

def url_quote(string, safe=None, encoding=None, errors=None): # reliably restored by inspect
    """
    quote('abc def') -> 'abc%20def'
    
        Each part of a URL, e.g. the path info, the query, etc., has a
        different set of reserved characters that must be quoted.
    
        RFC 2396 Uniform Resource Identifiers (URI): Generic Syntax lists
        the following reserved characters.
    
        reserved    = ";" | "/" | "?" | ":" | "@" | "&" | "=" | "+" |
                      "$" | ","
    
        Each of these characters is reserved in some component of a URL,
        but not necessarily in all of them.
    
        By default, the quote function is intended for quoting the path
        section of a URL.  Thus, it will not encode '/'.  This character
        is reserved, but in typical usage the quote function is being
        called on a path where the existing slash characters are used as
        reserved characters.
    
        string and safe may be either str or bytes objects. encoding and errors
        must not be specified if string is a bytes object.
    
        The optional encoding and errors parameters specify how to deal with
        non-ASCII characters, as accepted by the str.encode method.
        By default, encoding='utf-8' (characters are encoded with UTF-8), and
        errors='strict' (unsupported characters raise a UnicodeEncodeError).
    """
    pass

# classes

class bunch(dict):
    # no doc
    def __getattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class bytes(object):
    """
    bytes(iterable_of_ints) -> bytes
    bytes(string, encoding[, errors]) -> bytes
    bytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer
    bytes(int) -> bytes object of size given by the parameter initialized with null bytes
    bytes() -> empty bytes object
    
    Construct an immutable array of bytes from:
      - an iterable yielding integers in range(256)
      - a text string encoded using the specified encoding
      - any object implementing the buffer API.
      - an integer
    """
    def capitalize(self): # real signature unknown; restored from __doc__
        """
        B.capitalize() -> copy of B
        
        Return a copy of B with only its first character capitalized (ASCII)
        and the rest lower-cased.
        """
        pass

    def center(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        B.center(width[, fillchar]) -> copy of B
        
        Return B centered in a string of length width.  Padding is
        done using the specified fill character (default is a space).
        """
        pass

    def count(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.count(sub[, start[, end]]) -> int
        
        Return the number of non-overlapping occurrences of subsection sub in
        bytes B[start:end].  Optional arguments start and end are interpreted
        as in slice notation.
        """
        return 0

    def decode(self, *args, **kwargs): # real signature unknown
        """
        Decode the bytes using the codec registered for encoding.
        
          encoding
            The encoding with which to decode the bytes.
          errors
            The error handling scheme to use for the handling of decoding errors.
            The default is 'strict' meaning that decoding errors raise a
            UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
            as well as any other name registered with codecs.register_error that
            can handle UnicodeDecodeErrors.
        """
        pass

    def endswith(self, suffix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.endswith(suffix[, start[, end]]) -> bool
        
        Return True if B ends with the specified suffix, False otherwise.
        With optional start, test B beginning at that position.
        With optional end, stop comparing B at that position.
        suffix can also be a tuple of bytes to try.
        """
        return False

    def expandtabs(self, tabsize=8): # real signature unknown; restored from __doc__
        """
        B.expandtabs(tabsize=8) -> copy of B
        
        Return a copy of B where all tab characters are expanded using spaces.
        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        pass

    def find(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.find(sub[, start[, end]]) -> int
        
        Return the lowest index in B where subsection sub is found,
        such that sub is contained within B[start,end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    @classmethod
    def fromhex(cls, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Create a bytes object from a string of hexadecimal numbers.
        
        Spaces between two numbers are accepted.
        Example: bytes.fromhex('B9 01EF') -> b'\\xb9\\x01\\xef'.
        """
        pass

    def hex(self): # real signature unknown; restored from __doc__
        """
        B.hex() -> string
        
        Create a string of hexadecimal numbers from a bytes object.
        Example: b'\xb9\x01\xef'.hex() -> 'b901ef'.
        """
        return ""

    def index(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.index(sub[, start[, end]]) -> int
        
        Return the lowest index in B where subsection sub is found,
        such that sub is contained within B[start,end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the subsection is not found.
        """
        return 0

    def isalnum(self): # real signature unknown; restored from __doc__
        """
        B.isalnum() -> bool
        
        Return True if all characters in B are alphanumeric
        and there is at least one character in B, False otherwise.
        """
        return False

    def isalpha(self): # real signature unknown; restored from __doc__
        """
        B.isalpha() -> bool
        
        Return True if all characters in B are alphabetic
        and there is at least one character in B, False otherwise.
        """
        return False

    def isdigit(self): # real signature unknown; restored from __doc__
        """
        B.isdigit() -> bool
        
        Return True if all characters in B are digits
        and there is at least one character in B, False otherwise.
        """
        return False

    def islower(self): # real signature unknown; restored from __doc__
        """
        B.islower() -> bool
        
        Return True if all cased characters in B are lowercase and there is
        at least one cased character in B, False otherwise.
        """
        return False

    def isspace(self): # real signature unknown; restored from __doc__
        """
        B.isspace() -> bool
        
        Return True if all characters in B are whitespace
        and there is at least one character in B, False otherwise.
        """
        return False

    def istitle(self): # real signature unknown; restored from __doc__
        """
        B.istitle() -> bool
        
        Return True if B is a titlecased string and there is at least one
        character in B, i.e. uppercase characters may only follow uncased
        characters and lowercase characters only cased ones. Return False
        otherwise.
        """
        return False

    def isupper(self): # real signature unknown; restored from __doc__
        """
        B.isupper() -> bool
        
        Return True if all cased characters in B are uppercase and there is
        at least one cased character in B, False otherwise.
        """
        return False

    def join(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Concatenate any number of bytes objects.
        
        The bytes whose method is called is inserted in between each pair.
        
        The result is returned as a new bytes object.
        
        Example: b'.'.join([b'ab', b'pq', b'rs']) -> b'ab.pq.rs'.
        """
        pass

    def ljust(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        B.ljust(width[, fillchar]) -> copy of B
        
        Return B left justified in a string of length width. Padding is
        done using the specified fill character (default is a space).
        """
        pass

    def lower(self): # real signature unknown; restored from __doc__
        """
        B.lower() -> copy of B
        
        Return a copy of B with all ASCII characters converted to lowercase.
        """
        pass

    def lstrip(self, *args, **kwargs): # real signature unknown
        """
        Strip leading bytes contained in the argument.
        
        If the argument is omitted or None, strip leading  ASCII whitespace.
        """
        pass

    def maketrans(self, *args, **kwargs): # real signature unknown
        """
        Return a translation table useable for the bytes or bytearray translate method.
        
        The returned table will be one where each byte in frm is mapped to the byte at
        the same position in to.
        
        The bytes objects frm and to must be of the same length.
        """
        pass

    def partition(self, *args, **kwargs): # real signature unknown
        """
        Partition the bytes into three parts using the given separator.
        
        This will search for the separator sep in the bytes. If the separator is found,
        returns a 3-tuple containing the part before the separator, the separator
        itself, and the part after it.
        
        If the separator is not found, returns a 3-tuple containing the original bytes
        object and two empty bytes objects.
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """
        Return a copy with all occurrences of substring old replaced by new.
        
          count
            Maximum number of occurrences to replace.
            -1 (the default value) means replace all occurrences.
        
        If the optional argument count is given, only the first count occurrences are
        replaced.
        """
        pass

    def rfind(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.rfind(sub[, start[, end]]) -> int
        
        Return the highest index in B where subsection sub is found,
        such that sub is contained within B[start,end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def rindex(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.rindex(sub[, start[, end]]) -> int
        
        Return the highest index in B where subsection sub is found,
        such that sub is contained within B[start,end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raise ValueError when the subsection is not found.
        """
        return 0

    def rjust(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        B.rjust(width[, fillchar]) -> copy of B
        
        Return B right justified in a string of length width. Padding is
        done using the specified fill character (default is a space)
        """
        pass

    def rpartition(self, *args, **kwargs): # real signature unknown
        """
        Partition the bytes into three parts using the given separator.
        
        This will search for the separator sep in the bytes, starting and the end. If
        the separator is found, returns a 3-tuple containing the part before the
        separator, the separator itself, and the part after it.
        
        If the separator is not found, returns a 3-tuple containing two empty bytes
        objects and the original bytes object.
        """
        pass

    def rsplit(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the sections in the bytes, using sep as the delimiter.
        
          sep
            The delimiter according which to split the bytes.
            None (the default value) means split on ASCII whitespace characters
            (space, tab, return, newline, formfeed, vertical tab).
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        
        Splitting is done starting at the end of the bytes and working to the front.
        """
        pass

    def rstrip(self, *args, **kwargs): # real signature unknown
        """
        Strip trailing bytes contained in the argument.
        
        If the argument is omitted or None, strip trailing ASCII whitespace.
        """
        pass

    def split(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the sections in the bytes, using sep as the delimiter.
        
          sep
            The delimiter according which to split the bytes.
            None (the default value) means split on ASCII whitespace characters
            (space, tab, return, newline, formfeed, vertical tab).
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        """
        pass

    def splitlines(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the lines in the bytes, breaking at line boundaries.
        
        Line breaks are not included in the resulting list unless keepends is given and
        true.
        """
        pass

    def startswith(self, prefix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        B.startswith(prefix[, start[, end]]) -> bool
        
        Return True if B starts with the specified prefix, False otherwise.
        With optional start, test B beginning at that position.
        With optional end, stop comparing B at that position.
        prefix can also be a tuple of bytes to try.
        """
        return False

    def strip(self, *args, **kwargs): # real signature unknown
        """
        Strip leading and trailing bytes contained in the argument.
        
        If the argument is omitted or None, strip leading and trailing ASCII whitespace.
        """
        pass

    def swapcase(self): # real signature unknown; restored from __doc__
        """
        B.swapcase() -> copy of B
        
        Return a copy of B with uppercase ASCII characters converted
        to lowercase ASCII and vice versa.
        """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """
        B.title() -> copy of B
        
        Return a titlecased version of B, i.e. ASCII words start with uppercase
        characters, all remaining cased characters have lowercase.
        """
        pass

    def translate(self, *args, **kwargs): # real signature unknown
        """
        Return a copy with each character mapped by the given translation table.
        
          table
            Translation table, which must be a bytes object of length 256.
        
        All characters occurring in the optional argument delete are removed.
        The remaining characters are mapped through the given translation table.
        """
        pass

    def upper(self): # real signature unknown; restored from __doc__
        """
        B.upper() -> copy of B
        
        Return a copy of B with all ASCII characters converted to uppercase.
        """
        pass

    def zfill(self, width): # real signature unknown; restored from __doc__
        """
        B.zfill(width) -> copy of B
        
        Pad a numeric string B with zeros on the left, to fill a field
        of the specified width.  B is never truncated.
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
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

    def __init__(self, iterable_of_ints): # real signature unknown; restored from __doc__
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

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class html(object):
    # no doc
    def __html__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class Template(object):
    # no doc
    @classmethod
    def from_filename(cls, *args, **kwargs): # real signature unknown
        pass

    def substitute(self, *args, **kwargs): # real signature unknown
        pass

    def _add_line_info(self, *args, **kwargs): # real signature unknown
        pass

    def _eval(self, *args, **kwargs): # real signature unknown
        pass

    def _exec(self, *args, **kwargs): # real signature unknown
        pass

    def _interpret(self, *args, **kwargs): # real signature unknown
        pass

    def _interpret_code(self, *args, **kwargs): # real signature unknown
        pass

    def _interpret_codes(self, *args, **kwargs): # real signature unknown
        pass

    def _interpret_for(self, *args, **kwargs): # real signature unknown
        pass

    def _interpret_if(self, *args, **kwargs): # real signature unknown
        pass

    def _interpret_inherit(self, *args, **kwargs): # real signature unknown
        pass

    def _repr(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    default_encoding = 'utf8'
    default_inherit = None
    default_namespace = {
        'end_braces': '}}',
        'looper': None, # (!) forward: looper, real value is ''
        'start_braces': '{{',
    }
    __dict__ = None # (!) real value is ''


class HTMLTemplate(Template):
    # no doc
    def _repr(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    default_namespace = {
        'attr': None, # (!) forward: attr, real value is ''
        'end_braces': '}}',
        'html': html,
        'html_quote': None, # (!) forward: html_quote, real value is ''
        'looper': None, # (!) forward: looper, real value is ''
        'start_braces': '{{',
        'url': None, # (!) forward: url, real value is ''
    }


class looper(object):
    """
    Helper for looping (particularly in templates)
    
        Use this like::
    
            for loop, item in looper(seq):
                if loop.first:
                    ...
    """
    def __init__(self, seq): # reliably restored by inspect
        # no doc
        pass

    def __iter__(self): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class TemplateDef(object):
    # no doc
    def _parse_signature(self, *args, **kwargs): # real signature unknown
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        pass

    def __get__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class TemplateError(Exception):
    """ Exception raised while parsing a template """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class TemplateObject(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class TemplateObjectGetter(object):
    # no doc
    def __getattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class unicode_(object):
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


class _TemplateBreak(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class _TemplateContinue(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

basestring_ = (
    bytes,
    str,
)

in_re = None # (!) real value is ''

lead_whitespace_re = None # (!) real value is ''

single_statements = [
    'else',
    'endif',
    'endfor',
    'enddef',
    'continue',
    'break',
]

statement_re = None # (!) real value is ''

trail_whitespace_re = None # (!) real value is ''

var_re = None # (!) real value is ''

__all__ = [
    'TemplateError',
    'Template',
    'sub',
    'HTMLTemplate',
    'sub_html',
    'html',
    'bunch',
]

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {
    'lex (line 629)': "\n    Lex a string into chunks:\n\n        >>> lex('hey')\n        ['hey']\n        >>> lex('hey {{you}}')\n        ['hey ', ('you', (1, 7))]\n        >>> lex('hey {{')\n        Traceback (most recent call last):\n            ...\n        TemplateError: No }} to finish last expression at line 1 column 7\n        >>> lex('hey }}')\n        Traceback (most recent call last):\n            ...\n        TemplateError: }} outside expression at line 1 column 7\n        >>> lex('hey {{ {{')\n        Traceback (most recent call last):\n            ...\n        TemplateError: {{ inside expression at line 1 column 10\n\n    ",
    'parse (line 766)': '\n    Parses a string into a kind of AST\n\n        >>> parse(\'{{x}}\')\n        [(\'expr\', (1, 3), \'x\')]\n        >>> parse(\'foo\')\n        [\'foo\']\n        >>> parse(\'{{if x}}test{{endif}}\')\n        [(\'cond\', (1, 3), (\'if\', (1, 3), \'x\', [\'test\']))]\n        >>> parse(\'series->{{for x in y}}x={{x}}{{endfor}}\')\n        [\'series->\', (\'for\', (1, 11), (\'x\',), \'y\', [\'x=\', (\'expr\', (1, 27), \'x\')])]\n        >>> parse(\'{{for x, y in z:}}{{continue}}{{endfor}}\')\n        [(\'for\', (1, 3), (\'x\', \'y\'), \'z\', [(\'continue\', (1, 21))])]\n        >>> parse(\'{{py:x=1}}\')\n        [(\'py\', (1, 3), \'x=1\')]\n        >>> parse(\'{{if x}}a{{elif y}}b{{else}}c{{endif}}\')\n        [(\'cond\', (1, 3), (\'if\', (1, 3), \'x\', [\'a\']), (\'elif\', (1, 12), \'y\', [\'b\']), (\'else\', (1, 23), None, [\'c\']))]\n\n    Some exceptions::\n\n        >>> parse(\'{{continue}}\')\n        Traceback (most recent call last):\n            ...\n        TemplateError: continue outside of for loop at line 1 column 3\n        >>> parse(\'{{if x}}foo\')\n        Traceback (most recent call last):\n            ...\n        TemplateError: No {{endif}} at line 1 column 3\n        >>> parse(\'{{else}}\')\n        Traceback (most recent call last):\n            ...\n        TemplateError: else outside of an if block at line 1 column 3\n        >>> parse(\'{{if x}}{{for x in y}}{{endif}}{{endfor}}\')\n        Traceback (most recent call last):\n            ...\n        TemplateError: Unexpected endif at line 1 column 25\n        >>> parse(\'{{if}}{{endif}}\')\n        Traceback (most recent call last):\n            ...\n        TemplateError: if with no expression at line 1 column 3\n        >>> parse(\'{{for x y}}{{endfor}}\')\n        Traceback (most recent call last):\n            ...\n        TemplateError: Bad for (no "in") in \'x y\' at line 1 column 3\n        >>> parse(\'{{py:x=1\\ny=2}}\')\n        Traceback (most recent call last):\n            ...\n        TemplateError: Multi-line py blocks must start with a newline at line 1 column 3\n    ',
    'trim_lex (line 698)': "\n    Takes a lexed set of tokens, and removes whitespace when there is\n    a directive on a line by itself:\n\n       >>> tokens = lex('{{if x}}\\nx\\n{{endif}}\\ny', trim_whitespace=False)\n       >>> tokens\n       [('if x', (1, 3)), '\\nx\\n', ('endif', (3, 3)), '\\ny']\n       >>> trim_lex(tokens)\n       [('if x', (1, 3)), 'x\\n', ('endif', (3, 3)), 'y']\n    ",
}

