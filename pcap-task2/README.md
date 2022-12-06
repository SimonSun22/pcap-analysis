# Extract Ack and Seq

## This part prints the acknowledgement and sequence number for each TCP connection captured

### Capture process

```command
root-simon@rootsimon-VirtualBox:~/Desktop/pcap-test$ sudo tcpdump -w [xxx].pcap  -i enp0s3 host [domain]

root-simon@rootsimon-VirtualBox:~/Desktop/pcap-test$ curl [domain]
```

### Sample output

After trying parsing different domains, the same behavior that such 11 packets captured was discovered. And I assume this to be the normal TCP 3-Way handshake.

```command
root-simon@rootsimon-VirtualBox:~/Desktop/pcap-test$ python3 tcp_parse.py
Enter the file: facebook.pcap
Timestamp:  2022-12-06 21:13:18.874729
IP: 10.0.2.15 -> 157.240.241.35   (len=60) 
Seq=2237882255 Ack=0 

Timestamp:  2022-12-06 21:13:18.881262
IP: 157.240.241.35 -> 10.0.2.15   (len=44) 
Seq=41792001 Ack=2237882256 

Timestamp:  2022-12-06 21:13:18.881318
IP: 10.0.2.15 -> 157.240.241.35   (len=40) 
Seq=2237882256 Ack=41792002 

Timestamp:  2022-12-06 21:13:18.881536
IP: 10.0.2.15 -> 157.240.241.35   (len=116) 
Seq=2237882256 Ack=41792002 

Timestamp:  2022-12-06 21:13:18.881770
IP: 157.240.241.35 -> 10.0.2.15   (len=40) 

# 2237882332[this ACK] - 2237882256[previous SEQ] = 116 - 40[body length]

Seq=41792002 Ack=2237882332 

Timestamp:  2022-12-06 21:13:18.885497
IP: 157.240.241.35 -> 10.0.2.15   (len=236) 
Seq=41792002 Ack=2237882332 

Timestamp:  2022-12-06 21:13:18.885514
IP: 10.0.2.15 -> 157.240.241.35   (len=40) 
Seq=2237882332 Ack=41792198 

Timestamp:  2022-12-06 21:13:18.885746
IP: 10.0.2.15 -> 157.240.241.35   (len=40) 
Seq=2237882332 Ack=41792198 

Timestamp:  2022-12-06 21:13:18.886150
IP: 157.240.241.35 -> 10.0.2.15   (len=40) 
Seq=41792198 Ack=2237882333 

Timestamp:  2022-12-06 21:13:18.889920
IP: 157.240.241.35 -> 10.0.2.15   (len=40) 
Seq=41792198 Ack=2237882333 

Timestamp:  2022-12-06 21:13:18.889939
IP: 10.0.2.15 -> 157.240.241.35   (len=40) 
Seq=2237882333 Ack=41792199 

```
