
def run():
    while(1):
        input = raw_input("> ")
        processCmd(input)
        
        
def processCmd(input):
    if input == "hi":
        print "Why Hello There"

if __name__ == "__main__":
    run()