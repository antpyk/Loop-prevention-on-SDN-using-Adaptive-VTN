import httplib2, json


class getData:
    username = ""
    password = ""
    controllerIPADDR = ""

    def __init__(self, username, password, controllerIPADDR):
        self.username = username
        self.password = password
        self.controllerIPADDR = controllerIPADDR

    def getcontrollerIPADDR(self):
        return self.controllerIPADDR

    def getNetworkTopology(self):
        h = httplib2.Http(".cache")
        h.add_credentials(self.username, self.password)
        resp, topology_content = h.request(
            'http://' + self.controllerIPADDR + ':8181/restconf/operational/network-topology:network-topology/', "GET")
        topology_cont = topology_content.decode("utf-8")
        topology_j = json.loads(topology_cont)

        return topology_j

    def getInventoryConfig(self):
        h = httplib2.Http(".cache")
        h.add_credentials(self.username, self.password)
        resp, flowconfig_content = h.request(
            'http://' + self.controllerIPADDR + ':8181/restconf/config/opendaylight-inventory:nodes', "GET")
        flowconfig_cont = flowconfig_content.decode("utf-8")
        flowconfig_j = json.loads(flowconfig_cont)
        return flowconfig_j

    def getInventoryOperational(self):
        h = httplib2.Http(".cache")
        h.add_credentials(self.username, self.password)
        resp, flowoperation_content = h.request(
            'http://' + self.controllerIPADDR + ':8181/restconf/operational/opendaylight-inventory:nodes', "GET")
        flowoperation_cont = flowoperation_content.decode("utf-8")
        flowoperation_j = json.loads(flowoperation_cont)
        return flowoperation_j
