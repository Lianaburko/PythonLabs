def deserialize_json(s):
    index = 0 
    if s[index:index + 4] == 'None':
        s = s[index + 4::]
        return s, None

    elif s[index:index + 5] == 'False':
        s = s[index + 5::]
        return s, False

    elif s[index:index + 4] == 'True':
        s = s[index + 4::]
        return s, True

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

        #if s != '':
          #  return s, result
        return s ,result


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

