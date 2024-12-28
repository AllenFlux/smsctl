# project_url = "https://a2.pppkf.cc"
# project_url = "http://127.0.0.1:8822"
# prefix= "/sms-api/v1/"
# prefix= "/api/v1/"
import json
import os
home_dir = os.path.expanduser("~")
filename = home_dir + "/.smscli.json"
if os.path.exists(filename):
    with open(filename) as f:
        url = json.load(f)
else:
    url = {"url":"https://api.smscli.net"}
url_prefix = url["url"]