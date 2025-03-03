import os
import sys as system

def clear():
    if system.platform.startswith(('win32')):
        cls_v = os.system('cls')
        del cls_v
    elif system.platform.startswith(('linux', 'cygwin', 'darwin', 'freebsd')):
        os.system('clear')
