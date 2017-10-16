# encoding: utf-8
# module skimage.transform._seam_carving
# from D:\ProgramData\Anaconda3\lib\site-packages\skimage\transform\_seam_carving.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # D:\ProgramData\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def _seam_carve_v(*args, **kwargs): # real signature unknown
    """
    Carve vertical seams off an image.
    
        Carves out vertical seams from an image while using the given energy map to
        decide the importance of each pixel.[1]_
    
        Parameters
        ----------
        img : (M, N) or (M, N, 3) ndarray
            Input image whose vertical seams are to be removed.
        energy_map : (M, N) ndarray
            Cost array denoting importance of each pixel. The algorithm will try to
            retain high valued pixels.
        iters : int
            Number of vertical seams to be removed.
        border : int, optional
            The number of pixels in the right, left and bottom end of the image
            to be excluded from being considered for a seam. This is important as
            certain filters just ignore image boundaries and set them to `0`.
            By default border is set to `1`.
    
        Returns
        -------
        image : (M, N - iters, 3) ndarray of float
            The cropped image with the vertical seams removed.
    
        References
        ----------
        .. [1] Shai Avidan and Ariel Shamir
               "Seam Carving for Content-Aware Image Resizing"
               http://www.cs.jhu.edu/~misha/ReadingSeminar/Papers/Avidan07.pdf
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

