# encoding: utf-8
# module skimage.restoration._nl_means_denoising
# from D:\ProgramData\Anaconda3\lib\site-packages\skimage\restoration\_nl_means_denoising.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # D:\ProgramData\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def _fast_nl_means_denoising_2d(*args, **kwargs): # real signature unknown
    """
    Perform fast non-local means denoising on 2-D array, with the outer
        loop on patch shifts in order to reduce the number of operations.
    
        Parameters
        ----------
        image : ndarray
            2-D input data to be denoised, grayscale or RGB.
        s : int, optional
            Size of patches used for denoising.
        d : int, optional
            Maximal distance in pixels where to search patches used for denoising.
        h : float, optional
            Cut-off distance (in gray levels). The higher h, the more permissive
            one is in accepting patches.
    
        Returns
        -------
        result : ndarray
            Denoised image, of same shape as input image.
    
        References
        ----------
        J. Darbon, A. Cunha, T.F. Chan, S. Osher, and G.J. Jensen, Fast
        nonlocal filtering applied to electron cryomicroscopy, in 5th IEEE
        International Symposium on Biomedical Imaging: From Nano to Macro,
        2008, pp. 1331-1334.
    
        Jacques Froment. Parameter-Free Fast Pixelwise Non-Local Means
        Denoising. Image Processing On Line, 2014, vol. 4, p. 300-326.
    """
    pass

def _fast_nl_means_denoising_3d(*args, **kwargs): # real signature unknown
    """
    Perform fast non-local means denoising on 3-D array, with the outer
        loop on patch shifts in order to reduce the number of operations.
    
        Parameters
        ----------
        image : ndarray
            3-D input data to be denoised.
        s : int, optional
            Size of patches used for denoising.
        d : int, optional
            Maximal distance in pixels where to search patches used for denoising.
        h : float, optional
            cut-off distance (in gray levels). The higher h, the more permissive
            one is in accepting patches.
    
        Returns
        -------
        result : ndarray
            Denoised image, of same shape as input image.
    
        References
        ----------
        J. Darbon, A. Cunha, T.F. Chan, S. Osher, and G.J. Jensen, Fast
        nonlocal filtering applied to electron cryomicroscopy, in 5th IEEE
        International Symposium on Biomedical Imaging: From Nano to Macro,
        2008, pp. 1331-1334.
    
        Jacques Froment. Parameter-Free Fast Pixelwise Non-Local Means
        Denoising. Image Processing On Line, 2014, vol. 4, p. 300-326.
    """
    pass

def _nl_means_denoising_2d(*args, **kwargs): # real signature unknown
    """
    Perform non-local means denoising on 2-D RGB image
    
        Parameters
        ----------
        image : ndarray
            Input RGB image to be denoised
        s : int, optional
            Size of patches used for denoising
        d : int, optional
            Maximal distance in pixels where to search patches used for denoising
        h : float, optional
            Cut-off distance (in gray levels). The higher h, the more permissive
            one is in accepting patches.
    
        Returns
        -------
        result : ndarray
            Denoised image, of same shape as input image.
    """
    pass

def _nl_means_denoising_3d(*args, **kwargs): # real signature unknown
    """
    Perform non-local means denoising on 3-D array
    
        Parameters
        ----------
        image : ndarray
            Input data to be denoised.
        s : int, optional
            Size of patches used for denoising.
        d : int, optional
            Maximal distance in pixels where to search patches used for denoising.
        h : float, optional
            Cut-off distance (in gray levels).
    
        Returns
        -------
        result : ndarray
            Denoised image, of same shape as input image.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

