import unittest
from obj.memory import Memory

class TestMemoryMethods(unittest.TestCase):
    asmTestOpcodes = ["LDU", "ADD", "SUB"]
    asmTestValues = ["#44", "#66", "#88"]

    def test_init(self): 
        memorySingle = Memory(["LDU", "ADD", "SUB"], ["#44", "#66", "#88"])
        memorySingle.printMem()


if __name__ == '__main__':
        unittest.main()
