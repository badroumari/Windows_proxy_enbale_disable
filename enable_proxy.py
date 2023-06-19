from winreg import *
import ctypes
import sys
import random
from time import sleep


def enable_proxy(state,proxy):
    INTERNET_SETTINGS = OpenKey(HKEY_CURRENT_USER,
        r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
        0, KEY_ALL_ACCESS)
    def set_key(name, value, type):
        SetValueEx(INTERNET_SETTINGS, name, 0, type, value)
    if state == "off":
        set_key('ProxyEnable', 0, REG_DWORD)
        for i in range(10):
           sys.stdout.write("\r Changing Proxy In : %d Seconds" %int(i))
           sys.stdout.flush()
           sleep(1)
    elif state == "on":
        set_key('ProxyEnable', 1, REG_DWORD)
        set_key('ProxyServer', proxy, REG_SZ)

    INTERNET_OPTION_REFRESH = 37
    INTERNET_OPTION_SETTINGS_CHANGED = 39
    internet_set_option = ctypes.windll.Wininet.InternetSetOptionW
    internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)
    internet_set_option(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)
    return "\nProxy Enabled"

# port=random.randint(26745,26754)
# proxy="atlas.p.shifter.io:"+str(port)
# print(enable_proxy("off",proxy))
proxy=sys.argv[1]
print(enable_proxy("on",proxy))