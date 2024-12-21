# smsctl 

smsctl is a command-line tool designed for managing and automating SMS tasks, devices, projects, groups, chat/conversation records, and more. The CLI is flexible, allowing for quick integration into your workflows.

## Features  

- Management For Device: List and allocate devices to projects or groups, register new devices, etc.
- Management For Project & Group: Create, list, update, or delete projects and groups. 
- Management For Task: Create, list, upload/download task files, and manage SMS record history. 
- Management For Conversation: View, list, and reply to chat logs across different projects.

### Installation
Install smsctl from PyPI using:
```
pip install smsctl
```

This will provide the smsctl command-line interface.

### Quick Usage

After installation, run:
```
smsctl --help
```

This displays available commands and options. You can also check individual commands:
```
smsctl <command> --help
```
For example:
```
smsctl list-device --help
```
### Command Overview (Tables)

Below are summary tables of the smsctl commands grouped by functionality. 
> Refer to Commands in Detail for a more comprehensive breakdown.

Device Commands

| Command	 |Description	| Key Options           |
|:---------|:--------------|:----------------------|
|list-device	|Lists all devices (main user)	| --page (default 1)    |
|sub-list-device	|Lists devices for a sub-user	| --sub-user-id, --page |
|register-device	|Registers a new device	| (No parameters yet.)  |
|fetch-device-task	|Fetches tasks assigned to a device	| (No parameters yet.)  |
|report-task-result	|Reports results of a device task	| (No parameters yet.)  |
|report-receive-content	|Reports received content (e.g., incoming SMS)	| (No parameters yet.)  |

Project Commands

| Command	                                                                             | Description	                                              | Key Options               |
|:-------------------------------------------------------------------------------------|:----------------------------------------------------------|:--------------------------|
| list-project	                                                                        | Lists all projects	| --page (default 1)        |
| create-project	                                                                      | Creates a new project	| --project-name, --note    |
| delete-project	                                                                      | Deletes a project	| (No parameters yet.)      |
| update-project	                                                                      | Updates a project	| (No parameters yet.)      |
| allocate-device-to-project	| Allocates a device to a project	| --device-id, --project-id |

Task Commands

|Command	|Description	|Key Options|
|:---|:---|:---|
|create-task	|Creates a new task (sub-user context)	|--sub-user-id, --file, --task-name, --group-id, --interval-time, --timing-start-time|
|delete-task	|Deletes a task	|(No parameters yet.)|
|list-tasks	|Lists tasks for the main user	|--page (default 1)|
|sub-list-tasks	|Lists tasks for a specific sub-user	|--sub-user-id, --page|
|download-task	|Downloads a task’s file by filename	|--file-name|
|list-task-record	|Lists SMS records for the main user	|--page (default 1)|
|sub-list-task-record	|Lists SMS records for a specific sub-user	|--sub-user-id, --page|

Group Commands

|Command	|Description	|Key Options|
|:---|:---|:---|
|list-groups	|Lists all groups for a sub-user	|--sub-user-id|
|create-group	|Creates a new group in a specific project (sub-user context)	|--sub-user-id, --project-id, --group-name|
|allocate-device-to-group	|Allocates a device to a group (sub-user context)	|--sub-user-id, --group-id, --device-id|
|update-group	|Updates an existing group	|(No parameters yet.)|
|delete-group	|Deletes an existing group	|(No parameters yet.)|

Chat Commands

|Command	|Description	|Key Options|
|:---|:---|:---|
|list-chats	|Lists conversation records for a project	|--project-id, --page (default 1)|
|sub-list-chats	|Lists conversation records for a sub-user in a project	|--project-id, --sub-user-id, --page (default 1)|
|view-chat	|Views a specific chat log	|--chat-log-id|
|reply-chat	|Replies to a specific chat log	|--chat-log-id, --text|

### Commands in Detail

Below, you’ll find more detailed usage information for each command. Use the --help option to see all parameters and their defaults.

#### Device Commands
list-device
```
smsctl list-device [OPTIONS]
```
    Options:  
    •   -p, --page: Page number for the listing. Defaults to 1.

list-device
```
smsctl sub-list-device --sub-user-id <SUB_USER_ID> [OPTIONS]
```
    Options:
    •	-p, --page: Page number (default: 1).
    •	-sub-user-id, --sub-user-id: Required. ID of the sub-user.

register-device
```
smsctl register-device
```

	•	(Placeholder - no options yet.)

fetch-device-task
```aiignore
smsctl fetch-device-task
```

	•	(Placeholder - no options yet.)

report-task-result
```aiignore
smsctl report-task-result
```

	•	(Placeholder - no options yet.)

report-receive-content
```aiignore
smsctl report-receive-content
```

	•	(Placeholder - no options yet.)

#### Project Commands
list-project
```aiignore
smsctl list-project [OPTIONS]
```
	Options:
    •	-p, --page: Page number (default: 1).

create-project
```aiignore
smsctl create-project --project-name <NAME> [OPTIONS]
```

	Options:
    •	-project-name, --project-name: Required. Name of the project.
    •	-note, --note: Optional note (default: Create By (sms cli)).

delete-project
```aiignore
smsctl delete-project
```
	•	(Placeholder - no options yet.)

update-project
```aiignore
smsctl update-project
```
	•	(Placeholder - no options yet.)

