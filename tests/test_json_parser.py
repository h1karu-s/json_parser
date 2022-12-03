import unittest
import sys
sys.path.append('../json_parser')
from json_parser import JsonParser

class TestCSVPrinter(unittest.TestCase):

    def test_read(self):
        parser = JsonParser("./tables.json")
        flag = parser.read()
        self.assertEqual("Ok", flag)
    
    def test_get(self):
        parser = JsonParser("./tables.json")
        parser.read()
        data = parser.get_json()
        self.assertEqual(5, len(data))
    
    def test_get_type(self):
        parser = JsonParser("./tables.json")
        parser.read()
        t = parser.get_type()
        self.assertEqual("list", t)



if __name__ == "__main__":
    unittest.main()