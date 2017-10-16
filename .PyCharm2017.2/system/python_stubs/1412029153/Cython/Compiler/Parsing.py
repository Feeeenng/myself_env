# encoding: utf-8
# module Cython.Compiler.Parsing
# from D:\ProgramData\Anaconda3\lib\site-packages\Cython\Compiler\Parsing.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from Cython.Compiler.Scanning import StringSourceDescriptor

from _io import StringIO


# functions

def make_slice_node(*args, **kwargs): # real signature unknown
    pass

def print_parse_tree(*args, **kwargs): # real signature unknown
    pass

def p_code(*args, **kwargs): # real signature unknown
    pass

def p_c_arg_list(*args, **kwargs): # real signature unknown
    pass

def p_c_base_type(*args, **kwargs): # real signature unknown
    pass

def p_c_declarator(*args, **kwargs): # real signature unknown
    pass

def p_module(*args, **kwargs): # real signature unknown
    pass

# classes

class Ctx(object):
    # no doc
    def __call__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    allow_struct_enum_decorator = False
    api = 0
    cdef_flag = 0
    level = 'other'
    namespace = None
    nogil = 0
    overridable = 0
    templates = None
    typedef_flag = 0
    visibility = 'private'
    __dict__ = None # (!) real value is ''


# variables with complex values

__loader__ = None # (!) real value is ''

