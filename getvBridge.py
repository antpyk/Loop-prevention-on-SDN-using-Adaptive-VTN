import json
def getVBridge(h,controller_ip,vtn_name):

    resp, content = h.request('http://' + controller_ip + ':8083/vtn-webapi/vtns/' + vtn_name + '/vbridges/detail', "GET")

    # bytes to string
    cont = content.decode("utf-8")
    cont_j = json.loads(cont)
    return cont_j