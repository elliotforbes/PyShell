import socket

# Our sniffer class that will do all our packet sniffing
class sniffer():
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    
    def __init__(self):
        print "Sniffer Initialized"
        
    def run(self):
        print "hi"
        while(1):
            print(self.sock.recvfrom(65565))
            