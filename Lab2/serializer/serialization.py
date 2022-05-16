import inspect
import types
from inspect import isclass, isfunction, ismethod


def serialize(obj):

    if type(obj) in [types.MethodDescriptorType, types.MethodWrapperType, types.WrapperDescriptorType, 
    types.BuiltinMethodType, types.GetSetDescriptorType, types.MappingProxyType, types.MemberDescriptorType]:
        return "432"

    elif obj is None:
        return 'None'

    elif obj is True:
        return 'True'
    
    elif obj is False:
        return 'False'

    elif isinstance(obj, (int, float, str)):
        return obj
  
    elif isinstance(obj, (list,tuple,bytes,dict)):
        return obj
    
    elif inspect.isroutine(obj):
        return fun_serialization(obj)

    elif isclass(obj):
        return class_serialization(obj)

    else:
        return object_serialization(obj) 


def get_globals(fun):
    result = {}

    for key in fun.__globals__:

        if inspect.isroutine(fun.__globals__[key]):
            continue

        if isinstance(fun.__globals__[key], types.ModuleType):
            result[key] = serialize(fun.__globals__[key].__name__)

        elif key in fun.__code__.co_names and fun.__name__ != key:
            result[key] = serialize(fun.__globals__[key])

    return result


def fun_serialization(fun):
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
                    'co_code':list(fun.__code__.co_code),
                    'co_lnotab':list(fun.__code__.co_lnotab)
                }
            }
        }
    }

    return result


def class_serialization(cls):
    cls_dir = dir(cls)
    cls_dir.remove("__class__")
    cls_dir.remove("__getattribute__")
    cls_dir.remove("__new__")
    cls_dir.remove("__setattr__")
    cls_dir.remove("__delattr__")

    result = {
        "class_type":{
            "__attributes__":{},
            "__name__": cls.__name__,
            "__bases__": [serialize(base) for base in cls.__bases__ if base != object]
        }
    }

    for i in cls_dir:
        result["class_type"]["__attributes__"][i] = serialize(getattr(cls, i))

    return result


def object_serialization(obj):

    result = {
        "object_type":{
            "__class__": serialize(obj.__class__),
            "__attributes__": {},
        }
    }

    for key, value in inspect.getmembers(obj):
        if not key[0::2] == '__' and (not isfunction(value) or not ismethod(obj) or not isinstance(obj, types.LambdaType)) :
            result["object_type"]["__attributes__"][key] = serialize(value)

    return result



