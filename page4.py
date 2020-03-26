from tkinter import *
from create.createVBridge import *
from create.createVTN import *
from create.createController import *
from create.createInterface import *
from mapVTN.mapPort import *
from get.getvBridge import *
from get.getVTN import *
import httplib2


def vtn(page4,c_ip):

    hforvtn = httplib2.Http(".cache")  # =============Header login==============#
    hforvtn.add_credentials('admin', 'adminpass')  # =============Header login==============#

    #========================================= Frame 1 ==================================================#

    f1 = Frame(page4, width=400, height=250)
    f1.pack_propagate(False)
    f1.grid(row=0, column=1)

    nb = ttk.Notebook(f1)
    controller_tab = Frame(nb, width=200, height=200)
    vtn_tab = Frame(nb, width=200, height=200)
    vbridge_tab = Frame(nb, width=200, height=200)
    interface_tab = Frame(nb, width=200, height=200)
    portmap_tab = Frame(nb, width=200, height=200)

    c_name = 'controller1'          # Fix Controller Name
    vtn_name = StringVar()
    vb_name = StringVar()
    vb_vtn = StringVar()
    vb_con = 'controller1'          # Fix Controller Name
    if_name = StringVar()
    if_vb = StringVar()
    if_vtn = StringVar()
    port_vtn = StringVar()
    port_vb = StringVar()
    port_if = StringVar()
    port_sw = StringVar()
    port_port = StringVar()

    #================= Event Create =======================#

    def createCon():
        print(createController(hforvtn, c_ip, c_name))

    def createVt():
        print(createVTN(hforvtn, c_ip, vtn_name.get()))

    def createVBr():
        print(createVBridge(hforvtn, c_ip, vb_con, vb_vtn.get(), vb_name.get()))

    def createInt():
        print(createInterface(hforvtn, c_ip, if_vtn.get(), if_vb.get(), if_name.get()))

    def portMap():
        print(mapPort(hforvtn, c_ip, port_vtn.get(), port_vb.get(), port_if.get(), port_sw.get(), port_port.get()))

    # ================= Create Controller Tab ==================#
    # (Auto Create When start program)

    createCon()

    #############################################################
    controller_id_label = Label(controller_tab, text="Controller Name : ").grid(row=0, column=0,sticky=W,padx = 30, pady=(30,15))
    controller_id_entry = Entry(controller_tab, textvariable=c_name).grid(row=0, column=1, pady=(30,15))
    controller_button = Button(controller_tab, text=" Create Controller ", command=createCon).grid(row=1, column=1)

    # ================= Create VTN Tab =========================#

    vtn_id_label = Label(vtn_tab, text="VTN Name : ").grid(row=0, column=0, sticky=W,padx = 30, pady=(30,15))
    vtn_id_entry = Entry(vtn_tab, textvariable=vtn_name).grid(row=0, column=1, pady=(30,15))
    vtn_button = Button(vtn_tab, text=" Create VTN ", command=createVt).grid(row=1, column=1)

    # ================= Create VBridge Tab ====================#

    # vbridge_con_label = Label(vbridge_tab, text="Controller Name : ").grid(row=0, column=0, sticky=W, padx=30, pady=(30,0))
    # vbridge_con_entry = Entry(vbridge_tab, textvariable=vb_con).grid(row=0, column=1,pady=(30,0))
    vbridge_vtn_label = Label(vbridge_tab, text="VTN Name : ").grid(row=1, column=0, sticky=W,padx = 30,pady=(30,0))
    vbridge_vtn_entry = Entry(vbridge_tab, textvariable=vb_vtn).grid(row=1, column=1,pady=(30,0))
    vbridge_id_label = Label(vbridge_tab, text="vBridge :").grid(row=2, column=0, sticky=W, padx=30,pady=10)
    vbridge_id_entry = Entry(vbridge_tab, textvariable=vb_name).grid(row=2, column=1,pady=10)
    vbridge_button = Button(vbridge_tab, text=" Create vBridge ", command=createVBr).grid(row=3, column=1)

    # ================= Create Interface Tab ====================#

    interface_vtn_label = Label(interface_tab, text="VTN Name : ").grid(row=0, column=0, sticky=W, padx=30, pady=(30, 0))
    interface_vtn_entry = Entry(interface_tab, textvariable=if_vtn).grid(row=0, column=1, pady=(30, 0))
    interface_vb_label = Label(interface_tab, text="vBridge :").grid(row=1, column=0, sticky=W, padx=30, pady=10)
    interface_vb_entry = Entry(interface_tab, textvariable=if_vb).grid(row=1, column=1, pady=10)
    interface_name_label = Label(interface_tab, text="Interface :").grid(row=2, column=0, sticky=W, padx=30, pady=(0,10))
    interface_name_entry = Entry(interface_tab, textvariable=if_name).grid(row=2, column=1, pady=(0,10))
    interface_button = Button(interface_tab, text=" Create Interface ", command=createInt).grid(row=3, column=1)

    # ================= Map Port Tab ====================#

    port_vtn_label = Label(portmap_tab, text="VTN Name : ").grid(row=0, column=0, sticky=W, padx=30, pady=(30, 0))
    port_vtn_entry = Entry(portmap_tab, textvariable=port_vtn).grid(row=0, column=1, pady=(30, 0))
    port_vb_label = Label(portmap_tab, text="vBridge :").grid(row=1, column=0, sticky=W, padx=30, pady=10)
    port_vb_entry = Entry(portmap_tab, textvariable=port_vb).grid(row=1, column=1, pady=10)
    port_if_label = Label(portmap_tab, text="vBridge Port :").grid(row=2, column=0, sticky=W, padx=30, pady=(0,10))
    port_if_entry = Entry(portmap_tab, textvariable=port_if).grid(row=2, column=1, pady=(0,10))
    port_sw_label = Label(portmap_tab, text="Switch :").grid(row=3, column=0, sticky=W, padx=30, pady=(0,10))
    port_sw_entry = Entry(portmap_tab, textvariable=port_sw).grid(row=3, column=1, pady=(0,10))
    port_port_label = Label(portmap_tab, text="Switch Port :").grid(row=4, column=0, sticky=W, padx=30, pady=(0,10))
    port_port_entry = Entry(portmap_tab, textvariable=port_port).grid(row=4, column=1, pady=(0,10))
    port_button = Button(portmap_tab, text=" Map Port ", command=portMap).grid(row=5, column=1)

    # nb.add(controller_tab, text='Create Controller')
    nb.add(vtn_tab, text='Create VTN')
    nb.add(vbridge_tab, text='Create vBridge')
    nb.add(interface_tab, text='Create Interface')
    nb.add(portmap_tab, text='Port Map')
    nb.pack(expand=1, fill="both")

    #========================================= Frame 2 ==================================================#

    f2 = Frame(page4, width=400, height=250)
    f2.pack_propagate(False)
    f2.grid(row=0, column=0, padx=10)

    head_label2 = Label(f2, text="VTN Lists", font=("Helvetica", 15), fg='black')
    head_label2.pack(pady=10)

    sf2 = Frame(f2)
    sf2.pack()

    lb2 = Listbox(sf2, width=60)
    def listVtn():

        list_vtn = getVTN(hforvtn, c_ip)
        lb2.delete(0,'end')
        for i in range(len(list_vtn['vtns'])):
            lb2.insert(i,list_vtn['vtns'][i]['vtn_name'])
        lb2.config()
        lb2.pack()
        sf2.after(2000, listVtn)

    lb2.config()
    lb2.pack()
    sf2.after(0, listVtn)

    #============== Event OnDouble_item (ListBox) =============================#

    def OnDouble_item(event):
        list_vtn = getVTN(hforvtn, c_ip)
        detail = ""
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        print(list_vtn)
        vb_list = ""
        for i in range(len(list_vtn['vtns'])):
            if (value == list_vtn['vtns'][i]['vtn_name']):
                temp = getVBridge(hforvtn,c_ip,list_vtn['vtns'][i]['vtn_name'])
                for j in range(len(temp['vbridges'])):
                    vb_list += temp['vbridges'][j]['vbr_name']
                    if(len(temp['vbridges'])-1 > j):
                        vb_list += ", "
                detail += "VTN Name : " + list_vtn['vtns'][i]['vtn_name'] +"\nDescription : " + list_vtn['vtns'][i]['description'
                ] + "\nOperation Status : " + list_vtn['vtns'][i]['operstatus'] + "\nvBridges : " + vb_list

        txt3.config(state=NORMAL)
        txt3.delete('1.0', END)
        txt3.insert(INSERT, detail)
        txt3.config(state=DISABLED)

    lb2.bind("<Double-Button-1>", OnDouble_item)

    #========================================= Frame 3 ==================================================#

    f3 = Frame(page4, width=525, height=300)
    f3.pack_propagate(False)
    f3.grid(row=1, column=0,pady=10)
    head_label3 = Label(f3, text="VTN Details", font=("Helvetica", 15), fg='black')
    head_label3.pack(pady=10)
    sf3 = Frame(f3)

    sf3.pack()

    txt3 = Text(sf3, width=45, height=10)
    vbar = Scrollbar(sf3, orient=VERTICAL)
    vbar.pack(side=RIGHT, fill=Y)
    vbar.config(command=txt3.yview)
    txt3.config(yscrollcommand=vbar.set)

    txt3.pack()