# lines = [...]
# parsed_lines = [parsed_lines(line) for line in lines]



# def  parsed_lines(line):
#     # Split the line into parts
#     parts = line.split()

#     # # Get the address, bytes, and instruction
#     # address = parts[0]
#     # bytes = [int(x, 16) for x  in parts[1].split('/')]
#     # instruction = parts[2]

#     # # Determine the number of data bytes
#     # opcode = instruction[0]
#     # if opcode == 'A':
#     #     num_data_bytes = 0
#     # elif opcode == 'a':
#     #     num_data_bytes = 2
#     # elif
# def parse_file(filename):
#     # Open the file and read its contents
#     with open(filename, "r") as f:
#         content = f.read()
    
#     # Split the contents into lines
#     lines = content.split('\n')

#     # Initialize an empty array to store the parsed lines
#     parsed_lines = []

#     # Iterate over each line and parse it
#     for line in lines:
#         if line.strip():  # Ignore blank lines
#             parsed_lines.append(parsed_lines.lines(line))

#     return parsed_lines


class Parser:
    OPCODES = []
    VALUES = []
    FLAGS = []
    file = ""

    def __init__(self, f):
        self.file = f

    # Returns list of (string) OPCODES, (hex) VALUES, (string) FLAGS
    def parse(self):
        file = open(self.file, "r")

        lines = file.readlines()

        for line in lines:
            commands = line.split()
            self.OPCODES.append(commands[0])
            

            found = False
            for char in commands[1]:
                if (char == "#"):
                    self.FLAGS.append("literal")
                    found = True
                    break
            if (found == False):
                self.FLAGS.append("address")
            
            commands[1] = commands[1].replace("#", "")
            commands[1] = commands[1].replace("$", "")
            self.VALUES.append(hex(int(commands[1], 16)))
        
        return self.OPCODES, self.VALUES, self.FLAGS
            