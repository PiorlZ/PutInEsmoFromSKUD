import xml.etree.ElementTree as ET
import cx_XML
from Comper_lib.settings import PATH_FILE_NAME_OUTPUT_FROM_ESMO, PATH_FILE_NAME_OUTPUT_FROM_SCUD, PATH_FILE_RESULT


def get_data(file=None):
    root_node = ET.parse(file).getroot()
    result = []
    for tag in root_node.findall('item'):
        _list = []
        for el in tag:
            obj = [{'tag': el.tag, 'value': str(el.text).strip()}]
            _list += obj
        result += [_list]
    return result


def comp(scud_file=PATH_FILE_NAME_OUTPUT_FROM_SCUD, esmo_file=PATH_FILE_NAME_OUTPUT_FROM_ESMO):
    data = get_data(file=scud_file)     # Достаём данные СКУДа
    data1 = get_data(file=esmo_file)        # Достаём данные ЭСМО
    data2 = []    # Формируем разницу
    for row in data:
        for i in row:
            if i['tag'] == 'uid':   # Определяем тег uid
                value = i['value']  # Определяем тег value (Значение тэга)
                human = False   # Задаём порядок сравнения (Если False, то сравнение по uid)
                for row1 in data1:
                    for i1 in row1:
                        if i1['tag'] == 'uid':  # Если uid совпал, сравниваем остальные значения
                            if value == i1['value']:
                                for k in row:    # Если есть разница в остальных значениях (кроме uid), то..
                                    for u in row1:
                                        if k['tag'] == u['tag']:
                                            if k['value'] != u['value']:
                                                row1 = row  # Записываем разницу
                                                data2 += [row]
                                            else:
                                                human = True    # Если True, то ищем новые записи
                                                break
                if not human:
                    data2 += [row]    # Записываем новые данные
    return data2


def DiffXML(name=PATH_FILE_RESULT, scud_file=PATH_FILE_NAME_OUTPUT_FROM_SCUD, esmo_file=PATH_FILE_NAME_OUTPUT_FROM_ESMO):
    data = comp(scud_file, esmo_file)
    if not data:
        flag = False
    else:
        flag = True
    output_file = open(name, "w", encoding='utf-8')
    writer = cx_XML.Writer(output_file, numSpaces=4)
    writer.StartTag("Persons")
    for row in data:
        writer.StartTag("Person")
        for i in row:
            writer.WriteTagWithValue(i['tag'], i['value'])
        writer.EndTag()
    writer.EndTag()
    output_file.close()
    return flag