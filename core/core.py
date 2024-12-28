from controllers.main.sms_record_controller import controller_main_sms_record_list, \
    controller_main_sms_list_chat
from controllers.main.sms_report_controller import controller_main_download_task
from controllers.sub.sms_controller import sub_get_conversation_record, sub_post_conversation_record
from utils.formatters import display_project_table, display_project_creation_response, display_device_list, \
    display_device_list_for_sub_user, display_device_allocation_result, display_group_list, \
    display_group_creation_result, display_task_upload_result, format_tasks_table, \
    format_sub_tasks_table, format_sms_record_list, validate_sms_record_response, extract_sms_record_list, \
    format_sub_user_sms_records, validate_conversation_record_response, extract_conversation_record_list, \
    format_conversation_records, format_conversation_record, format_post_response
from utils.helpers import fetch_project_data, create_project, fetch_device_list, fetch_device_list_for_sub_user, \
    allocate_device_to_project, fetch_group_list, create_group, allocate_device_to_group, upload_task, fetch_tasks_data, \
    fetch_sub_tasks_data, fetch_sub_user_sms_records, fetch_conversation_record_data


# Example Usage:
# Fetch data and display it
def list_projects_with_details(page):
    """
    Fetches project data and displays it in a formatted table.

    Args:
        page (int): The page number to fetch.

    Returns:
        PrettyTable: A table displaying project details.
    """
    project_data = fetch_project_data(page)
    return display_project_table(project_data)

# Example Usage:
def handle_project_creation(project_name, note):
    """
    Handles the creation of a project and displays the response.

    Args:
        project_name (str): The name of the project to create.
        note (str): Additional notes for the project.

    Returns:
        PrettyTable: A table displaying the creation response.
    """
    response = create_project(project_name, note)
    return display_project_creation_response(response)


# Example Usage:
def handle_device_list(page):
    """
    Fetches and displays the device list for a given page.

    Args:
        page (int): The page number for pagination.

    Returns:
        PrettyTable | dict: A table displaying the device list if the request is successful,
                            otherwise, returns the error response.
    """
    response = fetch_device_list(page)
    return display_device_list(response)


# Example Usage:
def handle_device_list_for_sub_user(page, sub_user_id):
    """
    Fetches and displays the device list for a sub-user.

    Args:
        page (int): The page number for pagination.
        sub_user_id (int): The ID of the sub-user.

    Returns:
        PrettyTable | dict: A table displaying the device list if the request is successful,
                            otherwise, returns the error response.
    """
    response = fetch_device_list_for_sub_user(page, sub_user_id)
    return display_device_list_for_sub_user(response)

# Example Usage:
def handle_device_allocation_to_project(device_id, project_id):
    """
    Handles the device allocation to a project by fetching the response
    and displaying it in a tabular format.

    Args:
        device_id (int): The ID of the device to allocate.
        project_id (int): The ID of the project to which the device will be allocated.

    Returns:
        PrettyTable | dict: A table displaying the allocation result if successful,
                            otherwise, returns the error response.
    """
    response = allocate_device_to_project(device_id, project_id)
    return display_device_allocation_result(response)


def list_user_groups(sub_user_id):
    """
    Handles fetching and displaying the list of groups for a given sub-user ID.

    Args:
        sub_user_id (int): The ID of the sub-user whose groups will be listed.

    Returns:
        PrettyTable | dict: A table displaying the group list if successful,
                            otherwise, returns the error response.
    """
    response = fetch_group_list(sub_user_id)
    return display_group_list(response)


def handle_group_creation(group_name, project_id, sub_user_id):
    """
    Handles the group creation process by fetching the response and displaying it.

    Args:
        group_name (str): The name of the group to be created.
        project_id (int): The ID of the project the group is associated with.
        sub_user_id (int): The ID of the sub-user creating the group.

    Returns:
        PrettyTable: A table displaying the group creation result.
    """
    response = create_group(group_name, project_id, sub_user_id)
    return display_group_creation_result(response)


def handle_device_allocation(device_id, group_id, sub_user_id):
    """
    Handles the device allocation process by fetching the response and displaying it.

    Args:
        device_id (int): The ID of the device to be allocated.
        group_id (int): The ID of the group to which the device will be allocated.
        sub_user_id (int): The ID of the sub-user performing the allocation.

    Returns:
        PrettyTable: A table displaying the device allocation result.
    """
    response = allocate_device_to_group(device_id, group_id, sub_user_id)
    return display_device_allocation_result(response)

def handle_task_upload(kwargs):
    """
    Handles the task upload process by uploading the task and displaying the result.

    Args:
        kwargs (dict): The arguments required for uploading the task.

    Returns:
        PrettyTable: A table displaying the task upload result.
    """
    response = upload_task(kwargs)
    return display_task_upload_result(response)


