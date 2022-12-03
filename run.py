from src.json_parser import JsonParser

parser = JsonParser("./tables.json")
parser.read()
parser.parsing()