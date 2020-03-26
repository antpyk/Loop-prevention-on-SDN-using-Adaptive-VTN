from tkinter import ttk
from tkinter import *
from page1 import *
from page2 import *
from page3 import *
from page11 import *
from page4 import *

class sdnLoop:

    def __init__(self, master):

        c_ip = '10.0.2.2'  # =============Controller IP=============#

        self.master = master
        master.title("SDNCoop")
        master.geometry("1000x600")

        nb = ttk.Notebook(master)

        # --------------------------------------------------Page1-------------------------------------------------------

        page1 = ttk.Frame(master)
        topo(page1, c_ip)
        # root.after(0, topo(page1, c_ip))

        # --------------------------------------------------Page2-------------------------------------------------------

        page2 = ttk.Frame(nb)
        showDetail(page2,c_ip)

        # --------------------------------------------------Page3-------------------------------------------------------

        page3 = ttk.Frame(nb)
        showFlowtable(page3 ,c_ip)

        # --------------------------------------------------Page4-------------------------------------------------------

        page4 = ttk.Frame(nb)
        vtn(page4, c_ip)

        # --------------------------------------------------Page11-------------------------------------------------------

        # page11 = ttk.Frame(nb)
        # addFlowEntry(page11, c_ip)

        nb.add(page1, text='Topology')
        nb.add(page2, text='Switch')
        # nb.add(page11, text='Add Flow')
        nb.add(page3, text='Flow Table')
        nb.add(page4, text='VTN')
        nb.pack(expand=1, fill="both")

root = Tk()
my_gui = sdnLoop(root)
# root.after(5000,topo(page1, c_ip))
root.mainloop()