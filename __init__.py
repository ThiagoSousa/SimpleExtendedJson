from decoder import JsonDecoder
from json.decoder import JSONDecodeError


# loads the string as json reading
def loads(string):
    return JsonDecoder.decode(string)


# load the json from file
def load(f):
    string = open(f, "r").read().decode("utf-8")
    return loads(string)