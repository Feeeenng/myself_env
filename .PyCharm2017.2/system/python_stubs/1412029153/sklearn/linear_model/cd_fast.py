# encoding: utf-8
# module sklearn.linear_model.cd_fast
# from D:\ProgramData\Anaconda3\lib\site-packages\sklearn\linear_model\cd_fast.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # D:\ProgramData\Anaconda3\lib\site-packages\numpy\__init__.py
import numpy.linalg as linalg # D:\ProgramData\Anaconda3\lib\site-packages\numpy\linalg\__init__.py
import warnings as warnings # D:\ProgramData\Anaconda3\lib\warnings.py

# functions

def enet_coordinate_descent(*args, **kwargs): # real signature unknown
    """
    Cython version of the coordinate descent algorithm
            for Elastic-Net regression
    
            We minimize
    
            (1/2) * norm(y - X w, 2)^2 + alpha norm(w, 1) + (beta/2) norm(w, 2)^2
    """
    pass

def enet_coordinate_descent_gram(*args, **kwargs): # real signature unknown
    """
    Cython version of the coordinate descent algorithm
            for Elastic-Net regression
    
            We minimize
    
            (1/2) * w^T Q w - q^T w + alpha norm(w, 1) + (beta/2) * norm(w, 2)^2
    
            which amount to the Elastic-Net problem when:
            Q = X^T X (Gram matrix)
            q = X^T y
    """
    pass

def enet_coordinate_descent_multi_task(*args, **kwargs): # real signature unknown
    """
    Cython version of the coordinate descent algorithm
            for Elastic-Net mult-task regression
    
            We minimize
    
            (1/2) * norm(y - X w, 2)^2 + l1_reg ||w||_21 + (1/2) * l2_reg norm(w, 2)^2
    """
    pass

def sparse_enet_coordinate_descent(*args, **kwargs): # real signature unknown
    """
    Cython version of the coordinate descent algorithm for Elastic-Net
    
        We minimize:
    
            (1/2) * norm(y - X w, 2)^2 + alpha norm(w, 1) + (beta/2) * norm(w, 2)^2
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

