import lxml.etree as ET


def fix_xml(source, destination='file.xml'):
    """Fix XML file from trouble chars

    :param source: One-string xml content to fix
    :param destination: Full path to result file
    :return: None
    """
    # Parsing source content
    parser = ET.XMLParser(huge_tree=True, recover=True)
    tree = ET.fromstring(source, parser)

    # Main fix part
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

    # Write out to new file
    with open(destination, 'wb') as f:
        # f.write("<?xml version=\"1.0\" encoding=\"windows-1251\"?>\n".encode('windows-1251'))
        f.write(ET.tostring(tree, encoding='windows-1251', pretty_print=True))
    print('Writing', destination)
