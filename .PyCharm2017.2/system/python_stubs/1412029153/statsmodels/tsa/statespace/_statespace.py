# encoding: utf-8
# module statsmodels.tsa.statespace._statespace
# from D:\ProgramData\Anaconda3\lib\site-packages\statsmodels\tsa\statespace\_statespace.cp36-win_amd64.pyd
# by generator 1.145
"""
State Space Models

Author: Chad Fulton  
License: Simplified-BSD
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # D:\ProgramData\Anaconda3\lib\site-packages\numpy\__init__.py
import warnings as warnings # D:\ProgramData\Anaconda3\lib\warnings.py
import scipy.linalg.blas as blas # D:\ProgramData\Anaconda3\lib\site-packages\scipy\linalg\blas.py
import scipy.linalg.lapack as lapack # D:\ProgramData\Anaconda3\lib\site-packages\scipy\linalg\lapack.py

# functions

def cgbsv(kl, ku, ab, b, overwrite_ab=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    lub,piv,x,info = cgbsv(kl,ku,ab,b,[overwrite_ab,overwrite_b])
    
    Wrapper for ``cgbsv``.
    
    Parameters
    ----------
    kl : input int
    ku : input int
    ab : input rank-2 array('F') with bounds (2*kl+ku+1,n)
    b : input rank-2 array('F') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    lub : rank-2 array('F') with bounds (2*kl+ku+1,n) and ab storage
    piv : rank-1 array('i') with bounds (n)
    x : rank-2 array('F') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def cgerc(alpha, x, y, incx=None, incy=None, a=None, overwrite_x=None, overwrite_y=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = cgerc(alpha,x,y,[incx,incy,a,overwrite_x,overwrite_y,overwrite_a])
    
    Wrapper for ``cgerc``.
    
    Parameters
    ----------
    alpha : input complex
    x : input rank-1 array('F') with bounds (m)
    y : input rank-1 array('F') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 1
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 1
    incy : input int, optional
        Default: 1
    a : input rank-2 array('F') with bounds (m,n), optional
        Default: (0.0,0.0)
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('F') with bounds (m,n)
    """
    pass

def _ccompute_coefficients_from_multivariate_pacf(*args, **kwargs): # real signature unknown
    """
    Notes
        -----
    
        This uses the ?trmm BLAS functions which are not available in
        Scipy v0.11.0
    """
    pass

def _cconstrain_sv_less_than_one(*args, **kwargs): # real signature unknown
    """
    Transform arbitrary matrices to matrices with singular values less than
        one.
    
        Corresponds to Lemma 2.2 in Ansley and Kohn (1986). See
        `constrain_stationary_multivariate` for more details.
    """
    pass

def _dcompute_coefficients_from_multivariate_pacf(*args, **kwargs): # real signature unknown
    """
    Notes
        -----
    
        This uses the ?trmm BLAS functions which are not available in
        Scipy v0.11.0
    """
    pass

def _dconstrain_sv_less_than_one(*args, **kwargs): # real signature unknown
    """
    Transform arbitrary matrices to matrices with singular values less than
        one.
    
        Corresponds to Lemma 2.2 in Ansley and Kohn (1986). See
        `constrain_stationary_multivariate` for more details.
    """
    pass

def _scompute_coefficients_from_multivariate_pacf(*args, **kwargs): # real signature unknown
    """
    Notes
        -----
    
        This uses the ?trmm BLAS functions which are not available in
        Scipy v0.11.0
    """
    pass

def _sconstrain_sv_less_than_one(*args, **kwargs): # real signature unknown
    """
    Transform arbitrary matrices to matrices with singular values less than
        one.
    
        Corresponds to Lemma 2.2 in Ansley and Kohn (1986). See
        `constrain_stationary_multivariate` for more details.
    """
    pass

def _zcompute_coefficients_from_multivariate_pacf(*args, **kwargs): # real signature unknown
    """
    Notes
        -----
    
        This uses the ?trmm BLAS functions which are not available in
        Scipy v0.11.0
    """
    pass

