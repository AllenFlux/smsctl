import json
import os
import time

import click

# Project management-related functions
from core.core import (
    list_projects_with_details,   # Fetch and list projects with details
    handle_project_creation,     # Create a new project
)

# Device management-related functions
from core.core import (
    handle_device_list,                  # List all devices
    handle_device_list_for_sub_user,     # List devices assigned to a sub-user
    handle_device_allocation_to_project, # Allocate a device to a project
    list_user_groups,                    # Fetch groups of a user
    handle_group_creation,               # Create a new group
    handle_device_allocation,            # Allocate a device to a group
)

# Task management-related functions
from core.core import (
    handle_task_upload,         # Upload a new task
    list_tasks_with_details,    # List all tasks with details
    list_sub_tasks_with_details,# List tasks for a specific sub-user
    download_task_file,         # Download a task file
)

# Messaging-related functions
from core.core import (
    fetch_main_sms_record_list,          # Fetch SMS records for the main user
    list_sub_user_sms_records,           # List SMS records for a sub-user
    fetch_and_format_conversation_records, # Fetch and format conversation records
    fetch_main_conversation_records,     # Fetch main user conversation records
    fetch_conversation_record,           # Fetch a specific conversation record
    post_conversation_record,            # Post a new conversation record
)

# Utility functions
from utils.formatters import decode_task_file_content # Decode task file content to a readable format


@click.group()
def sms_cli():
    """
    smsctl is a command-line tool designed for managing and automating
    SMS tasks, devices, projects, groups, chat/conversation records, and more.
    The CLI is flexible, allowing for quick integration into your workflows.
    """
    pass

@click.command(name="config")
@click.option(
    "-url",
    "--url",
    default="https://a2.pppkf.cc/api/v1/",
    help="Sets the URL endpoint for the SMS CLI. Defaults to https://a2.pppkf.cc/api/v1/."
)
def sms_cli_config(url):
    """
    Configures the SMS CLI by storing the service endpoint URL
    in a local JSON configuration file.

    Args:
        url (str): The base URL endpoint for SMS CLI requests.
    """
    home_dir = os.path.expanduser("~")
    # Note: "~/.smscli.json" expands to a path under your home directory.
    # Make sure you handle that expansion properly in your actual code.
    with open(home_dir+"/.smscli.json", "w") as f:
        json.dump({"url": url}, f)
    click.echo(f"Configuration saved with URL: {url}")

@click.command(name="list-device")
@click.option(
    "-p",
    "--page",
    default=1,
    help="Page number for device listing. Defaults to the first page.",
)
def list_device(page):
    """
    Lists all devices associated with the main user.

    Args:
        page (int): The page number to fetch the device list from.

    Returns:
        Prints the device list to the console.
    """
    out = handle_device_list(page)
    click.echo(out)

@click.command(name="sub-list-device")
@click.option(
    "-p",
    "--page",
    default=1,
    help="Page number for device listing. Defaults to the first page.",
)
@click.option(
    "-sub-user-id",
    "--sub-user-id",
    help="The ID of the sub-user whose devices are to be listed.",
    type=int,
    required=True,
)
def sub_list_device(page, sub_user_id):
    """
    Lists all devices associated with a specific sub-user.

    Args:
        page (int): The page number to fetch the device list from.
        sub_user_id (int): The ID of the sub-user.

    Returns:
        Prints the device list for the sub-user to the console.
    """
    out = handle_device_list_for_sub_user(page,sub_user_id)
    click.echo(out)

# Project
@click.command(name="list-project")
@click.option(
    "-p",
    "--page",
    default=1,
    help="Page number for project listing. Defaults to the first page.",
)
def list_project(page):
    """
    Lists all projects associated with the main user.

    Args:
        page (int): The page number to fetch the project list from.

    Returns:
        Prints the project list to the console.
    """
    out = list_projects_with_details(page)
    click.echo(out)

@click.command(name="create-project")
@click.option(
    "-project-name",
    "--project-name",
    help="The name of the project to create.",
    type=str,
    required=True,
)
@click.option(
    "-note",
    "--note",
    help="Optional note about the project. Defaults to 'Created by SMS CLI'.",
    default="Create By (sms cli)",
    type=str,
)
def create_project(project_name, note):
    """
    Creates a new project.

    Args:
        project_name (str): The name of the new project.
        note (str): An optional note for the project.

    Returns:
        Prints the result of the project creation operation to the console.
    """
    out = handle_project_creation(project_name=project_name, note=note)
    click.echo(out)

