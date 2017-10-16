# encoding: utf-8
# module skimage.restoration._denoise_cy
# from D:\ProgramData\Anaconda3\lib\site-packages\skimage\restoration\_denoise_cy.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # D:\ProgramData\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def img_as_float(image, force_copy=False): # reliably restored by inspect
    """
    Convert an image to double-precision (64-bit) floating point format.
    
        Parameters
        ----------
        image : ndarray
            Input image.
        force_copy : bool, optional
            Force a copy of the data, irrespective of its current dtype.
    
        Returns
        -------
        out : ndarray of float64
            Output image.
    
        Notes
        -----
        The range of a floating point image is [0.0, 1.0] or [-1.0, 1.0] when
        converting from unsigned or signed datatypes, respectively.
        If the input image has a float type, intensity values are not modified
        and can be outside the ranges [0.0, 1.0] or [-1.0, 1.0].
    """
    pass

def _denoise_bilateral(*args, **kwargs): # real signature unknown
    pass

def _denoise_tv_bregman(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

