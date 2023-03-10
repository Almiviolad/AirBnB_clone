#!/usr/bin/python3
"script containing the file storage class"
class FileStorage:
    def __init__(self):
        self.__file_path = "JSON_file.json"
        self.__objects = {}

    def all(self):
        return self.__objects
    def new(self, obj):
        self.__objects = {obj.__class__.__name__+"."+obj.id:obj}
        
    def save(self):
        if self.__file_path == Null:
            pass
        else:
            with open(self.__file_path, 'w') as f:
                json.dump(self.__objects, f)

    def reload(self):
        if self.__file_path == Null:
            pass
        else:
            with open(self.__file_path) as fread:
                json.load(fread, self.__objects)
            
