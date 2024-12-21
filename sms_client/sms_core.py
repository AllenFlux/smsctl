import json

from controller_main.controller_main_device_list import controller_main_device_list
from controller_main.controller_main_project_list import controller_main_project_list, controller_main_project_create, \
    allocate_device_2_project
import prettytable as pt

from controller_main.controller_main_sms_record_list import controller_main_sms_record_list, \
    controller_main_sms_list_chat
from controller_main.controller_main_sms_report_list import controller_main_sms_report_list, \
    controller_main_download_task
from controller_sub.controller_sub_device_list import controller_sub_device_list
from controller_sub.controller_sub_group import controller_sub_group_list, controller_sub_group_create, \
    allocate_device_2_group, sub_upload_task
from controller_sub.controller_sub_sms import controller_sub_sms_record_list, controller_sub_sms_report_list, \
    sub_get_conversation_record_list, sub_get_conversation_record, sub_post_conversation_record


def m_list_project(page):
    data = controller_main_project_list(page)
    tb = pt.PrettyTable()
    if data["code"] == 0:
        data_row = data["data"]["data"]
    else:
        data_row = data
    tb.field_names = ["id", "name", "sub_user", "sub_user_id", "note"]
    for row in data_row:
        tb.add_row([row["id"], row["name"], row["associated_account"], row["associated_account_id"], row["note"]])

    return tb

def m_create_project(project_name, note):
    data = controller_main_project_create(project_name=project_name, note=note)
    tb = pt.PrettyTable()
    tb.field_names = ["code", "message", "data"]
    tb.add_row([data["code"], data["message"], data["data"]])
    return tb

def m_list_device_main(page):
    data = controller_main_device_list(page)
    if data["code"] != 0:
        return data
    data_row = data["data"]["data"]
    tb = pt.PrettyTable()
    tb.field_names = ["id", "device_number", "number", "project_id", "project_name", "sub_user", "sent_status"]
    for row in data_row:
        tb.add_row([row["id"], row["device_number"], row["number"], row["project_id"], row["assigned_items"],row["owner_account"], row["sent_status"]])
    return tb

def m_list_device_sub(page, sub_user_id):
    data = controller_sub_device_list(page, sub_user_id)
    if data["code"] != 0:
        return data
    data_row = data["data"]["data"]
    tb = pt.PrettyTable()
    tb.field_names = ["id", "device_number", "number", "project_id", "project_name", "sub_user", "sent_status"]
    for row in data_row:
        tb.add_row([row["id"], row["device_number"], row["number"], row["project_id"], row["assigned_items"],row["owner_account"], row["sent_status"]])
    return tb

def m_allocate_device_2_project(device_id, project_id):
    data = allocate_device_2_project(device_id=device_id, project_id=project_id)
    tb = pt.PrettyTable()
    tb.field_names = ["code", "message", "data"]
    tb.add_row([data["code"], data["message"], data["data"]])
    return tb

def m_list_group(sub_user_id):
    data = controller_sub_group_list(sub_user_id)
    tb = pt.PrettyTable()
    if data["code"] != 0:
        tb.field_names = ["code", "message", "data"]
        tb.add_row([data["code"], data["message"], data["data"]])
        return tb

    data_row = data["data"]["data"]
    tb.field_names = ["group_id", "group_name", "project_id"]
    for row in data_row:
        tb.add_row([row["group_id"], row["group_name"], row["project_id"]])
    return tb

def m_create_group(group_name, project_id, sub_user_id):
    data = controller_sub_group_create(group_name=group_name, project_id=project_id,
                                       sub_user_id=sub_user_id)
    tb = pt.PrettyTable()
    tb.field_names = ["code", "message", "data"]
    tb.add_row([data["code"], data["message"], data["data"]])
    return tb

def m_allocate_device_2_group(device_id,group_id,sub_user_id):
    data = allocate_device_2_group(device_id=device_id, group_id=group_id,
                                   sub_user_id=sub_user_id)
    tb = pt.PrettyTable()
    tb.field_names = ["code", "message", "data"]
    tb.add_row([data["code"], data["message"], data["data"]])
    return tb

def m_sub_upload_task(kwargs):
    data = sub_upload_task(**kwargs)
    tb = pt.PrettyTable()
    tb.field_names = ["code", "message", "data"]
    tb.add_row([data["code"], data["message"], data["data"]])
    return tb

def convert_task_status_2_text(status):
    status_note = "Unknown Status"
    if status == 1:
        status_note = "Not Started"
    elif status == 2:
        status_note = "Working On It"
    elif status == 3:
        status_note = "Done"
    elif status == 4:
        status_note = "Canceled"
    return status_note

def m_list_tasks(page):
    data = controller_main_sms_report_list(page)
    tb = pt.PrettyTable()
    if data["code"] != 0:
        return data
    data_row = data["data"]["data"]
    tb.field_names = ["id", "task_name", "file_name", "task_status", "total", "remaining", "sub_user"]
    for row in data_row:
        status = convert_task_status_2_text(int(row["task_status"]))
        tb.add_row([row["id"], row["task_name"], row["file_name"],status, row["sms_quantity"],row["surplus_quantity"], row["associated_account"]])
    return tb

