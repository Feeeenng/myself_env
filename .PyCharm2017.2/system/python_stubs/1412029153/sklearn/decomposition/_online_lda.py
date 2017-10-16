# encoding: utf-8
# module sklearn.decomposition._online_lda
# from D:\ProgramData\Anaconda3\lib\site-packages\sklearn\decomposition\_online_lda.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # D:\ProgramData\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def mean_change(*args, **kwargs): # real signature unknown
    """
    Calculate the mean difference between two arrays.
    
        Equivalent to np.abs(arr_1 - arr2).mean().
    """
    pass

def _dirichlet_expectation_1d(*args, **kwargs): # real signature unknown
    """
    Dirichlet expectation for a single sample:
            exp(E[log(theta)]) for theta ~ Dir(doc_topic)
        after adding doc_topic_prior to doc_topic, in-place.
    
        Equivalent to
            doc_topic += doc_topic_prior
            out[:] = np.exp(psi(doc_topic) - psi(np.sum(doc_topic)))
    """
    pass

def _dirichlet_expectation_2d(*args, **kwargs): # real signature unknown
    """
    Dirichlet expectation for multiple samples:
        E[log(theta)] for theta ~ Dir(arr).
    
        Equivalent to psi(arr) - psi(np.sum(arr, axis=1))[:, np.newaxis].
    
        Note that unlike _dirichlet_expectation_1d, this function doesn't compute
        the exp and doesn't add in the prior.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

