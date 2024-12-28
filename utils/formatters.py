import json

import prettytable as pt


def display_project_table(data):
    """
    Displays project data in a tabular format.

    Args:
        data (dict): The project data fetched from the controller.

    Returns:
        PrettyTable: A table displaying project details.
    """
    tb = pt.PrettyTable()

    # Define table headers
    tb.field_names = ["ID", "Name", "Sub User", "Sub User ID", "Note"]

    # Check if the response code is successful
    if data["code"] == 0:
        data_rows = data["data"]["data"]
    else:
        data_rows = data

    # Populate the table with project data
    for row in data_rows:
        tb.add_row([row["id"], row["name"], row["associated_account"], row["associated_account_id"], row["note"]])

    return tb

def display_project_creation_response(data):
    """
    Displays the project creation response in a tabular format.

    Args:
        data (dict): The response data from the project creation request.

    Returns:
        PrettyTable: A table displaying the creation response.
    """
    tb = pt.PrettyTable()
    tb.field_names = ["Code", "Message", "Data"]
    tb.add_row([data["code"], data["message"], data["data"]])
    return tb


def display_device_list(data):
    """
    Displays the device list in a tabular format.

    Args:
        data (dict): The response data containing device details.

    Returns:
        PrettyTable | dict: A table displaying the device list if the request is successful,
                            otherwise, returns the error response.
    """
    if data["code"] != 0:
        return data

    data_row = data["data"]["data"]
    tb = pt.PrettyTable()
    tb.field_names = ["ID", "Device Number", "Number", "Project ID", "Project Name", "Sub User", "Sent Status"]
    for row in data_row:
        tb.add_row([
            row["id"],
            row["device_number"],
            row["number"],
            row["project_id"],
            row["assigned_items"],
            row["owner_account"],
            row["sent_status"]
        ])
    return tb

def display_device_list_for_sub_user(data):
    """
    Displays the device list for a sub-user in a tabular format.

    Args:
        data (dict): The response data containing device details.

    Returns:
        PrettyTable | dict: A table displaying the device list if the request is successful,
                            otherwise, returns the error response.
    """
    if data["code"] != 0:
        return data

    data_row = data["data"]["data"]
    tb = pt.PrettyTable()
    tb.field_names = ["ID", "Device Number", "Number", "Project ID", "Project Name", "Sub User", "Sent Status"]
    for row in data_row:
        tb.add_row([
            row["id"],
            row["device_number"],
            row["number"],
            row["project_id"],
            row["assigned_items"],
            row["owner_account"],
            row["sent_status"]
        ])
    return tb

def display_device_allocation_result(data):
    """
    Displays the result of the device allocation operation in a tabular format.

    Args:
        data (dict): The response data from the device allocation operation.

    Returns:
        PrettyTable | dict: A table displaying the allocation result if successful,
                            otherwise, returns the error response.
    """
    tb = pt.PrettyTable()
    tb.field_names = ["Code", "Message", "Data"]
    tb.add_row([data.get("code"), data.get("message"), data.get("data")])
    return tb

def display_group_list(data):
    """
    Displays the list of groups in a tabular format.

    Args:
        data (dict): The response data containing group details.

    Returns:
        PrettyTable | dict: A table displaying the group list if successful,
                            otherwise, returns the error response.
    """
    tb = pt.PrettyTable()

    if data["code"] != 0:
        tb.field_names = ["Code", "Message", "Data"]
        tb.add_row([data.get("code"), data.get("message"), data.get("data")])
        return tb

    data_row = data["data"]["data"]
    tb.field_names = ["Group ID", "Group Name", "Project ID"]
    for row in data_row:
        tb.add_row([row.get("group_id"), row.get("group_name"), row.get("project_id")])
    return tb


def display_group_creation_result(data):
    """
    Displays the result of the group creation process in a tabular format.

    Args:
        data (dict): The response data containing the result of the group creation.

    Returns:
        PrettyTable: A table displaying the response details.
    """
    tb = pt.PrettyTable()
    tb.field_names = ["Code", "Message", "Data"]
    tb.add_row([data.get("code"), data.get("message"), data.get("data")])
    return tb

