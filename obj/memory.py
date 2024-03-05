class InstructionMemory():
    OPCODES = []
    VALUES = []
    
    def __init__(self, op, val):
        self.OPCODES = op
        self.VALUES = val

    def printMem(self):
        print("Instruction Memory Stack\n##############################")
        for i in range(0, len(self.OPCODES)):
            print("0x" + str(i) + ": " + self.OPCODES[i] + " " + self.VALUES[i])
        print("##############################")

    def fetch(self, programCounter):
        if programCounter == len(self.OPCODES):
            return -1
        else:
            return self.OPCODES[programCounter], self.VALUES[programCounter]



class DataMemory():
    VALUES = []

    def __init__(self, val):
        self.VALUES = val
    
    def printMem(self):
        print("Data Memory")
        for i in range(0, len(self.VALUES)):
            print("0x" + str(i) + ": " + self.VALUES[i])

    def fetch(self, programCounter):
        return self.VALUES[programCounter]
    
    def write(self, programCounter, val):
        self.VALUES[programCounter] = val

    

    
    
