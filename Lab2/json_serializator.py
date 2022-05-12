import types
from inspect import isclass, isfunction


def serialize_json(obj, indent, current_intent):
    if obj is None:
        return 'None'

    elif isinstance(obj, (int, float)):
        return str(obj)

    elif isinstance(obj, str):
        new_str = '"' + str(obj) + '"'
        return new_str
    
    elif isinstance(obj, (list,tuple,bytes)):
        return list_serialization(obj, indent, current_intent)

    elif isinstance(obj, dict):
        return dict_serialization(obj, indent, current_intent)
    
    elif isfunction(obj):
        return fun_serialization(obj, indent, current_intent)

    elif isclass(obj):
        return class_serialization(obj, indent, current_intent)

    return "432"

def list_serialization(obj, indent, current_indent = 0):

    if len(obj) == 0:
        result = '[]'
    else:
        result = '[' + '\n' 

        prev_gap = ' ' * current_indent
        current_indent += indent
        gap = ' ' * current_indent

        for i in range(len(obj)-1):
            result += gap + serialize_json(obj[i], indent, current_indent) + ',\n'
        
        result += gap + serialize_json(obj[len(obj)-1], indent, current_indent) + '\n'

        if current_indent != indent: 
            result += prev_gap  + ']'     
        else:
            result += ']'

    return result


def dict_serialization(obj, indent, current_indent = 0):
    if len(obj) == 0:
        result = '{}'
    else:
        result = '{' + '\n' 

        prev_gap = ' ' * current_indent
        current_indent += indent
        gap = ' ' * current_indent

        for k, v in obj.items():
            if isinstance(k, (int, float)):
                result += gap + '"' + serialize_json(k, indent, current_indent) + '"' + ':' + serialize_json(v, indent, current_indent) + ',\n'
            else:
                result += gap  + serialize_json(k, indent, current_indent) + ':' + serialize_json(v, indent, current_indent) + ',\n'
        
        if current_indent != indent: 
            result += prev_gap  + '}'     
        else:
            result += '}'
    return result 


def get_globals(fun):
    result = {}

    for key in fun.__globals__:

        if isinstance(fun.__globals__[key], types.ModuleType):
            result[key] = fun.__globals__[key].__name__

        elif key in fun.__code__.co_names and fun.__name__ != key:
            result[key] = fun.__globals__[key]

    return result


def fun_serialization(fun, indent, current_indent):
    globals = get_globals(fun)
    result = {
        "function_type": {
            "__globals__": globals,
            "__name__": fun.__name__,
            "__code__": {
                "code_type": {
                    'co_argcount':fun.__code__.co_argcount,
                    'co_posonlyargcount':fun.__code__.co_posonlyargcount,
                    'co_kwonlyargcount':fun.__code__.co_kwonlyargcount,
                    'co_nlocals':fun.__code__.co_nlocals,
                    'co_stacksize':fun.__code__.co_stacksize, 
                    'co_flags':fun.__code__.co_flags,
                    'co_filename':fun.__code__.co_filename,
                    'co_names':fun.__code__.co_names,
                    'co_firstlineno':fun.__code__.co_firstlineno,
                    'co_freevars':fun.__code__.co_freevars,
                    'co_cellvars':fun.__code__.co_cellvars,
                    'co_consts':fun.__code__.co_consts,
                    'co_varnames':fun.__code__.co_varnames,
                    'co_name':fun.__code__.co_name,
#
                    'co_code':list(fun.__code__.co_code),
                    'co_lnotab':list(fun.__code__.co_lnotab)
                }
            }
        }
    }
    res = dict_serialization(result, indent, current_indent)
    return res


def class_serialization(cls, indent, current_indent):
    cls_dir = dir(cls)
    cls_dir.remove("__class__")
    cls_dir.remove("__getattribute__")
    cls_dir.remove("__new__")
    cls_dir.remove("__setattr__")

    result = {
        "class_type":{
            "__attributes__":{},
            "__name__": cls.__name__,
            "__bases__": [class_serialization(base, indent, current_indent) for base in cls.__bases__ if base != object]
        }
    }

    for i in cls_dir:
        result["class_type"]["__attributes__"][i] = getattr(cls, i)
    
    res = dict_serialization(result, indent, current_indent)   

    return res


