import json
from faker import Faker
fake = Faker()

def generate_device_task_file(num):
    content_list = []
    phone_list = []
    for i in range(num):
        content_list.append(fake.text(max_nb_chars=20))
        phone_list.append(fake.phone_number())
    res = {"target_phone_number": phone_list, "content": content_list}
    with open("device_task_file.json", "w") as f:
        json.dump(res, f)
    return res