def _zconstrain_sv_less_than_one(*args, **kwargs): # real signature unknown
    """
    Transform arbitrary matrices to matrices with singular values less than
        one.
    
        Corresponds to Lemma 2.2 in Ansley and Kohn (1986). See
        `constrain_stationary_multivariate` for more details.
    """
    pass

# classes

class cKalmanFilter(object):
    """
    cKalmanFilter(model, filter=FILTER_CONVENTIONAL, inversion_method=INVERT_UNIVARIATE | SOLVE_CHOLESKY, stability_method=STABILITY_FORCE_SYMMETRY, tolerance=1e-19)
    
        A representation of the Kalman filter recursions.
    
        While the filter is mathematically represented as a recursion, it is here
        translated into Python as a stateful iterator.
    
        Because there are actually several types of Kalman filter depending on the
        state space model of interest, this class only handles the *iteration*
        aspect of filtering, and delegates the actual operations to four general
        workhorse routines, which can be implemented separately for each type of
        Kalman filter.
    
        In order to maintain a consistent interface, and because these four general
        routines may be quite different across filter types, their argument is only
        the stateful ?KalmanFilter object. Furthermore, in order to allow the
        different types of filter to substitute alternate matrices, this class
        defines a set of pointers to the various state space arrays and the
        filtering output arrays.
    
        For example, handling missing observations requires not only substituting
        `obs`, `design`, and `obs_cov` matrices, but the new matrices actually have
        different dimensions than the originals. This can be flexibly accomodated
        simply by replacing e.g. the `obs` pointer to the substituted `obs` array
        and replacing `k_endog` for that iteration. Then in the next iteration, when
        the `obs` vector may be missing different elements (or none at all), it can
        again be redefined.
    
        Each iteration of the filter (see `__next__`) proceeds in a number of
        steps.
    
        `initialize_object_pointers` initializes pointers to current-iteration
        objects (i.e. the state space arrays and filter output arrays).  
    
        `initialize_function_pointers` initializes pointers to the appropriate
        Kalman filtering routines (i.e. `forecast_conventional` or
        `forecast_exact_initial`, etc.).  
    
        `select_arrays` converts the base arrays into "selected" arrays using
        selection matrices. In particular, it handles the state covariance matrix
        and redefined matrices based on missing values.  
    
        `post_convergence` handles copying arrays from time $t-1$ to time $t$ when
        the Kalman filter has converged and they don't need to be re-calculated.  
    
        `forecasting` calls the Kalman filter `forcasting_<filter type>` routine
    
        `inversion` calls the appropriate function to invert the forecast error
        covariance matrix.  
    
        `updating` calls the Kalman filter `updating_<filter type>` routine
    
        `loglikelihood` calls the Kalman filter `loglikelihood_<filter type>` routine
    
        `prediction` calls the Kalman filter `prediction_<filter type>` routine
    
        `numerical_stability` performs end-of-iteration tasks to improve the numerical
        stability of the filter 
    
        `check_convergence` checks for convergence of the filter to steady-state.
    """
    def initialize_filter_object_pointers(self, *args, **kwargs): # real signature unknown
        pass

    def initialize_statespace_object_pointers(self, *args, **kwargs): # real signature unknown
        pass

    def seek(self, t, reset_convergence=True): # real signature unknown; restored from __doc__
        """
        seek(self, t, reset_convergence = True)
        
                Change the time-state of the filter
        
                Is usually called to reset the filter to the beginning.
        """
        pass

    def select_missing(self, *args, **kwargs): # real signature unknown
        pass

    def set_filter_method(self, filter_method, force_reset=True): # real signature unknown; restored from __doc__
        """
        set_filter_method(self, filter_method, force_reset=True)
        
                Change the filter method.
        """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Iterate the filter across the entire set of observations. """
        pass

    def __init__(self, model, filter=None, inversion_method=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Perform an iteration of the Kalman filter """
        pass

    conserve_memory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_filtered_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_forecast_error_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_predicted_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filtered_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filtered_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filter_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_fac = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_ipiv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_work = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    inversion_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endog2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endogstates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_posdef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_states = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_states2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ldwork = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loglikelihood = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loglikelihood_burn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    period_converged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    predicted_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    predicted_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_obs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stability_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    t = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time_invariant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class cStatespace(object):
    """
    cStatespace(obs, design, obs_intercept, obs_cov, transition, state_intercept, selection, state_cov)
    
        *See Durbin and Koopman (2012), Chapter 4 for all notation*
    """
    def initialize_approximate_diffuse(self, variance=1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ initialize_approximate_diffuse(variance=1e2) """
        pass

    def initialize_known(self, initial_state, initial_state_cov): # real signature unknown; restored from __doc__
        """ initialize_known(initial_state, initial_state_cov) """
        pass

    def initialize_stationary(self): # real signature unknown; restored from __doc__
        """ initialize_stationary() """
        pass

    def __init__(self, obs, design, obs_intercept, obs_cov, transition, state_intercept, selection, state_cov): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initialized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_posdef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_states = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    missing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nmissing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nobs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    obs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    obs_intercept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_intercept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time_invariant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class dKalmanFilter(object):
    """
    dKalmanFilter(model, filter=FILTER_CONVENTIONAL, inversion_method=INVERT_UNIVARIATE | SOLVE_CHOLESKY, stability_method=STABILITY_FORCE_SYMMETRY, tolerance=1e-19)
    
        A representation of the Kalman filter recursions.
    
        While the filter is mathematically represented as a recursion, it is here
        translated into Python as a stateful iterator.
    
        Because there are actually several types of Kalman filter depending on the
        state space model of interest, this class only handles the *iteration*
        aspect of filtering, and delegates the actual operations to four general
        workhorse routines, which can be implemented separately for each type of
        Kalman filter.
    
        In order to maintain a consistent interface, and because these four general
        routines may be quite different across filter types, their argument is only
        the stateful ?KalmanFilter object. Furthermore, in order to allow the
        different types of filter to substitute alternate matrices, this class
        defines a set of pointers to the various state space arrays and the
        filtering output arrays.
    
        For example, handling missing observations requires not only substituting
        `obs`, `design`, and `obs_cov` matrices, but the new matrices actually have
        different dimensions than the originals. This can be flexibly accomodated
        simply by replacing e.g. the `obs` pointer to the substituted `obs` array
        and replacing `k_endog` for that iteration. Then in the next iteration, when
        the `obs` vector may be missing different elements (or none at all), it can
        again be redefined.
    
        Each iteration of the filter (see `__next__`) proceeds in a number of
        steps.
    
        `initialize_object_pointers` initializes pointers to current-iteration
        objects (i.e. the state space arrays and filter output arrays).  
    
        `initialize_function_pointers` initializes pointers to the appropriate
        Kalman filtering routines (i.e. `forecast_conventional` or
        `forecast_exact_initial`, etc.).  
    
        `select_arrays` converts the base arrays into "selected" arrays using
        selection matrices. In particular, it handles the state covariance matrix
        and redefined matrices based on missing values.  
    
        `post_convergence` handles copying arrays from time $t-1$ to time $t$ when
        the Kalman filter has converged and they don't need to be re-calculated.  
    
        `forecasting` calls the Kalman filter `forcasting_<filter type>` routine
    
        `inversion` calls the appropriate function to invert the forecast error
        covariance matrix.  
    
        `updating` calls the Kalman filter `updating_<filter type>` routine
    
        `loglikelihood` calls the Kalman filter `loglikelihood_<filter type>` routine
    
        `prediction` calls the Kalman filter `prediction_<filter type>` routine
    
        `numerical_stability` performs end-of-iteration tasks to improve the numerical
        stability of the filter 
    
        `check_convergence` checks for convergence of the filter to steady-state.
    """
    def initialize_filter_object_pointers(self, *args, **kwargs): # real signature unknown
        pass

    def initialize_statespace_object_pointers(self, *args, **kwargs): # real signature unknown
        pass

    def seek(self, t, reset_convergence=True): # real signature unknown; restored from __doc__
        """
        seek(self, t, reset_convergence = True)
        
                Change the time-state of the filter
        
                Is usually called to reset the filter to the beginning.
        """
        pass

    def select_missing(self, *args, **kwargs): # real signature unknown
        pass

    def set_filter_method(self, filter_method, force_reset=True): # real signature unknown; restored from __doc__
        """
        set_filter_method(self, filter_method, force_reset=True)
        
                Change the filter method.
        """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Iterate the filter across the entire set of observations. """
        pass

    def __init__(self, model, filter=None, inversion_method=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Perform an iteration of the Kalman filter """
        pass

    conserve_memory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_filtered_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_forecast_error_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_predicted_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filtered_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filtered_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filter_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_fac = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_ipiv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_work = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    inversion_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endog2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endogstates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_posdef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_states = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_states2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ldwork = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loglikelihood = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loglikelihood_burn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    period_converged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    predicted_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    predicted_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_obs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stability_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    t = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time_invariant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class dStatespace(object):
    """
    dStatespace(obs, design, obs_intercept, obs_cov, transition, state_intercept, selection, state_cov)
    
        *See Durbin and Koopman (2012), Chapter 4 for all notation*
    """
    def initialize_approximate_diffuse(self, variance=1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ initialize_approximate_diffuse(variance=1e2) """
        pass

    def initialize_known(self, initial_state, initial_state_cov): # real signature unknown; restored from __doc__
        """ initialize_known(initial_state, initial_state_cov) """
        pass

    def initialize_stationary(self): # real signature unknown; restored from __doc__
        """ initialize_stationary() """
        pass

    def __init__(self, obs, design, obs_intercept, obs_cov, transition, state_intercept, selection, state_cov): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initialized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_posdef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_states = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    missing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nmissing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nobs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    obs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    obs_intercept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_intercept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time_invariant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class sKalmanFilter(object):
    """
    sKalmanFilter(model, filter=FILTER_CONVENTIONAL, inversion_method=INVERT_UNIVARIATE | SOLVE_CHOLESKY, stability_method=STABILITY_FORCE_SYMMETRY, tolerance=1e-19)
    
        A representation of the Kalman filter recursions.
    
        While the filter is mathematically represented as a recursion, it is here
        translated into Python as a stateful iterator.
    
        Because there are actually several types of Kalman filter depending on the
        state space model of interest, this class only handles the *iteration*
        aspect of filtering, and delegates the actual operations to four general
        workhorse routines, which can be implemented separately for each type of
        Kalman filter.
    
        In order to maintain a consistent interface, and because these four general
        routines may be quite different across filter types, their argument is only
        the stateful ?KalmanFilter object. Furthermore, in order to allow the
        different types of filter to substitute alternate matrices, this class
        defines a set of pointers to the various state space arrays and the
        filtering output arrays.
    
        For example, handling missing observations requires not only substituting
        `obs`, `design`, and `obs_cov` matrices, but the new matrices actually have
        different dimensions than the originals. This can be flexibly accomodated
        simply by replacing e.g. the `obs` pointer to the substituted `obs` array
        and replacing `k_endog` for that iteration. Then in the next iteration, when
        the `obs` vector may be missing different elements (or none at all), it can
        again be redefined.
    
        Each iteration of the filter (see `__next__`) proceeds in a number of
        steps.
    
        `initialize_object_pointers` initializes pointers to current-iteration
        objects (i.e. the state space arrays and filter output arrays).  
    
        `initialize_function_pointers` initializes pointers to the appropriate
        Kalman filtering routines (i.e. `forecast_conventional` or
        `forecast_exact_initial`, etc.).  
    
        `select_arrays` converts the base arrays into "selected" arrays using
        selection matrices. In particular, it handles the state covariance matrix
        and redefined matrices based on missing values.  
    
        `post_convergence` handles copying arrays from time $t-1$ to time $t$ when
        the Kalman filter has converged and they don't need to be re-calculated.  
    
        `forecasting` calls the Kalman filter `forcasting_<filter type>` routine
    
        `inversion` calls the appropriate function to invert the forecast error
        covariance matrix.  
    
        `updating` calls the Kalman filter `updating_<filter type>` routine
    
        `loglikelihood` calls the Kalman filter `loglikelihood_<filter type>` routine
    
        `prediction` calls the Kalman filter `prediction_<filter type>` routine
    
        `numerical_stability` performs end-of-iteration tasks to improve the numerical
        stability of the filter 
    
        `check_convergence` checks for convergence of the filter to steady-state.
    """
    def initialize_filter_object_pointers(self, *args, **kwargs): # real signature unknown
        pass

    def initialize_statespace_object_pointers(self, *args, **kwargs): # real signature unknown
        pass

    def seek(self, t, reset_convergence=True): # real signature unknown; restored from __doc__
        """
        seek(self, t, reset_convergence = True)
        
                Change the time-state of the filter
        
                Is usually called to reset the filter to the beginning.
        """
        pass

    def select_missing(self, *args, **kwargs): # real signature unknown
        pass

    def set_filter_method(self, filter_method, force_reset=True): # real signature unknown; restored from __doc__
        """
        set_filter_method(self, filter_method, force_reset=True)
        
                Change the filter method.
        """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Iterate the filter across the entire set of observations. """
        pass

    def __init__(self, model, filter=None, inversion_method=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Perform an iteration of the Kalman filter """
        pass

    conserve_memory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_filtered_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_forecast_error_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_predicted_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filtered_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filtered_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filter_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_fac = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_ipiv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_work = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    inversion_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endog2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endogstates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_posdef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_states = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_states2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ldwork = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loglikelihood = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loglikelihood_burn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    period_converged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    predicted_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    predicted_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_obs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stability_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    t = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time_invariant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class sStatespace(object):
    """
    sStatespace(obs, design, obs_intercept, obs_cov, transition, state_intercept, selection, state_cov)
    
        *See Durbin and Koopman (2012), Chapter 4 for all notation*
    """
    def initialize_approximate_diffuse(self, variance=1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ initialize_approximate_diffuse(variance=1e2) """
        pass

    def initialize_known(self, initial_state, initial_state_cov): # real signature unknown; restored from __doc__
        """ initialize_known(initial_state, initial_state_cov) """
        pass

    def initialize_stationary(self): # real signature unknown; restored from __doc__
        """ initialize_stationary() """
        pass

    def __init__(self, obs, design, obs_intercept, obs_cov, transition, state_intercept, selection, state_cov): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initialized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_posdef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_states = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    missing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nmissing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nobs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    obs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    obs_intercept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_intercept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time_invariant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class zKalmanFilter(object):
    """
    zKalmanFilter(model, filter=FILTER_CONVENTIONAL, inversion_method=INVERT_UNIVARIATE | SOLVE_CHOLESKY, stability_method=STABILITY_FORCE_SYMMETRY, tolerance=1e-19)
    
        A representation of the Kalman filter recursions.
    
        While the filter is mathematically represented as a recursion, it is here
        translated into Python as a stateful iterator.
    
        Because there are actually several types of Kalman filter depending on the
        state space model of interest, this class only handles the *iteration*
        aspect of filtering, and delegates the actual operations to four general
        workhorse routines, which can be implemented separately for each type of
        Kalman filter.
    
        In order to maintain a consistent interface, and because these four general
        routines may be quite different across filter types, their argument is only
        the stateful ?KalmanFilter object. Furthermore, in order to allow the
        different types of filter to substitute alternate matrices, this class
        defines a set of pointers to the various state space arrays and the
        filtering output arrays.
    
        For example, handling missing observations requires not only substituting
        `obs`, `design`, and `obs_cov` matrices, but the new matrices actually have
        different dimensions than the originals. This can be flexibly accomodated
        simply by replacing e.g. the `obs` pointer to the substituted `obs` array
        and replacing `k_endog` for that iteration. Then in the next iteration, when
        the `obs` vector may be missing different elements (or none at all), it can
        again be redefined.
    
        Each iteration of the filter (see `__next__`) proceeds in a number of
        steps.
    
        `initialize_object_pointers` initializes pointers to current-iteration
        objects (i.e. the state space arrays and filter output arrays).  
    
        `initialize_function_pointers` initializes pointers to the appropriate
        Kalman filtering routines (i.e. `forecast_conventional` or
        `forecast_exact_initial`, etc.).  
    
        `select_arrays` converts the base arrays into "selected" arrays using
        selection matrices. In particular, it handles the state covariance matrix
        and redefined matrices based on missing values.  
    
        `post_convergence` handles copying arrays from time $t-1$ to time $t$ when
        the Kalman filter has converged and they don't need to be re-calculated.  
    
        `forecasting` calls the Kalman filter `forcasting_<filter type>` routine
    
        `inversion` calls the appropriate function to invert the forecast error
        covariance matrix.  
    
        `updating` calls the Kalman filter `updating_<filter type>` routine
    
        `loglikelihood` calls the Kalman filter `loglikelihood_<filter type>` routine
    
        `prediction` calls the Kalman filter `prediction_<filter type>` routine
    
        `numerical_stability` performs end-of-iteration tasks to improve the numerical
        stability of the filter 
    
        `check_convergence` checks for convergence of the filter to steady-state.
    """
    def initialize_filter_object_pointers(self, *args, **kwargs): # real signature unknown
        pass

    def initialize_statespace_object_pointers(self, *args, **kwargs): # real signature unknown
        pass

    def seek(self, t, reset_convergence=True): # real signature unknown; restored from __doc__
        """
        seek(self, t, reset_convergence = True)
        
                Change the time-state of the filter
        
                Is usually called to reset the filter to the beginning.
        """
        pass

    def select_missing(self, *args, **kwargs): # real signature unknown
        pass

    def set_filter_method(self, filter_method, force_reset=True): # real signature unknown; restored from __doc__
        """
        set_filter_method(self, filter_method, force_reset=True)
        
                Change the filter method.
        """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Iterate the filter across the entire set of observations. """
        pass

    def __init__(self, model, filter=None, inversion_method=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Perform an iteration of the Kalman filter """
        pass

    conserve_memory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_filtered_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_forecast_error_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    converged_predicted_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filtered_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filtered_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filter_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_fac = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_ipiv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forecast_error_work = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    inversion_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endog2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endogstates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_posdef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_states = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_states2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ldwork = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loglikelihood = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loglikelihood_burn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    period_converged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    predicted_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    predicted_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_obs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stability_method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    t = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time_invariant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tmp3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class zStatespace(object):
    """
    zStatespace(obs, design, obs_intercept, obs_cov, transition, state_intercept, selection, state_cov)
    
        *See Durbin and Koopman (2012), Chapter 4 for all notation*
    """
    def initialize_approximate_diffuse(self, variance=1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ initialize_approximate_diffuse(variance=1e2) """
        pass

    def initialize_known(self, initial_state, initial_state_cov): # real signature unknown; restored from __doc__
        """ initialize_known(initial_state, initial_state_cov) """
        pass

    def initialize_stationary(self): # real signature unknown; restored from __doc__
        """ initialize_stationary() """
        pass

    def __init__(self, obs, design, obs_intercept, obs_cov, transition, state_intercept, selection, state_cov): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    design = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initialized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initial_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_endog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_posdef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k_states = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    missing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nmissing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nobs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    obs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    obs_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    obs_intercept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_cov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_intercept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time_invariant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

