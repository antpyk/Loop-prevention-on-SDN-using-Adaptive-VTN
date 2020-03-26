import httplib2,json
from create.createController import createController
from create.createInterface import createInterface
from create.createVBridge import createVBridge
from create.createVTN import createVTN
from mapVTN.mapVlan import mapVlan
from mapVTN.mapPort import mapPort

h = httplib2.Http(".cache")
h.add_credentials('admin', 'adminpass')

c_ip = '10.0.0.1'
c_name="controllerone"
vtn_name = "vtn1"
vb_name = "vb1"
# -----------------------------port map-------------------------------------------
# if_name = "if1"
# sw="openflow:1"
# port="openflow:1:2"
# test = createController(h,c_ip,"controllerone")
# print(test)
# testvtn = createVTN(h, c_ip, vtn_name)
# print(testvtn)
# testvb = createVBridge(h, c_ip, c_name, vtn_name, vb_name)
# print(testvb)
# testInt = createInterface(h,c_ip, vtn_name, vb_name, if_name)
# print(testInt)
# testInt2 = createInterface(h,c_ip, vtn_name, vb_name, "if2")
# print(testInt2)
# testMapPort = mapPort(h,c_ip,vtn_name,vb_name,if_name,sw,port)
# print(testMapPort)
# testMapPort2 = mapPort(h,c_ip,vtn_name,vb_name,if_name,"openflow:2","openflow:2:2")
# print(testMapPort2)

# -----------------------------vlan map-------------------------------------------
# test = createController(h,c_ip,"controllerone")
# print("Controller")
# print(test)
# testvtn = createVTN(h, c_ip, vtn_name)
# print("VTN")
# print(testvtn)
# testvb = createVBridge(h, c_ip, c_name, vtn_name, vb_name)
# print("Vb1")
# print(testvb)
# testMapVlan1 = mapVlan(h, c_ip, vtn_name, vb_name, "200")
# print("Vlan200")
# print(testMapVlan1)
# testvb2 = createVBridge(h, c_ip, c_name, vtn_name, "vb2")
# print("Vb2")
# print(testvb2)
# testMapVlan2 = mapVlan(h, c_ip, vtn_name, "vb2", "300")
# print("Vlan300")
# print(testMapVlan2)







