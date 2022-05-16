from serializer.my_json import Json
from serializer.my_toml import Toml
from serializer.my_yaml import Yaml

class Factory:
    def create_serializer(format):
        if format == ".json":
            return Json()
        elif format == ".toml":
            return Toml()
        return Yaml()