from obj.memory import InstructionMemory, DataMemory
# from obj.parser import Parser

class Processor:
    instructionMemory = None
    dataMemory = None
    programCounter = 0

    def __init__(self, instrMem, dataMem):
        self.instructionMemory = instrMem
        self.dataMemory = dataMem


    def execute(self):
        while (self.instructionMemory.fetch(self.programCounter) != -1):
            opcode, value = self.instructionMemory.fetch(self.programCounter)
            print(opcode + "\n")
            self.programCounter = self.programCounter + 1