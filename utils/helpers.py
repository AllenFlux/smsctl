# Main controllers for device management
from controllers.main.device_controller import (
    controller_main_device_list  # Fetch the list of devices for the main user
)

# Main controllers for project management
from controllers.main.project_controller import (
    controller_main_project_list,       # Fetch the list of projects for the main user
    controller_main_project_create,     # Create a new project for the main user
    allocate_device_2_project           # Allocate a device to a project
)

# Main controllers for SMS report management
from controllers.main.sms_report_controller import (
    controller_main_sms_report_list  # Fetch the SMS report list for the main user
)

# Sub-user controllers for device management
from controllers.sub.device_controller import (
    controller_sub_device_list  # Fetch the list of devices for a sub-user
)

# Sub-user controllers for group management
from controllers.sub.group_controller import (
    controller_sub_group_list,          # Fetch the list of groups for a sub-user
    controller_sub_group_create,        # Create a new group for a sub-user
    allocate_device_2_group,            # Allocate a device to a group
    sub_upload_task                     # Upload a task under a sub-user's group
)

# Sub-user controllers for SMS management
from controllers.sub.sms_controller import (
    controller_sub_sms_report_list,          # Fetch the SMS report list for a sub-user
    controller_sub_sms_record_list,          # Fetch the SMS records for a sub-user
    sub_get_conversation_record_list         # Fetch the conversation record list for a sub-user
)


def fetch_project_data(page):
    """
    Fetches project data from the controller.

    Args:
        page (int): The page number to fetch.

    Returns:
        dict: The response data from the controller.
    """
    return controller_main_project_list(page)

def create_project(project_name, note):
    """
    Sends a request to create a project with the given details.

    Args:
        project_name (str): The name of the project to create.
        note (str): Additional notes for the project.

    Returns:
        dict: The response data from the controller.
    """
    return controller_main_project_create(project_name=project_name, note=note)

def fetch_device_list(page):
    """
    Fetches the device list from the controller.

    Args:
        page (int): The page number for pagination.

    Returns:
        dict: The response data containing device details.
    """
    return controller_main_device_list(page)

def fetch_device_list_for_sub_user(page, sub_user_id):
    """
    Fetches the device list for a sub-user from the controller.

    Args:
        page (int): The page number for pagination.
        sub_user_id (int): The ID of the sub-user.

    Returns:
        dict: The response data containing device details.
    """
    return controller_sub_device_list(page, sub_user_id)

def allocate_device_to_project(device_id, project_id):
    """
    Allocates a device to a project by calling the relevant controller function.

    Args:
        device_id (int): The ID of the device to allocate.
        project_id (int): The ID of the project to which the device will be allocated.

    Returns:
        dict: The response data from the controller function.
    """
    return allocate_device_2_project(device_id=device_id, project_id=project_id)

def fetch_group_list(sub_user_id):
    """
    Fetches the list of groups for a given sub-user ID by calling the relevant controller function.

    Args:
        sub_user_id (int): The ID of the sub-user whose groups will be fetched.

    Returns:
        dict: The response data from the controller function.
    """
    return controller_sub_group_list(sub_user_id)

def create_group(group_name, project_id, sub_user_id):
    """
    Creates a group for a given sub-user ID and project ID.

    Args:
        group_name (str): The name of the group to be created.
        project_id (int): The ID of the project the group is associated with.
        sub_user_id (int): The ID of the sub-user creating the group.

    Returns:
        dict: The response data from the controller function.
    """
    return controller_sub_group_create(
        group_name=group_name,
        project_id=project_id,
        sub_user_id=sub_user_id
    )

def allocate_device_to_group(device_id, group_id, sub_user_id):
    """
    Allocates a device to a group for a specific sub-user.

    Args:
        device_id (int): The ID of the device to be allocated.
        group_id (int): The ID of the group to which the device will be allocated.
        sub_user_id (int): The ID of the sub-user performing the allocation.

    Returns:
        dict: The response data from the allocation process.
    """
    return allocate_device_2_group(
        device_id=device_id,
        group_id=group_id,
        sub_user_id=sub_user_id
    )

def upload_task(kwargs):
    """
    Uploads a task using the given keyword arguments.

    Args:
        kwargs (dict): The arguments required for uploading the task.

    Returns:
        dict: The response data from the task upload process.
    """
    return sub_upload_task(**kwargs)

def fetch_tasks_data(page):
    """
    Fetches task data from the main controller API.

    Args:
        page (int): The page number for task data.

    Returns:
        dict: The API response data containing task details.
    """
    return controller_main_sms_report_list(page)

def fetch_sub_tasks_data(page, sub_user_id):
    """
    Fetches sub-user task data from the controller.

    Args:
        page (int): The page number for task data.
        sub_user_id (int): The ID of the sub-user.

    Returns:
        dict: The API response data containing task details.
    """
    return controller_sub_sms_report_list(page, sub_user_id)

def fetch_sub_user_sms_records(page, sub_user_id):
    """
    Fetches the SMS record list for a sub-user from the controller.

    Args:
        page (int): The page number to fetch.
        sub_user_id (int): The sub-user ID.

    Returns:
        dict: The response data from the controller.
    """
    return controller_sub_sms_record_list(page, sub_user_id)

def fetch_conversation_record_data(sub_user_id, project_id, page):
    """
    Fetches the conversation record data from the controller.

    Args:
        sub_user_id (int): The ID of the sub-user.
        project_id (int): The ID of the project.
        page (int): The page number to fetch.

    Returns:
        dict: The response data from the controller.
    """
    return sub_get_conversation_record_list(sub_user_id, project_id, page)