#!/bin/usr/python3
import sys, zipfile
from oletools import oleobj, ooxml

filename = sys.argv[1]
if zipfile.is_zipfile(filename):
    xml_parser = ooxml.XmlParser(filename)
    for relationship, target in oleobj.find_external_relationships(xml_parser):
        print("Found relationship '%s' with external link %s" % (relationship, target))
        if target.startswith('mhtml:'):
            print("Potential exploit for CVE-2021-40444")
else:
    print("This is not an Office 2007+ file.")