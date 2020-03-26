def createInterface(h, c_ip, vtn_name, vb_name, if_name):
    url = 'http://' + c_ip + ':8083/vtn-webapi/vtns/' + vtn_name + '/vbridges/' + vb_name + '/interfaces.json'
    interface = '{"interface": {"if_name": "' + if_name + '"}}'

    resp, content = h.request(url, method='POST', headers={'Content-Type': 'application/json'}, body=interface)

    return content