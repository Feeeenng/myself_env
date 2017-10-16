# encoding: utf-8
# module skimage.transform._radon_transform
# from D:\ProgramData\Anaconda3\lib\site-packages\skimage\transform\_radon_transform.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # D:\ProgramData\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def bilinear_ray_sum(*args, **kwargs): # real signature unknown
    """
    Compute the projection of an image along a ray.
    
        Parameters
        ----------
        image : 2D array, dtype=float
            Image to project.
        theta : float
            Angle of the projection
        ray_position : float
            Position of the ray within the projection
    
        Returns
        -------
        projected_value : float
            Ray sum along the projection
        norm_of_weights :
            A measure of how long the ray's path through the reconstruction
            circle was
    """
    pass

def bilinear_ray_update(*args, **kwargs): # real signature unknown
    """
    Compute the update along a ray using bilinear interpolation.
    
        Parameters
        ----------
        image : 2D array, dtype=float
            Current reconstruction estimate.
        image_update : 2D array, dtype=float
            Array of same shape as ``image``. Updates will be added to this array.
        theta : float
            Angle of the projection.
        ray_position : float
            Position of the ray within the projection.
        projected_value : float
            Projected value (from the sinogram).
    
        Returns
        -------
        deviation :
            Deviation before updating the image.
    """
    pass

def sart_projection_update(*args, **kwargs): # real signature unknown
    """
    Compute update to a reconstruction estimate from a single projection
        using bilinear interpolation.
    
        Parameters
        ----------
        image : 2D array, dtype=float
            Current reconstruction estimate
        theta : float
            Angle of the projection
        projection : 1D array, dtype=float
            Projected values, taken from the sinogram
        projection_shift : float
            Shift the position of the projection by this many pixels before
            using it to compute an update to the reconstruction estimate
    
        Returns
        -------
        image_update : 2D array, dtype=float
            Array of same shape as ``image`` containing updates that should be
            added to ``image`` to improve the reconstruction estimate
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

