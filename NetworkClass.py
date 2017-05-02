from WindowClass import *
import socket

class net:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.result = 0

    def single_scan(self, ip, port):
        self.ip = ip
        self.port = port
        self.conn = self.sock.connect_ex((self.ip, int(self.port)))
        if self.conn == 0:
            self.result = 1
        else:
            self.result = 2