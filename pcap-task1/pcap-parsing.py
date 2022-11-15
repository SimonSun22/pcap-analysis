#!/usr/bin/env python3

import dpkt
import datetime

# Open pcap file in binary mode
f = open('test1.pcap', 'rb')
pcap = dpkt.pcap.Reader(f)

for timestamp, buf in pcap:
    eth = dpkt.ethernet.Ethernet(buf)

    # Make sure the Ethernet data contains an IP packet
    if not isinstance(eth.data, dpkt.ip.IP):
        print ('Non IP Packet type not supported %s\n' % eth.data.__class__.__name__)
        continue

    # Now grab the data within the Ethernet frame (the IP packet)
    ip = (eth.data)

    if isinstance(ip.data, dpkt.tcp.TCP):

        # Set the TCP data
        tcp = ip.data

        # Pull out fragment information (flags and offset all packed into off field, so use bitmasks)
        do_not_fragment = bool(ip.off & dpkt.ip.IP_DF)
        more_fragments = bool(ip.off & dpkt.ip.IP_MF)
        fragment_offset = ip.off & dpkt.ip.IP_OFFMASK

        print ('Timestamp: ', str(datetime.datetime.utcfromtimestamp(timestamp)))
        print ('IP: %s -> %s   (len=%d ttl=%d DF=%d MF=%d offset=%d) \n' % \
              (dpkt.ip.inet_to_str(ip.src), dpkt.ip.inet_to_str(ip.dst), ip.len, ip.ttl, do_not_fragment, more_fragments, fragment_offset))

f.close()