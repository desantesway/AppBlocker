# pyinstaller main.py --onefile --name="MSI Center Service (32 bit)" --icon="icon.ico"

from presets import adult, custom_sites, custom_apps, schedule, always
from killer import monitor_and_close_app, update_hosts, remove_hosts
from noti import send_notification
import time
from datetime import datetime, timedelta
import json
import os
import multiprocessing

def active(start, end):
    start = start.time()
    end = end.time()
    now = datetime.now().time()
    if start < end:
        return start <= now <= end
    else:
        return now >= start or now <= end
    
def site_killer(bbs, shared_info, blocks, wday, i, w_message, lock):
    while True:
        try:
            with lock:
                on = shared_info[wday][1][i] != 0
            if on:
                if len(blocks) > 0:
                    update_hosts(blocks)
                w_message.value = w_message.value + multiprocessing.current_process().name + " " + str(datetime.now()) + " " + bbs + "\n"
            else:
                remove_hosts()
                break
        except Exception as e:
            w_message.value = w_message.value + f"Unexpected error: {e}"
        time.sleep(30)
    os._exit(0)

def proc_killer(bbs, shared_info, blocks, wday, i, w_message, lock):
    unkillable = []
    while True:
        try:
            with lock:
                on = shared_info[wday][1][i] != 0
            if on:
                if len(blocks) > 0:
                    unkillable = monitor_and_close_app(blocks, unkillable)
                w_message.value = w_message.value + multiprocessing.current_process().name + " " + str(datetime.now()) + " " + bbs + "\n"
            else:
                break
        except Exception as e:
            w_message.value = w_message.value + f"Unexpected error: {e}"
        time.sleep(5)
    os._exit(0)
    
def writer(w_message, lock):
    while True:
        with lock:
            w_message.value = w_message.value + multiprocessing.current_process().name + " " + str(datetime.now()) + "\n"
            to_write = w_message.value
            if len(w_message.value) > (1024 * 1024):
                w_message.value = ""
        with open("./prints.log", "w") as log:
            log.write(to_write)
        time.sleep(300)
     
week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        
def remake(every, data):
    for everys in every:
        dict = {}
        dict['start'] = everys['start']
        dict['end'] = everys['end']
        if "apps" in everys:
            dict['apps'] = everys['apps']
        if "sites" in everys:
            dict["sites"] = everys["sites"]
        for k in week:
            data[k].append(dict)
    for i in range(len(data)):
        for times in data[week[i]]:
            if datetime.strptime(times["start"], "%H:%M").time() > datetime.strptime(times['end'], "%H:%M").time():
                dict = {}
                dict['start'] = '00:00'
                dict['end'] = times['end']
                if "apps" in times:
                    dict['apps'] = times['apps']
                if "sites" in times:
                    dict["sites"] = times["sites"]
                if i+1 >= len(week):
                    data[week[0]] += [dict]
                else:    
                    data[week[i+1]] += [dict]
    return data

