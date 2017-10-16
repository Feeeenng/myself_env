# encoding: utf-8
# module scipy.sparse.csgraph._shortest_path
# from D:\ProgramData\Anaconda3\lib\site-packages\scipy\sparse\csgraph\_shortest_path.cp36-win_amd64.pyd
# by generator 1.145
"""
Routines for performing shortest-path graph searches

The main interface is in the function :func:`shortest_path`.  This
calls cython routines that compute the shortest path using
the Floyd-Warshall algorithm, Dijkstra's algorithm with Fibonacci Heaps,
the Bellman-Ford algorithm, or Johnson's Algorithm.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # D:\ProgramData\Anaconda3\lib\warnings.py
import numpy as np # D:\ProgramData\Anaconda3\lib\site-packages\numpy\__init__.py
import numpy as __numpy
import scipy.sparse.compressed as __scipy_sparse_compressed
import scipy.sparse.sputils as __scipy_sparse_sputils


# functions

def bellman_ford(csgraph, directed=True, indices=None, return_predecessors=False, unweighted=False): # real signature unknown; restored from __doc__
    """
    bellman_ford(csgraph, directed=True, indices=None, return_predecessors=False,
                     unweighted=False)
    
        Compute the shortest path lengths using the Bellman-Ford algorithm.
    
        The Bellman-ford algorithm can robustly deal with graphs with negative
        weights.  If a negative cycle is detected, an error is raised.  For
        graphs without negative edge weights, dijkstra's algorithm may be faster.
    
        .. versionadded:: 0.11.0
    
        Parameters
        ----------
        csgraph : array, matrix, or sparse matrix, 2 dimensions
            The N x N array of distances representing the input graph.
        directed : bool, optional
            If True (default), then find the shortest path on a directed graph:
            only move from point i to point j along paths csgraph[i, j].
            If False, then find the shortest path on an undirected graph: the
            algorithm can progress from point i to j along csgraph[i, j] or
            csgraph[j, i]
        indices : array_like or int, optional
            if specified, only compute the paths for the points at the given
            indices.
        return_predecessors : bool, optional
            If True, return the size (N, N) predecesor matrix
        unweighted : bool, optional
            If True, then find unweighted distances.  That is, rather than finding
            the path between each point such that the sum of weights is minimized,
            find the path such that the number of edges is minimized.
    
        Returns
        -------
        dist_matrix : ndarray
            The N x N matrix of distances between graph nodes. dist_matrix[i,j]
            gives the shortest distance from point i to point j along the graph.
    
        predecessors : ndarray
            Returned only if return_predecessors == True.
            The N x N matrix of predecessors, which can be used to reconstruct
            the shortest paths.  Row i of the predecessor matrix contains
            information on the shortest paths from point i: each entry
            predecessors[i, j] gives the index of the previous node in the
            path from point i to point j.  If no path exists between point
            i and j, then predecessors[i, j] = -9999
    
        Raises
        ------
        NegativeCycleError:
            if there are negative cycles in the graph
    
        Notes
        -----
        This routine is specially designed for graphs with negative edge weights.
        If all edge weights are positive, then Dijkstra's algorithm is a better
        choice.
    """
    pass

def dijkstra(csgraph, directed=True, indices=None, return_predecessors=False, unweighted=False, limit=None): # real signature unknown; restored from __doc__
    """
    dijkstra(csgraph, directed=True, indices=None, return_predecessors=False,
                 unweighted=False, limit=np.inf)
    
        Dijkstra algorithm using Fibonacci Heaps
    
        .. versionadded:: 0.11.0
    
        Parameters
        ----------
        csgraph : array, matrix, or sparse matrix, 2 dimensions
            The N x N array of non-negative distances representing the input graph.
        directed : bool, optional
            If True (default), then find the shortest path on a directed graph:
            only move from point i to point j along paths csgraph[i, j].
            If False, then find the shortest path on an undirected graph: the
            algorithm can progress from point i to j along csgraph[i, j] or
            csgraph[j, i]
        indices : array_like or int, optional
            if specified, only compute the paths for the points at the given
            indices.
        return_predecessors : bool, optional
            If True, return the size (N, N) predecesor matrix
        unweighted : bool, optional
            If True, then find unweighted distances.  That is, rather than finding
            the path between each point such that the sum of weights is minimized,
            find the path such that the number of edges is minimized.
        limit : float, optional
            The maximum distance to calculate, must be >= 0. Using a smaller limit
            will decrease computation time by aborting calculations between pairs
            that are separated by a distance > limit. For such pairs, the distance
            will be equal to np.inf (i.e., not connected).
    
            .. versionadded:: 0.14.0
    
        Returns
        -------
        dist_matrix : ndarray
            The matrix of distances between graph nodes. dist_matrix[i,j]
            gives the shortest distance from point i to point j along the graph.
    
        predecessors : ndarray
            Returned only if return_predecessors == True.
            The matrix of predecessors, which can be used to reconstruct
            the shortest paths.  Row i of the predecessor matrix contains
            information on the shortest paths from point i: each entry
            predecessors[i, j] gives the index of the previous node in the
            path from point i to point j.  If no path exists between point
            i and j, then predecessors[i, j] = -9999
    
        Notes
        -----
        As currently implemented, Dijkstra's algorithm does not work for
        graphs with direction-dependent distances when directed == False.
        i.e., if csgraph[i,j] and csgraph[j,i] are not equal and
        both are nonzero, setting directed=False will not yield the correct
        result.
    
        Also, this routine does not work for graphs with negative
        distances.  Negative distances can lead to infinite cycles that must
        be handled by specialized algorithms such as Bellman-Ford's algorithm
        or Johnson's algorithm.
    """
    pass

def floyd_warshall(csgraph, directed=True, return_predecessors=False, unweighted=False, overwrite=False): # real signature unknown; restored from __doc__
    """
    floyd_warshall(csgraph, directed=True, return_predecessors=False,
                       unweighted=False, overwrite=False)
    
        Compute the shortest path lengths using the Floyd-Warshall algorithm
    
        .. versionadded:: 0.11.0
    
        Parameters
        ----------
        csgraph : array, matrix, or sparse matrix, 2 dimensions
            The N x N array of distances representing the input graph.
        directed : bool, optional
            If True (default), then find the shortest path on a directed graph:
            only move from point i to point j along paths csgraph[i, j].
            If False, then find the shortest path on an undirected graph: the
            algorithm can progress from point i to j along csgraph[i, j] or
            csgraph[j, i]
        return_predecessors : bool, optional
            If True, return the size (N, N) predecesor matrix
        unweighted : bool, optional
            If True, then find unweighted distances.  That is, rather than finding
            the path between each point such that the sum of weights is minimized,
            find the path such that the number of edges is minimized.
        overwrite : bool, optional
            If True, overwrite csgraph with the result.  This applies only if
            csgraph is a dense, c-ordered array with dtype=float64.
    
        Returns
        -------
        dist_matrix : ndarray
            The N x N matrix of distances between graph nodes. dist_matrix[i,j]
            gives the shortest distance from point i to point j along the graph.
    
        predecessors : ndarray
            Returned only if return_predecessors == True.
            The N x N matrix of predecessors, which can be used to reconstruct
            the shortest paths.  Row i of the predecessor matrix contains
            information on the shortest paths from point i: each entry
            predecessors[i, j] gives the index of the previous node in the
            path from point i to point j.  If no path exists between point
            i and j, then predecessors[i, j] = -9999
    
        Raises
        ------
        NegativeCycleError:
            if there are negative cycles in the graph
    """
    pass

def isspmatrix(x): # reliably restored by inspect
    # no doc
    pass

def isspmatrix_csc(x): # reliably restored by inspect
    # no doc
    pass

def isspmatrix_csr(x): # reliably restored by inspect
    # no doc
    pass

def johnson(csgraph, directed=True, indices=None, return_predecessors=False, unweighted=False): # real signature unknown; restored from __doc__
    """
    johnson(csgraph, directed=True, indices=None, return_predecessors=False,
                unweighted=False)
    
        Compute the shortest path lengths using Johnson's algorithm.
    
        Johnson's algorithm combines the Bellman-Ford algorithm and Dijkstra's
        algorithm to quickly find shortest paths in a way that is robust to
        the presence of negative cycles.  If a negative cycle is detected,
        an error is raised.  For graphs without negative edge weights,
        dijkstra() may be faster.
    
        .. versionadded:: 0.11.0
    
        Parameters
        ----------
        csgraph : array, matrix, or sparse matrix, 2 dimensions
            The N x N array of distances representing the input graph.
        directed : bool, optional
            If True (default), then find the shortest path on a directed graph:
            only move from point i to point j along paths csgraph[i, j].
            If False, then find the shortest path on an undirected graph: the
            algorithm can progress from point i to j along csgraph[i, j] or
            csgraph[j, i]
        indices : array_like or int, optional
            if specified, only compute the paths for the points at the given
            indices.
        return_predecessors : bool, optional
            If True, return the size (N, N) predecesor matrix
        unweighted : bool, optional
            If True, then find unweighted distances.  That is, rather than finding
            the path between each point such that the sum of weights is minimized,
            find the path such that the number of edges is minimized.
    
        Returns
        -------
        dist_matrix : ndarray
            The N x N matrix of distances between graph nodes. dist_matrix[i,j]
            gives the shortest distance from point i to point j along the graph.
    
        predecessors : ndarray
            Returned only if return_predecessors == True.
            The N x N matrix of predecessors, which can be used to reconstruct
            the shortest paths.  Row i of the predecessor matrix contains
            information on the shortest paths from point i: each entry
            predecessors[i, j] gives the index of the previous node in the
            path from point i to point j.  If no path exists between point
            i and j, then predecessors[i, j] = -9999
    
        Raises
        ------
        NegativeCycleError:
            if there are negative cycles in the graph
    
        Notes
        -----
        This routine is specially designed for graphs with negative edge weights.
        If all edge weights are positive, then Dijkstra's algorithm is a better
        choice.
    """
    pass

def shortest_path(csgraph, method='auto', directed=True, return_predecessors=False, unweighted=False, overwrite=False, indices=None): # real signature unknown; restored from __doc__
    """
    shortest_path(csgraph, method='auto', directed=True, return_predecessors=False,
                      unweighted=False, overwrite=False, indices=None)
    
        Perform a shortest-path graph search on a positive directed or
        undirected graph.
    
        .. versionadded:: 0.11.0
    
        Parameters
        ----------
        csgraph : array, matrix, or sparse matrix, 2 dimensions
            The N x N array of distances representing the input graph.
        method : string ['auto'|'FW'|'D'], optional
            Algorithm to use for shortest paths.  Options are:
    
               'auto' -- (default) select the best among 'FW', 'D', 'BF', or 'J'
                         based on the input data.
    
               'FW'   -- Floyd-Warshall algorithm.  Computational cost is
                         approximately ``O[N^3]``.  The input csgraph will be
                         converted to a dense representation.
    
               'D'    -- Dijkstra's algorithm with Fibonacci heaps.  Computational
                         cost is approximately ``O[N(N*k + N*log(N))]``, where
    		     ``k`` is the average number of connected edges per node.
    		     The input csgraph will be converted to a csr
    		     representation.
    
               'BF'   -- Bellman-Ford algorithm.  This algorithm can be used when
                         weights are negative.  If a negative cycle is encountered,
                         an error will be raised.  Computational cost is
                         approximately ``O[N(N^2 k)]``, where ``k`` is the average
                         number of connected edges per node. The input csgraph will
                         be converted to a csr representation.
    
               'J'    -- Johnson's algorithm.  Like the Bellman-Ford algorithm,
                         Johnson's algorithm is designed for use when the weights
                         are negative.  It combines the Bellman-Ford algorithm
                         with Dijkstra's algorithm for faster computation.
    
        directed : bool, optional
            If True (default), then find the shortest path on a directed graph:
            only move from point i to point j along paths csgraph[i, j].
            If False, then find the shortest path on an undirected graph: the
            algorithm can progress from point i to j along csgraph[i, j] or
            csgraph[j, i]
        return_predecessors : bool, optional
            If True, return the size (N, N) predecesor matrix
        unweighted : bool, optional
            If True, then find unweighted distances.  That is, rather than finding
            the path between each point such that the sum of weights is minimized,
            find the path such that the number of edges is minimized.
        overwrite : bool, optional
            If True, overwrite csgraph with the result.  This applies only if
            method == 'FW' and csgraph is a dense, c-ordered array with
            dtype=float64.
        indices : array_like or int, optional
            If specified, only compute the paths for the points at the given
            indices. Incompatible with method == 'FW'.
    
        Returns
        -------
        dist_matrix : ndarray
            The N x N matrix of distances between graph nodes. dist_matrix[i,j]
            gives the shortest distance from point i to point j along the graph.
    
        predecessors : ndarray
            Returned only if return_predecessors == True.
            The N x N matrix of predecessors, which can be used to reconstruct
            the shortest paths.  Row i of the predecessor matrix contains
            information on the shortest paths from point i: each entry
            predecessors[i, j] gives the index of the previous node in the
            path from point i to point j.  If no path exists between point
            i and j, then predecessors[i, j] = -9999
    
        Raises
        ------
        NegativeCycleError:
            if there are negative cycles in the graph
    
        Notes
        -----
        As currently implemented, Dijkstra's algorithm and Johnson's algorithm
        do not work for graphs with direction-dependent distances when
        directed == False.  i.e., if csgraph[i,j] and csgraph[j,i] are non-equal
        edges, method='D' may yield an incorrect result.
    """
    pass

def validate_graph(csgraph, directed, dtype="<class 'numpy.float64'>", csr_output=True, dense_output=True, copy_if_dense=False, copy_if_sparse=False, null_value_in=0, null_value_out=inf, infinity_null=True, nan_null=True): # reliably restored by inspect
    """ Routine for validation and conversion of csgraph inputs """
    pass

# classes

class csr_matrix(__scipy_sparse_compressed._cs_matrix, __scipy_sparse_sputils.IndexMixin):
    """
    Compressed Sparse Row matrix
    
        This can be instantiated in several ways:
            csr_matrix(D)
                with a dense matrix or rank-2 ndarray D
    
            csr_matrix(S)
                with another sparse matrix S (equivalent to S.tocsr())
    
            csr_matrix((M, N), [dtype])
                to construct an empty matrix with shape (M, N)
                dtype is optional, defaulting to dtype='d'.
    
            csr_matrix((data, (row_ind, col_ind)), [shape=(M, N)])
                where ``data``, ``row_ind`` and ``col_ind`` satisfy the
                relationship ``a[row_ind[k], col_ind[k]] = data[k]``.
    
            csr_matrix((data, indices, indptr), [shape=(M, N)])
                is the standard CSR representation where the column indices for
                row i are stored in ``indices[indptr[i]:indptr[i+1]]`` and their
                corresponding values are stored in ``data[indptr[i]:indptr[i+1]]``.
                If the shape parameter is not supplied, the matrix dimensions
                are inferred from the index arrays.
    
        Attributes
        ----------
        dtype : dtype
            Data type of the matrix
        shape : 2-tuple
            Shape of the matrix
        ndim : int
            Number of dimensions (this is always 2)
        nnz
            Number of nonzero elements
        data
            CSR format data array of the matrix
        indices
            CSR format index array of the matrix
        indptr
            CSR format index pointer array of the matrix
        has_sorted_indices
            Whether indices are sorted
    
        Notes
        -----
    
        Sparse matrices can be used in arithmetic operations: they support
        addition, subtraction, multiplication, division, and matrix power.
    
        Advantages of the CSR format
          - efficient arithmetic operations CSR + CSR, CSR * CSR, etc.
          - efficient row slicing
          - fast matrix vector products
    
        Disadvantages of the CSR format
          - slow column slicing operations (consider CSC)
          - changes to the sparsity structure are expensive (consider LIL or DOK)
    
        Examples
        --------
    
        >>> import numpy as np
        >>> from scipy.sparse import csr_matrix
        >>> csr_matrix((3, 4), dtype=np.int8).toarray()
        array([[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]], dtype=int8)
    
        >>> row = np.array([0, 0, 1, 2, 2, 2])
        >>> col = np.array([0, 2, 2, 0, 1, 2])
        >>> data = np.array([1, 2, 3, 4, 5, 6])
        >>> csr_matrix((data, (row, col)), shape=(3, 3)).toarray()
        array([[1, 0, 2],
               [0, 0, 3],
               [4, 5, 6]])
    
        >>> indptr = np.array([0, 2, 3, 6])
        >>> indices = np.array([0, 2, 2, 0, 1, 2])
        >>> data = np.array([1, 2, 3, 4, 5, 6])
        >>> csr_matrix((data, indices, indptr), shape=(3, 3)).toarray()
        array([[1, 0, 2],
               [0, 0, 3],
               [4, 5, 6]])
    
        As an example of how to construct a CSR matrix incrementally,
        the following snippet builds a term-document matrix from texts:
    
        >>> docs = [["hello", "world", "hello"], ["goodbye", "cruel", "world"]]
        >>> indptr = [0]
        >>> indices = []
        >>> data = []
        >>> vocabulary = {}
        >>> for d in docs:
        ...     for term in d:
        ...         index = vocabulary.setdefault(term, len(vocabulary))
        ...         indices.append(index)
        ...         data.append(1)
        ...     indptr.append(len(indices))
        ...
        >>> csr_matrix((data, indices, indptr), dtype=int).toarray()
        array([[2, 1, 0, 0],
               [0, 1, 1, 1]])
    """
    def getcol(self, i): # reliably restored by inspect
        """
        Returns a copy of column i of the matrix, as a (m x 1)
                CSR matrix (column vector).
        """
        pass

    def getrow(self, i): # reliably restored by inspect
        """
        Returns a copy of row i of the matrix, as a (1 x n)
                CSR matrix (row vector).
        """
        pass

    def tobsr(self, blocksize=None, copy=True): # reliably restored by inspect
        """
        Convert this matrix to Block Sparse Row format.
        
                With copy=False, the data/indices may be shared between this matrix and
                the resultant bsr_matrix.
        
                When blocksize=(R, C) is provided, it will be used for construction of
                the bsr_matrix.
        """
        pass

    def tocsc(self, copy=False): # reliably restored by inspect
        """
        Convert this matrix to Compressed Sparse Column format.
        
                With copy=False, the data/indices may be shared between this matrix and
                the resultant csc_matrix.
        """
        pass

    def tocsr(self, copy=False): # reliably restored by inspect
        """
        Convert this matrix to Compressed Sparse Row format.
        
                With copy=False, the data/indices may be shared between this matrix and
                the resultant csr_matrix.
        """
        pass

    def tolil(self, copy=False): # reliably restored by inspect
        """
        Convert this matrix to LInked List format.
        
                With copy=False, the data/indices may be shared between this matrix and
                the resultant lil_matrix.
        """
        pass

    def transpose(self, axes=None, copy=False): # reliably restored by inspect
        """
        Reverses the dimensions of the sparse matrix.
        
                Parameters
                ----------
                axes : None, optional
                    This argument is in the signature *solely* for NumPy
                    compatibility reasons. Do not pass in anything except
                    for the default value.
                copy : bool, optional
                    Indicates whether or not attributes of `self` should be
                    copied whenever possible. The degree to which attributes
                    are copied varies depending on the type of sparse matrix
                    being used.
        
                Returns
                -------
                p : `self` with the dimensions reversed.
        
                See Also
                --------
                np.matrix.transpose : NumPy's implementation of 'transpose'
                                      for matrices
        """
        pass

    def _get_row_slice(self, i, cslice): # reliably restored by inspect
        """ Returns a copy of row self[i, cslice] """
        pass

    def _get_submatrix(self, row_slice, col_slice): # reliably restored by inspect
        """ Return a submatrix of this matrix (new matrix is created). """
        pass

    def _swap(self, x): # reliably restored by inspect
        """ swap the members of x if this is a column-oriented matrix """
        pass

    def __getitem__(self, key): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, arg1, shape=None, dtype=None, copy=False): # reliably restored by inspect
        # no doc
        pass

    format = 'csr'


class DTYPE(__numpy.floating, float):
    """ 64-bit floating-point number. Character code 'd'. Python float compatible. """
    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass


class ITYPE(__numpy.signedinteger):
    """ 32-bit integer. Character code 'i'. C int compatible. """
    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass


class NegativeCycleError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

