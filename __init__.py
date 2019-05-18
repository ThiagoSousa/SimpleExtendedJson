from .decoder import JsonDecoder
from json.decoder import JSONDecodeError


# loads the string as json reading
def loads(string):
    j = JsonDecoder()
    return j.decode(string)


# load the json from file
def load(f):
    string = open(f, "r").read()
    return loads(string)