struct x8XPHEADER __packed {
    int8_t magic[0x8];            // Magic number "**TI83F*"
    int8_t second_signature[0x3]; // Second signature (Always 1A 0A 00)
    int8_t comments[0x2a];        // Comments section
    int16_t data_len;         // Length of code and code header
};

struct VARIABLE_ENTRY_HEADER __packed {
    int16_t entry_start;      // Offset to start of data in entry (Always 0B or 0D), for the program the data still has some header components
    int16_t program_size;     // Program Size
    int8_t entry_id;         // Variable type ID byte
    int8_t filename[0x8];         // Filename
    int8_t version;          // Version information
    int8_t flag;             // Flag, set to 0x80 if entry is archived
    int16_t entry_len;        // Length of the entry
    int16_t code_len;         // This is in the data technically but is the length of the code
};