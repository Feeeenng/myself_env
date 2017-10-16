# encoding: utf-8
# module Cython.Compiler.Code
# from D:\ProgramData\Anaconda3\lib\site-packages\Cython\Compiler\Code.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import shutil as shutil # D:\ProgramData\Anaconda3\lib\shutil.py
import sys as sys # <module 'sys' (built-in)>
import textwrap as textwrap # D:\ProgramData\Anaconda3\lib\textwrap.py
import hashlib as hashlib # D:\ProgramData\Anaconda3\lib\hashlib.py
import Cython.Compiler.Version as Version # D:\ProgramData\Anaconda3\lib\site-packages\Cython\Compiler\Version.py
import contextlib as __contextlib


# Variables with simple values

KEYWORDS_MUST_BE_BYTES = False

# functions

def funccontext_property(*args, **kwargs): # real signature unknown
    pass

def get_utility_dir(*args, **kwargs): # real signature unknown
    pass

def is_self_assignment(*args, **kwargs): # real signature unknown
    """ Matches zero or more characters at the beginning of the string. """
    pass

def modifier_output_mapper(*args, **kwargs): # real signature unknown
    """ D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None. """
    pass

def sub_tempita(*args, **kwargs): # real signature unknown
    """ Run tempita on string s with given context. """
    pass

