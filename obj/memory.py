class Memory():
    #OPCODES = []
    #VALUES = []
    
    def __init__(self, op, val):
        self.OPCODES = op
        self.VALUES = val

    def printMem(self):
        print("Instruction Memory Stack\n##############################")
        for i in range(0, len(self.OPCODES)):
            print("0x" + str(i) + ": " + self.OPCODES[i] + " " + self.VALUES[i])
        print("##############################")

    def getInstruction(programCounter):
        return OPCODES[programCounter], VALUES[programCounter]


    

    
    
