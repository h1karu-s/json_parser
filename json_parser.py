import json

class JsonParser:
    def __init__(self, file_name):
        self.name = file_name
    
    def read(self):
        try:
            with open(self.name) as f:
              self.data = json.load(f)
            return "Ok"
        except Exception as e:
            print(e)
            return "Error"
      
    def get_type(self):
        if isinstance(self.data, dict):
          return "dict"
        if isinstance(self.data, list):
          return "list"

    def get_json(self):
        return self.data
