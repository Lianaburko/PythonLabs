import yaml
import serializer.serialization
import serializer.deserialization


class Yaml:

    @staticmethod
    def dumps(obj):
        return yaml.dump(serializer.serialization.serialize(obj))
    
    @staticmethod
    def dump(obj, file):
        return file.write(Yaml.dumps(obj))

    @staticmethod
    def loads(obj):
        return serializer.deserialization.deserialize(yaml.load(obj, Loader = yaml.FullLoader))
    
    @staticmethod
    def load(file):
        return Yaml.loads(file.read())

    
