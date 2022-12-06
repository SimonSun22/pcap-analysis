import dpkt
import datetime

# Open pcap file in binary mode

f = open(input("Enter the file: "), 'rb')
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

        print ('Timestamp: ', str(datetime.datetime.utcfromtimestamp(timestamp)))
        print ('IP: %s -> %s   (len=%d) ' % \
              (dpkt.ip.inet_to_str(ip.src), dpkt.ip.inet_to_str(ip.dst), ip.len))
        print ('Seq=%d Ack=%d \n' % (tcp.seq, tcp.ack))

f.close()