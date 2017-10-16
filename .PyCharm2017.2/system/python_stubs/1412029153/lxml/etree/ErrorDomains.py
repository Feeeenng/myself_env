# encoding: utf-8
# module lxml.etree
# from D:\ProgramData\Anaconda3\lib\site-packages\lxml\etree.cp36-win_amd64.pyd
# by generator 1.145
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .object import object

class ErrorDomains(object):
    """ Libxml2 error domains """
    def _getName(self, *args, **kwargs): # real signature unknown
        """ D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    BUFFER = 29
    C14N = 21
    CATALOG = 20
    CHECK = 24
    DATATYPE = 15
    DTD = 4
    FTP = 9
    HTML = 5
    HTTP = 10
    I18N = 27
    IO = 8
    MEMORY = 6
    MODULE = 26
    NAMESPACE = 3
    NONE = 0
    OUTPUT = 7
    PARSER = 1
    REGEXP = 14
    RELAXNGP = 18
    RELAXNGV = 19
    SCHEMASP = 16
    SCHEMASV = 17
    SCHEMATRONV = 28
    TREE = 2
    URI = 30
    VALID = 23
    WRITER = 25
    XINCLUDE = 11
    XPATH = 12
    XPOINTER = 13
    XSLT = 22
    _names = {
        0: 'NONE',
        1: 'PARSER',
        2: 'TREE',
        3: 'NAMESPACE',
        4: 'DTD',
        5: 'HTML',
        6: 'MEMORY',
        7: 'OUTPUT',
        8: 'IO',
        9: 'FTP',
        10: 'HTTP',
        11: 'XINCLUDE',
        12: 'XPATH',
        13: 'XPOINTER',
        14: 'REGEXP',
        15: 'DATATYPE',
        16: 'SCHEMASP',
        17: 'SCHEMASV',
        18: 'RELAXNGP',
        19: 'RELAXNGV',
        20: 'CATALOG',
        21: 'C14N',
        22: 'XSLT',
        23: 'VALID',
        24: 'CHECK',
        25: 'WRITER',
        26: 'MODULE',
        27: 'I18N',
        28: 'SCHEMATRONV',
        29: 'BUFFER',
        30: 'URI',
    }
    __dict__ = None # (!) real value is ''


