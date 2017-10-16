# encoding: utf-8
# module Cython.Compiler.FlowControl
# from D:\ProgramData\Anaconda3\lib\site-packages\Cython\Compiler\FlowControl.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import Cython.Compiler.Options as Options # D:\ProgramData\Anaconda3\lib\site-packages\Cython\Compiler\Options.py
import Cython.Compiler.ParseTreeTransforms as __Cython_Compiler_ParseTreeTransforms
import Cython.Compiler.Visitor as __Cython_Compiler_Visitor


# functions

def __pyx_unpickle_AssignmentCollector(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_AssignmentList(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_ControlBlock(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_ControlFlow(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_ControlFlowAnalysis(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_ExitBlock(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_MessageCollection(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_NameAssignment(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Uninitialized(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Unknown(*args, **kwargs): # real signature unknown
    pass

def __reduce_cython__(*args, **kwargs): # real signature unknown
    pass

def __setstate_cython__(*args, **kwargs): # real signature unknown
    pass

# classes

class NameAssignment(object):
    # no doc
    def infer_type(self, *args, **kwargs): # real signature unknown
        pass

    def type_dependencies(self, *args, **kwargs): # real signature unknown
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    bit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    entry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    inferred_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_arg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_deletion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lhs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    refs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rhs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Argument(NameAssignment):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class AssignmentCollector(__Cython_Compiler_Visitor.TreeVisitor):
    # no doc
    def visit_CascadedAssignmentNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_Node(self, *args, **kwargs): # real signature unknown
        pass

    def visit_SingleAssignmentNode(self, *args, **kwargs): # real signature unknown
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

    __pyx_vtable__ = None # (!) real value is ''


class AssignmentList(object):
    # no doc
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

    bit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stats = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ConstantFolding(__Cython_Compiler_Visitor.VisitorTransform, __Cython_Compiler_ParseTreeTransforms.SkipDeclarations):
    """
    Calculate the result of constant expressions to store it in
        ``expr_node.constant_result``, and replace trivial cases by their
        constant result.
    
        General rules:
    
        - We calculate float constants to make them available to the
          compiler, but we do not aggregate them into a single literal
          node to prevent any loss of precision.
    
        - We recursively calculate constants from non-literal nodes to
          make them available to the compiler, but we only aggregate
          literal nodes at each step.  Non-literal nodes are never merged
          into a single node.
    """
    def visit_AddNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_BinopNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_BoolBinopNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_ComprehensionNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_CondExprNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_ExprNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_ExprStatNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_ForInStatNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_FormattedValueNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_IfStatNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_JoinedStrNode(self, node): # reliably restored by inspect
        """
        Clean up after the parser by discarding empty Unicode strings and merging
                substring sequences.  Empty or single-value join lists are not uncommon
                because f-string format specs are always parsed into JoinedStrNodes.
        """
        pass

    def visit_MergedDictNode(self, node): # reliably restored by inspect
        """ Unpack **args in place if we can. """
        pass

    def visit_MergedSequenceNode(self, node): # reliably restored by inspect
        """ Unpack *args in place if we can. """
        pass

    def visit_MulNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_Node(self, *args, **kwargs): # real signature unknown
        pass

    def visit_PrimaryCmpNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_SequenceNode(self, node): # reliably restored by inspect
        """ Unpack *args in place if we can. """
        pass

    def visit_SliceIndexNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_UnopNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def visit_WhileStatNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def _bool_node(self, node, value): # reliably restored by inspect
        # no doc
        pass

    def _calculate_const(self, node): # reliably restored by inspect
        # no doc
        pass

    def _calculate_constant_seq(self, node, sequence_node, factor): # reliably restored by inspect
        # no doc
        pass

    def _handle_NotNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def _handle_UnaryMinusNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def _handle_UnaryPlusNode(self, node): # reliably restored by inspect
        # no doc
        pass

    def _negate_operator(self, *args, **kwargs): # real signature unknown
        """ D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None. """
        pass

    def _widest_node_class(self, *nodes): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, reevaluate=False): # reliably restored by inspect
        """
        The reevaluate argument specifies whether constant values that were
                previously computed should be recomputed.
        """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    NODE_TYPE_ORDER = [
        None, # (!) real value is ''
        None, # (!) real value is ''
        None, # (!) real value is ''
        None, # (!) real value is ''
    ]
    __dict__ = None # (!) real value is ''


class ControlBlock(object):
    """
    Control flow graph node. Sequence of assignments and name references.
    
           children  set of children nodes
           parents   set of parent nodes
           positions set of position markers
    
           stats     list of block statements
           gen       dict of assignments generated by this block
           bounded   set  of entries that are definitely bounded in this block
    
           Example:
    
            a = 1
            b = a + c # 'c' is already bounded or exception here
    
            stats = [Assignment(a), NameReference(a), NameReference(c),
                         Assignment(b)]
            gen = {Entry(a): Assignment(a), Entry(b): Assignment(b)}
            bounded = set([Entry(a), Entry(c)])
    """
    def add_child(self, *args, **kwargs): # real signature unknown
        pass

    def detach(self, *args, **kwargs): # real signature unknown
        """ Detach block from parents and children. """
        pass

    def empty(self, *args, **kwargs): # real signature unknown
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

    bounded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    input = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    i_gen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    i_input = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    i_kill = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    i_output = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    i_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    output = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    positions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stats = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class ControlFlow(object):
    """
    Control-flow graph.
    
           entry_point ControlBlock entry point for this graph
           exit_point  ControlBlock normal exit point
           block       ControlBlock current block
           blocks      set    children nodes
           entries     set    tracked entries
           loops       list   stack for loop descriptors
           exceptions  list   stack for exception descriptors
    """
    def initialize(self, *args, **kwargs): # real signature unknown
        """ Set initial state, map assignments to bits. """
        pass

    def is_statically_assigned(self, *args, **kwargs): # real signature unknown
        pass

    def is_tracked(self, *args, **kwargs): # real signature unknown
        pass

    def map_one(self, *args, **kwargs): # real signature unknown
        pass

    def mark_argument(self, *args, **kwargs): # real signature unknown
        pass

    def mark_assignment(self, *args, **kwargs): # real signature unknown
        pass

    def mark_deletion(self, *args, **kwargs): # real signature unknown
        pass

    def mark_position(self, *args, **kwargs): # real signature unknown
        """ Mark position, will be used to draw graph nodes. """
        pass

    def mark_reference(self, *args, **kwargs): # real signature unknown
        pass

    def newblock(self, *args, **kwargs): # real signature unknown
        """
        Create floating block linked to `parent` if given.
        
                   NOTE: Block is NOT added to self.blocks
        """
        pass

    def nextblock(self, *args, **kwargs): # real signature unknown
        """
        Create block children block linked to current or `parent` if given.
        
                   NOTE: Block is added to self.blocks
        """
        pass

    def normalize(self, *args, **kwargs): # real signature unknown
        """ Delete unreachable and orphan blocks. """
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

    assmts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    block = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    blocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    entries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    entry_point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    exceptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    exit_point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loops = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class ControlFlowAnalysis(__Cython_Compiler_Visitor.CythonTransform):
    # no doc
    def mark_assignment(self, *args, **kwargs): # real signature unknown
        pass

    def mark_forloop_target(self, *args, **kwargs): # real signature unknown
        pass

    def mark_position(self, *args, **kwargs): # real signature unknown
        """ Mark position if DOT output is enabled. """
        pass

    def visit_AmpersandNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_AssignmentNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_AsyncForStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_BreakStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_CArgDeclNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_CascadedAssignmentNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ComprehensionNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ContinueStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_CTypeDefNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_DefNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_DelStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ForFromStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ForInStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_FromImportStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_FuncDefNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_GeneratorBodyDefNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_IfStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_InPlaceAssignmentNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_LoopNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ModuleNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_NameNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_Node(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ParallelAssignmentNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ParallelRangeNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ParallelWithBlockNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_PyClassDefNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_RaiseStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ReraiseStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ReturnStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_ScopedExprNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_SingleAssignmentNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_StatListNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_TryExceptStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_TryFinallyStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_WhileStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_WithStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def visit_WithTargetAssignmentStatNode(self, *args, **kwargs): # real signature unknown
        pass

    def _delete_privates(self, *args, **kwargs): # real signature unknown
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

    __pyx_vtable__ = None # (!) real value is ''


class ControlFlowState(list):
    # no doc
    def one(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    cf_is_null = False
    cf_maybe_null = False
    is_single = False
    __dict__ = None # (!) real value is ''


class ExceptionDescr(object):
    """
    Exception handling helper.
    
        entry_point   ControlBlock Exception handling entry point
        finally_enter ControlBlock Normal finally clause entry point
        finally_exit  ControlBlock Normal finally clause exit point
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class ExitBlock(ControlBlock):
    """ Non-empty exit point block. """
    def empty(self, *args, **kwargs): # real signature unknown
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

    __pyx_vtable__ = None # (!) real value is ''


class GV(object):
    """ Graphviz DOT renderer. """
    def render(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class GVContext(object):
    """ Graphviz subgraph object. """
    def add(self, *args, **kwargs): # real signature unknown
        pass

    def escape(self, *args, **kwargs): # real signature unknown
        pass

    def extract_sources(self, *args, **kwargs): # real signature unknown
        pass

    def nodeid(self, *args, **kwargs): # real signature unknown
        pass

    def render(self, *args, **kwargs): # real signature unknown
        """ Render graphviz dot graph """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class LoopDescr(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class MessageCollection(object):
    """ Collect error/warnings messages first then sort """
    def error(self, *args, **kwargs): # real signature unknown
        pass

    def report(self, *args, **kwargs): # real signature unknown
        pass

    def warning(self, *args, **kwargs): # real signature unknown
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


class NameDeletion(NameAssignment):
    # no doc
    def infer_type(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class NameReference(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class StaticAssignment(NameAssignment):
    """ Initialised at declaration time, e.g. stack allocation. """
    def infer_type(self, *args, **kwargs): # real signature unknown
        pass

    def type_dependencies(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class Uninitialized(object):
    """ Definitely not initialised yet. """
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


class Unknown(object):
    """ Coming from outer closure, might be initialised or not. """
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


# variables with complex values

__loader__ = None # (!) real value is ''

__pyx_capi__ = {
    'check_definitions': None, # (!) real value is ''
}

__spec__ = None # (!) real value is ''

__test__ = {}

