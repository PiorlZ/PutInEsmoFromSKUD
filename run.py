from Comper_lib.Export_From_SCUD import export_from_scud
from Comper_lib.Export_From_ESMO import export_from_esmo
from Comper_lib.RenameTags import rename_tags
from Comper_lib.RemoveTagsFromESMO import clean_tags
from Comper_lib.Difference import DiffXML
from Comper_lib.POST_API_ESMO import post_esmo

if __name__ == '__main__':
    export_from_scud()
    export_from_esmo()
    rename_tags(system='SCUD')
    rename_tags(system='ESMO')
    clean_tags()
    if DiffXML():
        post_esmo()
    else:
        print('Нет изменений')