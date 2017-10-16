# encoding: utf-8
# module sklearn.manifold._utils
# from D:\ProgramData\Anaconda3\lib\site-packages\sklearn\manifold\_utils.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # D:\ProgramData\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def _binary_search_perplexity(*args, **kwargs): # real signature unknown
    """
    Binary search for sigmas of conditional Gaussians.
    
        This approximation reduces the computational complexity from O(N^2) to
        O(uN). See the exact method '_binary_search_perplexity' for more details.
    
        Parameters
        ----------
        affinities : array-like, shape (n_samples, k)
            Distances between training samples and its k nearest neighbors.
    
        neighbors : array-like, shape (n_samples, k) or None
            Each row contains the indices to the k nearest neigbors. If this
            array is None, then the perplexity is estimated over all data
            not just the nearest neighbors.
    
        desired_perplexity : float
            Desired perplexity (2^entropy) of the conditional Gaussians.
    
        verbose : int
            Verbosity level.
    
        Returns
        -------
        P : array, shape (n_samples, n_samples)
            Probabilities of conditional Gaussian distributions p_i|j.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

