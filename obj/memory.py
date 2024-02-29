def memory():
    OPCODES = []
    VALUES = []
    
    def __init__(self, op, val):
        self.OPCODES = op
        self.VALUES = val

    def printMem():
        print("printMem Not Implemented!")

    def getInstruction(programCounter):
        return OPCODES[programCounter], VALUES[programCounter]

    

    
    
