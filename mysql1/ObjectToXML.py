from xml.dom.minidom import parseString
import jsonpickle
from dicttoxml import dicttoxml
from jsonpickle import json


class ObjectToXml:
    def __init__(self, myobject):
        self.myobject = myobject

    def to_xmlstring(self):

        nested_dict = json.loads(jsonpickle.encode(self.myobject, unpicklable=False))

        def my_item_func(x): return x[:-1]
        xml_string = dicttoxml(nested_dict, root=False, item_func=my_item_func, attr_type=False)

        return parseString(xml_string).toprettyxml(encoding="utf-8")