def m_list_tasks_sub(page, sub_user_id):
    data = controller_sub_sms_report_list(page, sub_user_id)
    tb = pt.PrettyTable()
    if data["code"] != 0:
        return data
    data_row = data["data"]["data"]
    tb.field_names = ["id", "task_name", "file_name", "task_status", "total", "remaining", "sub_user"]
    for row in data_row:
        status = convert_task_status_2_text(int(row["task_status"]))
        tb.add_row([row["id"], row["task_name"], row["file_name"],status, row["sms_quantity"],row["surplus_quantity"], row["associated_account"]])
    return tb

def m_download_task_file(file_name):
    data = controller_main_download_task(file_name)
    return data

def decode_download_task_file(data):
    tb = pt.PrettyTable()
    tb.field_names = ["No", "Target Phone Number", "Content"]
    dict_data = json.loads(data["data"]["json_data"])
    for i in range(len(dict_data["target_phone_number"])):
        tb.add_row([i, dict_data["target_phone_number"][i], dict_data["content"][i]])
    return tb, dict_data

def less_text(text):
    if len(text) > 20:
        return text[:20] + "..."
    return text
def convert_send_status_2_text(status):
    status_note = "Unknown Status"
    if status == 1:
        status_note = "Success"
    elif status == 2:
        status_note = "Failed"
    return status_note

def m_controller_main_sms_record_list(page):
    data = controller_main_sms_record_list(page)
    tb = pt.PrettyTable()
    if data["code"] != 0:
        return data
    data_row = data["data"]["data"]

    tb.field_names = ["id", "task_name", "task_id", "target_phone_number", "device_number", "sms_status", "reason","content"]
    for row in data_row:
        tb.add_row([row["id"], row["task_name"], row["sub_task_id"], row["target_phone_number"], row["device_number"],
                     convert_send_status_2_text(int(row["sms_status"])), row["reason"],less_text(row["sms_content"])])
    return tb

def m_controller_sub_sms_record_list(page, sub_user_id):
    data = controller_sub_sms_record_list(page, sub_user_id)
    tb = pt.PrettyTable()
    if data["code"] != 0:
        return data
    data_row = data["data"]["data"]

    tb.field_names = ["id", "task_name", "task_id", "target_phone_number", "device_number", "sms_status", "reason",
                      "content"]
    for row in data_row:
        tb.add_row([row["id"], row["task_name"], row["sub_task_id"], row["target_phone_number"], row["device_number"],
                    convert_send_status_2_text(int(row["sms_status"])), row["reason"], less_text(row["sms_content"])])
    return tb

def check_sent_or_receive(sent_or_receive):
    if sent_or_receive == 1:
        return "Sent"
    elif sent_or_receive == 2:
        return "Received"
    return "Unknown"

def m_sub_get_conversation_record_list(sub_user_id, project_id, page):
    data = sub_get_conversation_record_list(sub_user_id, project_id, page)
    if data["code"] != 0:
        return data
    tb = pt.PrettyTable()
    data_row = data["data"]["data"]
    tb.field_names = ["chat_log_id", "sent_or_receive", "target_phone_number", "content", "record_time"]
    for row in data_row:
        tb.add_row([row["chat_log_id"], check_sent_or_receive(row["sent_or_receive"]), row["target_phone_number"], less_text(row["content"]),  row["record_time"]])
    return tb

def m_main_get_conversation_record_list(project_id, page):
    data = controller_main_sms_list_chat(project_id, page)
    if data["code"] != 0:
        return data
    tb = pt.PrettyTable()
    data_row = data["data"]["data"]
    tb.field_names = ["chat_log_id", "sent_or_receive", "target_phone_number", "content", "record_time"]
    for row in data_row:
        tb.add_row([row["chat_log_id"], check_sent_or_receive(row["sent_or_receive"]), row["target_phone_number"], less_text(row["content"]), row["record_time"]])
    return tb

def m_sub_get_conversation_record(chat_log_id):
    data = sub_get_conversation_record(chat_log_id)
    if data["code"] != 0:
        return data
    tb = pt.PrettyTable()
    data_row = data["data"]["data"]
    tb.field_names = ["chat_log_id", "sent_or_receive", "target_phone_number", "content","record_time"]
    for row in data_row:
        tb.add_row([row["chat_log_id"], check_sent_or_receive(row["sent_or_receive"]), row["target_phone_number"],
                    less_text(row["content"]),row["record_time"]])
    return tb

def m_sub_post_conversation_record(chat_log_id, text):
    data = sub_post_conversation_record(chat_log_id, text)
    if data["code"] != 0:
        return data
    data = data["data"]
    tb = pt.PrettyTable()
    tb.field_names = ["un_send_task_num", "task_item_name(DeviceNumber)"]
    tb.add_row([data["un_send_task_num"], data["task_item_name"]])
    return tb