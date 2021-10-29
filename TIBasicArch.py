from binaryninja.architecture import Architecture
from binaryninja.function import InstructionInfo, InstructionTextToken, RegisterInfo
from binaryninja.enums import InstructionTextTokenType, Endianness, BranchType
from binaryninja.types import *

# import all the basic commands
from .basic_commands import *

use_default_loader_settings = True

# disassembler class for the TI Basic language
class Disassembler():

    # intialize the dictionary and the max key length
    def __init__(self):
        self.dict = basic_commands
        self.max_key_len = max([len(k) for k, v in self.dict.items()])

    # Get the first command in the data
    def get_command(self, data, readlen):

        # get the current data (from start with the length to read)
        current = data[0:readlen]

        # If length is nothing then return null, we shouldn't hit this
        if len(current) == 0:
            return "NULL", 0

        # while we can keep reading (length greater than 0) and we haven't found the bytes in the dictionary
        while readlen > 1 and not current in self.dict:

            # decrement readlen
            readlen -= 1

            # read the new bytes
            current = data[0:readlen]
        
        # if the bytes are in the dictionary
        if current in self.dict:
            
            # get the associated command
            command = self.dict[current]

        # if \x00 (byte we add to the end of the file) return END OF FILE
        elif current == b'\x00':
            command = 'END OF FILE'
            readlen = 1

        # otherwise return error
        else:
            command = 'Error'
            readlen = 1

        # return command and length
        return command, readlen

    # disassemble the next set of instructions
    def disassemble(self, data, addr):

        # get the max read length
        readlen = self.max_key_len

        # set commands we are going to return
        totalCommand = ''
        totalLen = 0

        # get the first command in the data
        command = self.get_command(data, readlen)

        # add the command to the return values
        totalCommand += command[0]
        totalLen += command[1]

        # if the command isn't a new line and while we can still read more data
        while command[0] != '\r\n' and totalLen < len(data):
            
            # get the next command
            command = self.get_command(data[totalLen:], readlen)

            # check that the command has length greater than 0
            if command[1] == 0:
                break

            # append the command and length to the total
            totalCommand += command[0]
            totalLen += command[1]

        # return the commands and total length
        return (totalCommand, totalLen)
        
# instantiate the disassembler
disasm = Disassembler()

# TI Basic architecture
class TIBASIC(Architecture):
    # set name
    name = 'TI-BASIC'

    # set max instruction length to the max amount that we are allowed to set it to since we search for \r\n
    max_instr_length = 256

    # set endianness
    endianness = Endianness.LittleEndian

    # add SP register to appease binja
    regs = {
        'SP': RegisterInfo('SP', 2)
    }
    stack_pointer = "SP"

    def get_instruction_info(self, data, addr):

        (instrTxt, instrLen) = disasm.disassemble(data, addr)
        
        result = InstructionInfo()

        result.length = instrLen

        # if we reached the end of file command set branch to function return so it doesn't analyze further
        if instrTxt == 'END OF FILE':
            result.add_branch(BranchType.FunctionReturn)

        return result 

    def get_instruction_text(self, data, addr):
        (instrTxt, instrLen) = disasm.disassemble(data, addr)

        result = []

        # if end of file is reached add string saying it was added by the plugin
        if instrTxt == 'END OF FILE':
            instrTxt += " - Added by plugin"

        result.append(InstructionTextToken(InstructionTextTokenType.TextToken, instrTxt))

        return result, instrLen

    def get_instruction_low_level_il(self, data, addr, il):
            return None