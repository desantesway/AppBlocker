from crypt_code import get_code
from pynput import keyboard
import time
import multiprocessing
import datetime

keys_pressed = ""
code = get_code()[:-18]

def sleep_min(start, sleep):
    while datetime.datetime.now() < start + datetime.timedelta(minutes=sleep):
        time.sleep(5)

def on_press(key):
    global keys_pressed, code
    try:
        keys_pressed += key.char
        if len(keys_pressed) > 30:
            keys_pressed = keys_pressed[-30:]
        #print(keys_pressed)
        if code in keys_pressed:
            keys_pressed = ""
            return False
    except Exception:
        pass
    
def listen():
    with keyboard.Listener(on_press=lambda key: on_press(key)) as listener:
        listener.join()

def listener(lock, disabled, message):
    with lock:
        message.value = message.value + multiprocessing.current_process().name + " " + str(datetime.datetime.now()) + "\n" 
    while True:
        print(disabled.value)
        listen()
        with lock:
            message.value = message.value + multiprocessing.current_process().name + " " + str(datetime.datetime.now()) + " " + "code detected!" + "\n" 
            disabled.value = 1
        # 115, 4, 1
        sleep_min(datetime.datetime.now(), 115)
        with lock:
            disabled.value = -5
        sleep_min(datetime.datetime.now(), 4)
        with lock:
            disabled.value = -1
        sleep_min(datetime.datetime.now(), 1)
        with lock:
            disabled.value = 0
            
if __name__ == "__main__":
    sleep_min(datetime.datetime.now(), 1)
    #listener(False, 0, "")