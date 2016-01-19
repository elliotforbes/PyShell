from modules import sniffer

# Our main controller, the entry point for our program
class Controller():

    sniff = None
    
    # Our constructor
    def __init__(self):
        print "PyShel v0.0.1 -----"
        print "-------------------"
        self.sniff = sniffer.sniffer()
        
    # our main input loop
    def run(self):
        while(1):
            input = raw_input("> ")
            self.processCmd(input)
            
    # decides what to do based on given input
    def processCmd(self, input):
        if input == "hi":
            print "Why Hello There"
        elif input == "sniff":
            self.startSniffer()
    
    # starts our network sniffer
    def startSniffer(self):
        self.sniff.run()

if __name__ == "__main__":
    control = Controller()
    control.run()