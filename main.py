from obj.memory import InstructionMemory, DataMemory
# from obj.parser import Parser
from obj.processor import Processor


if __name__ == "__main__":
    #parser = Parser()
    #instructionMemory = InstructionMemory(parser.getCodes, parser.getVals)

    instructionMemory = InstructionMemory(["ADD", "SUB", "END"], ["#66", "#88", "#00"])
    dataMemory = DataMemory(["00", "00", "00", "00", "00"])
    processor = Processor(instructionMemory, dataMemory)
    processor.execute()