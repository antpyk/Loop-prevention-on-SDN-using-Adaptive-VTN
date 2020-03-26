import networkx as nx
from operator import itemgetter
testmatchflow =[{'node': 'openflow:1', 'flowentry': {'instructions': {'instruction': [{'order': 0, 'apply-actions': {'action': [{'output-action': {'output-node-connector': '3'}, 'order': 0}]}}]}, 'table_id': 0, 'id': '0', 'match': {'ipv4-destination': '10.0.0.4/32', 'ipv4-source': '10.0.0.1/32', 'ethernet-match': {'ethernet-type': {'type': 2048}}}, 'flow-name': 'h1 ping h4'}}, {'node': 'openflow:2', 'flowentry': {'instructions': {'instruction': [{'order': 0, 'apply-actions': {'action': [{'output-action': {'output-node-connector': '2'}, 'order': 0}]}}]}, 'table_id': 0, 'id': '0', 'match': {'ipv4-destination': '10.0.0.4/32', 'ipv4-source': '10.0.0.1/32', 'ethernet-match': {'ethernet-type': {'type': 2048}}}, 'flow-name': 'h1 ping h4'}}]
testmatchflowinv =[{'node': 'openflow:2', 'flowentry': {'instructions': {'instruction': [{'order': 0, 'apply-actions': {'action': [{'output-action': {'output-node-connector': '3'}, 'order': 0}]}}]}, 'table_id': 0, 'id': '0', 'match': {'ipv4-destination': '10.0.0.4/32', 'ipv4-source': '10.0.0.1/32', 'ethernet-match': {'ethernet-type': {'type': 2048}}}, 'flow-name': 'h1 ping h4'}}, {'node': 'openflow:1', 'flowentry': {'instructions': {'instruction': [{'order': 0, 'apply-actions': {'action': [{'output-action': {'output-node-connector': '2'}, 'order': 0}]}}]}, 'table_id': 0, 'id': '0', 'match': {'ipv4-destination': '10.0.0.4/32', 'ipv4-source': '10.0.0.1/32', 'ethernet-match': {'ethernet-type': {'type': 2048}}}, 'flow-name': 'h1 ping h4'}}]

Graph=nx.DiGraph()
Graph.add_node('openflow:1',{'controlip': '192.168.1.10', 'interfaceip': '10.0.0.10', 'username': 'test', 'password': 'test','model':'Comware'})
Graph.add_node('openflow:2',{'controlip': '192.168.1.20', 'interfaceip': '10.0.0.20', 'username': 'test', 'password': 'test','model':'Comware'})
Graph.add_node('openflow:3',{'controlip': '192.168.1.30', 'interfaceip': '10.0.0.30', 'username': 'test', 'password': 'test','model':'Procurve'})
# Graph.add_node('host:5a:3c:93:76:4e:86',{'controlip': '192.168.1.12', 'interfaceip': '10.0.0.9', 'username': 'admin', 'password': 'admin'})
#newlink
# Graph.add_edge('openflow:1','openflow:3',{'source-tp': 'openflow:1:4', 'dest-tp': 'openflow:3:3', 'weight': 1, 'color': 'lime'})
# Graph.add_edge('openflow:3','openflow:1',{'source-tp': 'openflow:3:3', 'dest-tp': 'openflow:1:4', 'weight': 1, 'color': 'lime'})

Graph.add_edge('openflow:2','openflow:3',{'source-tp': 'openflow:2:1', 'dest-tp': 'openflow:3:1', 'weight': 1, 'color': 'lime','fixed': False, 'bandwidth': 0.1, 'utilization':0,'delay':0.1})
Graph.add_edge('openflow:3','openflow:2',{'source-tp': 'openflow:3:1', 'dest-tp': 'openflow:2:1', 'weight': 1, 'color': 'lime','fixed': True, 'bandwidth': 0.2, 'utilization':0,'delay':0.1})

Graph.add_edge('openflow:2','openflow:1',{'source-tp': 'openflow:2:8', 'dest-tp': 'openflow:1:3', 'weight': 1, 'color': 'lime','fixed': False, 'bandwidth': 0.4, 'utilization':0,'delay':0.1})
Graph.add_edge('openflow:1','openflow:2',{'source-tp': 'openflow:1:3', 'dest-tp': 'openflow:2:8', 'weight': 1, 'color': 'lime', 'fixed': True, 'bandwidth': 0.3, 'utilization':0,'delay':0.1})

Graph.add_edge('openflow:2','host:5a:3c:93:76:4e:86',{'source-tp': 'openflow:2:2', 'dest-tp': 'host:5a:3c:93:76:4e:86', 'weight': 1, 'color': 'lime','fixed': False, 'bandwidth': 1.2, 'utilization':0,'delay':0.1})

