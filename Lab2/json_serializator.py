def serialize_json(obj, indent, current_intent):
    if obj is None:
        return 'None'
    
    if obj is False:
        return 'False'
    
    if obj is True:
        return 'True'

    elif isinstance(obj, (int, float)):
        return str(obj)

    elif isinstance(obj, str):
        new_str = '"' + str(obj) + '"'
        return new_str
    
    elif isinstance(obj, (list,tuple,bytes)):
        return list_serialization(obj, indent, current_intent)

    elif isinstance(obj, dict):
        return dict_serialization(obj, indent, current_intent)
    

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



