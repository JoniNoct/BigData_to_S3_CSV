import lxml.etree as ET

def fix_xml(source):
    #parser = ET.XMLParser(encoding="windows-1251")
    tree = ET.fromstring(source)

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
    # return  ET.tostring(tree, encoding='windows-1251')

    # write out to new file
    newfile = "Output/Temp/UO_FULL/file.xml"
    with open(newfile, 'w') as f:
        f.write("<?xml version=\"1.0\" encoding=\"windows-1251\"?>\n")
        f.write(ET.tostring(tree, pretty_print=True).decode())
    print('Writing', newfile)

