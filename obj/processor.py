from obj.memory import InstructionMemory, DataMemory
# from obj.parser import Parser


#$ -> Hex format
## -> Number literal

# Values in accumulator are always going to be Python integer objects. The load instructions read in a hex string and output an
# integer (converting considering base 16). Store instructions read in an integer value from the regx/regy/acc and output a hex value. 

class Processor:
    instructionMemory = None
    dataMemory = None
    programCounter = 0
    accumulator = ""
    regX = 0
    regY = 0
    statusFlag = ""

    def __init__(self, instrMem, dataMem):
        self.instructionMemory = instrMem
        self.dataMemory = dataMem


    def execute(self):
        while (1 == 1):
            opcode, value, flag = self.instructionMemory.fetch(self.programCounter)

            if (opcode == "END"):
                break
            elif (opcode == "LDA"):
                self.LDA(value, flag)
                self.readAccumulator()
            elif (opcode == "LDX"):
                self.LDX(value, flag)
                self.readRegX()
            elif (opcode == "LDY"):
                self.LDY(value, flag)
                self.readRegY()
            elif (opcode == "STA"):
                self.STA(value)
                self.dataMemory.printMem()
            elif (opcode == "STX"):
                self.STX(value)
            elif (opcode == "STY"):
                self.STY(value)
                    

            self.programCounter = self.programCounter + 1

    def LDA(self, val, flag):
        if (flag == "literal"):
            self.accumulator = val
        else:
            self.accumulator = self.dataMemory.fetch(val)
    
    def LDX(self, val, flag):
        if (flag == "literal"):
            self.regX = val
        else:
            self.regX = self.dataMemory.fetch(val)

    def LDY(self, val, flag):
        if (flag == "literal"):
            self.regX = val
        else:
            self.regX = self.dataMemory.fetch(val)

    def STA(self, val):
        self.dataMemory.store(val, self.accumulator)

    def STX(self, val):
        self.dataMemory.store(val, self.regX)

    def STY(self, val):
        self.dataMemory.store(val, self.regY)

        





    def readAccumulator(self):
        print("Accumulator: " + self.accumulator)

    def readRegX(self):
        print("Register X: "  + self.regX)

    def readRegY(self):
        print("Register Y: " + self.regY)