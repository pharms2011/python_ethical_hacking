import optparse

import scapy.all as scapy

def net_scan():
    #0. Get Arguments from the command line
    options = get_args()
    ip = options.ip
    #1. Create ARP request to broadcast
    arp_request = arp_broadcast_request(ip)
    #2. Send Packet and recieve response
    response = scan(arp_request)
    #3. Parse Response
    answered_packets = parse_answered_packets(response)
    #4. Print result
    print_packets(answered_packets)
# 0. Get Arguments from the command line
def get_args():
    parser = optparse.OptionParser()

    parser.add_option("-t", "--target", dest="target", help="Ip address/range to scan for mac addresses")

    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an ip pr ip range, use --help for more info")
    if not options.new_mac:
        options.target = "10.0.0.65/24"
    return options

# 1. Create ARP request to boradcast channel
def arp_broadcast_request(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    return arp_request_broadcast

# 2. Send Packet and receive response
def scan(broadcast_request):
    # Send and Recieve = sr
    # sr + custome ether = srp
    answered, unanswered = scapy.srp(broadcast_request, timeout=1)
    results = parse_answered_packets(answered)
    print_packets(results)

# 3. Parse Response
def parse_answered_packets(answered):
    result = []
    for answer in answered:
        packet = {}
        packet['ip'] = answer.query.pdst
        packet['mac'] = answer.answer.src
        result.append(packet)
    return result

# 4. Print result
def print_packets(packets):
    print("----------------------------------------------------")
    for packet in packets:
        print("ip: " + packet['ip'] + "\t\t mac: " + packet['mac'])
    print("----------------------------------------------------")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    net_scan()