@click.command(name="delete-project")
def delete_project():
    """delete-project"""
    pass
@click.command(name="update-projec")
def update_project():
    """update-project"""
    pass

@click.command(name="allocate-device-to-project")
@click.option(
    "-device-id",
    "--device-id",
    help="The ID of the device to allocate to the project.",
    type=int,
    required=True,
)
@click.option(
    "-project-id",
    "--project-id",
    help="The ID of the project to allocate the device to.",
    type=int,
    required=True,
)
def allocate_device_to_project(device_id,project_id):
    """
    Allocates a device to a specific project.

    Args:
        device_id (int): The ID of the device to allocate.
        project_id (int): The ID of the target project.

    Returns:
        Prints the result of the allocation operation to the console.
    """
    out = handle_device_allocation_to_project(device_id, project_id)
    click.echo(out)

# Task
@click.command(name="create-task")
@click.option(
    "-sub-user-id",
    "--sub-user-id",
    help="The ID of the sub-user for whom the task is being created.",
    type=int,
    required=True,
)
@click.option(
    "-f",
    "--file",
    help="The path to the file associated with the task.",
    type=click.Path(exists=True),
    required=True,
)
@click.option(
    "-task-name",
    "--task-name",
    help="The name of the task.",
    type=str,
    required=True,
)
@click.option(
    "-group-id",
    "--group-id",
    help="The ID of the group associated with the task.",
    type=int,
    required=True,
)
@click.option(
    "-interval-time",
    "--interval-time",
    help="The interval time (in seconds) for task execution. Defaults to 1 second.",
    type=int,
    default=1,
    required=False,
)
@click.option(
    "-timing-start-time",
    "--timing-start-time",
    help="The start time for the task. Defaults to the current time.",
    type=str,
    default=str(time.time()),
    required=False,
)
def create_task(sub_user_id,file, task_name, group_id, interval_time, timing_start_time):
    """
    Creates a new task for a sub-user.

    Args:
        sub_user_id (int): The ID of the sub-user.
        file (str): The path to the task file.
        task_name (str): The name of the task.
        group_id (int): The ID of the group associated with the task.
        interval_time (int): The interval time for task execution.
        timing_start_time (str): The start time for the task.

    Returns:
        Prints the result of the task creation operation to the console.
    """
    out = handle_task_upload(
        dict(
            task_name=task_name,
            group_id=group_id,
            sub_user_id=sub_user_id,
            file=file,
            timing_start_time=timing_start_time,
            interval_time=str(interval_time),
        )
    )
    click.echo(out)
@click.command(name="delete-task")
def delete_task():
    """delete-task"""
    pass

@click.command(name="list-tasks")
@click.option(
    "-p",
    "--page",
    default=1,
    help="Page number for task listing. Defaults to the first page.",
)
def list_tasks(page):
    """
    Lists all tasks associated with the main user.

    Args:
        page (int): The page number to fetch the task list from.

    Returns:
        Prints the task list to the console.
    """
    out = list_tasks_with_details(page)
    click.echo(out)

@click.command(name="sub-list-tasks")
@click.option(
    "-p",
    "--page",
    default=1,
    help="Page number for sub-task listing. Defaults to the first page.",
)
@click.option(
    "-sub-user-id",
    "--sub-user-id",
    help="The ID of the sub-user whose tasks are to be listed.",
    type=int,
    required=True,
)
def sub_list_tasks(page, sub_user_id):
    """
    Lists all tasks associated with a specific sub-user.

    Args:
        page (int): The page number to fetch the sub-task list from.
        sub_user_id (int): The ID of the sub-user.

    Returns:
        Prints the sub-task list to the console.
    """
    out = list_sub_tasks_with_details(page, sub_user_id)
    click.echo(out)

@click.command(name="download-task")
@click.option(
    "-file-name",
    "--file-name",
    help="The File Name of the task whose file is to be downloaded.",
    type=str,
    required=True,
)
def download_task(file_name):
    """
        Downloads the file associated with a specific task.

        Args:
            file-name (str): The File Name of the task.

        Returns:
            Prints a success message with the save path upon successful download.
        """
    data = download_task_file(file_name)
    if data["code"] != 0:
        click.echo(data)
        return
    click.echo("Interpret the contents of the file.")
    out, dict_data = decode_task_file_content(data)
    click.echo(out)
    file_path = os.getcwd() + "/" + file_name
    click.echo("File storage path:" + file_path)
    with open(file_path, "w") as f:
        json.dump(dict_data, f)


