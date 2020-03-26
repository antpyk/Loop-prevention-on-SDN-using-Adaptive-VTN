

def mapPort(h, c_ip, vtn_name, vb_name,if_name, sw, port):
    url = 'http://' + c_ip + ':8083/vtn-webapi/vtns/' + vtn_name + '/vbridges/' + vb_name + '/interfaces/'+if_name+'/portmap'

    port_map = '{"portmap":{"logical_port_id": "PP-OF:'+sw+'-'+port+'","tagged": "false"}}'
    resp, content = h.request(url, method='PUT', headers={'Content-Type': 'application/json'}, body=port_map)

    print(content)

# Variable ---------------- example ---------- sw = 'openflow:1'
#  ------------------------------------------- port = 'openflow1:2'