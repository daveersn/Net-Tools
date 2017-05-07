import socket

class classic_conn:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.address = (self.ip, int(self.port))
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.settimeout(2)
        if self.conn.connect_ex(self.address) == 0:
            print "Can connect to {}".format(self.address)
        else:
            print "Can't connect to {}".format(self.address)
        self.conn.close()


for i in range(1, 5):
    conn = classic_conn(raw_input("Ip: "), input("Port: "))
