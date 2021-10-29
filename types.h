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