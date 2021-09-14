import lxml.etree as ET

def fix_xml(source, filename='file', index=1):
    #parser = ET.XMLParser(encoding="windows-1251")
    parser = ET.XMLParser(huge_tree = True, recover = True)
    tree = ET.fromstring(source, parser)

    for element in tree.xpath('.//*[@CONTENT=""]'):
        element.getparent().remove(element)

    for element in tree.xpath('.//*[count(child::*) = 0]'):
        if 'TextLine' in element.tag:
            element.getparent().remove(element)

    for element in tree.xpath('.//*[count(child::*) = 0]'):
        if 'TextBlock' in element.tag:
            element.getparent().remove(element)

    for element in tree.xpath('.//*[count(child::*) = 0]'):
        if 'ComposedBlock' in element.tag:
            element.getparent().remove(element)

    # write out to new file
    new_file = "Output/Temp/UO_FULL/"+filename+"_part_"+str(index)+".xml"
    with open(new_file, 'wb') as f:
        #f.write("<?xml version=\"1.0\" encoding=\"windows-1251\"?>\n".encode('windows-1251'))
        f.write(ET.tostring(tree, encoding='windows-1251', pretty_print=True))
    print('Writing', new_file)