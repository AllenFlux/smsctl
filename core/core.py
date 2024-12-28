# Main SMS record management controllers
from controllers.main.sms_record_controller import (
    controller_main_sms_record_list,  # Fetch the list of SMS records for the main user
    controller_main_sms_list_chat    # Fetch the SMS conversation list for the main user
)

# Main SMS report management controllers
from controllers.main.sms_report_controller import (
    controller_main_download_task  # Download task files for the main user
)

# Sub-user SMS management controllers
from controllers.sub.sms_controller import (
    sub_get_conversation_record,    # Fetch a conversation record for a sub-user
    sub_post_conversation_record    # Post a conversation record for a sub-user
)

# Utilities: Formatters for displaying data
from utils.formatters import (
    display_project_table,              # Display project data in table format
    display_project_creation_response, # Display the response of project creation
    display_device_list,               # Display the device list for the main user
    display_device_list_for_sub_user,  # Display the device list for a sub-user
    display_device_allocation_result,  # Display the result of device allocation
    display_group_list,                # Display the group list for a sub-user
    display_group_creation_result,     # Display the response of group creation
    display_task_upload_result,        # Display the result of task upload
    format_tasks_table,                # Format the main tasks table
    format_sub_tasks_table,            # Format the sub-tasks table
    format_sms_record_list,            # Format the main SMS record list
    validate_sms_record_response,      # Validate the SMS record response
    extract_sms_record_list,           # Extract SMS records from a response
    format_sub_user_sms_records,       # Format SMS records for a sub-user
    validate_conversation_record_response,  # Validate conversation record responses
    extract_conversation_record_list,       # Extract conversation records from a response
    format_conversation_records,            # Format conversation records for display
    format_conversation_record,             # Format a single conversation record
    format_post_response                    # Format the post conversation response
)

# Utilities: Helpers for core operations
from utils.helpers import (
    fetch_project_data,            # Fetch project data
    create_project,                # Create a new project
    fetch_device_list,             # Fetch the list of devices for the main user
    fetch_device_list_for_sub_user,  # Fetch the list of devices for a sub-user
    allocate_device_to_project,    # Allocate a device to a project
    fetch_group_list,              # Fetch the list of groups for a sub-user
    create_group,                  # Create a new group for a sub-user
    allocate_device_to_group,      # Allocate a device to a group
    upload_task,                   # Upload a task
    fetch_tasks_data,              # Fetch tasks data for the main user
    fetch_sub_tasks_data,          # Fetch tasks data for a sub-user
    fetch_sub_user_sms_records,    # Fetch SMS records for a sub-user
    fetch_conversation_record_data # Fetch conversation record data
)


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