Graph.add_edge('host:5a:3c:93:76:4e:86','openflow:2',{'source-tp': 'host:5a:3c:93:76:4e:86', 'dest-tp': 'openflow:2:2', 'weight': 1, 'color': 'lime','fixed': True, 'bandwidth': 1.3, 'utilization':0,'delay':0.1})
#Graph.add_edge('openflow:2','openflow:3',{'source-tp': 'openflow:2:6', 'dest-tp': 'openflow:3:6', 'weight': 1, 'color': 'lime'})
# #old link
# Graph.add_edge('openflow:1','openflow:2',{'source-tp': 'openflow:1:3', 'dest-tp': 'openflow:2:3', 'weight': 20, 'color': 'lime'})
#Graph.add_edge('openflow:2','host:5a:3c:93:76:4e:86',{'source-tp': 'openflow:2:2', 'dest-tp': 'host:5a:3c:93:76:4e:86', 'weight': 20, 'color': 'lime'})


###### THIS IS SUPER GRAPH FOR TEST FIND START STOP

def gentestmatch():
    ## outlist is node and outport
    outlist = [(1, 2), (2, 4),(4,6),(6,5)]

    import random
    random.shuffle(outlist)

    testmatch=[]
    for out in outlist:
        name = 'openflow:' + str(out[0])
        model = {'node': name, 'flowentry': {'instructions': {'instruction': [{'order': 0, 'apply-actions': {
            'action': [{'output-action': {'output-node-connector': str(out[1])}, 'order': 0}]}}]}, 'table_id': 0,
                                             'id': '0',
                                             'match': {'ipv4-destination': '10.0.0.4/32', 'ipv4-source': '10.0.0.1/32',
                                                       'ethernet-match': {'ethernet-type': {'type': 2048}}},
                                             'flow-name': 'h1 ping h4'}}
        testmatch.append(model)
    return testmatch


def getsupergraph():
    Graph2 = nx.DiGraph()
    edgelist=[(1,2),(1,3),(2,1),(2,3),(2,4),(2,5),(3,1),(3,2),(3,4),(4,2),(4,3),(4,5),(4,6),(5,2)
              ,(5,4),(5,6),(6,4),(6,5)]

    for i in range(0, 5):
        name='openflow:'+str(i)
        Graph2.add_node(name,
                       {'controlip': '192.168.1.10', 'interfaceip': '10.0.0.10', 'username': 'test', 'password': 'test',
                        'model': 'Comware'})
    for couple in edgelist:
        namesrc = 'openflow:' + str(couple[0])
        namedes = 'openflow:' + str(couple[1])
        Graph2.add_edge(namesrc, namedes,
                       {'source-tp': namesrc+':'+str(couple[1]), 'dest-tp': namedes+':'+str(couple[0]), 'weight': 1, 'color': 'lime'})

    return Graph2
#####
def gettestgraph():
    return Graph

def findstartstop(Graph,MatchFlow):
    start=''
    stop=''
    edgelist=Graph.edges()
    #print(edgelist)
    #print(len(testmatchflow))
    for flownode in MatchFlow:
        node =flownode['node']
        start=node
        score=1
        flowaction=flownode['flowentry']["instructions"]["instruction"][0]["apply-actions"]["action"][0]
        #print (flowaction)
        if 'output-action' in flowaction:
            outport =flowaction['output-action']["output-node-connector"]
            if not outport.isdigit() :
                continue
            sourcetp=node+':'+outport
            # print(sourcetp)
            for i in range(0,len(MatchFlow)):
                 #print("Round",i)
                 for edge in edgelist:
                     #print(type(edge))

                     edgeattri=Graph.get_edge_data(edge[0],edge[1])
                     ##
                     if 'openflow' not in(edgeattri)['dest-tp']:
                         continue
                     ##
                     if sourcetp == edgeattri['source-tp']:
                         #print("match")
                         newnodeid=edgeattri['dest-tp'][:-2]
                         #print('newnode '+newnodeid)
                         stop=newnodeid
                         for newnode in MatchFlow:
                             if(newnode['node']==newnodeid):
                                 sourcetp=newnodeid+flownode['flowentry']["instructions"]["instruction"][0]["apply-actions"]["action"][0]['output-action']["output-node-connector"]
                                 score+=1
                                 break
        if(score==len(MatchFlow)):
            break


    print("start : "+start)
    print("stop : " + stop)



    return (start,stop)
