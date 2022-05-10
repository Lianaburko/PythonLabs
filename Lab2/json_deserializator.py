import types

def deserialize_json(s):

    index = 0 
    if s[index:index + 4] == 'None':
        s = s[index + 4::]
        return s, None

    elif s[index] in '-0123456789':
        obj = ''
        check_float = False
        while s[index] != ',' and s[index] != '\n' and s[index] != ' ' and s[index] != ']' and s[index] != '}':
            obj += s[index]
            if index < len(s)-1:
                index += 1 
                if s[index] == '.':
                    check_float = True
            else:
                break
        s = s[index::]
        if check_float:
            res = float(obj)
        else:
            res = int(obj)
        return s, res
    
    elif s[index] == '"':
        index += 1
        obj = ''
        while s[index] != '"':
            obj += s[index]
            index += 1
        s = s[(index+1)::]
        res = obj 
        return s, res


    elif s[index] == '[':  #res - all list #s - string after ]
        res = ''
        weight = 0
        check = 'end'
        while check != '0]':
            res += s[index] 
            if s[index] == ']':
                weight += 1
            elif s[index] == '[':
                weight -= 1
            check = str(weight) + s[index]
            index += 1
        s = s[index::]    
        result = list_deserialization(res)
        return s, result


    elif s[index] == '{':
        res = ''
        weight = 0
        check = 'end'
        while check != '0}':
            res += s[index] 
            if s[index] == '}':
                weight += 1
            elif s[index] == '{':
                weight -= 1
            check = str(weight) + s[index]
            index += 1
        s = s[index::]   
        result = dict_deserialization(res)
        return s, result


def dict_deserialization(res):
    result = {}
    
    while res != '}':
        if res[0] in "{},\n []":
            res = res[1::]     
        elif res[0] == '"':
            res, key = deserialize_json(res)
            res = res[1:]
            res, value = deserialize_json(res)
            result[key] = value

    return result

def list_deserialization(res): # res - current list, 
    result = []
    res = res[1::]
    while res != ']':
        if res[0] in ",\n ":
            res = res[1::]     
        else:
            res, obj = deserialize_json(res)
            result.append(obj)

    return result

def fun_deserialization(obj):
    code_object_args = get_code_object_args(obj['function_type']['__code__']['code_type'])
    
    code = types.CodeType(*code_object_args)
    my_globals = obj['function_type']['__globals__']
    name = obj['function_type']['__name__']

    res = types.FunctionType(code, my_globals, name)
    res.__globals__["__builtins__"] = __import__("builtins") # for functions suh print
    res.__globals__.update({res.__name__: res}) # for recursion
    
    return res


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


FUNCTION_ATTRIBUTES = [
    "__code__",
    "__name__",
    "__defaults__",
    "__closure__"
]


CODE_OBJECT_ARGS = [
    'co_argcount',
    'co_posonlyargcount',
    'co_kwonlyargcount',
    'co_nlocals',
    'co_stacksize',
    'co_flags',
    'co_filename',
    'co_name',
    'co_firstlineno',
    'co_freevars',
#
    'co_cellvars',
    'co_consts',
    'co_names',
    'co_varnames',
#
    'co_code',
    'co_lnotab'
]
