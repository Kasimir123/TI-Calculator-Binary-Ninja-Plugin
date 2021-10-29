# TI Calculator Binary Ninja Plugin
Author: **Kasimir Schulz**

_Binary view for the TI calculator as well as ti basic and z80 ti architecture._

## Description:
This plugin contains three main components. A view for the TI Calculator, an architecture for the TI Basic language, and an architecture for TI specific Z80 assembly.

### TI Calculator View:

The view plugin defines the header for the 8XP program format which is the TI-83+ variable file format:

```c
struct x8XPHEADER {
    char magic[0x8];            // Magic number "**TI83F*"
    char second_signature[0x3]; // Second signature (Always 1A 0A 00)
    char comments[0x2a];        // Comments section
    char data_len[0x2];         // Length of code and code header
};

struct VARIABLE_ENTRY_HEADER {
    char entry_start[0x2];      // Offset to start of data in entry (Always 0B or 0D), for the program the data still has some header components
    char program_size[0x2];     // Program Size
    char entry_id[0x1];         // Variable type ID byte
    char filename[0x8];         // Filename
    char version[0x1];          // Version information
    char flag[0x1];             // Flag, set to 0x80 if entry is archived
    char entry_len[0x2];        // Length of the entry
    char code_len[0x2];         // This is in the data technically but is the length of the code
};
```

The view then checks if the file is a TI Basic program or a TI Assembly program by checking if \xbb\x6d is at the end of the header (address 0x4a). Then based on that information the view selects the correct architecture and does some modifications such as setting the hardcoded load address for the TI (0x9D95).

### TI Basic Architecture:

The TI Basic architecture decompiles the program back into the TI Basic programming language.

![image](https://user-images.githubusercontent.com/13757116/139357977-2b8f9a53-3201-46cc-aab4-07c9cffee6df.png)

### TI Z80 Architecture:

The TI Z80 architecture disassembles the program into Z80 assembly and parses out any TI specific instructions like romcalls.

![image](https://user-images.githubusercontent.com/13757116/139358007-fdb3477b-f011-4561-806f-f098cf109927.png)

## Required Dependencies

The following dependencies are required for this plugin:

 * pip - z80dis


## License

This plugin is released under a MIT license.

## Metadata Version

2