@click.command(name="list-task-record")
@click.option(
    "-p",
    "--page",
    default=1,
    help="Page number for SMS record listing. Defaults to the first page.",
)
def list_task_record(page):
    """
    Lists SMS records for the main user.

    Args:
        page (int): The page number to fetch the SMS record list from.

    Returns:
        Prints the SMS record list to the console.
    """
    out = fetch_main_sms_record_list(page)
    click.echo(out)

@click.command(name="sub-list-task-record")
@click.option(
    "-p",
    "--page",
    default=1,
    help="Page number for SMS record listing. Defaults to the first page.",
)
@click.option(
    "-sub-user-id",
    "--sub-user-id",
    help="The ID of the sub-user whose SMS records are to be listed.",
    type=int,
    required=True,
)
def sub_list_task_record(page, sub_user_id):
    """
        Lists SMS records for a specific sub-user.

        Args:
            page (int): The page number to fetch the SMS record list from.
            sub_user_id (int): The ID of the sub-user.

        Returns:
            Prints the SMS record list for the sub-user to the console.
    """
    out = list_sub_user_sms_records(page, sub_user_id)
    click.echo(out)

# Group
@click.command(name="list-groups")
@click.option(
    "-sub-user-id",
    "--sub-user-id",
    help="Page number for group listing. Defaults to the first page.",
    type=int,
    required=True,
)
def list_groups(sub_user_id):
    """
    Lists all groups associated with the main user.

    Args:
        page (int): The page number to fetch the group list from.

    Returns:
        Prints the group list to the console.
    """
    out = list_user_groups(sub_user_id)
    click.echo(out)

@click.command(name="create-group")
@click.option(
    "-sub-user-id",
    "--sub-user-id",
    help="The ID of the sub-user for whom the group is being created.",
    type=int,
    required=True,
)
@click.option(
    "-project-id",
    "--project-id",
    help="The ID of the project associated with the group.",
    type=int,
    required=True,
)
@click.option(
    "-group-name",
    "--group-name",
    help="The name of the group to be created.",
    type=str,
    required=True,
)
def create_group(sub_user_id, project_id, group_name):
    """
    Creates a new group for a specific sub-user within a given project.

    Args:
        sub_user_id (int): The ID of the sub-user for whom the group is being created.
        project_id (int): The ID of the project to which the group will belong.
        group_name (str): The name of the group to be created.

    Returns:
        None: Outputs the result of the group creation operation to the console.
    """
    out = handle_group_creation(group_name=group_name, project_id=project_id, sub_user_id=sub_user_id)
    click.echo(out)

@click.command(name="allocate-device-to-group")
@click.option(
    "-sub-user-id",
    "--sub-user-id",
    help="The ID of the sub-user for whom the group is being created.",
    type=int,
    required=True,
)
@click.option(
    "-group-id",
    "--group-id",
    help="The ID of the group to allocate the device to.",
    type=int,
    required=True,
)
@click.option(
    "-device-id",
    "--device-id",
    help="The ID of the device to allocate to the group.",
    type=int,
    required=True,
)
def allocate_device_to_group(sub_user_id, group_id, device_id ):
    """
    Allocates a device to a specific group.

    Args:
        sub_user_id (int): The ID of the sub-user for whom the group is being created.
        device_id (int): The ID of the device to allocate.
        group_id (int): The ID of the target group.

    Returns:
        Prints the result of the allocation operation to the console.
    """
    out = handle_device_allocation(sub_user_id=sub_user_id, group_id=group_id, device_id=device_id)
    click.echo(out)
    pass
@click.command(name="update-group")
def update_group():
    """update-group"""
    pass
@click.command(name="delete-group")
def delete_group():
    """delete-group"""
    pass
