# About the project

This project utilized **tcpdump** to capture the trafic when downloading a target file and analyzed the pcap file with **dpkt**.

## Capture with tcpdump
```command
root-simon@rootsimon-VirtualBox:~/Desktop/pcap-test$ sudo tcpdump -w test1.pcap  -i enp0s3 -c 30 -v tcp and port 443 and host 10.0.2.15

'-c 30': I limit the tcp connection count to 30 since the original file is a bit large
'port 443': I specify the port to 443 since it is a https:// website
```

## Download file with curl
```command
root-simon@rootsimon-VirtualBox:~/Desktop/pcap-test$ curl -O https://www.1001fonts.com/download/open-sans.zip
```

## Sample output of the program
```command
root-simon@rootsimon-VirtualBox:~/Desktop/pcap-test$ python3 pcap-parsing.py 

Timestamp:  2022-11-14 22:04:23.552870
IP: 10.0.2.15 -> 54.39.182.171   (len=60 ttl=64 DF=1 MF=0 offset=0) 

Timestamp:  2022-11-14 22:04:23.565373
IP: 54.39.182.171 -> 10.0.2.15   (len=44 ttl=64 DF=0 MF=0 offset=0) 
```

## Validate
```command
root-simon@rootsimon-VirtualBox:~/Desktop/pcap-test$ ping 1001fonts.com
PING 1001fonts.com (54.39.182.171) 56(84) bytes of data.
64 bytes from 1001fonts.com (54.39.182.171): icmp_seq=1 ttl=46 time=15.8 ms

'1001fonts.com (54.39.182.171)' matches the above output ip address
```
