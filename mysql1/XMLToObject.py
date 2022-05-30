import xmltodict
import json

class Helper:

    @staticmethod
    def dict2obj(d):
        return json.loads(json.dumps(d), object_hook=Obj)

class Obj(object):
    def __init__(self, dict_):
        self.__dict__.update(dict_)

class XmlToObject:
    def __init__(self, xml_filename):
        self.xml_filename = xml_filename

    def to_object(self):
        with open(self.xml_filename, "rb") as fd:
            dictionary = xmltodict.parse(fd.read())
            return Helper.dict2obj(dictionary)