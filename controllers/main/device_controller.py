import requests

from core import settings


def controller_main_device_list(page):
    url = settings.url_prefix + "sms/device/list"
    resp = requests.get(url, json={"pageNum":page})
    if resp.status_code != 200:
        raise Exception(resp.status_code)
    return resp.json()
