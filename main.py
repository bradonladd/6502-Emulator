from obj.memory import InstructionMemory, DataMemory
from obj.parser import Parser
from obj.processor import Processor


if __name__ == "__main__":
    parser = Parser("./programs/asm.txt")
    opcodes, values = parser.parse()

    instructionMemory = InstructionMemory(opcodes, values)
    dataMemory = DataMemory(["00", "00", "00", "00", "00"])
    processor = Processor(instructionMemory, dataMemory)
    processor.execute()