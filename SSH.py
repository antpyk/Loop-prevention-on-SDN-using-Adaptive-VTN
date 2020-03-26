from netmiko import ConnectHandler
import math
from wordextract import *
#
# ### PROCURVE
# # hpsw = {'device_type': 'hp_procurve','ip': '192.168.1.30','username': 'test','password': 'test'}
# hpsw = {'device_type': 'hp_comware','ip': '192.168.1.10','username': 'test','password': 'test'}
# net_connect = ConnectHandler(**hpsw)
# #net_connect
# # output = net_connect.send_command("show interfaces 21 hc")
# output = net_connect.send_command("ping 192.168.1.30")
#
#
# print(output)
# extdelay=wordextract.delaysmall(output)
# print('extracted avg delay',extdelay)
def establishconnectionenable(dtype,ip,username,password,command):

    hpsw = {'device_type': dtype, 'ip': ip, 'username': username, 'password': password}
    net_connect = ConnectHandler(**hpsw)
    # net_connect
    output =net_connect.send_command('config t')
    output += net_connect.send_command(command)

    return output


def establishconnection(dtype,ip,username,password,command):

    hpsw = {'device_type': dtype, 'ip': ip, 'username': username, 'password': password}

    net_connect = ConnectHandler(**hpsw)
    # net_connect
    output = net_connect.send_command(command)
    net_connect.disconnect()
    return output

def delay(Model,ControlIP,InterfaceIP,username,password):
    dtype=''
    if Model=='Procurve':
        dtype='hp_procurve'
    if Model=='Comware':
        dtype='hp_comware'
    ###
    command = 'ping '+InterfaceIP
    output = establishconnection(dtype,ControlIP,username,password,command)
    # print(output)
    delay=math.inf
    if Model=='Procurve':
        delay=delaybig(output)
    if Model=='Comware':
        delay = delaysmall(output)
    ###

    return delay
def bwutil(Model,ControlIP,InterfaceNumber,username,password):
    dtype = ''
    if Model == 'Procurve':
        dtype = 'hp_procurve'
        command='show interface '+str(InterfaceNumber)+' hc'
        commandbw='display interface '+str(InterfaceNumber)
        bwoutput = establishconnection(dtype, ControlIP, username, password, commandbw)

    if Model == 'Comware':
        dtype = 'hp_comware'
        command='display interface GigabitEthernet 1/0/'+str(InterfaceNumber)
    ###
    output = establishconnection(dtype, ControlIP, username, password, command)
    # print(output)
    bw=100
    if Model == 'Procurve':
        bw=bwbig(output,bwoutput)
        # bw=bwbigreal(bwoutput)
    if Model == 'Comware':
        bw = bwsmall(output)
    return bw


