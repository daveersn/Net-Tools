from WindowClass import *
import socket

class net:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def single_scan(self, ip, port):
        self.ip = ip
        self.port = port
        self.conn = self.sock.connect_ex((self.ip, self.port))
        if self.conn == 0:
            return 0
        else:
            return 1