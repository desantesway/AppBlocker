import psutil
import os
from noti import send_notification

def close_application(pid):
    """Close an application by its process ID."""
    try:
        os.system(f"kill {pid}")
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
        if len(processes) == 1:
            continue
        if len(processes) > 3:
            os.system(f'osascript -e \'quit app "{app}"\'')
        elif app.lower() == "steam" and len(processes) == 1:
            continue
        else:
            for process in processes:
                if process and process.info['pid'] not in sub:
                    close_application(process.info['pid'])
                    if process:
                        sub.append(process.info['pid'])
            if len(processes) > 0:
                send_notification("Focus!", f"{app} is blocked.", "Back to focusing!")
    return sub
    
def update_hosts(sites):
    redirect = "0.0.0.0"
    red_ipv6 = "::1"
    hosts_path = r"/private/etc/hosts"

    with open(hosts_path, 'r+') as hostfile:
            hosts_content = hostfile.read()

    new_entries = [red_ipv6 + ' ' + site + '\n' + redirect + ' ' + site + '\n' for site in sites if site not in hosts_content]

    if new_entries:
        with open(hosts_path, 'a+') as hostfile:
            hostfile.writelines(new_entries)

def remove_hosts():
    hosts_path = r"/private/etc/hosts"
    
    open(hosts_path, 'w+').close()

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
                    
remove_hosts()