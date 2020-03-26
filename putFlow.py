import httplib2


def putFlow(controller_ip, source_node, source_port, dest_port, flow_id):
    h = httplib2.Http(".cache")
    h.add_credentials('admin', 'admin')

    url = 'http://' + controller_ip + ':8181/restconf/config/opendaylight-inventory:nodes'
    jsoncomeback = '{"nodes":{"node":[{"id":"' + source_node + '",' \
                                                               '"flow-node-inventory:table":[{"id":0,"flow":[{"id":"' + str(
        flow_id) + '","flow-name":"flow' + str(flow_id) + '","instructions":' \
                                                          '{"instruction":[{"order":0,"apply-actions":{"action":[{"order":0,"output-action"' \
                                                          ':{"output-node-connector":"' + dest_port + '"}}]}}]},"priority":2,"table_id":0,"match":' \
                                                                                                      '{"in-port":"' + source_port + '"}}]}]}]}}'

    resp, content = h.request(url, method='PUT', headers={'Content-Type': 'application/json'}, body=jsoncomeback)

    print(content)
    print("Put Flow Success.")


def put2Flow(controller_ip, source_node, source_port, dest_port):
    h = httplib2.Http(".cache")
    h.add_credentials('admin', 'admin')

    flow_id = 0
    url = 'http://' + controller_ip + ':8181/restconf/config/opendaylight-inventory:nodes'
    jsoncomeback = '{"nodes":{"node":[{"id":"' + source_node + '",' \
                    '"flow-node-inventory:table":[{"id":0,"flow":[{"id":"' + str(flow_id) + '",' \
                    '"flow-name":"flow' + str(flow_id) + '","instructions":' \
                    '{"instruction":[{"order":0,"apply-actions":{"action":[{"order":0,"output-action"' \
                    ':{"output-node-connector":"' + dest_port + '"}}]}}]},"priority":1,"table_id":0,"match":' \
                    '{"in-port":"' + source_port + '"}},{"id":"' + str(flow_id+1) + '",' \
                    '"flow-name":"flow' + str(flow_id+1) + '","instructions":' \
                    '{"instruction":[{"order":0,"apply-actions":{"action":[{"order":0,"output-action"' \
                    ':{"output-node-connector":"' + source_port + '"}}]}}]},"priority":1,"table_id":0,"match":' \
                    '{"in-port":"' + dest_port + '"}}]}]}]}}'

    resp, content = h.request(url, method='put', headers={'Content-Type': 'application/json'}, body=jsoncomeback)

    print(content)
    print("Put Flow Success.")
def put2FlowPerNode(controller_ip, source_node, source_port, dest_port):
    h = httplib2.Http(".cache")
    h.add_credentials('admin', 'admin')

    flow_id = 0
    url = 'http://' + controller_ip + ':8181/restconf/config/opendaylight-inventory:nodes/node/'+ source_node +'/flow-node-inventory:table/0'
    jsoncomeback =  '{"flow-node-inventory:table":[{"id":0,"flow":[{"id":"' + str(flow_id) + '",' \
                    '"flow-name":"flow' + str(flow_id) + '","instructions":' \
                    '{"instruction":[{"order":0,"apply-actions":{"action":[{"order":0,"output-action"' \
                    ':{"output-node-connector":"' + dest_port + '"}}]}}]},"priority":1,"table_id":0,"match":' \
                    '{"in-port":"' + source_port + '"}},{"id":"' + str(flow_id+1) + '",' \
                    '"flow-name":"flow' + str(flow_id+1) + '","instructions":' \
                    '{"instruction":[{"order":0,"apply-actions":{"action":[{"order":0,"output-action"' \
                    ':{"output-node-connector":"' + source_port + '"}}]}}]},"priority":1,"table_id":0,"match":' \
                    '{"in-port":"' + dest_port + '"}}]}]}'

    resp, content = h.request(url, method='PUT', headers={'Content-Type': 'application/json'}, body=jsoncomeback)

    print(content)
    print("Put Flow Success.")

def clearFlow(controller_ip):
    h = httplib2.Http(".cache")
    h.add_credentials('admin', 'admin')

    url = 'http://' + controller_ip + ':8181/restconf/config/opendaylight-inventory:nodes'

    resp, content = h.request(url, method='DELETE', headers={'Content-Type': 'application/json'})

    print(content)
    print("Clear Flow Success.")