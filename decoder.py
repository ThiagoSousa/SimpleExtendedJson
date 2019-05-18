import re
import json
from json.decoder import JSONDecodeError


# JSON Decoder class
class JsonDecoder(object):

    def __init__(self, object_hook=None):
        self.object_hook = object_hook

    # class to decode a string of data into a dictionary containing the JSON information
    def decode(self, string):

        # replacing the mongodb objects in the extended json to the strict json version
        # try:
        string = re.sub(r'ObjectId\(\"(\S+)\"\)', r'"\1"', string)
        string = re.sub(r'NumberInt\((\S+)\)', r'\1', string)
        string = re.sub(r'NumberLong\((\S+)\)', r'\1', string)
        string = re.sub(r'NumberDecimal\((\S+)\)', r'\1', string)
        string = re.sub(r'Date\((\S+)\)', r'{"date":"\1"}', string)
        string = re.sub(r'Timestamp\((\S+)[,][ ]*(\S+)\)', r'{"timestamp":{"t":"\1","i":"\2"}}', string)
        string = re.sub(r'BinData\((\S+)[,][ ]*[\"](\S+)[\"]\)', r'{"binary":"\1","type":"\2"}', string)
        string = re.sub(r'DBRef\([\"](\S+)[\"][,][ ]*[\"](\S+)[\"]\)', r'{"ref":"\1","id":"\2"}', string)
        # string = re.sub(r':[ ]*undefined(\}|,)]', r'{"undefined":true}', string)
        # string = re.sub(r':[ ]*MaxKey(\}|,)]', r'{"maxkey":1}', string)
        # string = re.sub(r':[ ]*MinKey(\}|,)]', r'{"minkey":1}', string)
        # string = re.sub(r':[ ]*//\S+//\S+(\}|,)]', r'{"regex":"\1", "options":"\2"}', string)
        # string = re.sub(r':[ ]*//\S+//\S+(\}|,)]', r'{"regex":"\1", "options":"\2"}', string)
        # except Exception as err:
        #     msg = "Could not parse the Extended Json."
        #     raise JSONDecodeError(msg, err)

        # loading the json using the traditional json library
        #try:
        data = json.loads(string, object_hook=self.object_hook)
        #except JSONDecodeError as err:
        #    raise JSONDecodeError(err.msg)

        return data
