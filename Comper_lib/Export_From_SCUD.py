import os
from Comper_lib.settings import SCUD_SCHEMA,\
    PATH_FILE_NAME_OUTPUT_FROM_SCUD, SOURCE_TABLE, FOLDER,\
    IGNORE_LIST


def export_from_scud(login=SCUD_SCHEMA, table=SOURCE_TABLE,
                     file_name=PATH_FILE_NAME_OUTPUT_FROM_SCUD, folder=FOLDER, ignore=IGNORE_LIST):
    import cx_Oracle
    import cx_XML
    if not os.path.exists(folder):
        os.mkdir(folder)
    connection = cx_Oracle.connect(login)
    cursor = connection.cursor()
    query = "SELECT * FROM {0}".format(table)
    k = 0
    for i in ignore:
        k += 1
        if k == len(ignore):
            query += "WHERE {0} NOT LIKE '%{1}%'".format(i['col'], i['field'])
        else:
            query += "WHERE {0} NOT LIKE '%{1}%' AND ".format(i['col'], i['field'])
    cursor.execute(query)
    names = [item[0] for item in cursor.description]
    output_file = open(file_name, "w", encoding='utf-8')
    writer = cx_XML.Writer(output_file, numSpaces=4)
    writer.StartTag("Persons")
    for row in cursor:
        writer.StartTag("item")
        for name, value in zip(names, row):
            if value is None:
                continue
            if isinstance(value, cx_Oracle.ApiType):
                value = str(value)
            writer.WriteTagWithValue(name, value)
        writer.EndTag()
    writer.EndTag()
    output_file.close()
