import psutil
import os
from noti import send_notification
import time

def close_application(pid):
    """Close an application by its process ID."""
    try:
        os.system(f"taskkill /F /PID {pid}")
    except Exception as e:
        print(f"Failed to close process with PID {pid}: {e}")

def find_process_by_command_line(pattern):
    processes = []
    """Find processes with a command line matching the given pattern."""
    for process in psutil.process_iter(['pid', 'name']):
        try:
            if pattern.lower() in process.exe().lower():
                processes.append(process)
        except:
            continue
    return processes

def monitor_and_close_app(apps, sub):
    """Monitor if the app is open and close it if it is."""
    for app in apps:
        processes = find_process_by_command_line(app)
        for process in processes:
            if process and process.info['pid'] not in sub:
                close_application(process.info['pid'])
                if process:
                    sub.append(process.info['pid'])
        if len(processes) > 0:
            send_notification("Focus!", f"{app} is blocked.", "Back to focusing!")
    return sub
    
def update_hosts(sites):

    print(sites)
    redirect = "0.0.0.0"
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

    with open(hosts_path, 'r') as hostfile:
            hosts_content = hostfile.read()

    new_entries = [redirect + ' ' + site + '\n' for site in sites if site not in hosts_content]

    if new_entries:
        with open(hosts_path, 'a') as hostfile:
            hostfile.writelines(new_entries)

def remove_hosts():
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    
    open(hosts_path, 'w').close()

def monitor(apps, sub):
    """Monitor if the app is open and close it if it is."""
    for i in range(len(apps)):
        for app in apps[i]:
            processes = find_process_by_command_line(app)
            for process in processes:
                if process and process.info['pid'] not in sub:
                    send_notification("Focus!", f"{app} is blocked.")
                    if process:
                        sub.append(process.info['pid'])
