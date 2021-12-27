# Giving python system access allows programatic control over system configurations, including the MAC address of
# specific interfaces, This would allow you to
# sudo ifconfig eth0 down
# sudo ifconfig eth0 hw ether {MAC Address ex. 00:11:22:33:44:55}

# This is the module capable of runnning sys commands from any platform given the right permissions.

#!/usr/bin/env python

import subprocess

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    subprocess.call("ifconfig eth0 up", shell=True)
    subprocess.call("ifconfig", shell=True)

    # subprocess.call("ifconfig eth0 down", shell=True)
    # subprocess.call("ifconfig hw ether 11:22:33:44:55:66", shell=True)
    # subprocess.call("ifconfig eth0 up", shell=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Preston')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
