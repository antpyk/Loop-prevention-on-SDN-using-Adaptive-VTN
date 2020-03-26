import re
# Test String

testdelaysmall ='Ping 192.168.1.11 (192.168.1.11): 56 data bytes, press CTRL_C to break \n' \
      ' 56 bytes from 192.168.1.11: icmp_seq=0 ttl=128 time=3.457 ms \n  ' \
      '56 bytes from 192.168.1.11: icmp_seq=1 ttl=128 time=1.084 ms \n ' \
      '56 bytes from 192.168.1.11: icmp_seq=2 ttl=128 time=1.129 ms ' \
      '56 bytes from 192.168.1.11: icmp_seq=3 ttl=128 time=1.093 ms ' \
      '56 bytes from 192.168.1.11: icmp_seq=4 ttl=128 time=1.110 ms ' \
      '--- Ping statistics for 192.168.1.11 --- 5 packet(s) transmitted,' \
      ' 5 packet(s) received, 0.0% packet loss ' \
      'round-trip min/avg/max/std-dev = 1.084/1.575/3.457/0.941 ms'
testdelaybig='ping 192.168.1.11 ' \
             '192.168.1.11 is alive, time = 1 ms'
testutilbig =' Status and Counters - Port Counters for port 7'\
  'Name  :'\
  'MAC Address     : 5820b1-c01339'\
  'Link Status     : Up '\
 ' Totals (Since boot or last clear) : '\
  'Bytes Rx        : 94508              Bytes Tx        : 72416 '\
  ' Unicast Rx      : 16                 Unicast Tx      : 16 ' \
  'Bcast/Mcast Rx  : 626                Bcast/Mcast Tx  : 347 '\
  'Errors (Since boot or last clear) : '\
   'FCS Rx          : 0                  Drops Tx        : 0 '\
  ' Alignment Rx    : 0                  Collisions Tx   : 0 '\
  ' Runts Rx        : 0                  Late Colln Tx   : 0 '\
   'Giants Rx       : 0                  Excessive Colln : 0 '\
   'Total Rx Errors : 0                  Deferred Tx     : 0 '\
  'Others (Since boot or last clear) : '\
   'Discard Rx      : 0                  Out Queue Len   : 0 '\
   'Unknown Protos  : 0 '\
  'Rates (5 minute weighted average) : '\
   'Total Rx  (bps) : 4,863,616          Total Tx  (bps) : 1,553,712 '\
   'Unicast Rx (Pkts/sec) : 0            Unicast Tx (Pkts/sec) : 0 '\
   'B/Mcast Rx (Pkts/sec) : 0            B/Mcast Tx (Pkts/sec) : 0 '\
   'Utilization Rx  : 00.48 %            Utilization Tx  : 00.15 %'

testsmallbw ='display interface GigabitEthernet 1/0/11'\
 'GigabitEthernet1/0/11 '\
'Current state: UP'\
'Line protocol state: UP'\
'IP packet frame type: Ethernet II, hardware address: 2c23-3af4-0f82'\
'Description: GigabitEthernet1/0/11 Interface'\
'Bandwidth: 1000000 kbps'\
'Loopback is not set'\
'Media type is twisted pair'\
'Port hardware type is 1000_BASE_T'\
'1000Mbps-speed mode, full-duplex mode'\
'Link speed type is autonegotiation, link duplex type is autonegotiation'\
'Flow-control is not enabled'\
'Maximum frame length: 9216'\
'Allow jumbo frames to pass'\
'Broadcast max-ratio: 100%'\
'Multicast max-ratio: 100%'\
'Unicast max-ratio: 100%'\
'PVID: 1 '\
'MDI type: Automdix '\
'Port link-type: Access '\
' Tagged VLANs:   None '\
' Untagged VLANs: 1 '\
'Port priority: 0 '\
'Last clearing of counters: Never '\
' Peak input rate: 76 bytes/sec, at 2013-01-01 00:05:34 '\
' Peak output rate: 94 bytes/sec, at 2013-01-01 00:05:34 '\
' Last 300 second input: 0 packets/sec 25 bytes/sec 0% '\
 'Last 300 second output: 0 packets/sec 75 bytes/sec 79.9992% '\
 'Input (total):  462 packets, 89099 bytes '\
