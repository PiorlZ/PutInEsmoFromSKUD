from Comper_lib.settings import PATH_FILE_RESULT, URL_POST_ESMO
import requests
from requests.structures import CaseInsensitiveDict
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def post_esmo(url=URL_POST_ESMO):
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    data = open(PATH_FILE_RESULT, encoding='latin1')
    resp = requests.post(url, headers=headers, data=data, verify=False)
    print(resp.text)
