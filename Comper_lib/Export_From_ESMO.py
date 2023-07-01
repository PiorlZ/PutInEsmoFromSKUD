from Comper_lib.settings import FILE_NAME_OUTPUT_FROM_ESMO, FOLDER, URL_GET_ESMO
import os


def export_from_esmo(folder=FOLDER, name=FILE_NAME_OUTPUT_FROM_ESMO, url=URL_GET_ESMO):
    import pycurl
    if not os.path.exists(folder):
        os.mkdir(folder)
    file_name = os.path.join(folder, name)
    c = pycurl.Curl()
    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.SSL_VERIFYPEER, 0)
    c.setopt(pycurl.SSL_VERIFYHOST, 0)
    xml = c.perform_rs()
    my_file = open(file_name, 'w', encoding='utf-8')
    my_file.write(xml)
    my_file.close()
