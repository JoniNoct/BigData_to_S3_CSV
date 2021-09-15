import os


# def has_letter(source):
#     letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     for char in source:
#         for letter in letters:
#             if char == letter:
#                 return True
#     return False
#
# def split_contacts(source):
#     phones = []
#     emails = []
#     websites = []
#     content = [item.strip() for item in source.string.split(";")]
#     source.string = ""
#
#     for item in content:
#         if item.find("@") != -1:
#             emails.append(item)
#         elif not has_letter(item):
#             phones.append(item)
#         else:
#             websites.append(item)
#     if phones:
#         for phone in phones:
#             tag = Tag(builder=source.builder, is_xml=True, name='CONTACTS-PHONE')
#             tag.string = phone
#             source.append(tag)
#     if emails:
#         for email in emails:
#             tag = Tag(builder=source.builder, is_xml=True, name='CONTACTS-EMAIL')
#             tag.string = email
#             source.append(tag)
#     if websites:
#         for website in websites:
#             tag = Tag(builder=source.builder, is_xml=True, name='CONTACTS-WEBSITE')
#             tag.string = website
#             source.append(tag)
#     #return source
#
# def bigdata_segmentation(source, dest_folder, dest_file, subject_amount=20000):
#     """Splits a large file into smaller files
#
#     :param source: File to split
#     :param dest_folder: Folder for saving split files
#     :param dest_file: Name of split files
#     :param subject_amount: Number of objects in each segment
#     :return: None
#     """
#
#     # Initializing variables
#     upper_rows = []
#     content    = []
#     counter    = 0
#     index      = 1
#     if not os.path.exists('Output/Temp/' + dest_folder):
#         os.mkdir('Output/Temp/' + dest_folder)
#
#     # Basic file splitting work
#     with open(source,"r", encoding="windows-1251") as file:
#         upper_rows.append(file.readline())
#         upper_rows.append(file.readline())
#         upper_rows = "".join(upper_rows)
#
#         for line in file:
#             if line.find("</SUBJECT>") != -1:
#                 soup = BeautifulSoup(line, "xml")
#                 contacts = soup.find_all("CONTACTS")
#                 for contact in contacts:
#                     if contact.string is not None:
#                         contact = split_contacts(contact)
#                 # print(soup)
#                 content.append(str(soup.SUBJECT))
#                 counter += 1
#             else:
#                 content.append(line)
#             if counter == subject_amount:
#                 for i in range(len(content)):
#                     if content[i][-1] != '\n' and content[i].find("</DATA>") == -1:
#                         content[i] = content[i] + '\n'
#                 print("+1 file")
#                 with open("Output/Temp/" + dest_folder + "/" + dest_file + "_part_"+str(index)+".xml", "w", encoding="windows-1251") as output:
#                     output.write(upper_rows+"".join(content)+"</DATA>")
#                     output.close()
#                 content = []
#                 counter = 0
#                 index  += 1
#
#         for i in range(len(content)):
#             if content[i][-1] != '\n' and content[i].find("</DATA>") == -1:
#                 content[i] = content[i] + '\n'
#         with open("Output/Temp/" + dest_folder + "/" + dest_file + "_part_"+str(index)+".xml", "w", encoding="windows-1251") as output:
#             output.write(upper_rows + "".join(content))
#             output.close()

def bigdata_segmentation_xml(source, dest_folder, dest_file, subject_amount=20000):
    """Splits a large file into smaller files

    :param source: File to split
    :param dest_folder: Folder for saving split files
    :param dest_file: Name of split files
    :param subject_amount: Number of objects in each segment
    :return: None
    """

    # Initializing variables
    upper_rows = []
    content = []
    counter = 0
    index = 1
    if not os.path.exists('Output/Temp/' + dest_folder):
        os.mkdir('Output/Temp/' + dest_folder)

    # Basic file splitting work
    with open(source, "r", encoding='cp1252') as file:
        upper_rows.append(file.readline())
        upper_rows.append(file.readline())
        upper_rows = "".join(upper_rows)

        for line in file:
            content.append(line)
            if line.find("</SUBJECT>") != -1:
                counter += 1
            if counter == subject_amount:
                with open("Output/Temp/" + dest_folder + "/" + dest_file + "_part_" + str(index) + ".xml", "w",
                          encoding='cp1252') as output:
                    output.write(upper_rows + "".join(content) + "</DATA>")
                    output.close()
                content = []
                counter = 0
                index += 1
        with open("Output/Temp/" + dest_folder + "/" + dest_file + "_part_" + str(index) + ".xml", "w",
                  encoding='cp1252') as output:
            output.write(upper_rows + "".join(content) + "</DATA>")
            output.close()
