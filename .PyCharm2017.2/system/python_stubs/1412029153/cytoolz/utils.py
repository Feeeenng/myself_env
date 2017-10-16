# encoding: utf-8
# module cytoolz.utils
# from D:\ProgramData\Anaconda3\lib\site-packages\cytoolz\utils.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import os as os # D:\ProgramData\Anaconda3\lib\os.py
import cytoolz as cytoolz # D:\ProgramData\Anaconda3\lib\site-packages\cytoolz\__init__.py

# Variables with simple values

no_default = '__no__default__'

# functions

def consume(seq): # real signature unknown; restored from __doc__
    """
    consume(seq)
    
        Efficiently consume an iterable
    """
    pass

def include_dirs(): # real signature unknown; restored from __doc__
    """
    include_dirs()
     Return a list of directories containing the *.pxd files for ``cytoolz``
    
        Use this to include ``cytoolz`` in your own Cython project, which allows
        fast C bindinds to be imported such as ``from cytoolz cimport get``.
    
        Below is a minimal "setup.py" file using ``include_dirs``:
    
            from distutils.core import setup
            from distutils.extension import Extension
            from Cython.Distutils import build_ext
    
            import cytoolz.utils
    
            ext_modules=[
                Extension("mymodule",
                          ["mymodule.pyx"],
                          include_dirs=cytoolz.utils.include_dirs()
                         )
            ]
    
            setup(
              name = "mymodule",
              cmdclass = {"build_ext": build_ext},
              ext_modules = ext_modules
            )
    """
    pass

def raises(err, lamda): # real signature unknown; restored from __doc__
    """ raises(err, lamda) """
    pass

# no classes
# variables with complex values

__all__ = [
    'raises',
    'no_default',
    'include_dirs',
    'consume',
]

__loader__ = None # (!) real value is ''

__pyx_capi__ = {
    'consume': None, # (!) real value is ''
}

__spec__ = None # (!) real value is ''

__test__ = {}