def findnextnode(Graph,MatchFlow,used,newnode):

    edgelist = Graph.edges()
    flownode=newnode
    node = flownode['node']
    # print(type(MatchFlow))
    # print(type(used))
    # print(used)
    used.append(flownode)
    newlist = sorted(used, key=itemgetter('node'))
    matchsort=sorted(MatchFlow, key=itemgetter('node'))
    res=0
    if(newlist == matchsort):
        ###return flage of end point with name of end point
        return [True,node] ###Something this is stop
    else:
        flowaction = flownode['flowentry']["instructions"]["instruction"][0]["apply-actions"]["action"][0]
        # print (flowaction)
        if 'output-action' in flowaction:
            outport = flowaction['output-action']["output-node-connector"]

            if not outport.isdigit():
                ##RETURN DEADEND
                return  [False,node]
            sourcetp = node + ':' + outport
            # print(sourcetp)

            for edge in edgelist:
                ###Find Next node
                # print(type(edge))

                edgeattri = Graph.get_edge_data(edge[0], edge[1])
                ##
                if 'openflow' not in (edgeattri)['dest-tp']:
                    continue
                ##

                if sourcetp == edgeattri['source-tp']:
                    # print("match")
                    newnodeid = edgeattri['dest-tp'][:-2]
                    # print('newnode '+newnodeid)
                    stop = newnodeid
                    connectededge = edge

            for newnode in MatchFlow:
                if (newnode['node'] == newnodeid):
                    ######
                    # to call new node
                    res=findnextnode(Graph,MatchFlow,used,newnode)
                    ####

                    break
            if res != 0:
                return res
            else:

                print('deadend')
                return [False, node]



def newfindstartstop(Graph,MatchFlow):
    start = ''
    stop = ''

    edgelist = Graph.edges()
    # print(edgelist)
    # print(len(testmatchflow))
    for flownode in MatchFlow:
        used=[]
        node =flownode['node']
        canfindstopflag=False
        start=node
        score=1
        used.append(flownode)
        res=0
        flowaction=flownode['flowentry']["instructions"]["instruction"][0]["apply-actions"]["action"][0]
        #print (flowaction)
        if 'output-action' in flowaction:
            outport = flowaction['output-action']["output-node-connector"]

            if not outport.isdigit() :
                continue
            sourcetp = node + ':' + outport
            # print(sourcetp)
            global newnodeid
            newnodeid='0'
            for edge in edgelist:
                ###Find Next node
                # print(type(edge))

                edgeattri = Graph.get_edge_data(edge[0], edge[1])
                ##
                if 'openflow' not in (edgeattri)['dest-tp']:
                    continue
                ##

                if sourcetp == edgeattri['source-tp']:
                    # print("match")
                    newnodeid = edgeattri['dest-tp'][:-2]
                    # print('newnode '+newnodeid)
                    stop = newnodeid
                    connectededge=edge
            # res
            if newnodeid=='0':
                continue

            for newnode in MatchFlow:
                
                if (newnode['node'] == newnodeid):
                    ######
                    # to call new node
                    res = findnextnode(Graph, MatchFlow, used, newnode)
                    ####

                    break
        if res!= 0:
            thisnodecanstop=res[0]
            endpoint=res[1]
            if thisnodecanstop:
                return (start,endpoint)
        else:
            print('not from this node')





def dijkstraalgoritm(Graph,StartStop):
    Start=StartStop[0]
    Stop=StartStop[1]

    #print("find new path for "+Start+" to "+Stop)
    try:
        direction = nx.dijkstra_path(Graph, Start, Stop)
    except nx.exception.NetworkXNoPath as e:
        print(e)
        print('There is no direction')
        direction=[]
    print(direction)
    return direction




def outputportforeachnode(Graph,Direction):
    edgelist = Graph.edges()
    #print(edgelist)
    #print(len(edgelist))
    #print("now outport",len(Direction))
    if Direction ==[]: return
    Newoutport=[]
    for i in range(0,len(Direction)-1):
         # print("round",i)
         p=0
         for edge in edgelist :
             # print(p)
             p+=1
             a=edge[0]==Direction[i]
             # print(Direction[i]+"-->"+Direction[i+1])
             # print("edge "+edge[0]+"-->"+edge[1])
             b=edge[1]==Direction[i+1]
             #print(a)
             #print(b)
             if  a&  b:
                 # print('hi')
                 edgeattri = Graph.get_edge_data(edge[0], edge[1])
                 outport = edgeattri['source-tp'][-1:]
                 Newoutport.append({'node':Direction[i],'port':outport})
         #print('new ROund')
         edgelist = Graph.edges()
    print(Newoutport)
    return Newoutport