def display_task_upload_result(data):
    """
    Displays the result of the task upload process in a tabular format.

    Args:
        data (dict): The response data containing the result of the task upload.

    Returns:
        PrettyTable: A table displaying the response details.
    """
    tb = pt.PrettyTable()
    tb.field_names = ["Code", "Message", "Data"]
    tb.add_row([data.get("code"), data.get("message"), data.get("data")])
    return tb

def convert_task_status_to_text(status):
    """
    Converts a task status code into a human-readable text.

    Args:
        status (int): The status code of the task.

    Returns:
        str: The corresponding text for the task status.
    """
    status_map = {
        1: "Not Started",
        2: "Working On It",
        3: "Done",
        4: "Canceled"
    }
    return status_map.get(status, "Unknown Status")


def format_tasks_table(data):
    """
    Formats the task data into a pretty table.

    Args:
        data (dict): The API response data containing task details.

    Returns:
        pt.PrettyTable or dict: A formatted table of task details if successful, otherwise the raw error response.
    """
    # Check for errors in the response
    if data["code"] != 0:
        return data

    # Extract task data
    data_rows = data["data"]["data"]

    # Initialize pretty table
    tb = pt.PrettyTable()
    tb.field_names = ["ID", "Task Name", "File Name", "Status", "Total", "Remaining", "Sub User"]

    # Populate table rows
    for row in data_rows:
        status = convert_task_status_to_text(int(row["task_status"]))  # Convert status code to human-readable text
        tb.add_row([
            row["id"],
            row["task_name"],
            row["file_name"],
            status,
            row["sms_quantity"],
            row["surplus_quantity"],
            row["associated_account"]
        ])

    return tb


def format_sub_tasks_table(data):
    """
    Formats sub-user task data into a pretty table.

    Args:
        data (dict): The API response data containing task details.

    Returns:
        pt.PrettyTable or dict: A formatted table of sub-user task details if successful, otherwise the raw error response.
    """
    # Check for errors in the response
    if data["code"] != 0:
        return data

    # Extract task data
    data_rows = data["data"]["data"]

    # Initialize pretty table
    tb = pt.PrettyTable()
    tb.field_names = ["ID", "Task Name", "File Name", "Status", "Total", "Remaining", "Sub User"]

    # Populate table rows
    for row in data_rows:
        status = convert_task_status_to_text(int(row["task_status"]))  # Convert status code to human-readable text
        tb.add_row([
            row["id"],
            row["task_name"],
            row["file_name"],
            status,
            row["sms_quantity"],
            row["surplus_quantity"],
            row["associated_account"]
        ])

    return tb

def decode_task_file_content(data):
    """
    Decodes the downloaded task file content and formats it into a table.

    Args:
        data (dict): The response data containing the JSON content.

    Returns:
        tuple: A PrettyTable object displaying the content and a dictionary of the parsed JSON data.
    """
    if "data" not in data or "json_data" not in data["data"]:
        raise ValueError("Invalid data format. Expected 'data' with 'json_data' key.")

    # Parse JSON content
    dict_data = json.loads(data["data"]["json_data"])

    # Create PrettyTable for displaying the data
    tb = pt.PrettyTable()
    tb.field_names = ["No", "Target Phone Number", "Content"]

    for i, (phone, content) in enumerate(zip(dict_data["target_phone_number"], dict_data["content"])):
        tb.add_row([i, phone, content])

    return tb, dict_data

def truncate_text(text, max_length=20):
    """
    Truncates the given text if it exceeds the maximum length.

    Args:
        text (str): The input text to truncate.
        max_length (int): The maximum allowed length of the text.

    Returns:
        str: The truncated text with "..." appended if it exceeds max_length.
    """
    return text[:max_length] + "..." if len(text) > max_length else text

def send_status_to_text(status):
    """
    Converts the SMS send status to its corresponding text description.

    Args:
        status (int): The SMS send status code (1 for Success, 2 for Failed).

    Returns:
        str: The corresponding text description of the status.
    """
    status_map = {
        1: "Success",
        2: "Failed"
    }
    return status_map.get(status, "Unknown Status")

