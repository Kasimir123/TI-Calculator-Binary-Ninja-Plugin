from binaryninja.architecture import Architecture
from binaryninja.binaryview import *
from binaryninja.function import RegisterInfo, InstructionInfo, InstructionTextToken
from binaryninja.enums import InstructionTextTokenType, BranchType, SegmentFlag, SymbolType, SectionSemantics, Endianness
from binaryninja.types import *
from binaryninjaui import UIContext

# constants
CHECKSUM_LEN = 2
HEADER_END = 0x4a
ASSEMBLY_START = 0x4c
LOAD_OFFSET = 0x9d95

# Define our view
class TIView(BinaryView):
    name = 'TI'
    long_name = 'TI View'

    # check if this is an TI file
    @classmethod
    def is_valid_for_data(cls,data):

        # check for the magic number
        if data.read(0, 8) == b'**TI83F*':
            return True
        return False

    # intialize the binary view
    def __init__(self, data):
        BinaryView.__init__(self, parent_view = data, file_metadata = data.file)

        # check if this is an assembly file or not
        if data.read(HEADER_END, 2) != b'\xbb\x6d':
            # if not assembly set architecture to TI-BASIC
            self.platform = Architecture['TI-BASIC'].standalone_platform
            self.assembly = False
        else:
            # if assembly set architecture to TI-Z80
            self.platform = Architecture['TI-Z80'].standalone_platform
            self.assembly = True

        self.data = data


    # define all types in types.h
    def _define_types(self):
        path = os.path.dirname(os.path.abspath(__file__))
        result = self.platform.parse_types_from_source_file(os.path.join(path, "types.h"), auto_type_source="source")
        for type_name, _type in result.types.items():
            self.define_type(Type.generate_auto_type_id("source", type_name), type_name,_type)



    # initialize our view
    def init(self):

        # define types in types.h
        self._define_types()

        # if it is ti assembly then set code entrypoint to 0x4c, otherwise set to 0x4a
        entry = ASSEMBLY_START if self.assembly else HEADER_END

        # if it is a ti basic file then we say checksum has 0 length since we need to add bytes to the end for the decompiler
        checksum = CHECKSUM_LEN if self.assembly else 0

        # define the main header
        self.define_data_var(0x0,self.types['x8XPHEADER'])

        # define the variable entry header after the main header
        self.define_data_var(len(self.types['x8XPHEADER']), self.types['VARIABLE_ENTRY_HEADER'])

        # define the data segment
        self.add_auto_segment(0x0, HEADER_END, 0x0, HEADER_END, SegmentFlag.SegmentDenyExecute)

        # define the code segment (TI's load at 0x9d95)
        self.add_auto_segment(LOAD_OFFSET, len(self.parent_view) - entry - checksum, entry, len(self.parent_view) - entry - checksum, SegmentFlag.SegmentExecutable|SegmentFlag.SegmentContainsCode)
        
        # define header section
        self.add_user_section("Headers", 0x0, HEADER_END, SectionSemantics.ReadOnlyDataSectionSemantics)

        # define code section
        self.add_user_section("Code", LOAD_OFFSET, len(self.parent_view) - entry - checksum, SectionSemantics.ReadOnlyCodeSectionSemantics)

        # if this is a ti basic file then we add the bytes for \r\n and end of file to the end of the code section
        if not self.assembly:
            self.write(LOAD_OFFSET + len(self.parent_view) - entry - CHECKSUM_LEN, b'\x3f\x00')

        # add the entry point
        self.add_entry_point(LOAD_OFFSET)

        return True
    
    def perform_is_executable(self):
        return True