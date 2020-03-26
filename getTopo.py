import httplib2
import json

h = httplib2.Http(".cache")
h.add_credentials('admin', 'admin')

resp, content = h.request('http://10.0.0.1:8181/restconf/operational/network-topology:network-topology', "GET")

# bytes to string
cont = content.decode("utf-8")
print(cont)

# string to json
topo = json.loads(cont)

allnode = topo['network-topology']['topology'][0]['node']
alllink = topo['network-topology']['topology'][0]['link']

print(alllink)

# Show link
# print(len(alllink))
# for i in range(len(alllink)):
#     print(alllink[i])
# print()
#
# for i in range(len(alllink)):
#     print(alllink[i]['destination']['dest-node'])
# print()
# Show Host Detail
# for i in range(len(allnode)):
#     if(allnode[i]['node-id'][0:4] == "host"):
#         print("Host ID:", allnode[i]['node-id'])
#         print("\tMAC Address:" , allnode[i]['host-tracker-service:addresses'][0]['mac'])
#         print("\tIP Address:", allnode[i]['host-tracker-service:addresses'][0]['ip'])
#
# print()

# Show Switch Detail
# for i in range(len(allnode)):
#     if(allnode[i]['node-id'][0:4] != "host"):
#         print("Switch ID:" , allnode[i]['node-id'])
#         for j in range(len(allnode[i]['termination-point'])):
#             for k in range(len(alllink)):
#                 if((allnode[i]['node-id'] == alllink[k]['source']['source-node']) and (alllink[k]['source']['source-tp'][11:16] == allnode[i]['termination-point'][j]['tp-id'][11:16])):
#                     print("\tPort:", allnode[i]['termination-point'][j]['tp-id'][11:16], "connects",alllink[k]['destination']['dest-node'] )
