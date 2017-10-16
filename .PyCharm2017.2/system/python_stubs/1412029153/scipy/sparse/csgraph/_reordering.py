# encoding: utf-8
# module scipy.sparse.csgraph._reordering
# from D:\ProgramData\Anaconda3\lib\site-packages\scipy\sparse\csgraph\_reordering.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # D:\ProgramData\Anaconda3\lib\site-packages\numpy\__init__.py
from _warnings import warn

import numpy as __numpy
import scipy.sparse.base as __scipy_sparse_base
import scipy.sparse.compressed as __scipy_sparse_compressed
import scipy.sparse.sputils as __scipy_sparse_sputils


# functions

def isspmatrix(x): # reliably restored by inspect
    # no doc
    pass

def isspmatrix_coo(x): # reliably restored by inspect
    # no doc
    pass

def isspmatrix_csc(x): # reliably restored by inspect
    # no doc
    pass

def isspmatrix_csr(x): # reliably restored by inspect
    # no doc
    pass

def maximum_bipartite_matching(graph, perm_type='row'): # real signature unknown; restored from __doc__
    """
    maximum_bipartite_matching(graph, perm_type='row')
        
        Returns an array of row or column permutations that makes
        the diagonal of a nonsingular square CSC sparse matrix zero free.  
        
        Such a permutation is always possible provided that the matrix 
        is nonsingular. This function looks at the structure of the matrix 
        only. The input matrix will be converted to CSC matrix format if
        necessary.
    
        Parameters
        ----------
        graph : sparse matrix
            Input sparse in CSC format
        perm_type : str, {'row', 'column'}
            Type of permutation to generate.
    
        Returns
        -------
        perm : ndarray
            Array of row or column permutations.
    
        Notes
        -----
        This function relies on a maximum cardinality bipartite matching 
        algorithm based on a breadth-first search (BFS) of the underlying 
        graph.
    
        .. versionadded:: 0.15.0
    
        References
        ----------
        I. S. Duff, K. Kaya, and B. Ucar, "Design, Implementation, and 
        Analysis of Maximum Transversal Algorithms", ACM Trans. Math. Softw.
        38, no. 2, (2011).
    """
    pass

def reverse_cuthill_mckee(graph, symmetric_mode=False): # real signature unknown; restored from __doc__
    """
    reverse_cuthill_mckee(graph, symmetric_mode=False)
        
        Returns the permutation array that orders a sparse CSR or CSC matrix
        in Reverse-Cuthill McKee ordering.  
        
        It is assumed by default, ``symmetric_mode=False``, that the input matrix 
        is not symmetric and works on the matrix ``A+A.T``. If you are 
        guaranteed that the matrix is symmetric in structure (values of matrix 
        elements do not matter) then set ``symmetric_mode=True``.
        
        Parameters
        ----------
        graph : sparse matrix
            Input sparse in CSC or CSR sparse matrix format.
        symmetric_mode : bool, optional
            Is input matrix guaranteed to be symmetric.
    
        Returns
        -------
        perm : ndarray
            Array of permuted row and column indices.
     
        Notes
        -----
        .. versionadded:: 0.15.0
    
        References
        ----------
        E. Cuthill and J. McKee, "Reducing the Bandwidth of Sparse Symmetric Matrices",
        ACM '69 Proceedings of the 1969 24th national conference, (1969).
    """
    pass

def structural_rank(graph): # real signature unknown; restored from __doc__
    """
    structural_rank(graph)
        
        Compute the structural rank of a graph (matrix) with a given 
        sparsity pattern.
    
        The structural rank of a matrix is the number of entries in the maximum 
        transversal of the corresponding bipartite graph, and is an upper bound 
        on the numerical rank of the matrix. A graph has full structural rank 
        if it is possible to permute the elements to make the diagonal zero-free.
    
        Parameters
        ----------
        graph : sparse matrix
            Input sparse matrix.
    
        Returns
        -------
        rank : int
            The structural rank of the sparse graph.
    
        .. versionadded:: 0.19.0
        
        References
        ----------
        .. [1] I. S. Duff, "Computing the Structural Index", SIAM J. Alg. Disc. 
                Meth., Vol. 7, 594 (1986).
        
        .. [2] http://www.cise.ufl.edu/research/sparse/matrices/legend.html
    """
    pass

def _maximum_bipartite_matching(*args, **kwargs): # real signature unknown
    """ Maximum bipartite matching of a graph in CSC format. """
    pass

