from inspect import isfunction
import types


def deserialize(result):

    if isinstance(result,(int, str, bool, float)):
        return result 

    elif isinstance(result, dict):

        if 'function_type' in result.keys():
            my_fun = fun_deserialization(result)
            return my_fun

        elif 'class_type' in result.keys():
            my_class = class_deserialization(result)
            return my_class

        elif 'object_type' in result.keys():
            my_object = object_deserialization(result)
            return my_object

    return result


def fun_deserialization(obj):

    code_object_args = get_code_object_args(obj['function_type']['__code__']['code_type'])
    
    code = types.CodeType(*code_object_args)
    my_globals = obj['function_type']['__globals__']
    name = obj['function_type']['__name__']

    res = types.FunctionType(code, my_globals, name)
    for key, value in my_globals.items():
        try:
            res.__globals__[deserialize(key)] = __import__(deserialize(value))
        except:
            pass

    res.__globals__["__builtins__"] = __import__("builtins") # for functions such print
    res.__globals__.update({res.__name__: res}) # for recursion

    return res


def class_deserialization(obj):
    name = obj["class_type"]["__name__"]
    attributes = {}
    methods = []

    for key, value in obj["class_type"]["__attributes__"].items():

        if value == '432':
            continue

        if isfunction(value):
            methods.append(value)

        attributes[deserialize(key)] = deserialize(value)
    
    for method in methods:
        method.__globals__[name] = obj

    my_obj = attributes
    my_bases = (tuple(deserialize(base) for base in obj["class_type"]["__bases__"]))

    return type(name, my_bases, my_obj) 


def object_deserialization(obj):

    obj_class = deserialize(obj["object_type"]["__class__"])
    attributes = {}
    
    for key, value in obj["object_type"]["__attributes__"].items():
        attributes[deserialize(key)] = deserialize(value)

    result = object.__new__(obj_class)
    result.__dict__ = attributes

    return result


def get_code_object_args(obj):
    result = (obj['co_argcount'],
    obj['co_posonlyargcount'],
    obj['co_kwonlyargcount'],
    obj['co_nlocals'],
    obj['co_stacksize'],
    obj['co_flags'],
    bytes(obj['co_code']),  
    tuple(obj['co_consts']),
    tuple(obj['co_names']),
    tuple(obj['co_varnames']),
    obj['co_filename'],
    obj['co_name'],
    obj['co_firstlineno'],
    bytes(obj['co_lnotab']))
    obj['co_freevars'],
    tuple(obj['co_cellvars']),

    return result


