class InstructionMemory():
    OPCODES = []
    VALUES = []
    FLAGS = []
    
    def __init__(self, op, val, flags):
        self.OPCODES = op
        self.VALUES = val
        self.FLAGS = flags

    def printMem(self):
        print("Instruction Memory Stack\n##############################")
        for i in range(0, len(self.OPCODES)):
            print("0x" + str(i) + ": " + self.OPCODES[i] + " " + self.VALUES[i] + "  ---- " + self.FLAGS[i])
        print("##############################")

    def convertMemoryFromStringToHex(self):
        for i in range(0, len(self.VALUES)):
            self.VALUES[i] = self.VALUES[i]

    def fetch(self, programCounter):
        if programCounter == len(self.OPCODES):
            return -1
        else:
            return self.OPCODES[programCounter], self.VALUES[programCounter], self.FLAGS[programCounter]



class DataMemory():
    memSize = 255
    VALUES = []

    def __init__(self):
        for i in range (0, self.memSize):
            self.VALUES.append(hex(0))
    
    def printMem(self):
        print("Data Memory")
        for i in range(0, len(self.VALUES)):
            print("0x" + str(i) + ": " + self.VALUES[i])

    def fetch(self, addr):
        return self.VALUES[int(addr[2:])]
    
    def store(self, addr, val):
        self.VALUES[int(addr[2:])] = val

    

    
    
