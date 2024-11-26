#!/usr/bin/env python3

# This code snippet reads a pcap file and prints the length of the ICMP header of the 17th packet in the file. This is for my CCOM module

from scapy.all import rdpcap

packets = rdpcap(r"C:\Users\Seagu\Downloads\icmp-trace2.pcapng")

packet_7 = packets[6]

if packet_7.haslayer("ICMP"):
    icmp_layer = packet_7["ICMP"]
    print(f"ICMP header length: {len(icmp_layer)} bytes")

else:
    print("Packet 7 does not have an ICMP layer")    