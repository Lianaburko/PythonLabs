import serializer.serialization
import serializer.deserialization
import serializer.json_serializator
import serializer.json_deserializator

class Json:

    @staticmethod
    def dumps(obj,indent,current_indent = 0):
        my_dict = serializer.serialization.serialize(obj)
        return serializer.json_serializator.serialize_json(my_dict, indent, current_indent)
    
    @staticmethod
    def dump(obj, indent, current_indent, file):
        return file.write(Json.dumps(obj, indent, current_indent))

    @staticmethod
    def loads(obj):
        res = serializer.json_deserializator.deserialize_json(obj)

        if isinstance(res[1], dict):

            return (serializer.deserialization.deserialize(res[1]))
        return res[1]
    
    @staticmethod
    def load(file):
        return Json.loads(file.read())