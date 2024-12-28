import requests

from core import settings

"""http://192.168.1.14:8822/api/v1/sms/task/list"""

def controller_main_sms_report_list(page):
    url = settings.url_prefix + "sms/task/list"
    resp = requests.get(url, json={"pageNum": page})
    if resp.status_code != 200:
        raise Exception(resp.status_code)
    return resp.json()

def controller_main_download_task(file_name):
    url = settings.url_prefix + "sms/task/file"
    resp = requests.post(url, json={"file_name": file_name})
    if resp.status_code != 200:
        raise Exception(resp.status_code)
    return resp.json()