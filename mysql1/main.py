from lxml import etree
from XMLToObject import XmlToObject
from dummyObjects import dummyObjects
from ObjectToXML import ObjectToXml


if __name__ == "__main__":
    courseList = dummyObjects.create()
    pretty_xml = ObjectToXml(courseList).to_xmlstring()
    with open("courses.xml", "wb") as f:
        f.write(pretty_xml)

    object_from_xml=XmlToObject('courses.xml').to_object()

    courses1=object_from_xml.courses

    print("\nChecking documents:\n")

    dtd = etree.DTD(open('courses.dtd'))
    print("check generated courses.xml", dtd.validate(etree.parse('courses.xml')))
    print("check invalid courses_invalid.xml", dtd.validate(etree.parse('courses_invalid.xml')))




