import requests

from core import settings


def controller_sub_device_list(page, sub_user_id):
    url = settings.url_prefix + "sms/sub/device/list"
    resp = requests.get(url, json={"pageNum":page, "sub_user_id":sub_user_id})
    if resp.status_code != 200:
        raise Exception(resp.status_code)
    return resp.json()