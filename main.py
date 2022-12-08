import wmi
import time
import requests
import json

tg_chat_id = "TELEGRAM_CHAT_ID"
tg_token = "YOUR_TOKEN"
process_name = "something.exe"

# Initializing the wmi constructor
f = wmi.WMI()

url = f"https://api.telegram.org/bot5461713855:{tg_token}/sendMessage"

ip_req = requests.get("http://ip-api.com/json/")
ip_lookup = ip_req.text
ip_lookup2 = json.loads(ip_lookup)
my_ip = ip_lookup2["query"]

# Iterating through all the running processes
exe_count = int(input("How many exe files running? : "))
delay_time = int(input("How many seconds should it be for the delay time? : "))
while True:
    try:
        exe_list = []
        time.sleep(delay_time)
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        for process in f.Win32_Process():
            if process.Name == process_name:
                exe_list.append(process.Name)
        if len(exe_list) == int(exe_count) * 2:
            requests.post(
                url,
                data={
                    "chat_id": tg_chat_id,
                    "text": "IP ADDRESS: "
                    + my_ip
                    + " | Time: "
                    + str(current_time)
                    + " - "
                    + str(exe_count)
                    + " exes are running.",
                },
            ).json()

        else:
            requests.post(
                url,
                data={
                    "chat_id": tg_chat_id,
                    "text": "IP ADDRESS: "
                    + my_ip
                    + " | Time: "
                    + str(current_time)
                    + " - THE PROGRAMS ARE NOT RUNNING",
                },
            ).json()

    except Exception as e:
        print(e)
