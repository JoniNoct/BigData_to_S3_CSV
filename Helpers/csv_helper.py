import os
import csv
import lxml.etree as ET
from Helpers import fix_xml as fix


def xml_surface_schema(root):
    columns = []
    for child in list(root):
        columns.append(child.tag)
    return columns


def xml_inner_converter(source):
    row = ''
    delim = ';' if (len(list(source)) > 1) and (list(source)[0].tag == list(source)[1].tag) else ':'
    for child in list(source):
        if not list(child):
            if child.text:
                row += child.text + delim
            else:
                row += "None" + delim
        else:
            row += xml_inner_converter(child) + ";"
    return row[:-1]


def xml_main_converter(source, schema):
    row = []
    for item in schema:
        child = source.find(item)
        if child.text:
            row.append(child.text)
        elif list(child):
            row.append(xml_inner_converter(child))
        else:
            row.append("None")
    return row


def xml_to_csv(source, destination, schema_path, enc='windows-1251'):
    """Transform XML content into CSV file

    :param source: One-string xml content to transform
    :param destination: Destination path to save CSV file
    :param schema_path: Path to XML schema
    :param enc: Encoding argument
    :return: None
    """

    # Initializing variables
    shema_parser = ET.XMLParser(encoding=enc)
    source_parser = ET.XMLParser(huge_tree=True, recover=True)
    # Parse schema and source XML contents
    schema_tree = ET.parse(schema_path, shema_parser)
    source_tree = ET.fromstring(source, source_parser)
    # Taking titles
    schema = xml_surface_schema(schema_tree.getroot())
    # Main transformation part and writing csv file
    with open(destination, 'w', newline='', encoding=enc) as output:
        csv_writer = csv.writer(output)
        csv_writer.writerow(schema)
        for subject in list(source_tree):
            row = xml_main_converter(subject, schema)
            csv_writer.writerow(row)
        output.close()


def bigdata_segmentation_csv(source, dest_folder, dest_file, subject_amount=10000, enc='windows-1251'):
    """Splits a large file into smaller csv files

    :param source: File to split
    :param dest_folder: Folder for saving split files
    :param dest_file: Name of split files
    :param subject_amount: Number of objects in each segment
    :param enc: Encoding argument
    :return: None
    """

    # Initializing variables
    upper_rows = []
    content = []
    counter = 0
    index = 1
    if not os.path.exists('Output/Temp/' + dest_folder):
        os.mkdir('Output/Temp/' + dest_folder)
    schema_path = "Resources/Schema/17.1-EX_XML_EDR_UO_FULL.txt" if dest_folder[0] == 'U' else "Resources/Schema/17.2-EX_XML_EDR_FOP_FULL.txt"

    # Basic file splitting work
    with open(source, "r", encoding=enc) as file:
        file.readline()
        # upper_rows.append(file.readline())
        upper_rows.append(file.readline())
        upper_rows = "".join(upper_rows)

        for line in file:
            content.append(line)
            if line.find("</SUBJECT>") != -1:
                counter += 1
            if counter == subject_amount:
                xml_to_csv(upper_rows + "".join(content) + "</DATA>",
                           "Output/Temp/" + dest_folder + "/" + dest_file + "_part_" + str(index) + ".csv", schema_path)
                content = []
                counter = 0
                index += 1
        xml_to_csv(upper_rows + "".join(content) + "</DATA>",
                   "Output/Temp/" + dest_folder + "/" + dest_file + "_part_" + str(index) + ".csv", schema_path)