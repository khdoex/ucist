import xml.dom.minidom
import sys
from subprocess import *
debug = False

def process_xml(xmlString):
    if(len(xmlString)==0): return
    xml_dom = xml.dom.minidom.parseString(xmlString)
    if debug:
        u = xml_dom.toprettyxml(" ")
        print(u.encode('ascii','replace'))
    # ... rest of the code ...