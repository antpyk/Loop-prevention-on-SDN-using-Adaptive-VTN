import networkx as nx
import matplotlib.pyplot as plt
import httplib2
import json
# from tkinter import *
# from _sqlite3 import Row
# from networkx.algorithms.bipartite.basic import color
# from networkx.drawing.nx_pylab import draw_networkx_edge_labels
import warnings
warnings.filterwarnings("ignore")
import pandas
from RefreshCost import *

def createTopo(c_ip):
    g = nx.Graph()

    h = httplib2.Http(".cache")
    h.add_credentials('admin', 'admin')

    resp, content = h.request('http://' + c_ip + ':8181/restconf/operational/network-topology:network-topology/', "GET")
    colors=""
    # bytes to string
    cont = content.decode("utf-8")
    # string to json
    topo = json.loads(cont)

    color_map = []
    if 'node' in topo['network-topology']['topology'][0]:
        allnode = topo['network-topology']['topology'][0]['node']
        for i in range(len(allnode)):
            # yellow host
            if (allnode[i]['node-id'][0:4] == "host"):
                g.add_node(allnode[i]['node-id'])  # add node host
                color_map.append('yellow')
            # gray switch
            else:
                g.add_node(allnode[i]['node-id'])  # add node switch
                color_map.append('cyan')

    if 'link' in topo['network-topology']['topology'][0]:
        alllink = topo['network-topology']['topology'][0]['link']
        for j in range(len(alllink)):
            g.add_edge(alllink[j]['source']['source-node'], alllink[j]['destination']['dest-node'], weight=2, color="lime")

            # print(alllink[j]['source']['source-node'] + "/" + alllink[j]['destination']['dest-node'])
            # print("path")
            # print(nx.dijkstra_path(g,alllink[j]['source']['source-node'],alllink[j]['destination']['dest-node']))
            # print(">> " , g.get_edge_data(alllink[j]['source']['source-node'],alllink[j]['destination']['dest-node']))
        # print(nx.dijkstra_path(g, 'openflow:1', 'openflow:4'))
        edges = g.edges()
        colors = [g[u][v]['color'] for u, v in edges]

    pos = nx.spring_layout(g)

    plt.figure(figsize=(6, 4))

    nx.draw_networkx_edges(g, pos, width=2, edge_color=colors)
    # nx.draw_networkx_nodes(g, pos, node_shape='d')
    nx.draw(g, pos, node_size=1300, node_color=color_map, with_labels=True, font_size=10)
    labels = nx.get_edge_attributes(g,'weight')
    nx.draw_networkx_edge_labels(g,pos,edge_labels=labels,font_size=9)
    plt.savefig('C:\\Users\\COPS\\PycharmProjects\\SDN-v2\\create\\vtntest.png')
    # print(g.get_edge_data('openflow:1','openflow:2'))
    refreshCost(g)
    return g
    # plt.show()

    # -------------------------------------------


def getTopo(c_ip):
    h = httplib2.Http(".cache")
    h.add_credentials('admin', 'admin')

    resp, content = h.request('http://' + c_ip + ':8181/restconf/operational/network-topology:network-topology/', "GET")

    # bytes to string
    cont = content.decode("utf-8")
    # string to json
    topo = json.loads(cont)

    return topo
