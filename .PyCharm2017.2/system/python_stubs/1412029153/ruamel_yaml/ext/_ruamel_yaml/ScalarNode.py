# encoding: utf-8
# module ruamel_yaml.ext._ruamel_yaml
# from D:\ProgramData\Anaconda3\lib\site-packages\ruamel_yaml\ext\_ruamel_yaml.cp36-win_amd64.pyd
# by generator 1.145
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import ruamel_yaml.error as __ruamel_yaml_error
import ruamel_yaml.events as __ruamel_yaml_events
import ruamel_yaml.nodes as __ruamel_yaml_nodes
import ruamel_yaml.tokens as __ruamel_yaml_tokens


class ScalarNode(__ruamel_yaml_nodes.Node):
    """
    styles:
          ? -> set() ? key, no value
          " -> double quoted
          ' -> single quoted
          | -> literal style
          > ->
    """
    def __init__(self, tag, value, start_mark=None, end_mark=None, style=None, comment=None): # reliably restored by inspect
        # no doc
        pass

    id = 'scalar'


