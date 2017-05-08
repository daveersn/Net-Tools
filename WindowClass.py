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
        self.operating_mode = 1  # 0: Single port scan; 1: Range port scan; 2: Network mapper.
        self.v = IntVar()
        self.v.set(1)
        # Window frame
        self.frame_top = Frame(self.root)
        self.frame_top.pack(side=TOP)
        self.frame_right = Frame(self.root)
        self.frame_right.pack(side=RIGHT)
        self.ip_entry = Entry(self.frame_top, width=13)
        self.ip_entry.grid(row=1, column=0)
        self.scan_bt = Button(self.frame_top, text="Scan", command=self.start_scan)
        self.scan_bt.grid(row=1, column=3)
        self.ip_label = Label(self.frame_top, text="IP Address")
        self.ip_label.grid(row=0, column=0)
        if self.operating_mode == 0:
            self.port_entry = Entry(self.frame_top)
            self.port_entry.grid(row=1, column=1)
            self.port_label = Label(self.frame_top, text="Port")
            self.port_label.grid(row=0, column=1)
        elif self.operating_mode == 1:
            self.port_entry = Entry(self.frame_top, width=5)
            self.port_entry.grid(row=1, column=1)
            self.port_label = Label(self.frame_top, text="Port")
            self.port_label.grid(row=0, column=1)
            self.range_entry = Entry(self.frame_top, width=5)
            self.range_entry.grid(row=1, column=2)
            self.range_label = Label(self.frame_top, text="Range")
            self.range_label.grid(row=0, column=2)
        for self.txt in modes:
            Radiobutton(self.frame_right, text=self.txt, padx=20, variable=self.v, command=self.get).pack(anchor=W)

    def start_scan(self):
        self.ip = self.ip_entry.get()
        self.num_ip = socket.gethostbyname(self.ip)
        self.ip_label.configure(text="IP Address ({})".format(self.ip))
        print "[DEBUG] - Getting ip({}) from entry.".format(self.num_ip)
        if self.operating_mode == 0:
            self.port = self.port_entry.get()
            print "[DEBUG] - Starting single port scan"
            if net.scan(self.ip, self.port) == 0:
                print "[DEBUG] - [V] Port {} on {} is opened".format(self.port, self.ip)
            else:
                print "[DEBUG] - [X] Port {} on {} is closed".format(self.port, self.ip)

        elif self.operating_mode == 1:
            self.port = self.port_entry.get()
            self.range = self.range_entry.get()
            print self.port
            print self.range
            print "[DEBUG] - Starting range of ports scan"
            for self.port in range(int(self.port), int(self.range+1)):
                if net.scan(self.ip, self.port) == 0:
                    print "[DEBUG] - [V] Port {} on {} is opened".format(self.port, self.ip)
                else:
                    print "[DEBUG] - [X] Port {} on {} is closed".format(self.port, self.ip)

    def get(self):
        print self.v.get()