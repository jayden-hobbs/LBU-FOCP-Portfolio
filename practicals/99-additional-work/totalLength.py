#!/usr/bin/env python3

# This code snippet reads a pcap file and prints the total length of the 17th packet in the file. This is for my CCOM module

from scapy.all import rdpcap

packets = rdpcap(r"C:\Users\Seagu\Downloads\icmp-trace2.pcapng")
packet_index = 6
packet = packets[packet_index]

total_length = len(packet)

print(f"Total length of packet {packet_index + 1}: {total_length} bytes")