import json
import os
import time

import click

from sms_client.sms_core import m_list_project, m_create_project, m_list_device_main, m_allocate_device_2_project, \
    m_list_group, m_create_group, m_list_device_sub, m_allocate_device_2_group, m_sub_upload_task, m_list_tasks, \
    m_list_tasks_sub, m_download_task_file, decode_download_task_file, m_controller_main_sms_record_list, \
    m_controller_sub_sms_record_list, m_sub_get_conversation_record_list, m_main_get_conversation_record_list, \
    m_sub_get_conversation_record, m_sub_post_conversation_record


@click.group()
def sms_cli():
    """sms_cli"""
    pass

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
    out = m_list_device_main(page)
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
    out = m_list_device_sub(page,sub_user_id)
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
    out = m_list_project(page)
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
    out = m_create_project(project_name=project_name, note=note)
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
    out = m_allocate_device_2_project(device_id, project_id)
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
    out = m_sub_upload_task(
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
    out = m_list_tasks(page)
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
    out = m_list_tasks_sub(page, sub_user_id)
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
    data = m_download_task_file(file_name)
    if data["code"] != 0:
        click.echo(data)
        return
    click.echo("Interpret the contents of the file.")
    out, dict_data = decode_download_task_file(data)
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
    out = m_controller_main_sms_record_list(page)
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
    out = m_controller_sub_sms_record_list(page, sub_user_id)
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
    out = m_list_group(sub_user_id)
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
    out = m_create_group(group_name=group_name, project_id=project_id, sub_user_id=sub_user_id)
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
    out = m_allocate_device_2_group(sub_user_id=sub_user_id, group_id=group_id, device_id=device_id)
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
    out = m_main_get_conversation_record_list(project_id=project_id, page=page)
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
    out = m_sub_get_conversation_record_list(sub_user_id, project_id, page)
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
    out = m_sub_get_conversation_record(chat_log_id)
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
    out = m_sub_post_conversation_record(chat_log_id, text)
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

if __name__ == '__main__':
    sms_cli()