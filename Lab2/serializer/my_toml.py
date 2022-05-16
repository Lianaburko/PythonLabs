import toml
import yaml
import serializer.serialization
import serializer.deserialization
                
class Toml:
    @staticmethod
    def dumps(obj):
        return yaml.dump(serializer.serialization.serialize(obj))
    
    @staticmethod
    def dump(obj, file):
        return file.write(Toml.dumps(obj))

    @staticmethod
    def loads(obj):
        return serializer.deserialization.deserialize(yaml.load(obj, Loader = yaml.FullLoader))
    
    @staticmethod
    def load(file):
        return Toml.loads(file.read())

    
