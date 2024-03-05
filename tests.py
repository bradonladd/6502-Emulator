import unittest
from obj.memory import InstructionMemory, DataMemory

class TestInstructionMemoryMethods(unittest.TestCase):
    asmTestOpcodes = ["LDU", "ADD", "SUB"]
    asmTestValues = ["#44", "#66", "#88"]

    def test_init(self): 
        print("                       @Instruction Memory Init:@\n")
        memorySingle = InstructionMemory(self.asmTestOpcodes, self.asmTestValues)
        memorySingle.printMem()
    
    def test_fetch(self):
        print("                       @Instruction Memory Fetch:@\n")
        memorySingle = InstructionMemory(["LDU", "ADD", "SUB"], ["#44", "#66", "#88"])
        opcode, value = memorySingle.fetch(1)
        print(opcode + " " + value + "\n")

class TestDataMemoryMethods(unittest.TestCase):
    asmData = ["42", "66", "01"]
    
    def test_init(self):
        print("                       @Data Memory Init:@\n")
        dataSingle = DataMemory(self.asmData)
        dataSingle.printMem()
        print("\n")
    
    def test_fetch(self):
        print("                       @Data Memory Fetch:@\n")
        dataSingle = DataMemory(self.asmData)
        value = dataSingle.fetch(0)
        print(value + "\n")


if __name__ == '__main__':
        unittest.main()