'        40 unicasts, 69 broadcasts, 353 multicasts, 0 pauses'\
' Input (normal):  462 packets, - bytes'\
'        40 unicasts, 69 broadcasts, 353 multicasts, 0 pauses'\
' Input:  0 input errors, 0 runts, 0 giants, 0 throttles'\
'         0 CRC, 0 frame, - overruns, 0 aborts'\
'        - ignored, - parity errors'\
' Output (total): 965 packets, 138746 bytes'\
'         42 unicasts, 35 broadcasts, 888 multicasts, 0 pauses'\
' Output (normal): 965 packets, - bytes'\
'        42 unicasts, 35 broadcasts, 888 multicasts, 0 pauses'\
'Output: 0 output errors, - underruns, - buffer failures'\
'        0 aborts, 0 deferred, 0 collisions, 0 late collisions'\
'        0 lost carrier, - no carrier"'
testbigbw=' 21 current state: UP'\
' IP Packet Frame Type: n/a, Hardware Address: 5820b1-c0132b' \
          ' Description: 21 interface' \
          ' Loopback is n/a' \
          ' Media type is twisted Pair'\
' Port hardware type is 100/1005T'\
' 1000Mbps-speed mode,  full-duplex mode'\
' Link speed type is autonegotiation, link duplex type is autonegotiation'\
' Flow-control is not enabled'\
' The Maximum Frame Length is 9216'\
' Broadcast MAX-ratio: n/a'\
' Unicast MAX-ratio: n/a'\
' Multicast MAX-ratio:  n/a'\
' Jumbo frame: [ see "show jumbos"]'\
' PVID : 1'\
' Mdi type: MDIX'\
' Link delay is n/a'\
 'Port link-type: n/a'\
 ' Tagged   VLAN ID : none'\
 ' Untagged VLAN ID : 1'\
' Port priority: No-override'\
' Last clearing of counters: n/a'\
' Peak value of input: n/a'

def delaysmall(rawstring):
    key = 'round-trip min/avg/max/std-dev = '
    a = rawstring.find(key)
    ext = rawstring[a:]
    res = re.findall(r'[\d\.\d]+', ext)
    # print(ext)
    return float(res[-3])/10
#end
def delaybig(rawstring):
    key = 'is alive, time'
    a = rawstring.find(key)
    ext = rawstring[a:]
    res = re.findall(r'[\d\.\d]+', ext)
    # print(ext)
    return float(res[-1])/10
#end
def bwbig(rawstringUTIL,rawbw):
    key = 'Utilization Tx'
    a = rawstringUTIL.find(key)
    ext = rawstringUTIL[a:]
    res = re.findall(r'[\d\.\d]+', ext)
    # print(rawbw)
    bwstr=bwbigreal(rawbw)
    bw = float(bwstr)
    bw /= 1000
    # print('bw=', bw, 'Mbps')
    bw /= 10 * 1000
    # print('bw=', bw, '/10Gbps')
    # print(ext)
    # print(res)
    util= res[-1]
    return {'bandwidth':bw,'utilization':float(util)/100}
def bwbigreal(rawstring):
    key = 'Mbps-speed mode'
    a = rawstring.find(key)
    ext = rawstring[:a]
    # print(ext)
    res = re.findall(r'[\d\.\d]+', ext)
    # print(res)
    # print(res[-1])
    return res[-1]
def bwsmall(rawstring):
    key = 'output:'
    a = rawstring.find(key)
    ext = rawstring[a:]
    res = re.findall(r'[\d\.\d]+', ext)
    util=res[2]
    # print(ext)
    # print(res)
    # print(util)
    key2 = 'Bandwidth: '
    a2 = rawstring.find(key2)
    ext = rawstring[a2:]
    res2 = re.findall(r'[\d\.\d]+', ext)

    # print('res2',res2)

    bwstr=res2[0]
    bw=float(bwstr)
    bw/=1000
    # print('bw=',bw,'Mbps')
    bw /= 10*1000
    # print('bw=', bw, '/10Gbps')

    return {'bandwidth':bw,'utilization':float(util)/100}

# bwbigreal(testbigbw)
#bwbig(testbwbig)
# print(delaysmall(testdelaysmall))
# print(delaybig(testdelaybig))
# print(delaysmall(testdelaysmall))
# print(bwsmall(testsmallbw))