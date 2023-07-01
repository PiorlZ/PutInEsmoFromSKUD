from Comper_lib.settings import PATH_FILE_NAME_OUTPUT_FROM_ESMO, ESMO_TAGS
from xml.etree import cElementTree as ET


def clean_tags(filepath=PATH_FILE_NAME_OUTPUT_FROM_ESMO, tags=ESMO_TAGS):
    tree = ET.parse(filepath)
    root = tree.getroot()
    for i in tags:
        for node in root.iter('item'):
            for bpt in node.findall(i['tag']):
                node.remove(bpt)
    tree.write(filepath, encoding='utf-8')