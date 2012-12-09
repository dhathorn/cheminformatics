#!/usr/bin/python
import pprint
import sys
import xml.etree.ElementTree as ET
import print_for_matlab

PROPERTIES_FILENAME = "properties.txt"

def get_data(root):
    data = []
    compound_id = root.find("PC-Compound_id").find("PC-CompoundType").find("PC-CompoundType_id").find("PC-CompoundType_id_cid").text
    data.append(("id", "", compound_id))

    pc_compound_charge = root.find("PC-Compound_charge").text
    data.append(("charge", "", pc_compound_charge))

    pc_compound_props = root.find("PC-Compound_props")

    for info_data in pc_compound_props.findall("PC-InfoData"):
        label = info_data[0].find("PC-Urn").find("PC-Urn_label").text
        try:
            name = info_data[0].find("PC-Urn").find("PC-Urn_name").text
        except:
            name = ''
        value = info_data[1][0].text

        if properties.has_key(label + "|" + name):
            data.append((label, name, value))

    pc_count = root.find("PC-Compound_count")[0]
    if (len(pc_count) == 10):
        for e in pc_count:
            data.append((e.tag.lstrip("PC-Count_"), "", e.text))
        return data
    else:
        print "ERROR"
        return None


if __name__ == '__main__':
    properties = {}
    properties_file = open(PROPERTIES_FILENAME, "r")
    for l in properties_file:
        properties[l.strip()] = 1

    file_name = sys.argv[1]
    out_file_name = file_name.rstrip('.xml') + '.out'
    tree = ET.parse(file_name)
    print "parse of %s complete" % file_name
    root = tree.getroot()
    out_file = open(out_file_name, 'w')
    printer = print_for_matlab.print_for_matlab()

    if root.find("PC-Compound") is None:
        data = get_data(root)
        printer.print_to_file(data, out_file)
    else:
        for compound_root in root.findall("PC-Compound"):
            data = get_data(compound_root)
            printer.print_to_file(data, out_file)

    out_file.close()
