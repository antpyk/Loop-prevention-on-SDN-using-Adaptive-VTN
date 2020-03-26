import json

def getVTN(h,controller_ip):

    resp, content = h.request('http://' + controller_ip + ':8083/vtn-webapi/vtns/detail', "GET")

    # bytes to string
    cont = content.decode("utf-8")
    cont_j = json.loads(cont)

    return cont_j