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
    statusFlags = {
        "N": 0,
        "V": 0,
        "B": 0,
        "D": 0,
        "I": 0,
        "Z": 0,
        "C": 0
    }

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
                self.readStatusFlags()
            elif (opcode == "LDX"):
                self.LDX(value, flag)
                self.readRegX()
                self.readStatusFlags()
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
        if (flag == "literal"): self.accumulator = val
        else: self.accumulator = self.dataMemory.fetch(val)

        if (int(self.accumulator, 16) == 0): self.statusFlags["Z"] = 1
        else: self.statusFlags["Z"] = 0

        if ((int(self.accumulator, 16)) >= 128): self.statusFlags["N"] = 1
        else: self.statusFlags["N"] = 0

    def LDX(self, val, flag):
        if (flag == "literal"): self.regX = val
        else: self.regX = self.dataMemory.fetch(val)
        
        if (int(self.regX, 16) == 0): self.statusFlags["Z"] = 1
        else: self.statusFlags["Z"] = 0

        if ((int(self.regX, 16)) >= 128): self.statusFlags["N"] = 1
        else: self.statusFlags["N"] = 0

    def LDY(self, val, flag):
        if (flag == "literal"): self.regX = val
        else: self.regX = self.dataMemory.fetch(val)

        if (int(self.regY, 16) == 0): self.statusFlags["Z"] = 1
        else: self.statusFlags["Z"] = 0

        if ((int(self.regY, 16)) >= 128): self.statusFlags["N"] = 1
        else: self.statusFlags["N"] = 0

    def STA(self, val):
        self.dataMemory.store(val, self.accumulator)

    def STX(self, val):
        self.dataMemory.store(val, self.regX)

    def STY(self, val):
        self.dataMemory.store(val, self.regY)

    def TAX(self):
        self.regX = self.accumulator

        if (int(self.regX, 16) == 0): self.statusFlags["Z"] = 1
        else: self.statusFlags["Z"] = 0

        if ((int(self.regX, 16)) >= 128): self.statusFlags["N"] = 1
        else: self.statusFlags["N"] = 0

    def TAY(self):
        self.regY = self.accumulator

        if (int(self.regY, 16) == 0): self.statusFlags["Z"] = 1
        else: self.statusFlags["Z"] = 0

        if ((int(self.regY, 16)) >= 128): self.statusFlags["N"] = 1
        else: self.statusFlags["N"] = 0

    def TXA(self):
        self.accumlator = self.regX

        if (int(self.accumulator, 16) == 0): self.statusFlags["Z"] = 1
        else: self.statusFlags["Z"] = 0

        if ((int(self.accumulator, 16)) >= 128): self.statusFlags["N"] = 1
        else: self.statusFlags["N"] = 0

    def TYA(self):
        self.accumulator = self.regY

        if (int(self.accumulator, 16) == 0): self.statusFlags["Z"] = 1
        else: self.statusFlags["Z"] = 0

        if ((int(self.accumulator, 16)) >= 128): self.statusFlags["N"] = 1
        else: self.statusFlags["N"] = 0

    def INX(self):
        self.regX = hex(int(self.regX, 16) + 1)

        if (int(self.regX, 16) == 0): self.statusFlags["Z"] = 1
        else: self.statusFlags["Z"] = 0

        if ((int(self.regX, 16)) >= 128): self.statusFlags["N"] = 1
        else: self.statusFlags["N"] = 0

    def INY(self):
        self.regY = hex(int(self.regY, 16) + 1)

        if (int(self.regY, 16) == 0): self.statusFlags["Z"] = 1
        else: self.statusFlags["Z"] = 0

        if ((int(self.regY, 16)) >= 128): self.statusFlags["N"] = 1
        else: self.statusFlags["N"] = 0

    def ADC(self):
        # Accumulator plus value plus carry = new accumulator value
        




        

    def readAccumulator(self):
        print("Accumulator: " + self.accumulator)

    def readRegX(self):
        print("Register X: "  + self.regX)

    def readRegY(self):
        print("Register Y: " + self.regY)

    def readStatusFlags(self):
        print(self.statusFlags)