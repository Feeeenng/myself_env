# encoding: utf-8
# module lxml.etree
# from D:\ProgramData\Anaconda3\lib\site-packages\lxml\etree.cp36-win_amd64.pyd
# by generator 1.145
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .ParseError import ParseError

class XMLSyntaxError(ParseError):
    """ Syntax error while parsing an XML document. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