allocate-device-to-project
```aiignore
smsctl allocate-device-to-project --device-id <DEVICE_ID> --project-id <PROJECT_ID>
```
	Options:
    •	-device-id, --device-id: Required. The device ID.
    •	-project-id, --project-id: Required. The project ID.

### Task Commands
create-task
```aiignore
smsctl create-task \
  --sub-user-id <SUB_USER_ID> \
  --file <FILE_PATH> \
  --task-name <TASK_NAME> \
  --group-id <GROUP_ID> \
  [OPTIONS]
```
	Options:
	•	-sub-user-id, --sub-user-id: Required. Sub-user ID.
	•	-f, --file: Required. Path to the file for the task.
	•	-task-name, --task-name: Required. Name of the task.
	•	-group-id, --group-id: Required. Group ID for the task.
	•	-interval-time, --interval-time: Interval in seconds (default: 1).
	•	-timing-start-time, --timing-start-time: Start time (default: current time).

delete-task
```aiignore
smsctl delete-task
```

	•	(Placeholder - no options yet.)

list-tasks
```aiignore
smsctl list-tasks [OPTIONS]
```

	Options:
	•	-p, --page: Page number (default: 1).

sub-list-tasks
```aiignore
smsctl sub-list-tasks --sub-user-id <SUB_USER_ID> [OPTIONS]
```

	Options:
	•	-p, --page: Page number (default: 1).
	•	-sub-user-id, --sub-user-id: Required.

download-task
```aiignore
smsctl download-task --file-name <FILE_NAME>
```

	Options:
	•	-file-name, --file-name: Required. The name of the task file to download.

list-task-record
```aiignore
smsctl list-task-record [OPTIONS]
```

	•	Options:
	•	-p, --page: Page number (default: 1).

sub-list-task-record
```aiignore
smsctl sub-list-task-record --sub-user-id <SUB_USER_ID> [OPTIONS]
```

	Options:
	•	-p, --page: Page number (default: 1).
	•	-sub-user-id, --sub-user-id: Required.

### Group Commands
list-groups
```aiignore
smsctl list-groups --sub-user-id <SUB_USER_ID>
```

	Options:
	•	-sub-user-id, --sub-user-id: Required.
create-group
```aiignore
smsctl create-group \
  --sub-user-id <SUB_USER_ID> \
  --project-id <PROJECT_ID> \
  --group-name <GROUP_NAME>
```

	Options:
	•	-sub-user-id, --sub-user-id: Required.
	•	-project-id, --project-id: Required.
	•	-group-name, --group-name: Required.

allocate-device-to-group
```aiignore

smsctl allocate-device-to-group \
  --sub-user-id <SUB_USER_ID> \
  --group-id <GROUP_ID> \
  --device-id <DEVICE_ID>
```
	Options:
	•	-sub-user-id, --sub-user-id: Required.
	•	-group-id, --group-id: Required.
	•	-device-id, --device-id: Required.

update-group
```aiignore
smsctl update-group
```
	•	(Placeholder - no options yet.)

delete-group
```aiignore
smsctl delete-group
```
	•	(Placeholder - no options yet.)

### Chat Commands
list-chats
```aiignore
smsctl list-chats --project-id <PROJECT_ID> [OPTIONS]
```
	Options:
	•	-project-id, --project-id: Required.
	•	-p, --page: Page number (default: 1).

sub-list-chats
```aiignore
smsctl sub-list-chats --project-id <PROJECT_ID> --sub-user-id <SUB_USER_ID> [OPTIONS]
```

	Options:
	•	-project-id, --project-id: Required.
	•	-sub-user-id, --sub-user-id: Required.
	•	-p, --page: Page number (default: 1).

view-chat
```aiignore
smsctl view-chat --chat-log-id <CHAT_LOG_ID>
```
	Options:
	•	-chat-log-id, --chat-log-id: Required.

reply-chat
```aiignore
smsctl reply-chat --chat-log-id <CHAT_LOG_ID> --text <REPLY_TEXT>
```
	Options:
	•	-chat-log-id, --chat-log-id: Required.
	•	-text, --text: Required.

### Examples
List all devices on page 2:
```aiignore
smsctl list-device --page 2
```


Create a new project:
```aiignore
smsctl create-project --project-name "MyNewProject"
```


Allocate device 101 to project 10:
```aiignore
smsctl allocate-device-to-project --device-id 101 --project-id 10
```


Create a new task:
```aiignore
smsctl create-task \
  --sub-user-id 5 \
  --file /path/to/tasks/data.json \
  --task-name "BulkSMS" \
  --group-id 42 \
  --interval-time 5 \
  --timing-start-time 1672531200
```

Reply to chat log #200:
```aiignore
smsctl reply-chat --chat-log-id 200 --text "Thanks for your message!"
```

## Contributing
- Fork the repository. 
- Create a feature branch:
```aiignore
git checkout -b feature/awesome-feature
```
- Commit your changes:
```aiignore
git commit -am "Add new feature"
```


- Push to your branch:
```aiignore
git push origin feature/awesome-feature
```
- Create a Pull Request.

## All contributions (issues, PRs, feature requests) are welcome!

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contact
	•	GitHub Issues:  [Open an Issue](https://github.com/haozheng95/smscli/issues)
	•	Email: yinhaozheng77625961@gmail.com

Thank you for using smsctl!