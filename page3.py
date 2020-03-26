from tkinter import *
from get.getData import *
import httplib2
from tkinter import messagebox
from tkinter import ttk

def showFlowtable(page3, controller_ip):
    gd = getData("admin", "admin", controller_ip)
    config = gd.getInventoryOperational()
    # print(config)
    nodeID = ""
    flowID = ""

    def findtable0(j):
        if (len(j['nodes']) != 0):
            for i in range(len(j['nodes']['node'][1]['flow-node-inventory:table'])) :
                if j['nodes']['node'][0]['flow-node-inventory:table'][i]['id'] == 0 : # flow table number
                    # print(i)
                    return i


    def inserttotable(j):
        if 'errors' not in j:
            table = findtable0(j)
            if (len(j['nodes']) != 0):
                for a in range(len(j['nodes']['node'])):
                    if 'id' in j['nodes']['node'][a]:
                        node_id = j['nodes']['node'][a]['id']
                    else:
                        node_id = "-"



                    if 'flow' in j['nodes']['node'][a]['flow-node-inventory:table'][table]:
                        for b in range(len(j['nodes']['node'][a]['flow-node-inventory:table'][table]['flow'])):
                            flow_id = j['nodes']['node'][a]['flow-node-inventory:table'][table]['flow'][b]['id']
                            ethernet_type = ""
                            in_port = ""
                            action = ""
                            if 'match' in j['nodes']['node'][a]['flow-node-inventory:table'][table]['flow'][b]:
                                if 'ethernet-match' in j['nodes']['node'][a]['flow-node-inventory:table'][table]['flow'][b]['match']:
                                        if 'ethernet-type' in j['nodes']['node'][a]['flow-node-inventory:table'][table]['flow'][b]['match']['ethernet-match']:
                                            ethernet_type = j['nodes']['node'][a]['flow-node-inventory:table'][table]['flow'][b]['match']['ethernet-match']['ethernet-type']['type']
                                        else:
                                            ethernet_type = "-"
                                else:
                                    ethernet_type = "-"
                                if 'in-port' in \
                                        j['nodes']['node'][a]['flow-node-inventory:table'][table]['flow'][b]['match']:
                                    in_port = \
                                        j['nodes']['node'][a]['flow-node-inventory:table'][table]['flow'][b]['match'][
                                            'in-port']
                                else:
                                    in_port = "-"
                                if 'instructions' in j['nodes']['node'][a]['flow-node-inventory:table'][table]['flow'][b]:
                                    for c in range(len(j['nodes']['node'][a]['flow-node-inventory:table'][table]['flow'][b][
                                                           'instructions']['instruction'][0]['apply-actions']['action'])):






                                        if 'instructions' in j['nodes']['node'][a]['flow-node-inventory:table'][table]['flow'][b]:
                                            action += j['nodes']['node'][a]['flow-node-inventory:table'][table]['flow'][b][
                                                            'instructions']['instruction'][0]['apply-actions']['action'][c][
                                                            'output-action']['output-node-connector'] + " "

                                        else:
                                            action = "-"

                                else:
                                    action = "-"
                            tv.insert('', 'end', text=node_id,values=(flow_id, ethernet_type, in_port, action))
    def Refresh():
        config = gd.getInventoryOperational()
        tv.delete(*tv.get_children())
        inserttotable(config)

    def selectItem(event):
        global nodeID
        global flowID
        info = tv.get_children()
        for i in info:
            info2 = tv.set(i)
        for item in tv.selection():
            nodeID = tv.item(item)['text']
        # print(nodeID)
        flowID = info2['Flow ID']

    def Delete():
        global nodeID
        global flowID

        url = 'http://' + gd.getcontrollerIPADDR() + ':8181/restconf/operational/opendaylight-inventory:nodes/node/' + nodeID + "/table/0/flow/" + flowID
        print(url)
        h = httplib2.Http(".cache")
        resp, content = h.request(url, method='DELETE', headers={'Content-Type': 'application/json'})
        Refresh()
        msg = messagebox.showinfo("Spinner", "Delete Flow success")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    pf4 = Frame(page3)
    pf4.pack_propagate(False)
    pf4.pack(pady=50)

    tv = ttk.Treeview(pf4, height=20)
    yScroll = Scrollbar(pf4)
    yScroll.pack(side=RIGHT, fill=Y)
    yScroll.configure(command=tv.yview)
    tv.configure(yscrollcommand=yScroll.set)


    tv['columns'] = ('Flow ID', 'Ethernet Type', 'In-port', 'Action')
    tv.heading("#0", text='Node ID')
    tv.column("#0", anchor='center', width=100)
    tv.heading('Flow ID', text='Flow ID')
    tv.column('Flow ID', anchor='center', width=200)
    tv.column('Ethernet Type', anchor='center', width=120)
    tv.heading('Ethernet Type', text='Ethernet Type')
    tv.heading('In-port', text='In-port')
    tv.column('In-port', anchor='center', width=80)
    tv.heading('Action', text='Action')
    tv.column('Action', anchor='center', width=180)
    tv.bind('<ButtonRelease-1>', selectItem)

    tv.grid(sticky=(N, S, W, E))
    tv.grid_rowconfigure(0, weight=1)
    tv.grid_columnconfigure(0, weight=1)


    inserttotable(config)
    refresh_button = Button(page3, text="Refresh", command=Refresh)
    # refresh_button.place(x=670, y=510)
    refresh_button.place(x=750, y=510)

    # delete_button = Button(page3, text="Delete Flow", command=Delete)
    # delete_button.place(x=750, y=510)