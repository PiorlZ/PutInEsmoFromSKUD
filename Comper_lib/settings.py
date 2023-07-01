from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent
FOLDER = 'files'
FILE_NAME_RESULT = 'result.xml'
PATH_FILE_RESULT = os.path.join(BASE_DIR, FOLDER, FILE_NAME_RESULT)
FILE_NAME_PUT = 'put.bat'
PATH_FILE_PUT = os.path.join(BASE_DIR, FOLDER, FILE_NAME_PUT)


FILE_NAME_OUTPUT_FROM_SCUD = 'SCUD.xml'
PATH_FILE_NAME_OUTPUT_FROM_SCUD = os.path.join(BASE_DIR, FOLDER, FILE_NAME_OUTPUT_FROM_SCUD)
SCUD_SCHEMA = 'C##SCOTT/tiger'
SOURCE_TABLE = 'C##SCOTT.PERSON1'
SCUD_LIST = [
    {'was': 'NAME', 'need': 'Name'},
    {'was': 'UID1', 'need': 'uid'},
    {'was': 'ORG', 'need': 'Org'},
    {'was': 'DRIVERLICENSE', 'need': 'DriverLicense'},
    {'was': 'DR', 'need': 'Dr'},
    {'was': 'POL', 'need': 'Pol'},
    {'was': 'PHONE', 'need': 'Phone'},
    {'was': 'PROPUSK', 'need': 'Propusk'},
    {'was': 'TABNUMBER', 'need': 'TabNumber'},
    {'was': 'PERMIT', 'need': 'Permit'},
    {'was': 'PERSONLICENSE', 'need': 'PersonLicense'},
    {'was': 'DATAMEDSPRAVKA', 'need': 'DataMedSpravka'},
    {'was': 'STRUCTUR', 'need': 'Structure'},
    {'was': 'WORKING', 'need': 'Working'},
    {'was': 'ENABLED', 'need': 'Enabled'},
    {'was': 'FIRED', 'need': 'Fired'},
]
IGNORE_LIST = [
]


URL_POST_ESMO = ''
URL_GET_ESMO = ''
FILE_NAME_OUTPUT_FROM_ESMO = 'ESMO.xml'
PATH_FILE_NAME_OUTPUT_FROM_ESMO = os.path.join(BASE_DIR, FOLDER, FILE_NAME_OUTPUT_FROM_ESMO)
ESMO_LIST = [
    {'was': 'fio', 'need': 'Name'},
    {'was': 'org_name', 'need': 'Org'},
    {'was': 'dr', 'need': 'Dr'},
    {'was': 'propusk', 'need': 'Propusk'},
    {'was': 'tabnumber', 'need': 'TabNumber'},
    {'was': 'otdel_name', 'need': 'Structure'},
    {'was': 'working', 'need': 'Working'},
    {'was': 'enabled', 'need': 'Enabled'},
]

ESMO_TAGS = [
    {'tag': 'photo'},
    {'tag': 'phone'},
    {'tag': 'age'},
    {'tag': 'org_id'},
    {'tag': 'otdel_id'},
]