# Chat
@click.command(name="list-chats")
@click.option(
    "-project-id",
    "--project-id",
    help="The ID of the project whose conversation records are to be listed.",
    type=int,
    required=True,
)
@click.option(
    "-p",
    "--page",
    help="The page number to retrieve the conversation records from. Defaults to 1.",
    type=int,
    default=1,
)
def list_chats(project_id, page):
    """
    Retrieves and displays a list of conversation records associated with a specific project.

    Args:
        project_id (int): The ID of the project whose conversation records are being queried.
        page (int): The page number of the conversation record list to retrieve. Defaults to 1.

    Returns:
        None: Outputs the conversation records for the specified project and page to the console.
    """
    out = fetch_main_conversation_records(project_id=project_id, page=page)
    click.echo(out)

@click.command(name="sub-list-chats")
@click.option(
    "-project-id",
    "--project-id",
    help="The ID of the project whose conversation records are to be listed.",
    type=int,
    required=True,
)
@click.option(
    "-sub-user-id",
    "--sub-user-id",
    help="The ID of the sub-user whose conversation records are to be retrieved.",
    type=int,
    required=True,
)
@click.option(
    "-p",
    "--page",
    help="The page number to retrieve the conversation records from. Defaults to 1.",
    type=int,
    default=1,
)
def sub_list_chats(project_id, sub_user_id, page):
    """
    Retrieves and displays a list of conversation records for a specific sub-user
    within a given project.

    Args:
        project_id (int): The ID of the project associated with the conversation records.
        sub_user_id (int): The ID of the sub-user whose conversation records are being queried.
        page (int): The page number of the conversation records to retrieve. Defaults to 1.

    Returns:
        None: Outputs the conversation records for the specified sub-user and project to the console.
    """
    out = fetch_and_format_conversation_records(sub_user_id, project_id, page)
    click.echo(out)
@click.command(name="view-chat")
@click.option(
    "-chat-log-id",
    "--chat-log-id",
    help="The ID of the chat log to be viewed.",
    type=int,
    required=True,
)
def view_chat(chat_log_id):
    """
    Retrieves and displays the details of a specific chat log.

    Args:
        chat_log_id (int): The ID of the chat log to retrieve.

    Returns:
        None: Outputs the details of the specified chat log to the console.
    """
    out = fetch_conversation_record(chat_log_id)
    click.echo(out)

@click.command(name="reply-chat")
@click.option(
    "-chat-log-id",
    "--chat-log-id",
    help="The ID of the chat log to reply to.",
    type=int,
    required=True,
)
@click.option(
    "-text",
    "--text",
    help="The reply text to be sent for the specified chat log.",
    type=str,
    required=True,
)
def reply_chat(chat_log_id, text):
    """
    Sends a reply to a specific chat log.

    Args:
        chat_log_id (int): The ID of the chat log to reply to.
        text (str): The reply message to be sent.

    Returns:
        None: Outputs the result of the reply operation to the console.
    """
    out = post_conversation_record(chat_log_id, text)
    click.echo(out)

# Device
@click.command(name="register-device")
def register_device():
    """register-device"""
    pass
@click.command(name="fetch-device-task")
def fetch_device_task():
    """fetch-device-task"""
    pass
@click.command(name="report-task-result")
def report_task_result():
    """report-task-result"""
    pass
@click.command(name="report-receive-content")
def report_receive_content():
    """report-receive-content"""
    pass

sms_cli.add_command(list_project)
sms_cli.add_command(create_project)
sms_cli.add_command(delete_project)
sms_cli.add_command(update_project)
sms_cli.add_command(allocate_device_to_project)
sms_cli.add_command(create_task)
sms_cli.add_command(delete_task)
sms_cli.add_command(list_tasks)
sms_cli.add_command(sub_list_tasks)
sms_cli.add_command(list_task_record)
sms_cli.add_command(list_groups)
sms_cli.add_command(create_group)
sms_cli.add_command(allocate_device_to_group)
sms_cli.add_command(update_group)
sms_cli.add_command(delete_group)
sms_cli.add_command(list_chats)
sms_cli.add_command(view_chat)
sms_cli.add_command(reply_chat)
sms_cli.add_command(register_device)
sms_cli.add_command(fetch_device_task)
sms_cli.add_command(report_task_result)
sms_cli.add_command(report_receive_content)
sms_cli.add_command(list_device)
sms_cli.add_command(sub_list_device)
sms_cli.add_command(download_task)
sms_cli.add_command(sub_list_task_record)
sms_cli.add_command(sub_list_chats)
sms_cli.add_command(sms_cli_config)

if __name__ == '__main__':
    sms_cli()