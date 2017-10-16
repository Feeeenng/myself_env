# encoding: utf-8
# module lxml.etree
# from D:\ProgramData\Anaconda3\lib\site-packages\lxml\etree.cp36-win_amd64.pyd
# by generator 1.145
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .FallbackElementClassLookup import FallbackElementClassLookup

class ElementNamespaceClassLookup(FallbackElementClassLookup):
    """
    ElementNamespaceClassLookup(self, fallback=None)
    
        Element class lookup scheme that searches the Element class in the
        Namespace registry.
    """
    def get_namespace(self, ns_uri): # real signature unknown; restored from __doc__
        """
        get_namespace(self, ns_uri)
        
                Retrieve the namespace object associated with the given URI.
                Pass None for the empty namespace.
        
                Creates a new namespace object if it does not yet exist.
        """
        pass

    def __init__(self, fallback=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