def format_sms_record_list(data):
    """
    Formats the SMS record list data into a PrettyTable.

    Args:
        data (dict): The SMS record list data from the controller.

    Returns:
        PrettyTable: A table representation of the SMS records.
    """
    tb = pt.PrettyTable()
    tb.field_names = ["id", "task_name", "task_id", "target_phone_number",
                      "device_number", "sms_status", "reason", "content"]

    for row in data:
        tb.add_row([
            row["id"],
            row["task_name"],
            row["sub_task_id"],
            row["target_phone_number"],
            row["device_number"],
            send_status_to_text(int(row["sms_status"])),
            row["reason"],
            truncate_text(row["sms_content"])
        ])
    return tb

def validate_sms_record_response(data):
    """
    Validates the response for SMS record fetching.

    Args:
        data (dict): The response data from the controller.

    Returns:
        dict or None: The raw error response data, or None if no error.
    """
    if data["code"] != 0:
        return data
    return None

def extract_sms_record_list(data):
    """
    Extracts the SMS record list from the response data.

    Args:
        data (dict): The response data from the controller.

    Returns:
        list: The list of SMS records.
    """
    return data["data"]["data"]


def format_sub_user_sms_records(records):
    """
    Formats the SMS record list into a PrettyTable.

    Args:
        records (list): The list of SMS record data.

    Returns:
        PrettyTable: A PrettyTable object with formatted SMS records.
    """
    table = pt.PrettyTable()
    table.field_names = ["ID", "Task Name", "Task ID", "Target Phone Number", "Device Number", "SMS Status", "Reason",
                         "Content"]

    for record in records:
        table.add_row([
            record["id"],
            record["task_name"],
            record["sub_task_id"],
            record["target_phone_number"],
            record["device_number"],
            send_status_to_text(int(record["sms_status"])),
            record["reason"],
            truncate_text(record["sms_content"])
        ])

    return table

def validate_conversation_record_response(data):
    """
    Validates the response for conversation record fetching.

    Args:
        data (dict): The response data from the controller.

    Returns:
        dict or None: The raw error response data, or None if no error.
    """
    if data["code"] != 0:
        return data
    return None


def extract_conversation_record_list(data):
    """
    Extracts the conversation record list from the response data.

    Args:
        data (dict): The response data from the controller.

    Returns:
        list: The list of conversation records.
    """
    return data["data"]["data"]


def get_sent_or_receive_status(status_code):
    """
    Maps the sent/receive status code to a descriptive string.

    Args:
        status_code (int): The status code (1 for Sent, 2 for Received).

    Returns:
        str: A descriptive string for the status.
    """
    status_mapping = {
        1: "Sent",
        2: "Received"
    }
    return status_mapping.get(status_code, "Unknown")

def format_conversation_records(records):
    """
    Formats the conversation records into a PrettyTable.

    Args:
        records (list): The list of conversation record data.

    Returns:
        PrettyTable: A PrettyTable object with formatted conversation records.
    """
    table = pt.PrettyTable()
    table.field_names = ["Chat Log ID", "Sent/Receive", "Target Phone Number", "Content", "Record Time"]

    for record in records:
        table.add_row([
            record["chat_log_id"],
            get_sent_or_receive_status(record["sent_or_receive"]),
            record["target_phone_number"],
            truncate_text(record["content"]),
            record["record_time"]
        ])

    return table


def format_conversation_record(data_row):
    """
    Formats a single conversation record into a PrettyTable.

    Args:
        data_row (list): List of conversation record dictionaries.

    Returns:
        PrettyTable: A table formatted for display.
    """
    tb = pt.PrettyTable()
    tb.field_names = ["chat_log_id", "sent_or_receive", "target_phone_number", "content", "record_time"]

    # Populate the table with data
    for row in data_row:
        tb.add_row([
            row["chat_log_id"],
            get_sent_or_receive_status(row["sent_or_receive"]),
            row["target_phone_number"],
            truncate_text(row["content"]),
            row["record_time"]
        ])

    return tb

def format_post_response(data):
    """
    Formats the response from posting a conversation record into a PrettyTable.

    Args:
        data (dict): The response data from the server.

    Returns:
        PrettyTable: A table formatted for display.
    """
    tb = pt.PrettyTable()
    tb.field_names = ["Unsent Task Number", "Task Item Name (DeviceNumber)"]

    # Populate the table with response data
    tb.add_row([data["un_send_task_num"], data["task_item_name"]])

    return tb