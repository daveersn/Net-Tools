from Tkinter import *
from NetworkClass import *
import socket
Net = net()
class window:
    def __init__(self, root):
        self.root = root
        self.ip = 0
        self.num_ip = 0
        self.port = 0
        self.operating_mode = 0 # 0: Single port scan; 1: Range port scan; 2: Network mapper.
        # Window frame
        self.frame_top = Frame(self.root)
        self.frame_top.pack(side=TOP)
        self.ip_entry = Entry(self.frame_top)
        self.ip_entry.grid(row=1,column=0)
        self.scan_bt = Button(self.frame_top, text="Scan", command=self.start_scan)
        self.scan_bt.grid(row=1,column=2)
        self.ip_label = Label(self.frame_top, text="IP Address")
        self.ip_label.grid(row=0,column=0)
        if self.operating_mode == 0:
            self.port_entry = Entry(self.frame_top)
            self.port_entry.grid(row=1,column=1)
            self.port_label = Label(self.frame_top, text="Port")
            self.port_label.grid(row=0,column=1)

    def start_scan(self):
        self.ip = self.ip_entry.get()
        self.num_ip = socket.gethostbyname(self.ip)
        self.ip_label.configure(text="IP Address ({})".format(self.ip))
        print "[DEBUG] - Getting ip({}) from entry.".format(self.num_ip)
        if self.operating_mode == 0:
            self.port = self.port_entry.get()
            if self.port == "":
                self.port = None
                print "[DEBUG] - Port = None. Please enter a valid port."
            print "[DEBUG] - Operating mode = 0"
            print "[DEBUG] - Port: {}".format(self.port)
            print "[DEBUG] - Ip: {}".format(self.ip)
            print "[DEBUG] - Starting single port scan"
            if Net.single_scan(self.ip, self.port) == 0:
                print "[DEBUG] - [V] Port {} on {} is opened".format(self.port, self.ip)
            else:
                print "[DEBUG] - [X] Port {} on {} is closed".format(self.port,self.ip)