def __pyx_unpickle_FunctionState(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_PyObjectConst(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_PyrexCodeWriter(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_StringConst(*args, **kwargs): # real signature unknown
    pass

def __reduce_cython__(*args, **kwargs): # real signature unknown
    pass

def __setstate_cython__(*args, **kwargs): # real signature unknown
    pass

# classes

class CCodeConfig(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class CCodeWriter(object):
    """
    Utility class to output C code.
    
        When creating an insertion point one must care about the state that is
        kept:
        - formatting state (level, bol) is cloned and used in insertion points
          as well
        - labels, temps, exc_vars: One must construct a scope in which these can
          exist by calling enter_cfunc_scope/exit_cfunc_scope (these are for
          sanity checking and forward compatabilty). Created insertion points
          looses this scope and cannot access it.
        - marker: Not copied to insertion point
        - filename_table, filename_list, input_file_contents: All codewriters
          coming from the same root share the same instances simultaneously.
    """
    def all_new_labels(self, *args, **kwargs): # real signature unknown
        pass

    def as_pyobject(self, *args, **kwargs): # real signature unknown
        pass

    def begin_block(self, *args, **kwargs): # real signature unknown
        pass

    def build_function_modifiers(self, *args, **kwargs): # real signature unknown
        pass

    def copyto(self, *args, **kwargs): # real signature unknown
        pass

    def create_new(self, *args, **kwargs): # real signature unknown
        pass

    def declare_gilstate(self, *args, **kwargs): # real signature unknown
        pass

    def decrease_indent(self, *args, **kwargs): # real signature unknown
        pass

    def emit_marker(self, *args, **kwargs): # real signature unknown
        pass

    def end_block(self, *args, **kwargs): # real signature unknown
        pass

    def enter_cfunc_scope(self, *args, **kwargs): # real signature unknown
        pass

    def entry_as_pyobject(self, *args, **kwargs): # real signature unknown
        pass

    def error_goto(self, *args, **kwargs): # real signature unknown
        pass

    def error_goto_if(self, *args, **kwargs): # real signature unknown
        pass

    def error_goto_if_neg(self, *args, **kwargs): # real signature unknown
        pass

    def error_goto_if_null(self, *args, **kwargs): # real signature unknown
        pass

    def error_goto_if_PyErr(self, *args, **kwargs): # real signature unknown
        pass

    def exit_cfunc_scope(self, *args, **kwargs): # real signature unknown
        pass

    def getvalue(self, *args, **kwargs): # real signature unknown
        pass

    def get_all_labels(self, *args, **kwargs): # real signature unknown
        pass

    def get_argument_default_const(self, *args, **kwargs): # real signature unknown
        pass

    def get_cached_constants_writer(self, *args, **kwargs): # real signature unknown
        pass

    def get_loop_labels(self, *args, **kwargs): # real signature unknown
        pass

    def get_pyunicode_ptr_const(self, *args, **kwargs): # real signature unknown
        pass

    def get_py_const(self, *args, **kwargs): # real signature unknown
        pass

    def get_py_float(self, *args, **kwargs): # real signature unknown
        pass

    def get_py_int(self, *args, **kwargs): # real signature unknown
        pass

    def get_py_string_const(self, *args, **kwargs): # real signature unknown
        pass

    def get_py_version_hex(self, *args, **kwargs): # real signature unknown
        pass

    def get_string_const(self, *args, **kwargs): # real signature unknown
        pass

    def increase_indent(self, *args, **kwargs): # real signature unknown
        pass

    def indent(self, *args, **kwargs): # real signature unknown
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        """
        Inserts the contents of another code writer (created with
                the same global state) in the current location.
        
                It is ok to write to the inserted writer also after insertion.
        """
        pass

    def insertion_point(self, *args, **kwargs): # real signature unknown
        pass

    def intern(self, *args, **kwargs): # real signature unknown
        pass

    def intern_identifier(self, *args, **kwargs): # real signature unknown
        pass

    def label_used(self, *args, **kwargs): # real signature unknown
        pass

    def lookup_filename(self, *args, **kwargs): # real signature unknown
        pass

    def mark_pos(self, *args, **kwargs): # real signature unknown
        pass

    def new_error_label(self, *args, **kwargs): # real signature unknown
        pass

    def new_label(self, *args, **kwargs): # real signature unknown
        pass

    def new_loop_labels(self, *args, **kwargs): # real signature unknown
        pass

    def new_writer(self, *args, **kwargs): # real signature unknown
        """
        Creates a new CCodeWriter connected to the same global state, which
                can later be inserted using insert.
        """
        pass

    def new_yield_label(self, *args, **kwargs): # real signature unknown
        pass

    def put(self, *args, **kwargs): # real signature unknown
        pass

    def putln(self, *args, **kwargs): # real signature unknown
        pass

    def putln_openmp(self, *args, **kwargs): # real signature unknown
        pass

    def putln_tempita(self, *args, **kwargs): # real signature unknown
        pass

    def put_acquire_gil(self, *args, **kwargs): # real signature unknown
        """
        Acquire the GIL. The thread's thread state must have been initialized
                by a previous `put_release_gil`
        """
        pass

    def put_add_traceback(self, *args, **kwargs): # real signature unknown
        """
        Build a Python traceback for propagating exceptions.
        
                qualified_name should be the qualified name of the function.
        """
        pass

    def put_declare_refcount_context(self, *args, **kwargs): # real signature unknown
        pass

    def put_decref(self, *args, **kwargs): # real signature unknown
        pass

    def put_decref_clear(self, *args, **kwargs): # real signature unknown
        pass

    def put_decref_set(self, *args, **kwargs): # real signature unknown
        pass

    def put_ensure_gil(self, *args, **kwargs): # real signature unknown
        """
        Acquire the GIL. The generated code is safe even when no PyThreadState
                has been allocated for this thread (for threads not initialized by
                using the Python API). Additionally, the code generated by this method
                may be called recursively.
        """
        pass

    def put_error_if_neg(self, *args, **kwargs): # real signature unknown
        pass

    def put_error_if_unbound(self, *args, **kwargs): # real signature unknown
        pass

    def put_finish_refcount_context(self, *args, **kwargs): # real signature unknown
        pass

    def put_generated_by(self, *args, **kwargs): # real signature unknown
        pass

    def put_giveref(self, *args, **kwargs): # real signature unknown
        pass

    def put_goto(self, *args, **kwargs): # real signature unknown
        pass

    def put_gotref(self, *args, **kwargs): # real signature unknown
        pass

    def put_h_guard(self, *args, **kwargs): # real signature unknown
        pass

    def put_incref(self, *args, **kwargs): # real signature unknown
        pass

    def put_incref_memoryviewslice(self, *args, **kwargs): # real signature unknown
        pass

    def put_init_to_py_none(self, *args, **kwargs): # real signature unknown
        pass

    def put_init_var_to_py_none(self, *args, **kwargs): # real signature unknown
        pass

    def put_label(self, *args, **kwargs): # real signature unknown
        pass

    def put_or_include(self, *args, **kwargs): # real signature unknown
        pass

    def put_pymethoddef(self, *args, **kwargs): # real signature unknown
        pass

    def put_release_ensured_gil(self, *args, **kwargs): # real signature unknown
        """ Releases the GIL, corresponds to `put_ensure_gil`. """
        pass

    def put_release_gil(self, *args, **kwargs): # real signature unknown
        """ Release the GIL, corresponds to `put_acquire_gil`. """
        pass

    def put_safe(self, *args, **kwargs): # real signature unknown
        pass

    def put_setup_refcount_context(self, *args, **kwargs): # real signature unknown
        pass

    def put_tempita(self, *args, **kwargs): # real signature unknown
        pass

    def put_temp_declarations(self, *args, **kwargs): # real signature unknown
        pass

    def put_trace_call(self, *args, **kwargs): # real signature unknown
        pass

    def put_trace_declarations(self, *args, **kwargs): # real signature unknown
        pass

    def put_trace_exception(self, *args, **kwargs): # real signature unknown
        pass

    def put_trace_frame_init(self, *args, **kwargs): # real signature unknown
        pass

    def put_trace_return(self, *args, **kwargs): # real signature unknown
        pass

    def put_unraisable(self, *args, **kwargs): # real signature unknown
        """
        Generate code to print a Python warning for an unraisable exception.
        
                qualified_name should be the qualified name of the function.
        """
        pass

    def put_var_declaration(self, *args, **kwargs): # real signature unknown
        pass

    def put_var_decref(self, *args, **kwargs): # real signature unknown
        pass

    def put_var_decrefs(self, *args, **kwargs): # real signature unknown
        pass

    def put_var_decref_clear(self, *args, **kwargs): # real signature unknown
        pass

    def put_var_giveref(self, *args, **kwargs): # real signature unknown
        pass

    def put_var_gotref(self, *args, **kwargs): # real signature unknown
        pass

    def put_var_incref(self, *args, **kwargs): # real signature unknown
        pass

    def put_var_xdecref(self, *args, **kwargs): # real signature unknown
        pass

    def put_var_xdecrefs(self, *args, **kwargs): # real signature unknown
        pass

    def put_var_xdecrefs_clear(self, *args, **kwargs): # real signature unknown
        pass

    def put_var_xdecref_clear(self, *args, **kwargs): # real signature unknown
        pass

    def put_var_xgiveref(self, *args, **kwargs): # real signature unknown
        pass

    def put_var_xgotref(self, *args, **kwargs): # real signature unknown
        pass

    def put_var_xincref(self, *args, **kwargs): # real signature unknown
        pass

    def put_xdecref(self, *args, **kwargs): # real signature unknown
        pass

    def put_xdecref_clear(self, *args, **kwargs): # real signature unknown
        pass

    def put_xdecref_memoryviewslice(self, *args, **kwargs): # real signature unknown
        pass

    def put_xdecref_set(self, *args, **kwargs): # real signature unknown
        pass

    def put_xgiveref(self, *args, **kwargs): # real signature unknown
        pass

    def put_xgiveref_memoryviewslice(self, *args, **kwargs): # real signature unknown
        pass

    def put_xgotref(self, *args, **kwargs): # real signature unknown
        pass

    def redef_builtin_expect(self, *args, **kwargs): # real signature unknown
        pass

    def set_all_labels(self, *args, **kwargs): # real signature unknown
        pass

    def set_error_info(self, *args, **kwargs): # real signature unknown
        pass

    def set_global_state(self, *args, **kwargs): # real signature unknown
        pass

    def set_loop_labels(self, *args, **kwargs): # real signature unknown
        pass

    def undef_builtin_expect(self, *args, **kwargs): # real signature unknown
        """
        Redefine the macros likely() and unlikely to no-ops, depending on
                condition 'cond'
        """
        pass

    def unlikely(self, *args, **kwargs): # real signature unknown
        pass

    def use_label(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, *args, **kwargs): # real signature unknown
        pass

    def _build_marker(self, *args, **kwargs): # real signature unknown
        pass

    def _put_decref(self, *args, **kwargs): # real signature unknown
        pass

    def _put_var_decref_clear(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    break_label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    continue_label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    error_label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    labels_used = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    label_counter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    return_from_error_cleanup_label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    return_label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    yield_labels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    code_config = None
    globalstate = None
    __dict__ = None # (!) real value is ''


class closing(__contextlib.AbstractContextManager):
    """
    Context to automatically close something at the end of a block.
    
        Code like this:
    
            with closing(<module>.open(<arguments>)) as f:
                <block>
    
        is equivalent to this:
    
            f = <module>.open(<arguments>)
            try:
                <block>
            finally:
                f.close()
    """
    def __enter__(self): # reliably restored by inspect
        # no doc
        pass

    def __exit__(self, *exc_info): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, thing): # reliably restored by inspect
        # no doc
        pass

    _abc_cache = None # (!) real value is ''
    _abc_negative_cache = None # (!) real value is ''
    _abc_negative_cache_version = 36
    _abc_registry = None # (!) real value is ''
    __abstractmethods__ = None # (!) real value is ''


class ClosureTempAllocator(object):
    # no doc
    def allocate_temp(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class defaultdict(dict):
    """
    defaultdict(default_factory[, ...]) --> dict with default factory
    
    The default factory is called without arguments to produce
    a new value when a key is not present, in __getitem__ only.
    A defaultdict compares equal to a dict with the same items.
    All remaining arguments are treated the same as if they were
    passed to the dict constructor, including keyword arguments.
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ D.copy() -> a shallow copy of D. """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        """ D.copy() -> a shallow copy of D. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, default_factory, *some): # real signature unknown; restored from __doc__
        pass

    def __missing__(self, key): # real signature unknown; restored from __doc__
        """
        __missing__(key) # Called by __getitem__ for missing key; pseudo-code:
          if self.default_factory is None: raise KeyError((key,))
          self[key] = value = self.default_factory()
          return value
        """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    default_factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Factory for default value called by __missing__()."""



class FunctionState(object):
    # no doc
    def allocate_temp(self, *args, **kwargs): # real signature unknown
        """
        Allocates a temporary (which may create a new one or get a previously
                allocated and released one of the same type). Type is simply registered
                and handed back, but will usually be a PyrexType.
        
                If type.is_pyobject, manage_ref comes into play. If manage_ref is set to
                True, the temp will be decref-ed on return statements and in exception
                handling clauses. Otherwise the caller has to deal with any reference
                counting of the variable.
        
                If not type.is_pyobject, then manage_ref will be ignored, but it
                still has to be passed. It is recommended to pass False by convention
                if it is known that type will never be a Python object.
        
                static=True marks the temporary declaration with "static".
                This is only used when allocating backing store for a module-level
                C array literals.
        
                A C string referring to the variable is returned.
        """
        pass

    def all_free_managed_temps(self, *args, **kwargs): # real signature unknown
        """
        Return a list of (cname, type) tuples of refcount-managed Python
                objects that are not currently in use.  This is used by
                try-except and try-finally blocks to clean up temps in the
                error case.
        """
        pass

    def all_managed_temps(self, *args, **kwargs): # real signature unknown
        """ Return a list of (cname, type) tuples of refcount-managed Python objects. """
        pass

    def all_new_labels(self, *args, **kwargs): # real signature unknown
        pass

    def get_all_labels(self, *args, **kwargs): # real signature unknown
        pass

    def get_loop_labels(self, *args, **kwargs): # real signature unknown
        pass

    def init_closure_temps(self, *args, **kwargs): # real signature unknown
        pass

    def label_used(self, *args, **kwargs): # real signature unknown
        pass

    def new_error_label(self, *args, **kwargs): # real signature unknown
        pass

    def new_label(self, *args, **kwargs): # real signature unknown
        pass

    def new_loop_labels(self, *args, **kwargs): # real signature unknown
        pass

    def new_yield_label(self, *args, **kwargs): # real signature unknown
        pass

    def release_temp(self, *args, **kwargs): # real signature unknown
        """
        Releases a temporary so that it can be reused by other code needing
                a temp of the same type.
        """
        pass

    def set_all_labels(self, *args, **kwargs): # real signature unknown
        pass

    def set_loop_labels(self, *args, **kwargs): # real signature unknown
        pass

    def start_collecting_temps(self, *args, **kwargs): # real signature unknown
        """ Useful to find out which temps were used in a code block """
        pass

    def stop_collecting_temps(self, *args, **kwargs): # real signature unknown
        pass

    def temps_holding_reference(self, *args, **kwargs): # real signature unknown
        """
        Return a list of (cname,type) tuples of temp names and their type
                that are currently in use. This includes only temps of a
                Python object type which owns its reference.
        """
        pass

    def temps_in_use(self, *args, **kwargs): # real signature unknown
        """
        Return a list of (cname,type,manage_ref) tuples of temp names and their type
                that are currently in use.
        """
        pass

    def use_label(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    break_label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    can_trace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    closure_temps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collect_temps_stack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    continue_label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    error_label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    exc_vars = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gil_owned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    in_try_finally = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    labels_used = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    label_counter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    names_taken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    return_from_error_cleanup_label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    return_label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    should_declare_error_indicator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    temps_allocated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    temps_free = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    temps_used_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    temp_counter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uses_error_indicator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    yield_labels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class GlobalState(object):
    # no doc
    def add_cached_builtin_decl(self, *args, **kwargs): # real signature unknown
        pass

    def close_global_decls(self, *args, **kwargs): # real signature unknown
        pass

    def commented_file_contents(self, *args, **kwargs): # real signature unknown
        pass

    def finalize_main_c_code(self, *args, **kwargs): # real signature unknown
        pass

    def generate_cached_methods_decls(self, *args, **kwargs): # real signature unknown
        pass

    def generate_const_declarations(self, *args, **kwargs): # real signature unknown
        pass

    def generate_num_constants(self, *args, **kwargs): # real signature unknown
        pass

    def generate_object_constant_decls(self, *args, **kwargs): # real signature unknown
        pass

    def generate_string_constants(self, *args, **kwargs): # real signature unknown
        pass

    def get_cached_constants_writer(self, *args, **kwargs): # real signature unknown
        pass

    def get_cached_unbound_method(self, *args, **kwargs): # real signature unknown
        pass

    def get_float_const(self, *args, **kwargs): # real signature unknown
        pass

    def get_interned_identifier(self, *args, **kwargs): # real signature unknown
        pass

    def get_int_const(self, *args, **kwargs): # real signature unknown
        pass

    def get_pyunicode_ptr_const(self, *args, **kwargs): # real signature unknown
        pass

    def get_py_const(self, *args, **kwargs): # real signature unknown
        pass

    def get_py_string_const(self, *args, **kwargs): # real signature unknown
        pass

    def get_string_const(self, *args, **kwargs): # real signature unknown
        pass

    def initialize_main_c_code(self, *args, **kwargs): # real signature unknown
        pass

    def lookup_filename(self, *args, **kwargs): # real signature unknown
        pass

    def new_const_cname(self, *args, **kwargs): # real signature unknown
        pass

    def new_num_const(self, *args, **kwargs): # real signature unknown
        pass

    def new_num_const_cname(self, *args, **kwargs): # real signature unknown
        pass

    def new_py_const(self, *args, **kwargs): # real signature unknown
        pass

    def new_string_const(self, *args, **kwargs): # real signature unknown
        pass

    def new_string_const_cname(self, *args, **kwargs): # real signature unknown
        pass

    def put_cached_builtin_init(self, *args, **kwargs): # real signature unknown
        pass

    def put_pyobject_decl(self, *args, **kwargs): # real signature unknown
        pass

    def should_declare(self, *args, **kwargs): # real signature unknown
        pass

    def use_entry_utility_code(self, *args, **kwargs): # real signature unknown
        pass

    def use_utility_code(self, *args, **kwargs): # real signature unknown
        """
        Adds code to the C file. utility_code should
                a) implement __eq__/__hash__ for the purpose of knowing whether the same
                   code has already been included
                b) implement put_code, which takes a globalstate instance
        
                See UtilityCode.
        """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    code_layout = [
        'h_code',
        'filename_table',
        'utility_code_proto_before_types',
        'numeric_typedefs',
        'complex_type_declarations',
        'type_declarations',
        'utility_code_proto',
        'module_declarations',
        'typeinfo',
        'before_global_var',
        'global_var',
        'string_decls',
        'decls',
        'all_the_rest',
        'pystring_table',
        'cached_builtins',
        'cached_constants',
        'init_globals',
        'init_module',
        'cleanup_globals',
        'cleanup_module',
        'main_method',
        'utility_code_def',
        'end',
    ]
    directives = {}
    __dict__ = None # (!) real value is ''


class IntConst(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class UtilityCodeBase(object):
    """
    Support for loading utility code from a file.
    
        Code sections in the file can be specified as follows:
    
            ##### MyUtility.proto #####
    
            [proto declarations]
    
            ##### MyUtility.init #####
    
            [code run at module initialization]
    
            ##### MyUtility #####
            #@requires: MyOtherUtility
            #@substitute: naming
    
            [definitions]
    
        for prototypes and implementation respectively.  For non-python or
        -cython files backslashes should be used instead.  5 to 30 comment
        characters may be used on either side.
    
        If the @cname decorator is not used and this is a CythonUtilityCode,
        one should pass in the 'name' keyword argument to be used for name
        mangling of such entries.
    """
    def format_code(self, *args, **kwargs): # real signature unknown
        """ Format a code section for output. """
        pass

    def get_tree(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def load(cls, *args, **kwargs): # real signature unknown
        """
        Load utility code from a file specified by from_file (relative to
                Cython/Utility) and name util_code_name.  If from_file is not given,
                load it from the file util_code_name.*.  There should be only one
                file matched by this pattern.
        """
        pass

    @classmethod
    def load_as_string(cls, *args, **kwargs): # real signature unknown
        """ Load a utility code as a string. Returns (proto, implementation) """
        pass

    @classmethod
    def load_cached(cls, *args, **kwargs): # real signature unknown
        """ Calls .load(), but using a per-type cache based on utility name and file name. """
        pass

    @classmethod
    def load_utilities_from_file(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _add_utility(cls, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    is_cython_utility = False
    requires = None
    _utility_cache = {}
    __dict__ = None # (!) real value is ''


class LazyUtilityCode(UtilityCodeBase):
    """
    Utility code that calls a callback with the root code writer when
        available. Useful when you only have 'env' but not 'code'.
    """
    def put_code(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __name__ = 'LazyUtilityCode'


class NumConst(object):
    """
    Global info about a Python number constant held by GlobalState.
    
        cname       string
        value       string
        py_type     string     int, long, float
        value_code  string     evaluation code if different from value
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class partial(object):
    """
    partial(func, *args, **keywords) - new function with partial application
        of the given arguments and keywords.
    """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, func, *args, **keywords): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """tuple of arguments to future partial calls"""

    func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """function object to use in future partial calls"""

    keywords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """dictionary of keyword arguments to future partial calls"""


    __dict__ = None # (!) real value is ''


class PyObjectConst(object):
    """ Global info about a generic constant held by GlobalState. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    cname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class PyrexCodeWriter(object):
    # no doc
    def dedent(self, *args, **kwargs): # real signature unknown
        pass

    def indent(self, *args, **kwargs): # real signature unknown
        pass

    def putln(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    f = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class PyStringConst(object):
    """ Global info about a Python string constant held by GlobalState. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class PyxCodeWriter(object):
    """
    Can be used for writing out some Cython code. To use the indenter
        functionality, the Cython.Compiler.Importer module will have to be used
        to load the code to support python 2.4
    """
    def dedent(self, *args, **kwargs): # real signature unknown
        pass

    def getvalue(self, *args, **kwargs): # real signature unknown
        pass

    def indent(self, *args, **kwargs): # real signature unknown
        pass

    def indenter(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Instead of
        
                    with pyx_code.indenter("for i in range(10):"):
                        pyx_code.putln("print i")
        
                write
        
                    if pyx_code.indenter("for i in range(10);"):
                        pyx_code.putln("print i")
                        pyx_code.dedent()
        """
        pass

    def insertion_point(self, *args, **kwargs): # real signature unknown
        pass

    def named_insertion_point(self, *args, **kwargs): # real signature unknown
        pass

    def putln(self, *args, **kwargs): # real signature unknown
        pass

    def put_chunk(self, *args, **kwargs): # real signature unknown
        pass

    def _putln(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class StringConst(object):
    """ Global info about a C string constant held by GlobalState. """
    def add_py_version(self, *args, **kwargs): # real signature unknown
        pass

    def get_py_string_const(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    cname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    escaped_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    py_strings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    py_versions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class UtilityCode(UtilityCodeBase):
    """
    Stores utility code to add during code generation.
    
        See GlobalState.put_utility_code.
    
        hashes/equals by instance
    
        proto           C prototypes
        impl            implemenation code
        init            code to call on module initialization
        requires        utility code dependencies
        proto_block     the place in the resulting file where the prototype should
                        end up
        name            name of the utility code (or None)
        file            filename of the utility code file this utility was loaded
                        from (or None)
    """
    def inject_string_constants(self, *args, **kwargs): # real signature unknown
        """ Replace 'PYIDENT("xyz")' by a constant Python identifier cname. """
        pass

    def inject_unbound_methods(self, *args, **kwargs): # real signature unknown
        """ Replace 'UNBOUND_METHOD(type, "name")' by a constant Python identifier cname. """
        pass

    def none_or_sub(self, *args, **kwargs): # real signature unknown
        """ Format a string in this utility code with context. If None, do nothing. """
        pass

    def put_code(self, *args, **kwargs): # real signature unknown
        pass

    def specialize(self, *args, **kwargs): # real signature unknown
        pass

    def wrap_c_strings(self, *args, **kwargs): # real signature unknown
        """ Replace CSTRING('''xyz''') by a C compatible string """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class TempitaUtilityCode(UtilityCode):
    # no doc
    @classmethod
    def load_cached(cls, *args, **kwargs): # real signature unknown
        pass

    def none_or_sub(self, *args, **kwargs): # real signature unknown
        """ Format a string in this utility code with context. If None, do nothing. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Template(object):
    """ A string class for supporting $-substitutions. """
    def safe_substitute(*args, **kws): # reliably restored by inspect
        # no doc
        pass

    def substitute(*args, **kws): # reliably restored by inspect
        # no doc
        pass

    def _invalid(self, mo): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, template): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    delimiter = '$'
    flags = 2
    idpattern = '[_a-z][_a-z0-9]*'
    pattern = None # (!) real value is ''
    __dict__ = None # (!) real value is ''


# variables with complex values

basicsize_builtins_map = {
    'PyTypeObject': 'PyHeapTypeObject',
}

non_portable_builtins_map = {
    'basestring': (
        'PY_MAJOR_VERSION >= 3',
        'str',
    ),
    'bytes': (
        'PY_MAJOR_VERSION < 3',
        'str',
    ),
    'raw_input': (
        'PY_MAJOR_VERSION >= 3',
        'input',
    ),
    'unicode': '<value is a self-reference, replaced by this string>',
    'xrange': (
        'PY_MAJOR_VERSION >= 3',
        'range',
    ),
}

special_py_methods = None # (!) real value is ''

uncachable_builtins = [
    'WindowsError',
    '_',
]

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

