from tkinter import *
from get.getData import *
from tkinter import messagebox
import httplib2, json


x = 13
table_id = '0'
instruction_order = '0'
action_order = '0'
node_id_value = ""
action_value = ""
Action = {}


def addFlowEntry(page11, controller_ip):
    gd = getData("admin", "admin", controller_ip)
    inventory = gd.getInventoryOperational()

    top = Frame(page11)
    top.pack(padx=10, pady=50)

    def OnDouble_nodeID(event):
        widget = event.widget
        selection = widget.curselection()
        global node_id_value
        node_id_value = widget.get(selection[0])

    def OnDouble_action(event):
        widget = event.widget
        selection = widget.curselection()
        global action_value
        action_value = widget.get(selection[0])
        if (action_value == "output-action-case"):
            output_node_connector_label = Label(top, text="Output Node Connector : ").grid(row=14, column=0, sticky=W,
                                                                                           pady=5, padx=5)
            output_node_connector_entry.config(state=NORMAL)
            output_node_connector_entry.grid(row=14, column=1, pady=5)
        elif (action_value == "drop-action-case"):
            output_node_connector_entry.config(state=DISABLED)

    node_id_label = Label(top, text="Node ID : ").grid(row=0, column=0, sticky=W, pady=5)
    flow_id_label = Label(top, text="Flow ID : ").grid(row=1, column=0, sticky=W, pady=5)
    flow_name_label = Label(top, text="Flow Name : ").grid(row=2, column=0, sticky=W, pady=5)
    priority_label = Label(top, text="Priority : ").grid(row=3, column=0, sticky=W, pady=5)
    match_label = Label(top, text="Match").grid(row=4, column=0, sticky=W, pady=5)
    ethernet_match_label = Label(top, text="Ethernet Match").grid(row=5, column=0, sticky=W, padx=10, pady=5)
    ethernet_src_label = Label(top, text="Ethernet Source : ").grid(row=6, column=0, sticky=W, padx=20, pady=5)
    ethernet_dest_label = Label(top, text="Ethernet Destination : ").grid(row=7, column=0, sticky=W, padx=20, pady=5)
    ethernet_type_label = Label(top, text="Ethernet Type :").grid(row=8, column=0, sticky=W, padx=20, pady=5)
    ipv4_src_label = Label(top, text="IPv4 Source :").grid(row=9, column=0, sticky=W, padx=10, pady=5)
    ipv4_dest_label = Label(top, text="IPv4 Destination :").grid(row=10, column=0, sticky=W, padx=10, pady=5)
    instructions_label = Label(top, text="Instructions").grid(row=11, column=0, sticky=W, pady=5)
    instruction_label = Label(top, text="Instruction :").grid(row=12, column=0, sticky=W, padx=10, pady=5)
    action_label = Label(top, text="Action :").grid(row=13, column=0, sticky=W, padx=20, pady=5)

    node_id_lb = Listbox(top, height=2)
    for i in range(len(inventory['nodes']['node'])):
        node_id_lb.insert(i, inventory['nodes']['node'][i]['id'])
    node_id_lb.bind("<Double-Button-1>", OnDouble_nodeID)
    node_id_lb.grid(row=0, column=1, pady=5)
    #
    # top.pack_propagate(False)
    # top.grid(row=0, column=0, padx=10)
    # sf1 = Frame(top)
    # sf1.pack()
    #
    # node_id_lb = Listbox(sf1, height=2)
    # # node_id_lb.grid(row=0, column=1, pady=5, sticky=W)
    # for i in range(len(inventory['nodes']['node'])):
    #     node_id_lb.insert(i, inventory['nodes']['node'][i]['id'])
    # node_id_lb.bind("<Double-Button-1>", OnDouble_nodeID)
    # vbar = Scrollbar(sf1, orient=VERTICAL)
    # vbar.pack(side=RIGHT, fill=Y)
    # vbar.config(command=node_id_lb.yview)
    # node_id_lb.config(yscrollcommand=vbar.set)
    # node_id_lb.pack()

    flow_id_entry = Entry(top)
    flow_id_entry.grid(row=1, column=1)
    flow_name_entry = Entry(top)
    flow_name_entry.grid(row=2, column=1)
    ethernet_src_entry = Entry(top)
    priority_entry = Entry(top)
    priority_entry.grid(row=3, column=1)
    priority_entry.insert(INSERT, "0")
    ethernet_src_entry.grid(row=6, column=1, padx=5)
    ethernet_dest_entry = Entry(top)
    ethernet_dest_entry.grid(row=7, column=1, padx=5)
    ethernet_type_entry = Entry(top)
    ethernet_type_entry.grid(row=8, column=1)
    ipv4_src_entry = Entry(top)
    ipv4_src_entry.grid(row=9, column=1)
    ipv4_dest_entry = Entry(top)
    ipv4_dest_entry.grid(row=10, column=1)
    instruction_entry = Entry(top)
    instruction_entry.grid(row=12, column=1)
    instruction_entry.insert(INSERT, "apply-actions-case")
    instruction_entry.config(state="readonly")
    action_lb = Listbox(top, height=2)
    action_lb.insert(1, "output-action-case")
    action_lb.insert(2, "drop-action-case")
    action_lb.bind("<Double-Button-1>", OnDouble_action)
    action_lb.grid(row=13, column=1, pady=5)
    output_node_connector_entry = Entry(top)

    def putFlow():
        url = 'http://' + gd.getcontrollerIPADDR() + ':8181/restconf/config/opendaylight-inventory:nodes/node/' + node_id_value + '/table/' + table_id + '/flow/' + flow_id_entry.get()
        FlowEntry = {}
        FlowEntry.update({"id": flow_id_entry.get()})
        FlowEntry.update({"flow-name": flow_name_entry.get()})
        Instructions = {}
        Instruction = {}
        Actions = {}
        global Action
        Action = {}
        Action.update({"order": action_order})  # แก้ไข
        if (action_value == "drop-action-case"):
            Action.update({"drop-action": {}})  # แก้ไข
        elif (action_value == "output-action-case"):
            Action.update({"output-action": {'output-node-connector': output_node_connector_entry.get()}})  # แก้ไข
        Actions.update({"action": [Action]})
        Instruction.update({"order": instruction_order})
        Instruction.update({"apply-actions": Actions})  # แก้ไข
        Instructions.update({"instruction": [Instruction]})
        FlowEntry.update({"instructions": Instructions})
        FlowEntry.update({"priority": priority_entry.get()})
        FlowEntry.update({"table_id": table_id})
        Match = {}
        Ethernet_Match = {}
        if (ethernet_type_entry.get() != ""):
            Ethernet_Match.update({'ethernet-type': {'type': ethernet_type_entry.get()}})
        if (ethernet_src_entry.get() != ""):
            Ethernet_Match.update({'ethernet-source': {'address': ethernet_src_entry.get()}})
        if (ethernet_dest_entry.get() != ""):
            Ethernet_Match.update({'ethernet-destination': {'address': ethernet_dest_entry.get()}})
        Match.update({'ethernet-match': Ethernet_Match})
        if (ipv4_src_entry.get() != ""):
            Match.update({"ipv4-source": ipv4_src_entry.get()})
        if (ipv4_dest_entry.get() != ""):
            Match.update({"ipv4-destination": ipv4_dest_entry.get()})
        FlowEntry.update({"match": Match})
        completeFlowEntry = {"flow-node-inventory:flow": [FlowEntry]}
        completeFlowEntry = json.dumps(completeFlowEntry)
        print(url)
        print(completeFlowEntry)
        resp, content = h.request(url, method='PUT', headers={'Content-Type': 'application/json'},
                                  body=completeFlowEntry)
        messagebox.showinfo("Spinner", "Put-Flow success")

    put_button = Button(top, text="Put Flow", command=putFlow)
    put_button.grid(row=14, column=2, sticky=E, pady=10)