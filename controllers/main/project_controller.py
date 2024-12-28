import requests

from core import settings

"""http://192.168.1.14:8822/api/v1/sms/project/list"""
def controller_main_project_list(page):
    url = settings.url_prefix + "sms/project/list"
    resp = requests.get(url, json={"pageNum": page})
    if resp.status_code != 200:
        raise Exception(resp.status_code)
    return resp.json()

def controller_main_project_list_items(sub_user_id):
    url = settings.url_prefix + "sms/project/items"
    resp = requests.get(url, json={"sub_user_id": sub_user_id})
    if resp.status_code != 200:
        raise Exception(resp.status_code)
    return resp.json()

def controller_main_project_create(project_name, note):
    url = settings.url_prefix + "sms/project"
    resp = requests.post(url, json={"project_name": project_name,"note": note})
    if resp.status_code != 200:
        raise Exception(resp.status_code)
    return resp.json()


def allocate_sub_account_2_project(project_id,account_id):
    url = settings.url_prefix + "sms/account/project"
    resp = requests.post(url, json={"project_id": project_id, "account_id":account_id})
    if resp.status_code != 200:
        raise Exception(resp.status_code)
    return resp.json()


def allocate_device_2_project(device_id, project_id):
    url = settings.url_prefix + "sms/device/project"
    resp = requests.post(url, json={"device_id_list": [device_id], "project_id": project_id})
    if resp.status_code != 200:
        raise Exception(resp.status_code)
    return resp.json()

if __name__ == '__main__':
    print(controller_main_project_list_items(0))