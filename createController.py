def createController(h, c_ip, c_name):
    url = 'http://' + c_ip + ':8083/vtn-webapi/controllers.json'

    controller = '{"controller": {"controller_id": "' + c_name + '", "ipaddr":"' + c_ip + '", "type": "odc", "version": "1.0", "auditstatus":"enable"}}'

    resp, content = h.request(url, method='POST', headers={'Content-Type': 'application/json'}, body=controller)

    return content