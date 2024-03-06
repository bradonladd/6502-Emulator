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
            opcode, value = self.instructionMemory.fetch(self.programCounter)

            if (opcode == "END"):
                break
            elif (opcode == "LDA"):
                self.LDA(value)
                self.readAccumulator()
            elif (opcode == "LDX"):
                self.LDX(value)
                self.readRegX()
            elif (opcode == "LDY"):
                self.LDY(value)
                self.readRegY()

            self.programCounter = self.programCounter + 1

    def LDA(self, val):
        self.accumulator = val
    
    def LDX(self, val):
        self.regX = val

    def LDY(self, val):
        self.regY = val



    def readAccumulator(self):
        print(self.accumulator)

    def readRegX(self):
        print(self.regX)

    def readRegY(self):
        print(self.regY)