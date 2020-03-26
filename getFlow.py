import httplib2

h = httplib2.Http(".cache")
h.add_credentials('admin', 'admin')
controller_ip = '10.0.0.1'
# controller_ip = input("Controller Ip : ")

#/node/openflow:1/table/01.254
resp, content = h.request('http://'+controller_ip+':8181/restconf/operational/opendaylight-inventory:nodes/node/openflow:1/table/0', "GET")
# convert bytes to string
cont = content.decode("utf-8")
print (cont)