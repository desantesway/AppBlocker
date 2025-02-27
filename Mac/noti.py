import os

def send_notification(title, message, button):
    os.system(f'''
        osascript -e 'tell application "System Events" to activate' -e 'delay 0.1' -e 'display dialog "{message}" buttons {'{"' + button + '"}'} default button "{button}" with title "{title}" giving up after 60'
    ''')