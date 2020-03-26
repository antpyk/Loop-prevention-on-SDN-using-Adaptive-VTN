from tkinter import *
from get.getData import *

def showDetail(page2, controller_ip):
    gd = getData("admin", "admin", controller_ip)
    inventory = gd.getInventoryOperational()
    network_topology = gd.getNetworkTopology()


    def OnDouble_Device(event):

        switch_detail = ""
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        for i in range(len(inventory['nodes']['node'])):
            if (value == inventory['nodes']['node'][i]['id']):
                switch_id = inventory['nodes']['node'][i]['id']
                manufacturer = inventory['nodes']['node'][i]['flow-node-inventory:manufacturer']
                hardware = inventory['nodes']['node'][i]['flow-node-inventory:hardware']
                serial_no = inventory['nodes']['node'][i]['flow-node-inventory:serial-number']
                software = inventory['nodes']['node'][i]['flow-node-inventory:software']
                count_port = 0
                list_port = ""
                for j in range(len(inventory['nodes']['node'][i]['node-connector'])):
                    count_port += 1
                    list_port += "\t Port: " + str(
                        inventory['nodes']['node'][i]['node-connector'][j]['flow-node-inventory:port-number']) + "\n"

                amount_port = "Amount Port : " + str(count_port) + "\n" + list_port
                switch_detail = "Switch-ID : " + switch_id + "\n" + "Manufacturer : " + manufacturer + "\n" + "Hardware : " + hardware + "\n" + "Serial Number : " + serial_no + "\n" + "Software : " + software + "\n" + amount_port

        txt3.config(state=NORMAL)
        txt3.delete('1.0', END)
        txt3.insert(INSERT, switch_detail)
        txt3.config(state=DISABLED)

    def OnDouble_Link(event):

        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        src = value.split(" <-> ")[0]
        dest = value.split(" <-> ")[1]

        for i in range(len(network_topology['network-topology']['topology'][0]['link'])):
            if (src == network_topology['network-topology']['topology'][0]['link'][i]['source'][
                'source-node'] and dest ==
                    network_topology['network-topology']['topology'][0]['link'][i]['destination']['dest-node']):
                src_node_connector = network_topology['network-topology']['topology'][0]['link'][i]['source'][
                    'source-tp']
                dest_node_connector = network_topology['network-topology']['topology'][0]['link'][i]['destination'][
                    'dest-tp']
                for a in range(len(inventory['nodes']['node'])):
                    if (src == inventory['nodes']['node'][a]['id']):
                        for b in range(len(inventory['nodes']['node'][a]['node-connector'])):
                            if (src_node_connector == inventory['nodes']['node'][a]['node-connector'][b]['id']):
                                link_down = \
                                inventory['nodes']['node'][a]['node-connector'][b]['flow-node-inventory:state'][
                                    'link-down']
                    elif (dest == inventory['nodes']['node'][a]['id']):
                        for b in range(len(inventory['nodes']['node'][a]['node-connector'])):
                            if (dest_node_connector == inventory['nodes']['node'][a]['node-connector'][b]['id']):
                                link_down = \
                                inventory['nodes']['node'][a]['node-connector'][b]['flow-node-inventory:state'][
                                    'link-down']

        if (link_down):
            E2.config(state=NORMAL)
            E2.delete(0, END)
            E2.insert(INSERT, "Link down")
            E2.config(state="readonly")
        else:
            E2.config(state=NORMAL)
            E2.delete(0, END)
            E2.insert(INSERT, "Link up")
            E2.config(state="readonly")
        # E1.config(state=NORMAL)
        # E1.delete(0, END)
        # E1.insert(INSERT, src_node_connector + "/" + dest_node_connector)
        # E1.config(state="readonly")
# -------------------------------------------------------------------------------------------------------------------------
    f1 = Frame(page2, width=400, height=250)
    f1.pack_propagate(False)
    f1.grid(row=0, column=0, padx=10)
    head_label1 = Label(f1, text="Switch", font=("Helvetica", 15), fg='black')
    head_label1.pack(pady=10)
    sf1 = Frame(f1)
    sf1.pack()
    Lb1 = Listbox(sf1, width=60)
    if(len(inventory['nodes']) != 0 ) :
        for i in range(len(inventory['nodes']['node'])):
            Lb1.insert(i, inventory['nodes']['node'][i]['id'])
    Lb1.bind("<Double-Button-1>", OnDouble_Device)
    vbar = Scrollbar(sf1, orient=VERTICAL)
    vbar.pack(side=RIGHT, fill=Y)
    vbar.config(command=Lb1.yview)
    Lb1.config(yscrollcommand=vbar.set)
    Lb1.pack()
# ------------------------------------------------------------------------------------------------------------------------
    f2 = Frame(page2, width=525, height=300)
    f2.pack_propagate(False)
    f2.grid(row=1, column=0)
    head_label2 = Label(f2, text="List of Link", font=("Helvetica", 15), fg='black')
    head_label2.pack(pady=10)
    sf2 = Frame(f2)
    sf2.pack()
    Lb2 = Listbox(sf2, width=60)

    sf22 = Frame(f2)
    sf22.pack()

    if 'link' in network_topology['network-topology']['topology'][0]:
        L2 = Label(sf22, text="Link-Status  :", font=("Helvetica", 10))
        L2.grid(row=1, column=0, pady=5)
        E2 = Entry(sf22)
        E2.grid(row=1, column=1)


        for i in range(len(network_topology['network-topology']['topology'][0]['link'])):
            Lb2.insert(i,
                       network_topology['network-topology']['topology'][0]['link'][i]['source']['source-node'] + " <-> " +
                       network_topology['network-topology']['topology'][0]['link'][i]['destination']['dest-node'])
        Lb2.bind("<Double-Button-1>", OnDouble_Link)
        vbar = Scrollbar(sf2, orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=Lb2.yview)
        Lb2.config(yscrollcommand=vbar.set)
    Lb2.pack()
# ------------------------------------------------------------------------------------------------------------------------
    f3 = Frame(page2, width=400, height=250)
    f3.pack_propagate(False)
    f3.grid(row=0, column=1)
    head_label3 = Label(f3, text=" Switch Detail", font=("Helvetica", 15), fg='black')
    head_label3.pack(pady=10)
    sf3 = Frame(f3)

    sf3.pack()

    txt3 = Text(sf3, width=45, height=10)
    vbar = Scrollbar(sf3, orient=VERTICAL)
    vbar.pack(side=RIGHT, fill=Y)
    vbar.config(command=txt3.yview)
    txt3.config(yscrollcommand=vbar.set)

    txt3.pack()
