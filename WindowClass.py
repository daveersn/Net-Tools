from Tkinter import *
from NetworkClass import *
import socket

net = Net()
modes = [("Single scan", 1), ("Range scan", 2), ("Netmap", 3)]

class Window:
    def __init__(self, root):
        self.root = root
        self.ip = 0
        self.num_ip = 0
        self.port = 0
        self.range = 0
        self.operating_mode = [0, 0]  # 0: Single port scan; 1: Range port scan; 2: Network mapper.
        self.v = IntVar()
        self.v.set(0)
        # Window frame
        # Widgets declaration
        self.frame_top = Frame(self.root)
        self.frame_right = Frame(self.root)
        self.frame_bottom = Frame(self.root)
        self.ip_entry = Entry(self.frame_top, width=13)
        self.scan_bt = Button(self.frame_top, text="Scan", command=self.start_scan)
        self.ip_label = Label(self.frame_top, text="IP Address")
        self.port_entry = Entry(self.frame_top, width=5)
        self.port_label = Label(self.frame_top, text="Port")
        self.range_entry = Entry(self.frame_top, width=5)
        self.range_label = Label(self.frame_top, text="Range")
        self.main_text = Text(self.frame_bottom, height=2, width=30)
        # Widgets grid
        self.frame_top.pack(side=LEFT)
        self.frame_right.pack(side=RIGHT)
        self.frame_bottom.pack(side=LEFT, anchor=W)
        for text, val in modes:
            Radiobutton(self.frame_right, text=text, padx=20, variable=self.v, command=self.get, value=val).pack(side=TOP, anchor=W)
        self.main_text.grid(row=10, column=0)

        self.ss_widgets = [
        self.ip_entry,      # 0
        self.scan_bt,       # 1
        self.ip_label,      # 2
        self.port_entry,    # 3
        self.port_label     # 4
        ]

        self.rs_widgets = [
        self.range_entry,   # 0
        self.range_label    # 1
        ]

    def ss_widgets_grid(self):
        self.ss_widgets[0].grid(row=1, column=0, sticky=W)
        self.ss_widgets[1].grid(row=1, column=3)
        self.ss_widgets[2].grid(row=0, column=0)
        self.ss_widgets[3].grid(row=1, column=1)
        self.ss_widgets[4].grid(row=0, column=1)
        self.rs_widgets_forget()

    def rs_widgets_forget(self):
        for i in self.rs_widgets:
            i.grid_forget()

    def rs_widgets_grid(self):
        self.rs_widgets[0].grid(row=1, column=2)
        self.rs_widgets[1].grid(row=0, column=2)

    def start_scan(self):
        self.ip = self.ip_entry.get()
        self.num_ip = socket.gethostbyname(self.ip)
        self.ip_label.configure(text="IP Address ({})".format(self.ip))
        print "[DEBUG] - Getting ip({}) from entry.".format(self.num_ip)

        if self.operating_mode[0] == 0:     # Single scan
            self.port = self.port_entry.get()
            print "[DEBUG] - Starting single port scan"
            if net.scan(self.ip, self.port) == 0:
                print "[DEBUG] - [V] Port {} on {} is opened".format(self.port, self.ip)
            else:
                print "[DEBUG] - [X] Port {} on {} is closed".format(self.port, self.ip)

        elif self.operating_mode[0] == 1:       # Range scan
            self.port = self.port_entry.get()
            self.range = self.range_entry.get()
            print "[DEBUG] - Starting range of ports scan"
            for self.port in range(int(self.port), int(self.range)+1):
                if net.scan(self.ip, self.port) == 0:
                    print "[DEBUG] - [V] Port {} on {} is opened".format(self.port, self.ip)
                else:
                    print "[DEBUG] - [X] Port {} on {} is closed".format(self.port, self.ip)

    def om_update(self, new_value):
        self.operating_mode[1] = self.operating_mode[0]
        self.operating_mode[0] = new_value

    def get(self):
        if self.v.get() == 1:
            self.om_update(0)
            self.ss_widgets_grid()
            if self.operating_mode[1] == 1:
                self.rs_widgets_forget()
        elif self.v.get() == 2:
            self.om_update(1)
            self.ss_widgets_grid()
            self.rs_widgets_grid()
        elif self.v.get() == 3:
            self.om_update(2)