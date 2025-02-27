import subprocess
import sys
import os

if __name__ == "__main__":
    subprocess.Popen(
        [sys.executable, os.path.dirname(os.path.realpath(__file__)) + "/main.py"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        start_new_session=True,
        preexec_fn=os.setpgrp  # Fully detach process
    )

    print("Parent process is exiting, but the child will continue running.")
    sys.exit(0)