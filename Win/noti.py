import os
import time
import pyautogui
import ctypes

def send_notification(title, message, button):
    ctypes.windll.user32.MessageBoxW(0, message, title, 1)

