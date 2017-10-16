# encoding: utf-8
# module numba._helperlib
# from D:\ProgramData\Anaconda3\lib\site-packages\numba\_helperlib.cp36-win_amd64.pyd
# by generator 1.145
""" No docs """
# no imports

# Variables with simple values

long_max = 2147483647
long_min = -2147483648

py_buffer_size = 80

py_gil_state_size = 4

# functions

def rnd_get_np_state_ptr(*args, **kwargs): # real signature unknown
    pass

def rnd_get_py_state_ptr(*args, **kwargs): # real signature unknown
    pass

def rnd_get_state(*args, **kwargs): # real signature unknown
    pass

def rnd_seed(*args, **kwargs): # real signature unknown
    pass

def rnd_set_state(*args, **kwargs): # real signature unknown
    pass

def rnd_shuffle(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

c_helpers = {
    'acos': 140704988255024,
    'acosf': 140704988255008,
    'acosh': 140704988254928,
    'acoshf': 140704988254912,
    'adapt_buffer': 140704988258608,
    'adapt_ndarray': 140704988258816,
    'asin': 140704988255056,
    'asinf': 140704988255040,
    'asinh': 140704988254960,
    'asinhf': 140704988254944,
    'atan': 140704988254992,
    'atan2': 140704988254416,
    'atan2_fixed': 140704988254432,
    'atan2f': 140704988254400,
    'atanf': 140704988254976,
    'atanh': 140704988254896,
    'atanhf': 140704988254880,
    'attempt_nocopy_reshape': 140704988257648,
    'ceil': 140704988254688,
    'ceilf': 140704988254672,
    'complex_adaptor': 140704988259504,
    'cos': 140704988255216,
    'cosf': 140704988255200,
    'cosh': 140704988255120,
    'coshf': 140704988255104,
    'cpow': 140704988260272,
    'cpowf': 140704988260000,
    'create_np_datetime': 140704988257184,
    'create_np_timedelta': 140704988257104,
    'do_raise': 140704988255472,
    'erf': 140704988259920,
    'erfc': 140704988259888,
    'erfcf': 140704988259872,
    'erff': 140704988259904,
    'exp': 140704988254864,
    'expf': 140704988254848,
    'expm1': 140704988254832,
    'expm1f': 140704988254816,
    'extract_np_datetime': 140704988257360,
    'extract_np_timedelta': 140704988257264,
    'extract_record_data': 140704988259376,
    'ez_cgeev': 140704988233184,
    'ez_gelsd': 140704988222592,
    'ez_geqrf': 140704988226624,
    'ez_gesdd': 140704988227504,
    'ez_rgeev': 140704988234448,
    'ez_xxgetri': 140704988235872,
    'ez_xxgqr': 140704988225680,
    'ez_xxxevd': 140704988230448,
    'fabs': 140704988254768,
    'fabsf': 140704988254736,
    'fatal_error': 140704988256048,
    'fixed_fmod': 140704988261072,
    'fixed_fmodf': 140704988261008,
    'floor': 140704988254720,
    'floorf': 140704988254704,
    'fmod': 140704988254464,
    'fmodf': 140704988254448,
    'fptoui': 140704988257088,
    'fptouif': 140704988257072,
    'frexp': 140704988260768,
    'frexpf': 140704988260624,
    'gamma': 140704988259984,
    'gammaf': 140704988259968,
    'get_buffer': 140704988258784,
    'get_np_random_state': 140704988220640,
    'get_py_random_state': 140704988220704,
    'get_pyobject_private_data': 140704988256592,
    'gil_ensure': 140704988257040,
    'gil_release': 140704988257024,
    'ldexp': 140704988260528,
    'ldexpf': 140704988260416,
    'lgamma': 140704988259952,
    'lgammaf': 140704988259936,
    'log': 140704988254656,
    'log10': 140704988254624,
    'log10f': 140704988254608,
    'log1p': 140704988254592,
    'log1pf': 140704988254576,
    'logf': 140704988254640,
    'ndarray_new': 140704988258512,
    'poisson_ptrs': 140704988218000,
    'pow': 140704988254496,
    'powf': 140704988254480,
    'py_type': 140704988257008,
    'recreate_record': 140704988259056,
    'release_buffer': 140704988258592,
    'reset_pyobject_private_data': 140704988256448,
    'rnd_init': 140704988221936,
    'rnd_shuffle': 140704988222032,
    'round': 140704988254560,
    'roundf': 140704988254544,
    'sdiv': 140704988260960,
    'set_fnclex': 140704988260992,
    'set_pyobject_private_data': 140704988256768,
    'signbit': 140704988259840,
    'signbitf': 140704988259856,
    'sin': 140704988255248,
    'sinf': 140704988255232,
    'sinh': 140704988255152,
    'sinhf': 140704988255136,
    'sqrt': 140704988254800,
    'sqrtf': 140704988254784,
    'srem': 140704988260896,
    'tan': 140704988255184,
    'tanf': 140704988255168,
    'tanh': 140704988255088,
    'tanhf': 140704988255072,
    'trunc': 140704988254528,
    'truncf': 140704988254512,
    'udiv': 140704988260928,
    'unpack_slice': 140704988256096,
    'unpickle': 140704988255264,
    'urem': 140704988260864,
    'xgesv': 140704988222240,
    'xxdot': 140704988248816,
    'xxgemm': 140704988248064,
    'xxgemv': 140704988248464,
    'xxgetrf': 140704988236912,
    'xxnrm2': 140704988247760,
    'xxpotrf': 140704988235584,
}

npymath_exports = {
    'npy_exp2': 140704988262576,
    'npy_exp2f': 140704988263088,
    'npy_log2': 140704988262384,
    'npy_log2f': 140704988262368,
    'npy_logaddexp': 140704988262608,
    'npy_logaddexp2': 140704988262768,
    'npy_logaddexp2f': 140704988262400,
    'npy_logaddexpf': 140704988262944,
    'npy_modf': 140704988262592,
    'npy_modff': 140704988262352,
    'npy_nextafter': 140704988263584,
    'npy_nextafterf': 140704988263568,
    'npy_spacing': 140704988263488,
    'npy_spacingf': 140704988263600,
}

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

