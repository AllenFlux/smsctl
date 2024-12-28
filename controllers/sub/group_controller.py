import requests
from requests_toolbelt import MultipartEncoder

from core import settings

"""http://192.168.1.14:8822/api/v1/sms/sub/group/list"""
def controller_sub_group_list(sub_user_id):
    url = settings.url_prefix + "sms/sub/group/list"
    resp = requests.get(url, json={"sub_user_id":sub_user_id})
    if resp.status_code != 200:
        raise Exception(resp.status_code)
    return resp.json()

def controller_sub_group_create(group_name, project_id,sub_user_id):
    url = settings.url_prefix + "sms/sub/group"
    resp = requests.post(url, json={"group_name":group_name,"project_id": project_id, "sub_user_id":sub_user_id})
    if resp.status_code != 200:
        raise Exception(resp.status_code)
    return resp.json()

def allocate_device_2_group(device_id, group_id, sub_user_id):
    url = settings.url_prefix + "sms/sub/device/group"
    resp = requests.post(url,json={"device_id_list":[device_id],"group_id":group_id, "sub_user_id":sub_user_id})
    if resp.status_code != 200:
        raise Exception(resp.status_code)
    return resp.json()

def sub_upload_task(task_name, group_id, sub_user_id, file, timing_start_time, interval_time):
    url  = settings.url_prefix + "sms/sub/task"
    with open(file) as f:
        m = MultipartEncoder(
            fields={'interval_time': interval_time,
                    'timing_start_time': timing_start_time,
                    'sub_user_id': str(sub_user_id),
                    "task_name":task_name,
                    "group_id":str(group_id),
                    'file': ('filename', f.read(), 'text/plain')}
        )
        resp = requests.post(url,
                             data=m,
                             headers={'Content-Type': m.content_type})
    # Save Task ID
    if resp.status_code == 200:
        return resp.json()