def delFlow(h, controller_ip):
    import httplib2, json

    # controller_ip = '10.0.0.1'
    # controller_ip = input("Controller Ip : ")

    url = 'http://' + controller_ip + '6:8181/restconf/config/opendaylight-inventory:nodes'

    jsoncomeback = '{"nodes":{"node":[{"id":"openflow:2","flow-node-inventory:table":[{"id":0,"flow":[{"id":"2","flow-name":"flow2","instructions":{"instruction":[{"order":0,"apply-actions":{"action":[{"order":0,"output-action":{"output-node-connector":"3"}}]}}]},"priority":2,"table_id":0,"match":{"ethernet-match":{"ethernet-type":{"type":2048}},"ipv4-source":"10.0.0.5/32","ipv4-destination":"10.0.0.1/32"}},{"id":"1","flow-name":"flow1","instructions":{"instruction":[{"order":0,"apply-actions":{"action":[{"order":0,"output-action":{"output-node-connector":"1"}}]}}]},"priority":1,"table_id":0,"match":{"ethernet-match":{"ethernet-type":{"type":2048}},"ipv4-source":"10.0.0.1/32","ipv4-destination":"10.0.0.3/32"}}]}]},{"id":"openflow:3","flow-node-inventory:table":[{"id":0,"flow":[{"id":"2","flow-name":"flow2","instructions":{"instruction":[{"order":0,"apply-actions":{"action":[{"order":0,"output-action":{"output-node-connector":"4"}}]}}]},"priority":2,"table_id":0,"match":{"ethernet-match":{"ethernet-type":{"type":2048}},"ipv4-source":"10.0.0.5/32","ipv4-destination":"10.0.0.1/32"}}]}]},{"id":"openflow:1","flow-node-inventory:table":[{"id":0,"flow":[{"id":"2","flow-name":"flow2","instructions":{"instruction":[{"order":0,"apply-actions":{"action":[{"order":0,"output-action":{"output-node-connector":"1"}}]}}]},"priority":2,"table_id":0,"match":{"ethernet-match":{"ethernet-type":{"type":2048}},"ipv4-source":"10.0.0.5/32","ipv4-destination":"10.0.0.1/32"}},{"id":"1","flow-name":"flow1","instructions":{"instruction":[{"order":0,"apply-actions":{"action":[{"order":0,"output-action":{"output-node-connector":"4"}}]}}]},"priority":1,"table_id":0,"match":{"ethernet-match":{"ethernet-type":{"type":2048}},"ipv4-source":"10.0.0.1/32","ipv4-destination":"10.0.0.3/32"}}]}]}]}}'

    resp, content = h.request(url, method='DELETE', headers={'Content-Type': 'application/json'}, body=jsoncomeback)

    return (content)