__pyx_capi__ = {
    '_append_escape_sequence': None, # (!) real value is ''
    '_extract_docstring': None, # (!) real value is ''
    '_p_factor': None, # (!) real value is ''
    'check_for_non_ascii_characters': None, # (!) real value is ''
    'expect_ellipsis': None, # (!) real value is ''
    'is_memoryviewslice_access': None, # (!) real value is ''
    'looking_at_base_type': None, # (!) real value is ''
    'looking_at_call': None, # (!) real value is ''
    'looking_at_dotted_name': None, # (!) real value is ''
    'looking_at_expr': None, # (!) real value is ''
    'looking_at_name': None, # (!) real value is ''
    'make_slice_node': None, # (!) real value is ''
    'make_slice_nodes': None, # (!) real value is ''
    'p_DEF_statement': None, # (!) real value is ''
    'p_IF_statement': None, # (!) real value is ''
    'p_and_expr': None, # (!) real value is ''
    'p_and_test': None, # (!) real value is ''
    'p_api': None, # (!) real value is ''
    'p_arith_expr': None, # (!) real value is ''
    'p_as_name': None, # (!) real value is ''
    'p_assert_statement': None, # (!) real value is ''
    'p_async_statement': None, # (!) real value is ''
    'p_atom': None, # (!) real value is ''
    'p_backquote_expr': None, # (!) real value is ''
    'p_binop_expr': None, # (!) real value is ''
    'p_binop_operator': None, # (!) real value is ''
    'p_bit_expr': None, # (!) real value is ''
    'p_bracketed_base_type': None, # (!) real value is ''
    'p_break_statement': None, # (!) real value is ''
    'p_buffer_or_template': None, # (!) real value is ''
    'p_c_arg_decl': None, # (!) real value is ''
    'p_c_arg_list': None, # (!) real value is ''
    'p_c_array_declarator': None, # (!) real value is ''
    'p_c_base_type': None, # (!) real value is ''
    'p_c_class_definition': None, # (!) real value is ''
    'p_c_class_options': None, # (!) real value is ''
    'p_c_complex_base_type': None, # (!) real value is ''
    'p_c_declarator': None, # (!) real value is ''
    'p_c_enum_definition': None, # (!) real value is ''
    'p_c_enum_item': None, # (!) real value is ''
    'p_c_enum_line': None, # (!) real value is ''
    'p_c_func_declarator': None, # (!) real value is ''
    'p_c_func_or_var_declaration': None, # (!) real value is ''
    'p_c_modifiers': None, # (!) real value is ''
    'p_c_simple_base_type': None, # (!) real value is ''
    'p_c_simple_declarator': None, # (!) real value is ''
    'p_c_struct_or_union_definition': None, # (!) real value is ''
    'p_call': None, # (!) real value is ''
    'p_call_build_packed_args': None, # (!) real value is ''
    'p_call_parse_args': None, # (!) real value is ''
    'p_calling_convention': None, # (!) real value is ''
    'p_cascaded_cmp': None, # (!) real value is ''
    'p_cat_string_literal': None, # (!) real value is ''
    'p_cdef_block': None, # (!) real value is ''
    'p_cdef_extern_block': None, # (!) real value is ''
    'p_cdef_statement': None, # (!) real value is ''
    'p_class_statement': None, # (!) real value is ''
    'p_cmp_op': None, # (!) real value is ''
    'p_code': None, # (!) real value is ''
    'p_comp_for': None, # (!) real value is ''
    'p_comp_if': None, # (!) real value is ''
    'p_comp_iter': None, # (!) real value is ''
    'p_comparison': None, # (!) real value is ''
    'p_compile_time_expr': None, # (!) real value is ''
    'p_compiler_directive_comments': None, # (!) real value is ''
    'p_continue_statement': None, # (!) real value is ''
    'p_cpp_class_attribute': None, # (!) real value is ''
    'p_cpp_class_definition': None, # (!) real value is ''
    'p_ctypedef_statement': None, # (!) real value is ''
    'p_decorators': None, # (!) real value is ''
    'p_def_statement': None, # (!) real value is ''
    'p_del_statement': None, # (!) real value is ''
    'p_dict_or_set_maker': None, # (!) real value is ''
    'p_doc_string': None, # (!) real value is ''
    'p_dotted_name': None, # (!) real value is ''
    'p_else_clause': None, # (!) real value is ''
    'p_except_clause': None, # (!) real value is ''
    'p_exception_value_clause': None, # (!) real value is ''
    'p_exec_statement': None, # (!) real value is ''
    'p_expression_or_assignment': None, # (!) real value is ''
    'p_f_string': None, # (!) real value is ''
    'p_f_string_expr': None, # (!) real value is ''
    'p_factor': None, # (!) real value is ''
    'p_for_bounds': None, # (!) real value is ''
    'p_for_from_relation': None, # (!) real value is ''
    'p_for_from_step': None, # (!) real value is ''
    'p_for_iterator': None, # (!) real value is ''
    'p_for_statement': None, # (!) real value is ''
    'p_for_target': None, # (!) real value is ''
    'p_from_import_statement': None, # (!) real value is ''
    'p_fused_definition': None, # (!) real value is ''
    'p_genexp': None, # (!) real value is ''
    'p_global_statement': None, # (!) real value is ''
    'p_ident': None, # (!) real value is ''
    'p_ident_list': None, # (!) real value is ''
    'p_if_clause': None, # (!) real value is ''
    'p_if_statement': None, # (!) real value is ''
    'p_ignorable_statement': None, # (!) real value is ''
    'p_import_statement': None, # (!) real value is ''
    'p_imported_name': None, # (!) real value is ''
    'p_include_statement': None, # (!) real value is ''
    'p_index': None, # (!) real value is ''
    'p_int_literal': None, # (!) real value is ''
    'p_lambdef': None, # (!) real value is ''
    'p_lambdef_nocond': None, # (!) real value is ''
    'p_list_maker': None, # (!) real value is ''
    'p_memoryviewslice_access': None, # (!) real value is ''
    'p_module': None, # (!) real value is ''
    'p_name': None, # (!) real value is ''
    'p_new_expr': None, # (!) real value is ''
    'p_nogil': None, # (!) real value is ''
    'p_nonlocal_statement': None, # (!) real value is ''
    'p_not_test': None, # (!) real value is ''
    'p_opt_cname': None, # (!) real value is ''
    'p_opt_string_literal': None, # (!) real value is ''
    'p_optional_ellipsis': None, # (!) real value is ''
    'p_or_test': None, # (!) real value is ''
    'p_pass_statement': None, # (!) real value is ''
    'p_positional_and_keyword_args': None, # (!) real value is ''
    'p_power': None, # (!) real value is ''
    'p_print_statement': None, # (!) real value is ''
    'p_property_decl': None, # (!) real value is ''
    'p_py_arg_decl': None, # (!) real value is ''
    'p_raise_statement': None, # (!) real value is ''
    'p_rassoc_binop_expr': None, # (!) real value is ''
    'p_return_statement': None, # (!) real value is ''
    'p_shift_expr': None, # (!) real value is ''
    'p_sign_and_longness': None, # (!) real value is ''
    'p_simple_expr_list': None, # (!) real value is ''
    'p_simple_statement': None, # (!) real value is ''
    'p_simple_statement_list': None, # (!) real value is ''
    'p_sizeof': None, # (!) real value is ''
    'p_slice_element': None, # (!) real value is ''
    'p_starred_expr': None, # (!) real value is ''
    'p_statement': None, # (!) real value is ''
    'p_statement_list': None, # (!) real value is ''
    'p_string_literal': None, # (!) real value is ''
    'p_struct_enum': None, # (!) real value is ''
    'p_subscript': None, # (!) real value is ''
    'p_subscript_list': None, # (!) real value is ''
    'p_suite': None, # (!) real value is ''
    'p_suite_with_docstring': None, # (!) real value is ''
    'p_target': None, # (!) real value is ''
    'p_template_definition': None, # (!) real value is ''
    'p_term': None, # (!) real value is ''
    'p_test': None, # (!) real value is ''
    'p_test_nocond': None, # (!) real value is ''
    'p_test_or_starred_expr': None, # (!) real value is ''
    'p_test_or_starred_expr_list': None, # (!) real value is ''
    'p_testlist': None, # (!) real value is ''
    'p_testlist_comp': None, # (!) real value is ''
    'p_testlist_star_expr': None, # (!) real value is ''
    'p_trailer': None, # (!) real value is ''
    'p_try_statement': None, # (!) real value is ''
    'p_typecast': None, # (!) real value is ''
    'p_varargslist': None, # (!) real value is ''
    'p_visibility': None, # (!) real value is ''
    'p_while_statement': None, # (!) real value is ''
    'p_with_gil': None, # (!) real value is ''
    'p_with_items': None, # (!) real value is ''
    'p_with_statement': None, # (!) real value is ''
    'p_with_template': None, # (!) real value is ''
    'p_xor_expr': None, # (!) real value is ''
    'p_yield_expression': None, # (!) real value is ''
    'p_yield_statement': None, # (!) real value is ''
    'wrap_compile_time_constant': None, # (!) real value is ''
}

__spec__ = None # (!) real value is ''

__test__ = {}