def blocks(data):
    manager = multiprocessing.Manager()
    
    shared_info = manager.list([]) 
    
    for i in range(len(week)):
        scheds = []
        for _ in range(len(data[week[i]])):
            scheds.append(0)
        shared_info.append([week[i], scheds])
    w_message = manager.Value('c', "")
    lock = manager.Lock() 
    processes = []
    
    p = multiprocessing.Process(target=writer, args=(w_message, lock), name=f'Writer')
    processes.append(p)
    p.start()
    
    j = 0
    
    while True:
        
        rn = time.localtime()
        weekday = week[rn.tm_wday]
        with lock:
            for i in range(len(shared_info)):
                if shared_info[i][0] != weekday:
                    shared_info[i] = [shared_info[i][0], [0] * len(shared_info[i][1])]
        for i in range(len(data[weekday])):
            schedule = data[weekday][i]
            s_start = datetime.strptime(schedule["start"], "%H:%M")
            s_end = datetime.strptime(schedule["end"], "%H:%M")
            bbs = ('','')
            if "apps" in schedule:
                bbs = (bbs[0] + schedule["apps"], bbs[1])
            if "sites" in schedule:
                bbs = (bbs[0], bbs[1] + schedule["sites"])
            with lock:
                if active(s_start, s_end) and shared_info[rn.tm_wday][1][i] >= 0 and shared_info[rn.tm_wday][1][i] != 369:
                    
                    blocks = ([], [])

                    if "daily_apps" in bbs[0]:
                        blocks = (blocks[0] + custom_apps(), blocks[1])
                    if "daily_sites" in bbs[1]:
                        blocks = (blocks[0], blocks[1] + custom_sites())
                    if "adult_sites" in bbs[1]:
                        blocks = (blocks[0], blocks[1] + adult())
                    if "?" in bbs[1]:
                        for sites in bbs[1].split('?'):
                            if "www" in sites:
                                blocks = (blocks[0], blocks[1] + [sites] + [sites.replace('www.','')])
                        
                    temp = shared_info[rn.tm_wday][1]
                    temp[i] = 369
                    shared_info[rn.tm_wday] = [shared_info[rn.tm_wday][0], temp]
                    if len(blocks[0]) > 0:
                        p = multiprocessing.Process(target=proc_killer, args=(bbs[0], shared_info, blocks[0], rn.tm_wday, i, w_message, lock), name=f'Process Killer-{j}')
                        processes.append(p)
                        p.start()
                    if len(blocks[1]) > 0:
                        p = multiprocessing.Process(target=site_killer, args=(bbs[1], shared_info, blocks[1], rn.tm_wday, i, w_message, lock), name=f'Site Killer-{j}')
                        processes.append(p)
                        p.start()
                    j += 1
                        
                    send_notification("Focus!", f"{bbs[0]} {bbs[1]} is active.", "Back to work!")  
                    w_message.value = w_message.value + "Started blocking: " + f"{bbs[0]} {bbs[1]}" + " " + str(datetime.now()) + "\n"
                elif not active(s_start, s_end) and (shared_info[rn.tm_wday][1][i] == 369 or shared_info[rn.tm_wday][1][i] <= -1):
                    send_notification("Done!", f"{bbs[0]} {bbs[1]} is deactived.", "Thank you!")
                    temp = shared_info[rn.tm_wday][1]
                    temp[i] = 0
                    shared_info[rn.tm_wday] = [shared_info[rn.tm_wday][0], temp]
                elif not active(s_start, s_end - timedelta(minutes = 1)) and shared_info[rn.tm_wday][1][i] == -5:
                    send_notification("Almost done!", f"{bbs[0]} {bbs[1]} will be deactived in 1 minute.", "Fasho")
                    temp = shared_info[rn.tm_wday][1]
                    temp[i] = -1
                    shared_info[rn.tm_wday] = [shared_info[rn.tm_wday][0], temp]
                elif not active(s_start, s_end - timedelta(minutes = 5)) and shared_info[rn.tm_wday][1][i] == 369:
                    send_notification("Almost done!", f"{bbs[0]} {bbs[1]} will be deactived in 5 minutes.", "Fasho")
                    temp = shared_info[rn.tm_wday][1]
                    temp[i] = -5
                    shared_info[rn.tm_wday] = [shared_info[rn.tm_wday][0], temp]
                elif active(s_start - timedelta(minutes = 1), s_end) and shared_info[rn.tm_wday][1][i] == 5:
                    send_notification("Get ready!", f"{bbs[0]} {bbs[1]} will be active in 1 minute.", "Getting ready!")
                    temp = shared_info[rn.tm_wday][1]
                    temp[i] = 1
                    shared_info[rn.tm_wday] = [shared_info[rn.tm_wday][0], temp]
                elif active(s_start - timedelta(minutes = 5), s_end) and shared_info[rn.tm_wday][1][i] == 0:
                    send_notification("Get ready!", f"{bbs[0]} {bbs[1]} will be active in 5 minutes.", "Getting ready!")
                    temp = shared_info[rn.tm_wday][1]
                    temp[i] = 5
                    shared_info[rn.tm_wday] = [shared_info[rn.tm_wday][0], temp]
        time.sleep(5)

if __name__ == "__main__":

    multiprocessing.freeze_support()
    
    file = schedule()

    data = json.loads(file)


    if data["vacation"]:
        file = always()
        data = json.loads(file)

    wth  = data["week"]["every_day"]
    what = data["week"]
    del what["every_day"]

    while True:
        try:
            remove_hosts()
            break
        except Exception as e:
            print("No permission")
            time.sleep(10)

    blocks(remake(wth, what))
    
    