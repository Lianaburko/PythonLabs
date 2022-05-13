import yaml
import serialization
import deserialization


class Yaml:
    @staticmethod
    def dumps(obj):
        return yaml.dump(serialization.serialize(obj))
    
    @staticmethod
    def dump(obj, file):
        return file.write(Yaml.dumps(obj))


    @staticmethod
    def loads(obj):
        return deserialization.deserialize(yaml.load(obj, Loader = yaml.FullLoader))
    
    @staticmethod
    def load(file):
        return Yaml.loads(file.read())

    