def _reverse_cuthill_mckee(*args, **kwargs): # real signature unknown
    """
    Reverse Cuthill-McKee ordering of a sparse symmetric CSR or CSC matrix.  
        We follow the original Cuthill-McKee paper and always start the routine
        at a node of lowest degree for each connected component.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class csc_matrix(__scipy_sparse_compressed._cs_matrix, __scipy_sparse_sputils.IndexMixin):
    """
    Compressed Sparse Column matrix
    
        This can be instantiated in several ways:
    
            csc_matrix(D)
                with a dense matrix or rank-2 ndarray D
    
            csc_matrix(S)
                with another sparse matrix S (equivalent to S.tocsc())
    
            csc_matrix((M, N), [dtype])
                to construct an empty matrix with shape (M, N)
                dtype is optional, defaulting to dtype='d'.
    
            csc_matrix((data, (row_ind, col_ind)), [shape=(M, N)])
                where ``data``, ``row_ind`` and ``col_ind`` satisfy the
                relationship ``a[row_ind[k], col_ind[k]] = data[k]``.
    
            csc_matrix((data, indices, indptr), [shape=(M, N)])
                is the standard CSC representation where the row indices for
                column i are stored in ``indices[indptr[i]:indptr[i+1]]``
                and their corresponding values are stored in
                ``data[indptr[i]:indptr[i+1]]``.  If the shape parameter is
                not supplied, the matrix dimensions are inferred from
                the index arrays.
    
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
            Data array of the matrix
        indices
            CSC format index array
        indptr
            CSC format index pointer array
        has_sorted_indices
            Whether indices are sorted
    
        Notes
        -----
    
        Sparse matrices can be used in arithmetic operations: they support
        addition, subtraction, multiplication, division, and matrix power.
    
        Advantages of the CSC format
            - efficient arithmetic operations CSC + CSC, CSC * CSC, etc.
            - efficient column slicing
            - fast matrix vector products (CSR, BSR may be faster)
    
        Disadvantages of the CSC format
          - slow row slicing operations (consider CSR)
          - changes to the sparsity structure are expensive (consider LIL or DOK)
    
    
        Examples
        --------
    
        >>> import numpy as np
        >>> from scipy.sparse import csc_matrix
        >>> csc_matrix((3, 4), dtype=np.int8).toarray()
        array([[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]], dtype=int8)
    
        >>> row = np.array([0, 2, 2, 0, 1, 2])
        >>> col = np.array([0, 0, 1, 2, 2, 2])
        >>> data = np.array([1, 2, 3, 4, 5, 6])
        >>> csc_matrix((data, (row, col)), shape=(3, 3)).toarray()
        array([[1, 0, 4],
               [0, 0, 5],
               [2, 3, 6]])
    
        >>> indptr = np.array([0, 2, 3, 6])
        >>> indices = np.array([0, 2, 2, 0, 1, 2])
        >>> data = np.array([1, 2, 3, 4, 5, 6])
        >>> csc_matrix((data, indices, indptr), shape=(3, 3)).toarray()
        array([[1, 0, 4],
               [0, 0, 5],
               [2, 3, 6]])
    """
    def getcol(self, i): # reliably restored by inspect
        """
        Returns a copy of column i of the matrix, as a (m x 1)
                CSC matrix (column vector).
        """
        pass

    def getrow(self, i): # reliably restored by inspect
        """
        Returns a copy of row i of the matrix, as a (1 x n)
                CSR matrix (row vector).
        """
        pass

    def nonzero(self): # reliably restored by inspect
        """
        nonzero indices
        
                Returns a tuple of arrays (row,col) containing the indices
                of the non-zero elements of the matrix.
        
                Examples
                --------
                >>> from scipy.sparse import csr_matrix
                >>> A = csr_matrix([[1,2,0],[0,0,3],[4,0,5]])
                >>> A.nonzero()
                (array([0, 0, 1, 2, 2]), array([0, 1, 2, 0, 2]))
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

    def _swap(self, x): # reliably restored by inspect
        """ swap the members of x if this is a column-oriented matrix """
        pass

    def __getitem__(self, key): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, arg1, shape=None, dtype=None, copy=False): # reliably restored by inspect
        # no doc
        pass

    def __iter__(self): # reliably restored by inspect
        # no doc
        pass

    format = 'csc'


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


class SparseEfficiencyWarning(__scipy_sparse_base.SparseWarning):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

