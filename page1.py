from tkinter import *
from create.createTopology import *
from create.putFlow import *

isFirstRound = True
compare = False

def topo(page1,c_ip):
    F1 = Frame(page1, width=650, height=500, padx=120)
    F1.grid(row=0, column=0)
    topo_label = Label(F1, text="Topology", font=("Helvetica", 20), fg='blue')
    topo_label.grid(pady=10)

    f1 = Frame(F1, width=600, height=530)
    f1.grid(padx=10, pady=10)
    photo = ""
    canvas = Canvas(f1, width=600, height=500)


    def RecoverTopo():
        global old_topo
        global isFirstRound
        global compare
        if not (isFirstRound):
            topo = getTopo(c_ip)
            if(old_topo['network-topology']['topology'][0]['node'] != topo['network-topology']['topology'][0]['node']
                and old_topo['network-topology']['topology'][0]['link'] != topo['network-topology']['topology'][0]['link']):
                compare = True
        if (isFirstRound or compare):
            clearFlow(c_ip)
            g = createTopo(c_ip)

            # page1.after(5000,createTop())
            # nx.dijkstra_path(g, 'openflow:1', 'openflow:4')
            def create_canvas():
                global photo
                Image = open("C:\\Users\\COPS\\PycharmProjects\\SDN-v2\\create\\vtntest.png")
                photo = PhotoImage(file=Image.name)
                canvas.create_image(0, 0, image=photo, anchor='nw')
                Image.close()

            canvas.after(0, create_canvas())
            canvas.config(width=600, height=400)
            canvas.config()
            canvas.pack(side=LEFT, expand=True, fill=BOTH)
#==============================Shortest Path With Dijkstra =============================================#
            list = []
            topo = getTopo(c_ip)
            old_topo = topo
            allnode = topo['network-topology']['topology'][0]['node']
            alllink = topo['network-topology']['topology'][0]['link']
            # ========================= Find All Link With Dijkstra ==========================#
            for i in range(len(allnode)):
                for j in range(i + 1, len(allnode)):
                    if (allnode[i]['node-id'][0:4] == 'host' and allnode[j]['node-id'][0:4] == 'host'):
                        list.append(nx.dijkstra_path(g, allnode[i]['node-id'], allnode[j]['node-id']))
                        # print(nx.dijkstra_path(g, allnode[i]['node-id'], allnode[j]['node-id']))

            for i in range(len(list)):
                print(list[i])
                source_tp = ''

                for j in range(len(list[i]) - 1):
                    # print(j)
                    # print(list[i][j])

                    print("Add flow to Switch " + list[i][j] + " and Switch " + list[i][j + 1])

                    for k in range(len(alllink)):
                        if ((list[i][j] in alllink[k]['source']['source-node']) and
                                (list[i][j + 1] in alllink[k]['destination']['dest-node'])):
                            # print(alllink[k])
                            break

                    if ('openflow' in list[i][j]):
                        put2FlowPerNode(c_ip, alllink[k]['source']['source-node'], source_tp,
                                        alllink[k]['source']['source-tp'])

                    source_tp = alllink[k]['destination']['dest-tp']
#==============================Shortest Path With Dijkstra =============================================#
        print('1')
        isFirstRound = False
        compare = False
        f1.after(5000,RecoverTopo)


    f1.after(0,RecoverTopo)

