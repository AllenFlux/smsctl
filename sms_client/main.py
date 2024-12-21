import click

from controller_main.controller_main_device_list import controller_main_device_list
from controller_main.controller_main_project_list import controller_main_project_list, controller_main_project_create, \
    allocate_sub_account_2_project, allocate_device_2_project
from controller_main.controller_main_sms_record_list import controller_main_sms_record_list
from controller_main.controller_main_sms_report_list import controller_main_sms_report_list
from controller_sub.controller_sub_device_list import controller_sub_device_list
from controller_sub.controller_sub_group import controller_sub_group_list, controller_sub_group_create, \
    allocate_device_2_group
from format_printer.printer_controller_main import printer_main_list, printer_action_result, printer_sub_list
from generate_data.generate_task_file import generate_device_task_file


@click.group()
def cli_group():
    """CLI commands for SMS Backend Project"""

@click.command(name="controller-main-device")
@click.argument("action")
@click.option(
    "-p",
    "--page",
    default=1,
    help="List Page Num",
)
def controller_main_device(action, page):
    """Action of Main Controller Device. Supported operations[List]"""
    action = action.lower()
    if action == "list":
        data = controller_main_device_list(page)
        out = printer_main_list(data)
        click.echo(out)
    else:
        click.echo("controller_main_device")


@click.command(name="controller-main-project")
@click.argument("action")
@click.option(
    "-p",
    "--page",
    default=1,
    help="List Page Num",
)
def controller_main_project(action, page):
    """Action of Main Controller project. Supported operations[
    list,
    create,
    allocate_sub_account_2_project,
    allocate_device_2_project,
    ]"""
    action = action.lower()
    if action == "list":
        data = controller_main_project_list(page)
        out = printer_main_list(data)
        click.echo(out)
    elif action == "create":
        data = controller_main_project_create(project_name=click.prompt("Project Name"), note=click.prompt("Note"))
        out = printer_action_result(data)
        click.echo(out)
    elif action == "allocate_sub_account_2_project":
        data = allocate_sub_account_2_project(project_id=click.prompt("Project ID"), account_id=click.prompt("Sub Account ID"))
        out = printer_action_result(data)
        click.echo(out)
    elif action == "allocate_device_2_project":
        data = allocate_device_2_project(device_id=click.prompt("Device ID"), project_id=click.prompt("Project ID"))
        out = printer_action_result(data)
        click.echo(out)
    else:
        click.echo("controller_main_project")

@click.command(name="controller-main-sms")
@click.argument("module")
@click.option(
    "-a",
    "--action",
    help="Operations performed on the module",
)
@click.option(
    "-p",
    "--page",
    default=1,
    help="List Page Num",
)
def controller_main_sms(module, action, page):
    """Action of Main Controller SMS, Select [report] or [record] as the module you want to operate on. Supported operations[list]"""
    module = module.lower()
    action = action.lower()
    if module == "report":
        if action == "list":
            data = controller_main_sms_report_list(page)
            out = printer_main_list(data)
            click.echo(out)
    elif module == "record":
        if action == "list":
            data = controller_main_sms_record_list(page)
            out = printer_main_list(data)
            click.echo(out)
    else:
        click.echo("controller_main_device")

@click.command(name="generate-fake")
@click.argument("action")
def generate_fake(action):
    """Generate Fake task-file on current location"""
    if action == "task-file":
        data = generate_device_task_file(num=int(click.prompt("Number of Task items")))
        out = printer_action_result(data)
        click.echo(out)


Sub_Account_ID = 886

@click.command(name="controller-sub-device")
@click.argument("action")
@click.option(
    "-p",
    "--page",
    default=1,
    help="List Page Num",
)
def controller_sub_device(action, page):
    """Action of Sub Controller Device. Supported operations[List]"""
    action = action.lower()
    if action == "list":
        data = controller_sub_device_list(page, Sub_Account_ID)
        out = printer_sub_list(data)
        click.echo(out)
    else:
        click.echo("controller_sub_device")

@click.command(name="controller-sub-group")
@click.argument("action")
def controller_sub_group(action):
    """Action of Sub Controller Group. Supported operations[List]"""
    action = action.lower()
    if action == "list":
        data = controller_sub_group_list(Sub_Account_ID)
        out = printer_sub_list(data)
        click.echo(out)
    elif action == "create":
        data = controller_sub_group_create(group_name=click.prompt("Group Name"), project_id=click.prompt("Project ID"),sub_user_id=Sub_Account_ID)
        out = printer_action_result(data)
        click.echo(out)
    elif action == "allocate_device_2_group":
        data = allocate_device_2_group(device_id=click.prompt("Device ID"), group_id=click.prompt("Group ID"), sub_user_id=Sub_Account_ID)
        out = printer_action_result(data)
        click.echo(out)
    else:
        click.echo("controller_sub_device")

def controller_sub_sms():
    pass

cli_group.add_command(controller_main_device)
cli_group.add_command(controller_main_project)
cli_group.add_command(controller_main_sms)
cli_group.add_command(generate_fake)
cli_group.add_command(controller_sub_device)
cli_group.add_command(controller_sub_group)

if __name__ == '__main__':
    cli_group()