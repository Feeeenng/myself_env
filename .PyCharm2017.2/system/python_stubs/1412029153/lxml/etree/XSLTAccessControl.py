# encoding: utf-8
# module lxml.etree
# from D:\ProgramData\Anaconda3\lib\site-packages\lxml\etree.cp36-win_amd64.pyd
# by generator 1.145
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .object import object

class XSLTAccessControl(object):
    """
    XSLTAccessControl(self, read_file=True, write_file=True, create_dir=True, read_network=True, write_network=True)
    
        Access control for XSLT: reading/writing files, directories and
        network I/O.  Access to a type of resource is granted or denied by
        passing any of the following boolean keyword arguments.  All of
        them default to True to allow access.
    
        - read_file
        - write_file
        - create_dir
        - read_network
        - write_network
    
        For convenience, there is also a class member `DENY_ALL` that
        provides an XSLTAccessControl instance that is readily configured
        to deny everything, and a `DENY_WRITE` member that denies all
        write access but allows read access.
    
        See `XSLT`.
    """
    def __init__(self, read_file=True, write_file=True, create_dir=True, read_network=True, write_network=True): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The access control configuration as a map of options."""


    DENY_ALL = None # (!) real value is ''
    DENY_WRITE = None # (!) real value is ''
    __pyx_vtable__ = None # (!) real value is ''


