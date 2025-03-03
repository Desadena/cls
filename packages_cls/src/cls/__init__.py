import os
import sys as system

def clear():
    if system.platform.startswith(('win32')):
        cmd = "cls"
    elif system.platform.startswith(('linux', 'cygwin', 'darwin', 'freebsd')):
        cmd = "clear"
    else:
        print("Platform not recognised")
        cmd = input("Clear screen command on your computer")
    cmd_cls_v = os.system(cmd)
    del cmd_cls_v
