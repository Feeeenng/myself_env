# encoding: utf-8
# module sklearn.neighbors.quad_tree
# from D:\ProgramData\Anaconda3\lib\site-packages\sklearn\neighbors\quad_tree.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # D:\ProgramData\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def check_array(array, accept_sparse=False, dtype=None, order=None, copy=False, force_all_finite=True, ensure_2d=True, allow_nd=False, ensure_min_samples=1, ensure_min_features=1, warn_on_dtype=False, estimator=None): # reliably restored by inspect
    """
    Input validation on an array, list, sparse matrix or similar.
    
        By default, the input is converted to an at least 2D numpy array.
        If the dtype of the array is object, attempt converting to float,
        raising on failure.
    
        Parameters
        ----------
        array : object
            Input object to check / convert.
    
        accept_sparse : string, boolean or list/tuple of strings (default=False)
            String[s] representing allowed sparse matrix formats, such as 'csc',
            'csr', etc. If the input is sparse but not in the allowed format,
            it will be converted to the first listed format. True allows the input
            to be any format. False means that a sparse matrix input will
            raise an error.
    
            .. deprecated:: 0.19
               Passing 'None' to parameter ``accept_sparse`` in methods is
               deprecated in version 0.19 "and will be removed in 0.21. Use
               ``accept_sparse=False`` instead.
    
        dtype : string, type, list of types or None (default="numeric")
            Data type of result. If None, the dtype of the input is preserved.
            If "numeric", dtype is preserved unless array.dtype is object.
            If dtype is a list of types, conversion on the first type is only
            performed if the dtype of the input is not in the list.
    
        order : 'F', 'C' or None (default=None)
            Whether an array will be forced to be fortran or c-style.
            When order is None (default), then if copy=False, nothing is ensured
            about the memory layout of the output array; otherwise (copy=True)
            the memory layout of the returned array is kept as close as possible
            to the original array.
    
        copy : boolean (default=False)
            Whether a forced copy will be triggered. If copy=False, a copy might
            be triggered by a conversion.
    
        force_all_finite : boolean (default=True)
            Whether to raise an error on np.inf and np.nan in X.
    
        ensure_2d : boolean (default=True)
            Whether to raise a value error if X is not 2d.
    
        allow_nd : boolean (default=False)
            Whether to allow X.ndim > 2.
    
        ensure_min_samples : int (default=1)
            Make sure that the array has a minimum number of samples in its first
            axis (rows for a 2D array). Setting to 0 disables this check.
    
        ensure_min_features : int (default=1)
            Make sure that the 2D array has some minimum number of features
            (columns). The default value of 1 rejects empty datasets.
            This check is only enforced when the input data has effectively 2
            dimensions or is originally 1D and ``ensure_2d`` is True. Setting to 0
            disables this check.
    
        warn_on_dtype : boolean (default=False)
            Raise DataConversionWarning if the dtype of the input data structure
            does not match the requested dtype, causing a memory copy.
    
        estimator : str or estimator instance (default=None)
            If passed, include the name of the estimator in warning messages.
    
        Returns
        -------
        X_converted : object
            The converted and validated X.
    """
    pass

# classes

class _QuadTree(object):
    """
    Array-based representation of a QuadTree.
    
        This class is currently working for indexing 2D data (regular QuadTree) and
        for indexing 3D data (OcTree). It is planned to split the 2 implementations
        using `Cython.Tempita` to save some memory for QuadTree.
    
        Note that this code is currently internally used only by the Barnes-Hut
        method in `sklearn.manifold.TSNE`. It is planned to be refactored and
        generalized in the future to be compatible with nearest neighbors API of
        `sklearn.neighbors` with 2D and 3D data.
    """
    def build_tree(self, *args, **kwargs): # real signature unknown
        """ Build a tree from an arary of points X. """
        pass

    def get_cell(self, *args, **kwargs): # real signature unknown
        """
        return the id of the cell containing the query point or raise 
                ValueError if the point is not in the tree
        """
        pass

    def test_summarize(self, *args, **kwargs): # real signature unknown
        pass

    def _check_coherence(self, *args, **kwargs): # real signature unknown
        """
        Check the coherence of the cells of the tree.
        
                Check that the info stored in each cell is compatible with the info
                stored in descendent and sibling cells. Raise a ValueError if this
                fails.
        """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        """ Getstate re-implementation, for pickling. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Reduce re-implementation, for pickling. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Setstate re-implementation, for unpickling. """
        pass

    capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cell_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cumulative_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leafs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_dimensions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    verbose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


# variables with complex values

CELL_DTYPE = None # (!) real value is ''

__loader__ = None # (!) real value is ''

__pyx_capi__ = {
    'EPSILON': None, # (!) real value is ''
}

__spec__ = None # (!) real value is ''

__test__ = {}

