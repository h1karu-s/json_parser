import json

class JsonParser:
    def __init__(self, file_name):
        self.name = file_name
    
    def read(self):
        try:
            with open(self.name) as f:
              self.data = json.load(f)
            return "Ok"
        except:
            return "Error"
      
    def get_type(self):
        if isinstance(self.data, dict):
          return "dict"
        if isinstance(self.data, list):
          return "list"

    
    def get_json(self):
        return self.data

            

    # def parsing(self):
    #     if isinstance(self.data, dict):
    #         print('dict型です')
    #         print(self.data.keys())
    #     if isinstance(self.data, list):
    #         print('list型です')
    #         print(f"要素数は{len(self.data)}です")
    #         d = self.data[0]
    #         if isinstance(d, dict):
    #             print(f"その下の階層にはdictになっており、keyは{d.keys()}")
    #         if isinstance(d, list):
    #             print(f"さらに下の階層もlistです。要素は{len(d)}です")