#!/usr/bin/python3

def validUTF8(data):
    # Initialize a variable to track the number of expected continuation bytes
    expected_bytes = 0

    # Iterate through each byte in the data list
    for num in data:
        # Get the binary representation of the byte
        byte = num & 0xFF  # Only keep the last 8 bits

        # Check the number of leading 1s to determine expected number of bytes
        if expected_bytes == 0:
            if (byte >> 5) == 0b110:
                expected_bytes = 1
            elif (byte >> 4) == 0b1110:
                expected_bytes = 2
            elif (byte >> 3) == 0b11110:
                expected_bytes = 3
            elif (byte >> 7) == 0:
                continue
            else:
                return False

        else:
            if (byte >> 6) != 0b10:
                return False
            expected_bytes -= 1

    return expected_bytes == 0