def list_tasks_with_details(page):
    """
    Combines fetching task data and formatting it into a pretty table.

    Args:
        page (int): The page number for task data.

    Returns:
        pt.PrettyTable or dict: A formatted table of task details if successful, otherwise the raw error response.
    """
    # Fetch task data
    data = fetch_tasks_data(page)
    # Format and return the task table
    return format_tasks_table(data)

def list_sub_tasks_with_details(page, sub_user_id):
    """
    Combines fetching sub-user task data and formatting it into a pretty table.

    Args:
        page (int): The page number for task data.
        sub_user_id (int): The ID of the sub-user.

    Returns:
        pt.PrettyTable or dict: A formatted table of sub-user task details if successful, otherwise the raw error response.
    """
    # Fetch sub-user task data
    data = fetch_sub_tasks_data(page, sub_user_id)
    # Format and return the sub-user task table
    return format_sub_tasks_table(data)

def download_task_file(file_name):
    """
    Downloads the task file from the main controller.

    Args:
        file_name (str): The name of the task file to be downloaded.

    Returns:
        dict: The response data from the download operation.
    """
    return controller_main_download_task(file_name)


def fetch_main_sms_record_list(page):
    """
    Fetches and formats the main SMS record list.

    Args:
        page (int): The page number to fetch.

    Returns:
        PrettyTable or dict: A PrettyTable object with SMS records,
                             or the raw error response data.
    """
    data = controller_main_sms_record_list(page)
    if data["code"] != 0:
        return data  # Return error response if code is not 0

    data_row = data["data"]["data"]
    return format_sms_record_list(data_row)

def list_sub_user_sms_records(page, sub_user_id):
    """
    Fetches and formats the SMS record list for a sub-user.

    Args:
        page (int): The page number to fetch.
        sub_user_id (int): The sub-user ID.

    Returns:
        PrettyTable or dict: A PrettyTable object with SMS records,
                             or the raw error response data.
    """
    # Step 1: Fetch data from the controller
    response_data = fetch_sub_user_sms_records(page, sub_user_id)

    # Step 2: Validate the response
    error_response = validate_sms_record_response(response_data)
    if error_response:
        return error_response

    # Step 3: Extract and format the records
    record_list = extract_sms_record_list(response_data)
    return format_sub_user_sms_records(record_list)



def fetch_and_format_conversation_records(sub_user_id, project_id, page):
    """
    Fetches and formats conversation records for a sub-user.

    Args:
        sub_user_id (int): The ID of the sub-user.
        project_id (int): The ID of the project.
        page (int): The page number to fetch.

    Returns:
        PrettyTable or dict: A PrettyTable object with conversation records,
                             or the raw error response data.
    """
    # Step 1: Fetch the conversation records
    response_data = fetch_conversation_record_data(sub_user_id, project_id, page)

    # Step 2: Validate the response
    error_response = validate_conversation_record_response(response_data)
    if error_response:
        return error_response

    # Step 3: Extract and format the conversation records
    record_list = extract_conversation_record_list(response_data)
    return format_conversation_records(record_list)


def fetch_main_conversation_records(project_id, page):
    """
    Fetches the conversation records for a given project and page number.

    Args:
        project_id (int): The project ID for which to fetch the records.
        page (int): The page number to fetch.

    Returns:
        PrettyTable or dict: A formatted table of conversation records,
                             or the raw error response if any error occurs.
    """
    # Fetch data from the controller
    data = controller_main_sms_list_chat(project_id, page)

    # Check for errors in the response
    if data["code"] != 0:
        return data  # Return raw error response if the code is not 0

    # Format and return the table
    return format_conversation_records(data["data"]["data"])


def fetch_conversation_record(chat_log_id):
    """
    Fetches a specific conversation record based on chat log ID.

    Args:
        chat_log_id (int): The ID of the chat log to fetch.

    Returns:
        PrettyTable or dict: A formatted table of the conversation record,
                             or the raw error response if an error occurs.
    """
    # Fetch data from the controller
    data = sub_get_conversation_record(chat_log_id)

    # Check for errors in the response
    if data["code"] != 0:
        return data  # Return raw error response if the code is not 0

    # Format and return the conversation record
    return format_conversation_record(data["data"]["data"])

def post_conversation_record(chat_log_id, text):
    """
    Posts a new conversation record and returns the response.

    Args:
        chat_log_id (int): The ID of the chat log.
        text (str): The content of the conversation record.

    Returns:
        PrettyTable or dict: A formatted table with the response data,
                             or the raw error response if an error occurs.
    """
    # Call the controller to post the conversation record
    data = sub_post_conversation_record(chat_log_id, text)

    # Check for errors in the response
    if data["code"] != 0:
        return data  # Return raw error response if the code is not 0

    # Format and return the response data
    return format_post_response(data["data"])