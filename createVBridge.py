def createVBridge(h, c_ip, c_name, vtn_name, vb_name):
    url = 'http://' + c_ip + ':8083/vtn-webapi/vtns/' + vtn_name + '/vbridges.json'

    vbridge = '{"vbridge" : {"vbr_name":"' + vb_name + '","controller_id":"' + c_name + '","domain_id":"(DEFAULT)" }}'

    resp, content = h.request(url, method='POST', headers={'Content-Type': 'application/json'}, body=vbridge)

    return content