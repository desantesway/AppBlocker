import subprocess
import sys
import os

if __name__ == "__main__":
    subprocess.Popen(
        [sys.executable, "/Users/pedro/Documents/Apps/BlockApps/BlockApp/main.py"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        start_new_session=True,
        preexec_fn=os.setpgrp  # Fully detach process
    )

    print("Parent process is exiting, but the child will continue running.")
    sys.exit(0)