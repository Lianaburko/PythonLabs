import serialization
import deserialization
import json_serializator
import json_deserializator

class Json:
    @staticmethod
    def dumps(obj,indent,current_indent = 0):
        my_dict = serialization.serialize(obj)
        return json_serializator.serialize_json(my_dict, indent, current_indent)
    
    @staticmethod
    def dump(obj, indent, current_indent, file):
        return file.write(Json.dumps(obj, indent, current_indent))

    @staticmethod
    def loads(obj):
        res = json_deserializator.deserialize_json(obj)
        if isinstance(res[1], dict):
            return (deserialization.deserialize(res[1]))
        return res[1]
    
    @staticmethod
    def load(file):
        return Json.loads(file.read())