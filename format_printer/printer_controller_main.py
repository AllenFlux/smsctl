import prettytable as pt

def printer_main_list(data):
    data_list = data["data"]["data"]
    if len(data_list) == 0:
        return data
    tb = pt.PrettyTable()
    tb.field_names = data_list[0].keys()
    for d in data_list:
        tb.add_row(d.values())
    return tb

def printer_action_result(data):
    tb = pt.PrettyTable()
    if type(data) is dict and "target_phone_number" in data and "content" in data:
        tb.field_names = data.keys()
        for i in range(len(data["target_phone_number"])):
            tb.add_row([data["target_phone_number"][i], data["content"][i]])
        return tb
    elif data["code"] == 0:
        data_row = data["data"]
    else:
        data_row = data
    if data_row is None:
        data_row = data
    tb.field_names = data_row.keys()
    tb.add_row(data_row.values())
    return tb

def printer_sub_list(data):
    if data["code"] == 50:
        return printer_action_result(data)
    return printer_main_list(data)