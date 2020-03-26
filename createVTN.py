def createVTN(h, c_ip, vtn_name):
    url = 'http://' + c_ip + ':8083/vtn-webapi/vtns.json'

    vtn = '{"vtn" : {"vtn_name":"' + vtn_name + '","description":"test VTN1" }}'

    resp, content = h.request(url, method='POST', headers={'Content-Type': 'application/json'}, body=vtn)

    return content