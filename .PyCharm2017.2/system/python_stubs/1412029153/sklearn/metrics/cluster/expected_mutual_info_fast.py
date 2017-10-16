# encoding: utf-8
# module sklearn.metrics.cluster.expected_mutual_info_fast
# from D:\ProgramData\Anaconda3\lib\site-packages\sklearn\metrics\cluster\expected_mutual_info_fast.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # D:\ProgramData\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def expected_mutual_information(*args, **kwargs): # real signature unknown
    """ Calculate the expected mutual information for two labelings. """
    pass

def gammaln(x): # reliably restored by inspect
    """
    Logarithm of the absolute value of the Gamma function for real inputs.
    
        Parameters
        ----------
        x : array-like
            Values on the real line at which to compute ``gammaln``
    
        Returns
        -------
        gammaln : ndarray
            Values of ``gammaln`` at x.
    
        See Also
        --------
        gammasgn : sign of the gamma function
        loggamma : principal branch of the logarithm of the gamma function
    
        Notes
        -----
        When used in conjunction with `gammasgn`, this function is useful
        for working in logspace on the real axis without having to deal with
        complex numbers, via the relation ``exp(gammaln(x)) = gammasgn(x)*gamma(x)``.
    
        Note that `gammaln` currently accepts complex-valued inputs, but it is not
        the same function as for real-valued inputs, and the branch is not
        well-defined --- using `gammaln` with complex is deprecated and will be
        disallowed in future Scipy versions.
    
        For complex-valued log-gamma, use `loggamma` instead of `gammaln`.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

