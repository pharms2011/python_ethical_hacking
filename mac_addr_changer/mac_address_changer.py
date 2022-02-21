# Giving python system access allows programatic control over system configurations, including the MAC address of
# specific interfaces, This would allow you to
# sudo ifconfig eth0 down
# sudo ifconfig eth0 hw ether {MAC Address ex. 00:11:22:33:44:55}

# This is the module capable of runnning sys commands from any platform given the right permissions.

#!/usr/bin/env python

import subprocess
import optparse
import re

def get_args():
        parser = optparse.OptionParser()

        parser.add_option("-i","--interface", dest="interface", help = "Interface to help change your MAC Address")
        parser.add_option("-m","--mac", dest="new_mac", help = "New Mac Address") 

        (options, arguments) = parser.parse_args()

        if not options.interface:
            parser.error("[-] Please specify an interface, use --help for more info")
        if not options.new_mac:
            options.new_mac = "11:22:33:44:55:66"
        return options
        

def change_mac(interface, mac_addr):
        # Use a breakpoint in the code line below to debug your script.
    subprocess.call("ifconfig", shell=True)

    call_set_interface_down = "fconfig " + interface + " down"
    call_set_interface_up = "fconfig " + interface + " up"
    call_set_mac_addr = "ifconfig " + interface + "hw ether " +mac_addr

    print(call_set_interface_down)
    # subprocess.call(call_set_interface_down, shell=True)
    subprocess.call(["ifconfig", interface, "down"])
    print(call_set_mac_addr)
    # subprocess.call(call_set_mac_addr, shell=True)
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_addr])
    print(call_set_interface_up)
    # subprocess.call(call_set_interface_up, shell=True)
    subprocess.call(["ifconfig", interface, "down"])

    # subprocess.call("ifconfig", shell=True)


def verify_mac_change(interface, mac_addr):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_addr_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    mac_addr_result = mac_addr_search_result.group(0)

    if mac_addr_result == mac_addr:
        print("Interface changed successsfully")
    else:
        print("Interface " + interface + " not changed successsfully, value is " + mac_addr_result)



def mac_changer():
    options = get_args()

    # interface = input("Please enter the interface you would like to change: ")
    interface = options.interface
    # mac_addr = input("Please enter the new mac address for " + interface + ":")
    mac_addr = options.new_mac

    change_mac(interface, mac_addr)

    verify_mac_change(interface, mac_addr)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mac_changer()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
