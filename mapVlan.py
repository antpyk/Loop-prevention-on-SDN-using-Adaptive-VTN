import httplib2,json

def mapVlan(h, c_ip, vtn_name, vb_name, vlan):
    url = 'http://' + c_ip + ':8083/vtn-webapi/vtns/' + vtn_name + '/vbridges/v' + vb_name + '/vlanmaps.json'

    vlan_id = '{"vlanmap" : {"vlan_id": ' + vlan + ' }}'
    # print(vlan_id)
    resp, content = h.request(url, method='POST', headers={'Content-Type': 'application/json'}, body=vlan_id)

    print(content)

    # '{"vlanmap" : {"vlan_id": 400 }}'
    # http://127.0.0.1:8083/vtn-webapi/vtns/vtn1/vbridges/vb1/vlanmaps.json