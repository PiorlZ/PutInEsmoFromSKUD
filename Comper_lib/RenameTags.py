from Comper_lib.settings import PATH_FILE_NAME_OUTPUT_FROM_SCUD, PATH_FILE_NAME_OUTPUT_FROM_ESMO, SCUD_LIST, ESMO_LIST


def replace(file_path, pattern, subst):
    from os import fdopen, remove
    from tempfile import mkstemp
    from shutil import move, copymode
    fh, abs_path = mkstemp()
    with fdopen(fh, 'w', encoding='utf-8') as new_file:
        with open(file_path, encoding='utf-8') as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    copymode(file_path, abs_path)
    remove(file_path)
    move(abs_path, file_path)


def add(x, y):
    _dict = [{'was': '<' + x + '>', 'need': '<' + y + '>'}, {'was': '</' + x + '>', 'need': '</' + y + '>'}]
    return _dict


def rename_tags(scud_list=SCUD_LIST, esmo_list=ESMO_LIST,
                scud_file=PATH_FILE_NAME_OUTPUT_FROM_SCUD, esmo_file=PATH_FILE_NAME_OUTPUT_FROM_ESMO, system=None):
    if system is None:
        print('Не указана система. Должно быть значение "ESMO" или "SCUD"')
        exit(-1)
    if system == 'SCUD':
        _dict = []
        for i in scud_list:
            _dict += add(i['was'], i['need'])
        for i in _dict:
            replace(scud_file, i['was'], i['need'])  # Замена неправильных блоков на нужные для ЭСМО
    if system == 'ESMO':
        _dict = []
        for i in esmo_list:
            _dict += add(i['was'], i['need'])
        for i in _dict:
            replace(esmo_file, i['was'], i['need'])  # Замена неправильных блоков на нужные для ЭСМО
